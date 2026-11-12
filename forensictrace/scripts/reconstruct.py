#!/usr/bin/env python3
"""Causal incident reconstruction from one ForensicTrace evidence file.

Reads the JSON the C engine wrote (schema 2 or 3) and derives

  processes     process tree with the exact spawn event of each child
  files         what happened to each file, and by whom
  connections   source, destination, protocol and byte counts of each connection
  graph         nodes (process, file, endpoint) and relations between them
  findings      rule-based suspicious activity, each citing its events
  answers       the investigator's questions: who started it, who downloaded
                what, which files were affected, which endpoints were contacted

Every relation lists the events that support it and a confidence score. The
score is rule-based and explained by its factors; it is NOT a calibrated
probability. "observed" relations come straight from one or more syscalls;
"inferred" relations connect observations the kernel never linked itself
(for example: the bytes written to this file came from that socket).

Nothing is claimed about evidence that was not collected: under config A the
file and network answers are "not collected", never "none".

Usage:  reconstruct.py run.json [--json] [-o graph.json]
"""
import argparse
import ipaddress
import json
import re
import sys
from collections import defaultdict

O_ACCMODE, O_WRONLY, O_RDWR = 0o3, 0o1, 0o2
O_CREAT, O_EXCL, O_TRUNC, O_DIRECTORY = 0o100, 0o200, 0o1000, 0o200000
EINPROGRESS = -115

SENSITIVE = re.compile(r"^(/etc/(shadow|gshadow|sudoers(\.d/.*)?|passwd|group|crontab)"
                       r"|/root/.*|.*/\.ssh/.*|/var/spool/cron/.*)$")
DEVICE = re.compile(r"^/dev/(?!shm/)")
SYSTEM = re.compile(r"^(/usr/|/lib|/lib64/|/bin/|/sbin/|/etc/|/proc/|/sys/|/snap/|/var/lib/"
                    r"|/run/|/var/run/|/var/cache/|/opt/)"
                    r"|/\.local/(lib|share)/|/site-packages/|/__pycache__/|/pyvenv\.cfg$"
                    r"|\.(pyc|mo|so)(\.[0-9.]+)?$")
TEMP = re.compile(r"^(/tmp/|/var/tmp/|/dev/shm/)")
INTERPRETER = re.compile(r"/(ba|da|z|k|c)?sh$|/python[0-9.]*$|/perl$|/ruby$|/node$|/php$")
NON_PATH = re.compile(r"^(socket:|pipe:|anon_inode:|fd:|sockfd=|code=|unix:|memfd:)")


def load_evidence(path):
    # Raw paths in a trace can hold any bytes; a stray one must not stop the analysis.
    with open(path, encoding="utf-8", errors="replace") as fh:
        return json.load(fh)


def base(path):
    return path.rstrip("/").rsplit("/", 1)[-1] or path


def detail_field(event, name):
    m = re.search(rf"(?:^| ){name}=(\S+)", event.get("detail", ""))
    return m.group(1) if m else None


def split_endpoint(text):
    """'1.2.3.4:80' or '[::1]:80' -> (host, port). IPv4-mapped IPv6 is shown as IPv4."""
    m = re.match(r"^\[?([0-9a-fA-F:.]+)\]?:(\d+)$", text or "")
    if not m:
        return None, None
    host = m.group(1)
    if host.lower().startswith("::ffff:"):
        host = host[7:]
    return host, int(m.group(2))


def ip_scope(host):
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return "unknown"
    if ip.is_loopback:
        return "loopback"
    if ip.is_unspecified:
        return "unspecified"
    if ip.is_link_local:
        return "link-local"
    if ip.is_private:
        return "private"
    return "public"


class Reconstruction:
    def __init__(self, doc):
        self.doc = doc
        self.events = doc.get("events", [])
        self.config = doc.get("config", "")
        self.custody_schema = doc.get("schema_version", 2) >= 3
        self.collected = {
            "process": True,
            "file": self.config in ("B", "C", "D"),
            "network": self.config in ("C", "D"),
        }
        self.relations = []
        self.nodes = {}
        self.findings = []
        self.processes = {}
        self.files = {}
        self.connections = []
        self.base_ts = self.events[0]["ts_ns"] if self.events else 0

    # ---- relation helpers ---------------------------------------------------

    def ms(self, event):
        return round((event["ts_ns"] - self.base_ts) / 1e6, 3)

    def relate(self, kind, src, dst, events, confidence, tier, rule, factors, summary, at=None, **extra):
        """Merge repeats of one relation between the same two nodes."""
        for r in self.relations:
            if r["kind"] == kind and r["src"] == src and r["dst"] == dst:
                r["evidence"] = sorted(set(r["evidence"]) | {e["id"] for e in events})
                r["count"] += 1
                if "bytes" in extra:
                    r["bytes"] = r.get("bytes", 0) + extra["bytes"]
                return r
        rel = {
            "id": len(self.relations) + 1, "kind": kind, "src": src, "dst": dst,
            "ms": self.ms(at or events[0]), "evidence": sorted({e["id"] for e in events}),
            "confidence": round(min(confidence, 0.99), 2), "tier": tier, "rule": rule,
            "factors": factors, "summary": summary, "count": 1,
        }
        rel.update(extra)
        self.relations.append(rel)
        return rel

    def process_label(self, pid, event=None):
        """Name a process by the program it was running at `event`, or by its last program.
        A shell that later execs another program (bash -c '...; rm x') changes name."""
        p = self.processes.get(pid)
        exe = (event.get("exe") if event else None) or (p["exe"] if p else "")
        return f"{base(exe) if exe else 'process'} ({pid})"

    # ---- stage 1: processes ---------------------------------------------------

    def build_processes(self):
        spawn_by_child = {}
        for e in self.events:
            if e["syscall"] in ("clone", "clone3", "fork", "vfork") and (e.get("ret") or 0) > 0:
                spawn_by_child.setdefault(e["ret"], e)

        for e in self.events:
            pid = e["pid"]
            p = self.processes.get(pid)
            if p is None:
                p = self.processes[pid] = {
                    "pid": pid, "ppid": e["ppid"], "uid": e.get("uid", -1),
                    "exe": e.get("exe") or "", "exec_chain": [],
                    "first_ms": self.ms(e), "last_ms": self.ms(e),
                    "first_event": e["id"], "exit_code": None, "event_count": 0,
                    "counts": defaultdict(int), "parent": None, "spawn_event": None,
                    "children": [], "failed": 0,
                }
            p["event_count"] += 1
            p["counts"][e["type"]] += 1
            p["last_ms"] = self.ms(e)
            ret = e.get("ret")
            if ret is not None and -4096 < ret < 0 and ret != EINPROGRESS:
                p["failed"] += 1
            if e["syscall"] in ("execve", "execveat") and e.get("target"):
                p["exec_chain"].append({"path": e["target"], "event": e["id"], "ms": self.ms(e)})
                p["exe"] = e["target"]
            elif e["syscall"] in ("exit", "exit_group"):
                m = re.match(r"code=(-?\d+)", e.get("target", ""))
                p["exit_code"] = int(m.group(1)) if m else None
            elif not p["exe"] and e.get("exe"):
                p["exe"] = e["exe"]

        for pid, p in self.processes.items():
            spawn = spawn_by_child.get(pid)
            if spawn is not None and spawn["pid"] in self.processes and spawn["pid"] != pid:
                p["parent"], p["spawn_event"] = spawn["pid"], spawn["id"]
                p["parent_confidence"] = 0.99
            elif p["ppid"] in self.processes and p["ppid"] != pid:
                p["parent"] = p["ppid"]
                p["parent_confidence"] = 0.8
            if p["parent"] is not None:
                self.processes[p["parent"]]["children"].append(pid)

    def node_process(self, pid):
        key = f"p:{pid}"
        if key not in self.nodes:
            p = self.processes[pid]
            self.nodes[key] = {"id": key, "type": "process", "label": base(p["exe"]) if p["exe"] else "process",
                               "pid": pid, "exe": p["exe"], "first_ms": p["first_ms"]}
        return key

    def node_file(self, path):
        key = f"f:{path}"
        if key not in self.nodes:
            f = self.files[path]
            self.nodes[key] = {"id": key, "type": "file", "label": base(path), "path": path,
                               "category": f["category"], "first_ms": f["first_ms"]}
        return key

    def node_endpoint(self, conn):
        endpoint = conn["endpoint"]
        key = f"n:{endpoint}"
        if key not in self.nodes:
            self.nodes[key] = {"id": key, "type": "endpoint", "label": endpoint,
                               "scope": conn["scope"], "proto": conn["proto"], "first_ms": conn["ms"]}
        return key

    # ---- stage 2: files -------------------------------------------------------

    def file_record(self, path, event):
        f = self.files.get(path)
        if f is None:
            cat = ("sensitive" if SENSITIVE.match(path) else
                   "device" if DEVICE.match(path) else
                   "system" if SYSTEM.search(path) else "user")
            f = self.files[path] = {
                "path": path, "category": cat, "temp": bool(TEMP.match(path)),
                "first_ms": self.ms(event), "last_ms": self.ms(event),
                "ops": defaultdict(int), "processes": set(), "events": [],
                "bytes_written": 0, "bytes_read": 0, "timeline": [],
            }
        f["last_ms"] = self.ms(event)
        return f

    def file_op(self, path, event, op, bytes_=0):
        f = self.file_record(path, event)
        f["ops"][op] += 1
        f["processes"].add(event["pid"])
        if len(f["events"]) < 500:
            f["events"].append(event["id"])
        f["timeline"].append({"op": op, "pid": event["pid"], "event": event["id"], "ms": self.ms(event),
                              "bytes": bytes_, "exe": event.get("exe", "")})
        return f

    def build_files(self):
        # dataflow view used by the inference rules below
        self.ops_by_pid = defaultdict(list)
        for e in self.events:
            name, target, ret = e["syscall"], e.get("target", ""), e.get("ret")
            if e["type"] != "file" or not target.startswith("/") or NON_PATH.match(target):
                continue
            failed = ret is not None and -4096 < ret < 0
            if name in ("open", "openat"):
                m = re.search(r"flags=0x([0-9a-f]+)", e.get("detail", ""))
                flags = int(m.group(1), 16) if m else 0
                if flags & O_DIRECTORY:
                    continue
                writes = (flags & O_ACCMODE) in (O_WRONLY, O_RDWR)
                if failed:
                    if ret == -2 and not SENSITIVE.match(target):
                        continue        # probing for optional files is normal program start-up
                    self.file_op(target, e, "write_denied" if writes else "read_denied")
                elif writes and flags & O_CREAT and (flags & O_EXCL or flags & O_TRUNC):
                    existing = self.files.get(target)
                    live = existing and existing["ops"].get("created", 0) + existing["ops"].get("overwritten", 0) > \
                        existing["ops"].get("deleted", 0)
                    self.file_op(target, e, "overwritten" if live else "created")
                elif writes:
                    self.file_op(target, e, "opened_for_write")
                else:
                    self.file_op(target, e, "opened")
            elif name == "write" and not failed:
                self.file_op(target, e, "wrote", ret or 0)
                self.files[target]["bytes_written"] += ret or 0
            elif name == "read" and not failed and (ret or 0) > 0:
                self.file_op(target, e, "read", ret)
                self.files[target]["bytes_read"] += ret
            elif name in ("unlink", "unlinkat") and not failed:
                self.file_op(target, e, "deleted")
            elif name in ("chmod", "fchmodat") and not failed:
                self.file_op(target, e, "chmod")
        for e in self.events:
            if e["syscall"] in ("execve", "execveat") and e.get("target", "").startswith("/"):
                self.file_op(e["target"], e, "executed")

    def file_is_relevant(self, f):
        ops = f["ops"]
        if f["category"] == "sensitive":
            return True
        if f["category"] == "device":
            return False
        if f["category"] == "system":
            return any(ops.get(k) for k in ("created", "overwritten", "wrote", "deleted", "chmod"))
        return True

    # ---- stage 3: connections ---------------------------------------------------

    def build_connections(self):
        by_socket, by_pid = {}, defaultdict(list)
        self.unix_connections = []
        for e in self.events:
            name = e["syscall"]
            if name not in ("connect", "accept", "accept4"):
                continue
            target = e.get("target", "")
            if name == "connect" and target.startswith("unix:"):
                self.unix_connections.append(e)
                continue
            remote = detail_field(e, "remote")
            local = detail_field(e, "local")
            if name == "connect" and target.startswith("sockfd="):
                continue                # connect(AF_UNSPEC) only dissolves a UDP association
            ret = e.get("ret")
            if name != "connect" and (ret is None or ret < 0):
                continue
            dst_host, dst_port = split_endpoint(remote if name == "connect" and remote else target)
            if name == "connect" and dst_host is None and remote is None:
                dst_host, dst_port = None, None
            src_host, src_port = split_endpoint(local)
            if name != "connect":       # accept: the far end is the source of the connection
                src_host, src_port = split_endpoint(remote)
                dst_host, dst_port = split_endpoint(local)
            conn = {
                "event": e["id"], "ms": self.ms(e), "pid": e["pid"], "exe": e.get("exe", ""),
                "direction": "outbound" if name == "connect" else "inbound",
                "src_host": src_host, "src_port": src_port, "dst_host": dst_host, "dst_port": dst_port,
                "proto": detail_field(e, "proto") or "unknown",
                "socket": detail_field(e, "socket"),
                "scope": ip_scope(dst_host) if dst_host else "unknown",
                "endpoint": f"{dst_host}:{dst_port}" if dst_host else target,
                "ret": ret, "bytes_sent": 0, "bytes_received": 0, "data_events": [],
            }
            refused = name == "connect" and ret is not None and ret < 0 and ret != EINPROGRESS
            conn["state"] = "failed" if refused else "attempted"
            if name == "connect" and ret == 0:
                conn["state"] = "established"
            if name != "connect":
                conn["state"] = "accepted"
            self.connections.append(conn)
            by_pid[e["pid"]].append(conn)
            if conn["socket"]:
                by_socket[conn["socket"]] = conn

        # byte counts: exact via the socket inode (schema 3), otherwise same-process order
        self.recv_events = defaultdict(list)
        for e in self.events:
            name, target = e["syscall"], e.get("target", "")
            if name not in ("sendto", "recvfrom", "read", "write") or not target.startswith("socket:["):
                continue
            ret = e.get("ret") or 0
            if ret <= 0:
                continue
            inode = target[8:-1]
            conn, tied = by_socket.get(inode), True
            if conn is None:
                earlier = [c for c in by_pid.get(e["pid"], []) if c["event"] < e["id"]
                           and c["direction"] == "outbound" and c["state"] != "failed"
                           and c["scope"] != "unspecified"]
                conn, tied = (earlier[-1] if earlier else None), False
            if conn is None:
                continue
            received = name in ("recvfrom", "read")
            conn["bytes_received" if received else "bytes_sent"] += ret
            conn["data_events"].append(e["id"])
            if conn["state"] == "attempted":
                conn["state"] = "established"
            if received:
                self.recv_events[e["pid"]].append((e, conn, tied))

        for c in self.connections:
            # A UDP "connect" that never moves data is a resolver or route probe, not contact.
            c["probe"] = c["direction"] == "outbound" and not c["data_events"] and (
                c["proto"] == "udp" or c["scope"] == "unspecified" or c["dst_host"] is None)

        # both ends of a loopback connection in the same trace: exact 4-tuple match
        for c in self.connections:
            if c["direction"] != "outbound" or c["src_port"] is None:
                continue
            for s in self.connections:
                if s["direction"] == "inbound" and s["src_port"] == c["src_port"] and \
                        s["dst_port"] == c["dst_port"] and s["src_host"] == c["src_host"]:
                    c["peer_pid"], s["peer_pid"] = s["pid"], c["pid"]

    # ---- stage 4: observed relations ----------------------------------------------

    def observed_relations(self):
        for pid, p in self.processes.items():
            if p["parent"] is None:
                continue
            exact = p["spawn_event"] is not None
            ev = [self.by_id[p["spawn_event"]]] if exact else [self.by_id[p["first_event"]]]
            self.relate("spawned", self.node_process(p["parent"]), self.node_process(pid), ev,
                        p["parent_confidence"], "observed",
                        "fork/clone return value" if exact else "PPID of the child",
                        [{"label": "the parent's fork/clone returned exactly this PID", "value": 0.99}] if exact else
                        [{"label": "only the child's PPID links them; the spawn call was not captured", "value": 0.8}],
                        f"{self.process_label(p['parent'], ev[0] if exact else None)} started {self.process_label(pid)}")

        verbs = {"created": ("created", 0.98), "overwritten": ("overwrote", 0.98), "wrote": ("wrote", 0.95),
                 "read": ("read", 0.95), "deleted": ("deleted", 0.98), "chmod": ("changed mode of", 0.98),
                 "read_denied": ("tried to read", 0.98), "write_denied": ("tried to write", 0.98),
                 "opened_for_write": ("opened for writing", 0.9)}
        for f in self.files.values():
            if not self.file_is_relevant(f):
                continue
            for item in f["timeline"]:
                op = item["op"]
                if op not in verbs:
                    continue
                pid = item["pid"]
                event = self.by_id[item["event"]]
                verb, conf = verbs[op]
                basis = "file descriptor resolved through /proc at the time of the call" \
                    if op in ("wrote", "read") else "path argument of the syscall, with its return value"
                extra = {"bytes": item["bytes"]} if item["bytes"] else {}
                if op == "chmod":
                    extra["mode"] = detail_field(event, "mode")
                    extra["adds_exec"] = _adds_exec(extra["mode"])
                if op in ("read_denied", "write_denied"):
                    m = re.search(r"err=(.*)$", event.get("detail", ""))
                    extra["error"] = m.group(1) if m else ""
                self.relate(op, self.node_process(pid), self.node_file(f["path"]), [event], conf, "observed",
                            f"{event['syscall']} syscall", [{"label": basis, "value": conf}],
                            f"{self.process_label(pid)} {verb} {f['path']}", **extra)

        for c in self.connections:
            if c.get("probe") or c["dst_host"] is None:
                continue
            ev = [self.by_id[c["event"]]]
            if c["direction"] == "outbound":
                conf = {"established": 0.97, "attempted": 0.7, "failed": 0.97}[c["state"]]
                kind = "connect_failed" if c["state"] == "failed" else "connected"
                basis = {"established": "connect() with data moved on the same socket",
                         "attempted": "connect() issued, but no data was seen on the socket",
                         "failed": "connect() returned an error"}[c["state"]]
                verb = "failed to connect to" if c["state"] == "failed" else "connected to"
                self.relate(kind, self.node_process(c["pid"]), self.node_endpoint(c), ev, conf, "observed",
                            "connect syscall", [{"label": basis, "value": conf}],
                            f"{self.process_label(c['pid'])} {verb} {c['endpoint']}/{c['proto']}",
                            bytes=c["bytes_sent"] + c["bytes_received"])
            else:
                has_peer = "peer_pid" in c
                conf = 0.97 if has_peer else 0.9
                self.relate("accepted", self.node_endpoint(c), self.node_process(c["pid"]), ev, conf, "observed",
                            "accept syscall",
                            [{"label": "client and server ends share the same address and port pair" if has_peer
                              else "accept() returned a connection", "value": conf}],
                            f"{self.process_label(c['pid'])} accepted a connection on {c['endpoint']}")

    # ---- stage 5: inferred relations ------------------------------------------------

    def server_pids(self):
        """Processes that accept connections, plus their worker threads and children."""
        servers = {c["pid"] for c in self.connections if c["direction"] == "inbound"}
        changed = True
        while changed:
            changed = False
            for pid, p in self.processes.items():
                if pid not in servers and p["parent"] in servers and not p["exec_chain"]:
                    servers.add(pid)
                    changed = True
        return servers

    def infer_downloads(self):
        """Received from a socket, then wrote a file: the file's content probably came from there."""
        self.downloads = []
        if not (self.collected["network"] and self.collected["file"]):
            return
        for pid, received in self.recv_events.items():
            writes = [e for e in self.events if e["pid"] == pid and e["syscall"] == "write"
                      and (e.get("ret") or 0) > 0 and e.get("target", "").startswith("/")
                      and e["target"] in self.files and self.file_is_relevant(self.files[e["target"]])]
            for path in {w["target"] for w in writes}:
                file_writes = [w for w in writes if w["target"] == path]
                first_write = file_writes[0]
                prior = [r for r in received if r[0]["id"] < first_write["id"]]
                if not prior:
                    continue
                recv_event, conn, tied = prior[-1]
                bytes_in = sum(r[0].get("ret") or 0 for r in prior)
                bytes_out = sum(w.get("ret") or 0 for w in file_writes)
                other_input = [e for e in self.events if e["pid"] == pid and e["syscall"] == "read"
                               and recv_event["id"] < e["id"] < first_write["id"]
                               and e.get("target", "") in self.files
                               and self.files[e["target"]]["category"] != "system"]
                score = 0.55
                factors = [{"label": "same process received network data, then wrote this file", "value": 0.55}]
                if tied:
                    score += 0.15
                    factors.append({"label": "received bytes are tied to this connection by its socket inode",
                                    "value": 0.15})
                if not other_input:
                    score += 0.10
                    factors.append({"label": "no other non-system file was read between receiving and writing",
                                    "value": 0.10})
                if bytes_out <= bytes_in:
                    score += 0.05
                    factors.append({"label": f"bytes written ({bytes_out}) fit within bytes received ({bytes_in})",
                                    "value": 0.05})
                score = min(score, 0.9)
                factors.append({"label": "file content is not captured, so identical bytes are not proven",
                                "value": 0})
                rel = self.relate(
                    "downloaded", self.node_process(pid), self.node_file(path),
                    [self.by_id[conn["event"]], recv_event] + file_writes[:5], score, "inferred",
                    "network input followed by file output", factors,
                    f"{self.process_label(pid)} downloaded {path} from {conn['endpoint']}",
                    at=first_write, bytes=bytes_out, endpoint=conn["endpoint"])
                self.downloads.append({"relation": rel, "pid": pid, "path": path, "endpoint": conn["endpoint"]})

    def infer_execution(self):
        """A file written during the trace, later executed: payload execution."""
        self.dropped_execs = []
        if not self.collected["file"]:
            return
        for e in self.events:
            if e["syscall"] not in ("execve", "execveat") or not e.get("target") or (e.get("ret") or 0) < 0:
                continue
            path = e["target"]
            f = self.files.get(path)
            if not f or SYSTEM.search(path):
                continue
            history = [t for t in f["timeline"] if t["event"] < e["id"]]
            writes = [t for t in history if t["op"] in ("created", "overwritten", "wrote")]
            if not writes:
                self.relate("executed", self.node_file(path), self.node_process(e["pid"]), [e], 0.99, "observed",
                                  "execve syscall", [{"label": "execve of this path succeeded", "value": 0.99}],
                                  f"{self.process_label(e['pid'])} executed {path}")
                continue
            last_write = writes[-1]
            modes = [t for t in history if t["op"] == "chmod" and t["event"] > last_write["event"]
                     and _adds_exec(detail_field(self.by_id[t["event"]], "mode"))]
            deleted = [t for t in history if t["op"] == "deleted" and t["event"] > last_write["event"]]
            score = 0.70
            factors = [{"label": "same path was written earlier in this trace, then executed", "value": 0.70}]
            if not deleted:
                score += 0.10
                factors.append({"label": "file was not deleted between the write and the execution", "value": 0.10})
            if modes:
                score += 0.10
                factors.append({"label": "execute permission was added between the write and the execution",
                                "value": 0.10})
            if self.same_tree(last_write["pid"], e["pid"]):
                score += 0.05
                factors.append({"label": "writer and executor belong to the same process tree", "value": 0.05})
            factors.append({"label": "inode is not recorded, so the path is assumed to name the same file",
                            "value": 0})
            evidence = [self.by_id[last_write["event"]], e] + [self.by_id[t["event"]] for t in modes[-1:]]
            rel = self.relate("executed", self.node_file(path), self.node_process(e["pid"]), evidence, score,
                              "inferred", "file written, then executed", factors,
                              f"file {path}, written earlier in this trace, was executed as "
                              f"{self.process_label(e['pid'])}", at=e)
            self.dropped_execs.append({"relation": rel, "path": path, "pid": e["pid"], "event": e["id"],
                                       "writer": last_write["pid"], "chmod": bool(modes)})

    def infer_interpretation(self):
        """A shell or interpreter reading a user file is usually running it as a script."""
        if not self.collected["file"]:
            return
        servers = self.server_pids()
        command = self.doc.get("command", "")
        for f in self.files.values():
            if f["category"] != "user":
                continue
            for pid in sorted(f["processes"]):
                p = self.processes[pid]
                if pid in servers or not INTERPRETER.search(p["exe"] or ""):
                    continue
                reads = [t for t in f["timeline"] if t["pid"] == pid and t["op"] == "read"]
                if not reads:
                    continue
                writes = [t for t in f["timeline"] if t["op"] in ("created", "overwritten", "wrote")
                          and t["event"] < reads[0]["event"] and t["pid"] != pid]
                named = pid == self.root_pid and base(f["path"]) in command
                if not writes and not named:
                    continue
                score = 0.55
                factors = [{"label": f"interpreter {base(p['exe'])} read this file", "value": 0.55}]
                if named:
                    score += 0.35
                    factors.append({"label": "the traced command line names this file", "value": 0.35})
                if writes:
                    score += 0.25
                    factors.append({"label": "file was written by another process earlier in this trace",
                                    "value": 0.25})
                evidence = [self.by_id[reads[0]["event"]]] + [self.by_id[t["event"]] for t in writes[-1:]]
                self.relate("interpreted", self.node_file(f["path"]), self.node_process(pid), evidence,
                            min(score, 0.9), "inferred", "script read by an interpreter", factors,
                            f"{self.process_label(pid)} ran the script {f['path']}",
                            at=self.by_id[reads[0]["event"]])

    def same_tree(self, a, b):
        def ancestors(pid):
            seen = []
            while pid is not None and pid not in seen:
                seen.append(pid)
                pid = self.processes[pid]["parent"] if pid in self.processes else None
            return seen
        return bool(set(ancestors(a)) & set(ancestors(b)))

    def lineage(self, pid):
        chain = []
        while pid is not None and pid in self.processes and pid not in chain:
            chain.append(pid)
            pid = self.processes[pid]["parent"]
        return list(reversed(chain))

    # ---- stage 6: findings ----------------------------------------------------------

    def finding(self, rule, severity, title, events, why):
        self.findings.append({"rule": rule, "severity": severity, "title": title,
                              "events": sorted(set(events)), "why": why})

    def build_findings(self):
        for d in self.dropped_execs:
            downloaded = next((x for x in self.downloads if x["path"] == d["path"]), None)
            if downloaded:
                self.finding("FT-DOWNLOAD-EXEC", "critical",
                             f"Downloaded file executed: {base(d['path'])}",
                             downloaded["relation"]["evidence"] + d["relation"]["evidence"],
                             f"{d['path']} arrived from {downloaded['endpoint']} and was then run. "
                             "This is the classic download-and-execute pattern.")
            else:
                self.finding("FT-DROP-EXEC", "high", f"File created during the trace was executed: {base(d['path'])}",
                             d["relation"]["evidence"],
                             f"{d['path']} did not exist as an executable before this run started writing it.")
        for f in self.files.values():
            ops = f["ops"]
            if f["category"] == "sensitive":
                denied = ops.get("read_denied", 0) + ops.get("write_denied", 0)
                touched = ops.get("opened", 0) + ops.get("read", 0)
                changed = ops.get("wrote", 0) + ops.get("overwritten", 0) + ops.get("opened_for_write", 0)
                # /etc/passwd and /etc/group are world-readable and looked up by normal programs
                routine = f["path"] in ("/etc/passwd", "/etc/group") and not denied and not changed
                if (denied or touched or changed) and not routine:
                    verb = "denied access to" if denied and not touched else "accessed"
                    self.finding("FT-SENSITIVE-FILE", "high", f"Process {verb} {f['path']}", f["events"][:20],
                                 "Attempts on credential or privilege files are evidence even when they fail.")
            if ops.get("executed") and f["temp"] and not any(d["path"] == f["path"] for d in self.dropped_execs):
                self.finding("FT-EXEC-TEMP", "medium", f"Program run from a temporary directory: {base(f['path'])}",
                             f["events"][:20], "Legitimate software rarely runs from world-writable directories.")
            if ops.get("overwritten") and f["category"] in ("user", "sensitive"):
                self.finding("FT-OVERWRITE", "medium", f"File overwritten during the trace: {base(f['path'])}",
                             [t["event"] for t in f["timeline"] if t["op"] in ("overwritten", "wrote")],
                             f"{f['path']} was truncated and rewritten after it already held content from this run.")
            if ops.get("deleted") and f["category"] in ("user", "sensitive"):
                wrote = [t for t in f["timeline"] if t["op"] in ("created", "overwritten", "wrote")]
                gone = [t for t in f["timeline"] if t["op"] == "deleted"]
                if wrote and any(g["event"] > wrote[0]["event"] for g in gone):
                    self.finding("FT-CREATE-DELETE", "medium", f"File created and then deleted: {base(f['path'])}",
                                 [wrote[0]["event"]] + [g["event"] for g in gone],
                                 "Short-lived files can indicate an attempt to remove traces.")
        for c in self.connections:
            if c["direction"] != "outbound" or c.get("probe") or c["state"] == "failed" or c["dst_host"] is None:
                continue
            descended = any(d["pid"] in self.lineage(c["pid"]) for d in self.dropped_execs)
            if descended:
                self.finding("FT-PAYLOAD-OUTBOUND", "high",
                             f"Executed payload connected out to {c['endpoint']}",
                             [c["event"]] + c["data_events"][:5],
                             "A process descended from a file dropped during this trace opened a network connection.")
            elif c["scope"] in ("public", "unknown"):
                self.finding("FT-OUTBOUND", "low", f"Outbound connection to {c['endpoint']}", [c["event"]],
                             "Recorded for review; an outbound connection alone is not suspicious.")
        if self.doc.get("truncated"):
            self.finding("FT-EVIDENCE-TRUNCATED", "high", "Evidence is incomplete: the event cap was reached", [],
                         "Events after the cap were dropped, so this reconstruction may miss later activity.")
        if self.doc.get("untraced_processes"):
            self.finding("FT-EVIDENCE-UNTRACED", "high", "Some processes were not traced", [],
                         f"{self.doc['untraced_processes']} processes exceeded the tracer's limit.")
        order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        self.findings.sort(key=lambda x: (order[x["severity"]], x["events"][0] if x["events"] else 0))

    # ---- stage 7: answers ---------------------------------------------------------

    def build_answers(self):
        not_file = None if self.collected["file"] else f"not collected: configuration {self.config} records no file events"
        not_net = None if self.collected["network"] else f"not collected: configuration {self.config} records no network events"
        root = self.processes.get(self.root_pid)
        answers = {"initiator": None, "downloads": [], "downloads_note": None, "affected_files": [],
                   "affected_files_note": not_file, "endpoints": [], "endpoints_note": not_net,
                   "executions": [], "chain": []}
        if root:
            first = self.events[0]
            answers["initiator"] = {
                "pid": root["pid"], "exe": root["exe"], "uid": root["uid"], "command": self.doc.get("command", ""),
                "evidence": [first["id"]], "confidence": 0.99,
                "basis": "first event of the trace; the traced command was started by ForensicTrace itself",
            }
        if not_file or not_net:
            answers["downloads_note"] = not_net or not_file
        elif not self.downloads:
            answers["downloads_note"] = "no process received network data and then wrote a non-system file"
        for d in self.downloads:
            rel = d["relation"]
            answers["downloads"].append({
                "pid": d["pid"], "exe": self.processes[d["pid"]]["exe"], "file": d["path"], "endpoint": d["endpoint"],
                "bytes": rel.get("bytes", 0), "evidence": rel["evidence"], "confidence": rel["confidence"],
                "lineage": [{"pid": p, "exe": self.processes[p]["exe"]} for p in self.lineage(d["pid"])],
            })
        for d in self.dropped_execs:
            answers["executions"].append({"file": d["path"], "pid": d["pid"], "exe": self.processes[d["pid"]]["exe"],
                                          "evidence": d["relation"]["evidence"],
                                          "confidence": d["relation"]["confidence"]})
        for f in self.files.values():
            changed = {k: v for k, v in f["ops"].items()
                       if k in ("created", "overwritten", "wrote", "deleted", "chmod",
                                "read_denied", "write_denied", "opened_for_write")}
            if not changed or not self.file_is_relevant(f):
                continue
            rels = [r for r in self.relations if r["dst"] == f"f:{f['path']}" or r["src"] == f"f:{f['path']}"]
            answers["affected_files"].append({
                "path": f["path"], "category": f["category"], "ops": changed,
                "processes": [{"pid": p, "exe": self.processes[p]["exe"]} for p in sorted(f["processes"])],
                "bytes_written": f["bytes_written"], "evidence": f["events"][:20],
                "confidence": max((r["confidence"] for r in rels), default=0.9),
            })
        seen = {}
        for c in self.connections:
            if c["direction"] != "outbound" or c.get("probe") or c["dst_host"] is None:
                continue
            item = seen.get(c["endpoint"])
            if item is None:
                item = seen[c["endpoint"]] = {
                    "endpoint": c["endpoint"], "scope": c["scope"], "proto": c["proto"], "state": c["state"],
                    "processes": [], "evidence": [], "bytes_sent": 0, "bytes_received": 0,
                    "confidence": 0.97 if c["state"] in ("established", "failed") else 0.7,
                }
            item["processes"].append({"pid": c["pid"], "exe": c["exe"]})
            item["evidence"].append(c["event"])
            item["bytes_sent"] += c["bytes_sent"]
            item["bytes_received"] += c["bytes_received"]
        answers["endpoints"] = list(seen.values())
        answers["chain"] = self.attack_chain()
        # files on the attack chain first, plain deletions (often clean-up) last
        on_chain = {e["dst"] for e in self.relations if e["id"] in answers["chain"]}
        answers["affected_files"].sort(key=lambda f: (f"f:{f['path']}" not in on_chain, set(f["ops"]) == {"deleted"}))
        return answers

    def attack_chain(self):
        """Ordered path through the incident; its strength is its weakest relation."""
        by_pair = {(r["kind"], r["src"], r["dst"]): r for r in self.relations}
        steps = []

        def add(kind, src, dst):
            r = by_pair.get((kind, src, dst))
            if r and r not in steps:
                steps.append(r)

        target = self.dropped_execs[0] if self.dropped_execs else None
        for d in self.dropped_execs:
            if any(x["path"] == d["path"] for x in self.downloads):
                target = d
                break
        down = None
        if target:
            down = next((x for x in self.downloads if x["path"] == target["path"]), None)
        elif self.downloads:
            down = self.downloads[0]
        if not target and not down:
            return []
        start = down["pid"] if down else target["writer"]
        lineage = self.lineage(start)
        for a, b in zip(lineage, lineage[1:]):
            add("spawned", f"p:{a}", f"p:{b}")
        def add_lineage(pid):
            chain = self.lineage(pid)
            for a, b in zip(chain, chain[1:]):
                add("spawned", f"p:{a}", f"p:{b}")

        for r in self.relations:
            if r["kind"] == "interpreted" and r["dst"] in {f"p:{p}" for p in lineage}:
                steps.append(r)
                for w in self.relations:    # who wrote the script that was run
                    if w["kind"] == "created" and w["dst"] == r["src"]:
                        steps.append(w)
                        add_lineage(int(w["src"][2:]))
        if down:
            ep = f"n:{down['endpoint']}"
            add("connected", f"p:{down['pid']}", ep)
            add("created", f"p:{down['pid']}", f"f:{down['path']}")
            steps.append(down["relation"])
        if target:
            path = f"f:{target['path']}"
            add("created", f"p:{target['writer']}", path)
            for r in self.relations:
                if r["dst"] == path and r["kind"] == "chmod" and r.get("adds_exec"):
                    steps.append(r)
                    add_lineage(int(r["src"][2:]))
            ex_lineage = self.lineage(target["pid"])
            for a, b in zip(ex_lineage, ex_lineage[1:]):
                add("spawned", f"p:{a}", f"p:{b}")
            steps.append(target["relation"])
            # what the payload then did: everything below the executed process
            descendants, frontier = set(), [target["pid"]]
            while frontier:
                pid = frontier.pop()
                if pid in descendants:
                    continue
                descendants.add(pid)
                frontier.extend(self.processes[pid]["children"])
            for r in self.relations:
                src_pid = int(r["src"][2:]) if r["src"].startswith("p:") else None
                if src_pid in descendants and r["kind"] in ("created", "overwritten", "wrote", "deleted", "connected",
                                                            "connect_failed", "downloaded", "chmod", "read_denied"):
                    steps.append(r)
                elif src_pid in descendants and r["kind"] == "spawned":
                    dst_pid = int(r["dst"][2:])
                    if self.has_effect(dst_pid):
                        steps.append(r)
        unique = []
        for r in steps:
            if r not in unique:
                unique.append(r)
        unique.sort(key=lambda r: r["ms"])
        return [r["id"] for r in unique]

    def has_effect(self, pid):
        key = f"p:{pid}"
        return any(r["src"] == key and r["kind"] not in ("spawned", "read") for r in self.relations)

    # ---- assembly -------------------------------------------------------------------

    def run(self):
        self.by_id = {e["id"]: e for e in self.events}
        self.root_pid = self.events[0]["pid"] if self.events else None
        self.build_processes()
        self.build_files()
        self.build_connections()
        self.observed_relations()
        self.infer_downloads()
        self.infer_execution()
        self.infer_interpretation()
        self.build_findings()
        answers = self.build_answers()
        self.mark_noise()
        return self.result(answers)

    def mark_noise(self):
        """Processes with no effect and no effective descendant are hidden by default."""
        effective = set()
        for r in self.relations:
            if r["kind"] == "spawned":
                continue
            for key in (r["src"], r["dst"]):
                if key.startswith("p:"):
                    effective.add(int(key[2:]))
        for pid in list(effective):
            effective.update(self.lineage(pid))
        for node in self.nodes.values():
            if node["type"] == "process":
                node["noise"] = node["pid"] not in effective
            elif node["type"] == "file":
                only_read = all(r["kind"] == "read" for r in self.relations
                                if r["dst"] == node["id"] or r["src"] == node["id"])
                node["noise"] = only_read
            else:
                node["noise"] = False

    def signal_events(self):
        """Events worth showing first: everything except program start-up and resolver noise."""
        cited = {i for r in self.relations for i in r["evidence"]}
        cited |= {i for f in self.findings for i in f["events"]}
        relevant = {f["path"] for f in self.files.values() if self.file_is_relevant(f)}
        keep = []
        for e in self.events:
            target = e.get("target", "")
            if e["id"] in cited or e["type"] == "process" or (e["type"] == "file" and target in relevant):
                keep.append(e["id"])
        for c in self.connections:
            if not c.get("probe"):
                keep.append(c["event"])
                keep.extend(c["data_events"])
        return sorted(set(keep))

    def result(self, answers):
        relevant_files = [f for f in self.files.values() if self.file_is_relevant(f)]
        suspicious = [f for f in self.findings if f["severity"] in ("critical", "high", "medium")]
        by_type = defaultdict(int)
        for e in self.events:
            by_type[e["type"]] += 1
        # a loopback connection seen from both ends is one connection, not two
        connections = [c for c in self.connections if not c.get("probe")
                       and not (c["direction"] == "inbound" and "peer_pid" in c)]
        processes = []
        for p in self.processes.values():
            item = dict(p)
            item["counts"] = dict(p["counts"])
            processes.append(item)
        files = []
        for f in sorted(self.files.values(), key=lambda x: x["first_ms"]):
            item = dict(f)
            item["ops"] = dict(f["ops"])
            item["processes"] = sorted(f["processes"])
            item["relevant"] = self.file_is_relevant(f)
            item["timeline"] = f["timeline"][:200]
            files.append(item)
        rel_ids = {r["id"] for r in self.relations}
        return {
            "signal_events": self.signal_events(),
            "collected": self.collected,
            "summary": {
                "processes": len(self.processes),
                "syscalls": len(self.events),
                "files_accessed": len(self.files),
                "files_relevant": len(relevant_files),
                "connections": len(connections),
                "connections_filtered": sum(1 for c in self.connections if c.get("probe")),
                "suspicious": len(suspicious),
                "findings_by_severity": _count(f["severity"] for f in self.findings),
                "events_by_type": dict(by_type),
                "duration_ms": round(self.doc.get("duration_ns", 0) / 1e6, 3),
                "inferred_relations": sum(1 for r in self.relations if r["tier"] == "inferred"),
                "observed_relations": sum(1 for r in self.relations if r["tier"] == "observed"),
            },
            "processes": processes,
            "root_pid": self.root_pid,
            "files": files,
            "connections": self.connections,
            "unix_connections": [{"event": e["id"], "pid": e["pid"], "target": e["target"],
                                  "ret": e.get("ret")} for e in self.unix_connections],
            "graph": {"nodes": list(self.nodes.values()),
                      "edges": [r for r in self.relations if r["id"] in rel_ids]},
            "findings": self.findings,
            "answers": answers,
        }


def _count(items):
    out = defaultdict(int)
    for item in items:
        out[item] += 1
    return dict(out)


def _adds_exec(mode):
    try:
        return bool(int(mode, 8) & 0o111)
    except (TypeError, ValueError):
        return False


def reconstruct(doc):
    return Reconstruction(doc).run()


def print_text(result):
    s = result["summary"]
    print(f"{s['processes']} processes, {s['syscalls']} events, {s['files_relevant']} relevant files, "
          f"{s['connections']} connections, {s['suspicious']} suspicious findings")
    a = result["answers"]
    if a["initiator"]:
        print(f"\nInitiated by : pid {a['initiator']['pid']}  {a['initiator']['command']}")
    for d in a["downloads"]:
        print(f"Downloaded   : {d['file']} from {d['endpoint']} by pid {d['pid']} ({d['confidence']:.0%}, "
              f"events {d['evidence']})")
    if a["downloads_note"]:
        print(f"Downloads    : {a['downloads_note']}")
    for e in a["executions"]:
        print(f"Executed     : {e['file']} as pid {e['pid']} ({e['confidence']:.0%})")
    for f in a["affected_files"]:
        print(f"File affected: {f['path']}  {', '.join(sorted(f['ops']))}")
    if a["affected_files_note"]:
        print(f"Files        : {a['affected_files_note']}")
    for n in a["endpoints"]:
        print(f"Endpoint     : {n['endpoint']}/{n['proto']} ({n['scope']}, {n['state']})")
    if a["endpoints_note"]:
        print(f"Endpoints    : {a['endpoints_note']}")
    if result["findings"]:
        print("\nFindings")
        for f in result["findings"]:
            print(f"  [{f['severity']:<8}] {f['rule']:<20} {f['title']}")
    edges = {r["id"]: r for r in result["graph"]["edges"]}
    if a["chain"]:
        print("\nReconstructed chain (weakest link "
              f"{min(edges[i]['confidence'] for i in a['chain']):.0%})")
        for i in a["chain"]:
            r = edges[i]
            print(f"  {r['ms']:>10.3f} ms  {r['confidence']:.0%}  {r['tier']:<8}  {r['summary']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("evidence")
    ap.add_argument("--json", action="store_true", help="print the full reconstruction as JSON")
    ap.add_argument("-o", "--output", help="write the full reconstruction as JSON to this file")
    args = ap.parse_args()
    result = reconstruct(load_evidence(args.evidence))
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=1)
    if args.json:
        json.dump(result, sys.stdout, indent=1)
    elif not args.output:
        print_text(result)


if __name__ == "__main__":
    main()
