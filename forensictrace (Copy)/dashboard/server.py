#!/usr/bin/env python3
"""ForensicTrace dashboard: a local web interface over the C engine's evidence.

The dashboard never collects or rewrites evidence itself. It reads the JSON files
the engine wrote, derives the views with scripts/reconstruct.py, and calls the
forensictrace binary for tracing, verification and export.

Standard library only, so it runs on an isolated analysis machine.

  python3 dashboard/server.py [--port 8377] [--evidence-dir DIR] [--sign-key KEY]

It binds to 127.0.0.1 only. Evidence is untrusted input (a trace can contain any
file name), and starting a trace runs a program, so requests are restricted to
this origin and state-changing calls need the token from /api/session.
"""
import argparse
import csv
import json
import os
import re
import secrets
import statistics
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import reconstruct  # noqa: E402

STATIC = Path(__file__).resolve().parent / "static"
STATIC_FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
}
BINARY = ROOT / "forensictrace"
CASES_DIR = ROOT / "cases"
EXPORTS_DIR = ROOT / "exports"
DEFAULT_KEY = Path.home() / ".config" / "forensictrace" / "investigator.key"
EXAMPLES_PUBKEY = ROOT / "docs" / "examples" / "custody_demo" / "demo.key.pub"

CSP = ("default-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; "
       "connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")

CONFIG_NAMES = {"A": "Process", "B": "Process + file", "C": "Process + file + network", "D": "All syscalls"}
# Sufficiency thresholds of the study (docs/limitations.md section 3)
QUALITY = [("coverage_pct", "Event coverage", "%", 80), ("accuracy_pct", "Reconstruction accuracy", "%", 80),
           ("ordering_pct", "Ordering correctness", "%", 70), ("explainability", "Explainability", "/15", 10)]
COST = [("storage_kb", "Storage", "KB"), ("tracer_cpu_ms", "Tracer CPU", "ms"),
        ("processing_ms", "Processing time", "ms"), ("events", "Events recorded", "")]
HEADER_RE = {
    "scenario": re.compile(r'"scenario":\s*"([^"]*)"'),
    "config": re.compile(r'"config":\s*"([^"]*)"'),
    "mode": re.compile(r'"collection_mode":\s*"([^"]*)"'),
    "events": re.compile(r'"event_count":\s*(\d+)'),
    "schema": re.compile(r'"schema_version":\s*(\d+)'),
    "case_id": re.compile(r'"case_id":\s*"([^"]*)"'),
    "investigator": re.compile(r'"investigator":\s*"([^"]*)"'),
    "started": re.compile(r'"started_utc":\s*"([^"]*)"'),
}


class ApiError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


class Store:
    """Evidence locations, the session token and a small reconstruction cache."""

    def __init__(self, extra_dirs, sign_key, pubkey):
        self.token = secrets.token_urlsafe(24)
        self.sign_key = sign_key
        self.pubkey = pubkey
        self.roots = [
            ("cases", "Investigations", CASES_DIR, True),
            ("examples", "Examples", ROOT / "docs" / "examples", False),
            ("runs", "Study runs (ptrace)", ROOT / "experiments" / "runs", False),
            ("runs_seccomp", "Study runs (seccomp)", ROOT / "experiments" / "runs_seccomp", False),
        ]
        for i, d in enumerate(extra_dirs):
            self.roots.insert(1 + i, (f"dir{i}", f"Evidence: {d}", Path(d).resolve(), True))
        self.cache = {}
        self.cache_lock = threading.Lock()
        self.run_lock = threading.Lock()
        self.scenarios = self._load_scenarios()

    @staticmethod
    def _load_scenarios():
        out = {}
        for path in sorted((ROOT / "scenarios" / "ground_truth").glob("scenario*.json")):
            gt = json.loads(path.read_text(encoding="utf-8"))
            script = ROOT / "scenarios" / gt["script"]
            if script.is_file():
                out[gt["scenario"]] = {"script": script, "description": gt["description"]}
        return out

    def list_cases(self):
        cases = []
        for key, label, root, writable in self.roots:
            if not root.is_dir():
                continue
            for path in root.rglob("*.json"):
                if path.name.endswith(".manifest.json"):
                    continue
                meta = self._header(path)
                if meta is None:
                    continue
                rel = path.relative_to(root).as_posix()
                cases.append({"id": f"{key}/{rel}", "group": label, "name": path.stem, "writable": writable,
                              "modified": path.stat().st_mtime, **meta})
        order = {r[1]: i for i, r in enumerate(self.roots)}
        cases.sort(key=lambda c: (order[c["group"]], -c["modified"] if c["writable"] else 0, c["name"]))
        return cases

    @staticmethod
    def _header(path):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                head = fh.read(4096)
        except OSError:
            return None
        if '"event_count"' not in head:
            return None
        meta = {}
        for key, rx in HEADER_RE.items():
            m = rx.search(head)
            meta[key] = m.group(1) if m else ""
        return meta

    def resolve(self, case_id):
        """Map a case id to a file; the id must name a real file inside a known root."""
        key, _, rel = (case_id or "").partition("/")
        for k, _label, root, writable in self.roots:
            if k == key:
                path = (root / rel).resolve()
                if path.is_relative_to(root.resolve()) and path.suffix == ".json" and path.is_file():
                    return path, writable, k
        raise ApiError(404, "unknown case")

    def pubkey_for(self, root_key, path):
        """The key evidence here must be signed by. Reference data predates signing."""
        if root_key == "examples":
            signed_demo = path.parent == EXAMPLES_PUBKEY.parent and EXAMPLES_PUBKEY.is_file()
            return EXAMPLES_PUBKEY if signed_demo else None
        if root_key in ("runs", "runs_seccomp"):
            return None
        return self.pubkey

    def case(self, case_id):
        path, writable, root_key = self.resolve(case_id)
        stamp = (str(path), path.stat().st_mtime_ns)
        with self.cache_lock:
            hit = self.cache.get(stamp)
        if hit is None:
            try:
                doc = reconstruct.load_evidence(path)
                hit = {"doc": doc, "analysis": reconstruct.reconstruct(doc)}
            except (ValueError, KeyError, TypeError, AttributeError, IndexError) as err:
                # A tampered file may no longer parse; custody can still report on it.
                raise ApiError(422, f"evidence cannot be read: {err}") from err
            with self.cache_lock:
                if len(self.cache) >= 8:
                    self.cache.pop(next(iter(self.cache)))
                self.cache[stamp] = hit
        report = path.with_suffix(".md")
        return {"id": case_id, "writable": writable, "has_report": report.is_file(), **hit}

    def verify(self, case_id, audit=False, investigator=None):
        path, writable, root_key = self.resolve(case_id)
        if not BINARY.is_file():
            raise ApiError(503, "forensictrace binary not found: run make")
        cmd = [str(BINARY), "verify", str(path), "--json"]
        if not (audit and writable):
            cmd.append("--no-audit")
        pub = self.pubkey_for(root_key, path)
        if pub:
            cmd += ["--pubkey", str(pub)]
        if investigator:
            cmd += ["--investigator", investigator]
        p = subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=120, cwd=ROOT)
        if p.returncode not in (0, 1):
            raise ApiError(500, p.stderr.strip() or "verification could not run")
        result = json.loads(p.stdout)
        result["pinned_key"] = str(pub) if pub else None
        return result

    def custody(self, case_id):
        path, writable, _ = self.resolve(case_id)
        out = {"verification": self.verify(case_id), "manifest": None, "audit": [], "writable": writable}
        manifest = Path(f"{path}.manifest.json")
        if manifest.is_file():
            try:
                out["manifest"] = json.loads(manifest.read_text(encoding="utf-8", errors="replace"))
            except ValueError:
                out["manifest"] = None
        audit = Path(f"{path}.audit.jsonl")
        if audit.is_file():
            for line in audit.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    out["audit"].append(json.loads(line))
                except ValueError:
                    out["audit"].append({"action": "unreadable entry", "detail": line[:200]})
        return out

    def export(self, case_id, investigator):
        path, writable, root_key = self.resolve(case_id)
        if not writable:
            raise ApiError(403, "this evidence is read-only reference data")
        dest = EXPORTS_DIR / f"{path.stem}_{time.strftime('%Y%m%d-%H%M%S')}"
        cmd = [str(BINARY), "export", str(path), "--to", str(dest)]
        pub = self.pubkey_for(root_key, path)
        if pub:
            cmd += ["--pubkey", str(pub)]
        if investigator:
            cmd += ["--investigator", investigator]
        p = subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=120, cwd=ROOT)
        if p.returncode == 2:
            raise ApiError(500, p.stderr.strip() or "export failed")
        return {"directory": str(dest.relative_to(ROOT)), "verified": p.returncode == 0,
                "files": sorted(x.name for x in dest.iterdir())}

    def investigate(self, scenario, config, mode, investigator, case_id):
        if scenario not in self.scenarios:
            raise ApiError(400, "unknown scenario")
        if config not in CONFIG_NAMES or mode not in ("ptrace", "seccomp"):
            raise ApiError(400, "invalid configuration or mode")
        if not re.fullmatch(r"[A-Za-z0-9._-]{1,64}", case_id):
            raise ApiError(400, "case id may use letters, digits, dot, dash and underscore (64 at most)")
        if not 0 < len(investigator) <= 100 or not investigator.isprintable():
            raise ApiError(400, "enter an investigator name of at most 100 characters")
        if not BINARY.is_file():
            raise ApiError(503, "forensictrace binary not found: run make")
        CASES_DIR.mkdir(exist_ok=True)
        stem = f"{case_id}_{scenario}_{config}_{time.strftime('%Y%m%d-%H%M%S')}"
        output = CASES_DIR / f"{stem}.json"
        cmd = [str(BINARY), "--config", config, "--mode", mode, "--output", str(output),
               "--report", str(CASES_DIR / f"{stem}.md"), "--scenario", scenario, "--quiet",
               "--investigator", investigator, "--case", case_id]
        if self.sign_key:
            cmd += ["--sign-key", str(self.sign_key)]
        cmd += ["--", "bash", str(self.scenarios[scenario]["script"].relative_to(ROOT))]
        # Scenarios use fixed ports and work directories, so one runs at a time.
        if not self.run_lock.acquire(blocking=False):
            raise ApiError(409, "another investigation is running")
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=180, cwd=ROOT)
        finally:
            self.run_lock.release()
        if p.returncode != 0 or not output.is_file():
            raise ApiError(500, "tracing failed: " + (p.stderr.strip()[-300:] or "no output"))
        return {"id": f"cases/{output.name}", "signed": bool(self.sign_key)}

    def compare(self, mode, scenario):
        name = "results" if mode == "ptrace" else "results_seccomp"
        path = ROOT / name / "results.csv"
        if not path.is_file():
            raise ApiError(404, "experiment results not found")
        with open(path, newline="", encoding="utf-8") as fh:
            rows = [r for r in csv.DictReader(fh) if scenario == "ALL" or r["scenario"] == scenario]
        if not rows:
            raise ApiError(404, "no runs for that scenario")
        configs = []
        for cfg, label in CONFIG_NAMES.items():
            subset = [r for r in rows if r["config"] == cfg]
            metrics = {}
            for key, *_rest in QUALITY + COST:
                vals = [float(r[key]) for r in subset]
                metrics[key] = {"mean": statistics.fmean(vals), "min": min(vals), "max": max(vals)}
            # The study's rule (scripts/analyze.py): every run must meet every threshold.
            sufficient = all(metrics[k]["min"] >= t for k, _l, _u, t in QUALITY)
            configs.append({"config": cfg, "label": label, "runs": len(subset), "metrics": metrics,
                            "sufficient": sufficient})
        return {"mode": mode, "scenario": scenario, "configs": configs,
                "quality": [{"key": k, "label": l, "unit": u, "threshold": t} for k, l, u, t in QUALITY],
                "cost": [{"key": k, "label": l, "unit": u} for k, l, u in COST],
                "scenarios": sorted({r["scenario"] for r in rows}) if scenario != "ALL" else None}


class Handler(BaseHTTPRequestHandler):
    store = None
    port = 0
    server_version = "ForensicTraceDashboard"

    def log_message(self, fmt, *args):
        pass

    def _send(self, status, body, ctype="application/json; charset=utf-8", extra=None):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Content-Security-Policy", CSP)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, status=200):
        self._send(status, json.dumps(obj, ensure_ascii=False, separators=(",", ":"), default=str)
                   .encode("utf-8", "replace"))

    def _host_ok(self):
        # A page on another site can point its own DNS name at 127.0.0.1; reject that.
        return self.headers.get("Host", "") in (f"127.0.0.1:{self.port}", f"localhost:{self.port}")

    def _dispatch(self, fn):
        if not self._host_ok():
            self._json({"error": "forbidden host"}, 403)
            return
        try:
            fn()
        except ApiError as err:
            self._json({"error": err.message}, err.status)
        except subprocess.TimeoutExpired:
            self._json({"error": "the engine did not finish in time"}, 504)
        except BrokenPipeError:
            pass
        except Exception as err:  # the dashboard must stay up whatever a file contains
            print(f"[dashboard] {type(err).__name__}: {err}", file=sys.stderr)
            self._json({"error": f"internal error: {type(err).__name__}"}, 500)

    def do_GET(self):
        self._dispatch(self._get)

    def do_POST(self):
        self._dispatch(self._post)

    def _get(self):
        url = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        store = self.store
        if url.path in STATIC_FILES:
            name, ctype = STATIC_FILES[url.path]
            self._send(200, (STATIC / name).read_bytes(), ctype)
        elif url.path == "/api/session":
            self._json({"token": store.token, "signing": bool(store.sign_key),
                        "default_key": str(DEFAULT_KEY), "user": os.environ.get("USER", ""),
                        "binary": BINARY.is_file(), "config_names": CONFIG_NAMES,
                        "scenarios": {k: v["description"] for k, v in store.scenarios.items()}})
        elif url.path == "/api/cases":
            self._json({"cases": store.list_cases()})
        elif url.path == "/api/case":
            self._json(store.case(q.get("id")))
        elif url.path == "/api/custody":
            self._json(store.custody(q.get("id")))
        elif url.path == "/api/compare":
            self._json(store.compare(q.get("mode", "ptrace"), q.get("scenario", "ALL")))
        elif url.path == "/api/report":
            path, _w, _k = store.resolve(q.get("id"))
            report = path.with_suffix(".md")
            if not report.is_file():
                raise ApiError(404, "this case has no report")
            self._send(200, report.read_bytes(), "text/plain; charset=utf-8",
                       {"Content-Disposition": f'attachment; filename="{re.sub(r"[^A-Za-z0-9._-]", "_", report.name)}"'})
        else:
            raise ApiError(404, "not found")

    def _post(self):
        if self.headers.get("X-FT-Token") != self.store.token:
            raise ApiError(403, "missing session token")
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            raise ApiError(415, "expected JSON")
        length = int(self.headers.get("Content-Length") or 0)
        if length > 65536:
            raise ApiError(413, "request too large")
        body = json.loads(self.rfile.read(length) or b"{}")
        path = urlparse(self.path).path
        who = str(body.get("investigator", "")).strip()[:100]
        if path == "/api/verify":
            self._json(self.store.verify(body.get("id"), audit=True, investigator=who or None))
        elif path == "/api/export":
            self._json(self.store.export(body.get("id"), who or None))
        elif path == "/api/investigate":
            self._json(self.store.investigate(str(body.get("scenario", "")), str(body.get("config", "")),
                                              str(body.get("mode", "ptrace")), who, str(body.get("case_id", "")).strip()))
        else:
            raise ApiError(404, "not found")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8377)
    ap.add_argument("--evidence-dir", action="append", default=[], help="extra folder of evidence JSON files")
    ap.add_argument("--sign-key", help=f"Ed25519 key for new investigations (default {DEFAULT_KEY} if present)")
    ap.add_argument("--pubkey", help="public key that evidence must be signed by (default: the signing key's .pub)")
    args = ap.parse_args()

    sign_key = Path(args.sign_key) if args.sign_key else (DEFAULT_KEY if DEFAULT_KEY.is_file() else None)
    pubkey = Path(args.pubkey) if args.pubkey else (Path(f"{sign_key}.pub") if sign_key else None)
    if pubkey and not pubkey.is_file():
        pubkey = None
    Handler.store = Store(args.evidence_dir, sign_key, pubkey)
    Handler.port = args.port
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    server.daemon_threads = True
    print(f"ForensicTrace dashboard: http://127.0.0.1:{args.port}")
    if not sign_key:
        print(f"New investigations will be UNSIGNED. Create a key with: make keys ({DEFAULT_KEY})")
    if not BINARY.is_file():
        print("forensictrace binary not found: run make to enable tracing and verification")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
