#!/usr/bin/env python3
"""Attack the custody chain and check that `forensictrace verify` catches each attack.

Every attack starts from a fresh signed copy of one real run. The hash chain is
recomputed here, independently of the C code, which also proves that
docs/custody.md specifies the format completely.

Prints one "[PASS] name" or "[FAIL] name" per check; run_tests.sh counts them.
Usable on its own for a demonstration:  python3 tests/test_custody.py
"""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIN = str(ROOT / "forensictrace")
EVENT_FIELDS = ["event_uid", "id", "ts_ns", "ts_wall", "type", "syscall", "pid", "ppid", "uid",
                "exe", "target", "detail", "ret", "parent_event", "resource_event"]
HEADER_FIELDS = ["session_id", "case_id", "investigator", "os_user", "hostname", "kernel", "scenario", "command",
                 "config", "collection_mode", "started_utc", "finished_utc", "event_count", "raw_event_count",
                 "dropped_failed_exec", "truncated", "untraced_processes"]
failures = 0


def report(ok, name, note=""):
    global failures
    failures += 0 if ok else 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{f' ({note})' if note and not ok else ''}")


def text(value):
    """A JSON value as the chain hashes it."""
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    return str(value)


def hash_fields(prefix, names, values):
    h = hashlib.sha256()
    h.update(prefix.encode() + b"\n")
    for name, value in zip(names, values):
        raw = text(value).encode("utf-8", "surrogateescape")
        h.update(f"{name}={len(raw)}:".encode() + raw + b"\n")
    return h.hexdigest()


def event_hash(prev, event):
    return hash_fields(prev, EVENT_FIELDS, [event[k] for k in EVENT_FIELDS])


def genesis(doc):
    c = doc["custody"]
    return hash_fields("ForensicTrace-chain-v1", HEADER_FIELDS, [doc.get(k, c.get(k)) for k in HEADER_FIELDS])


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8", errors="surrogateescape"))


def save(path, doc):
    Path(path).write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8", errors="surrogateescape")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rewrite_sidecar(path):
    Path(f"{path}.sha256").write_text(f"{sha256(path)}  {path}\n")


def rechain(doc):
    """What an attacker with full file access does: recompute every hash."""
    prev = doc["custody"]["chain_genesis"] = genesis(doc)
    for e in doc["events"]:
        e["prev_hash"] = prev
        prev = e["event_hash"] = event_hash(prev, e)
    doc["custody"]["chain_head"] = prev


def verify(path, pubkey=None):
    cmd = [BIN, "verify", str(path), "--json", "--no-audit"]
    if pubkey:
        cmd += ["--pubkey", str(pubkey)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, json.loads(p.stdout) if p.stdout.strip() else {}


def kinds(result):
    return {i["kind"] for i in result.get("issues", [])}


class Lab:
    def __init__(self, tmp):
        self.tmp = Path(tmp)
        self.key = self.tmp / "keys" / "investigator.key"
        self.pub = Path(f"{self.key}.pub")
        self.attacker_key = self.tmp / "keys" / "attacker.key"
        for key in (self.key, self.attacker_key):
            subprocess.run([BIN, "keygen", "--key", str(key)], check=True, capture_output=True)
        self.original = self.tmp / "original"
        self.original.mkdir()
        self.evidence = self.original / "run.json"
        subprocess.run([BIN, "--config", "C", "--quiet", "--investigator", "Test Analyst", "--case", "T-1",
                        "--sign-key", str(self.key), "--report", str(self.original / "run.md"),
                        "--output", str(self.evidence), "--", "/bin/sh", "-c", "echo a > /dev/null; ls /tmp > /dev/null"],
                       check=True, capture_output=True, cwd=ROOT)
        self.n = 0

    def copy(self):
        """A fresh copy of the signed run, in its own directory."""
        self.n += 1
        d = self.tmp / f"attack{self.n}"
        shutil.copytree(self.original, d)
        return d / "run.json"


def main():
    with tempfile.TemporaryDirectory(prefix="ft_custody_") as tmp:
        lab = Lab(tmp)
        doc = load(lab.evidence)
        events = doc["events"]
        middle = len(events) // 2
        middle_id = events[middle]["id"]

        # ---- evidence contents --------------------------------------------------
        c = doc.get("custody", {})
        report(doc.get("schema_version") == 3 and c.get("investigator") == "Test Analyst"
               and c.get("case_id") == "T-1" and len(c.get("session_id", "")) == 36,
               "custody: session, investigator and case recorded")
        report(all(e["event_uid"].startswith(c["session_id"]) and e["ts_wall"].endswith("Z") for e in events)
               and len({e["event_uid"] for e in events}) == len(events),
               "custody: every event has a unique id and a UTC timestamp")

        # ---- the format is fully specified: recompute it without the C code --------
        prev, ok = genesis(doc), True
        ok = prev == c["chain_genesis"]
        for e in events:
            ok = ok and e["prev_hash"] == prev and event_hash(prev, e) == e["event_hash"]
            prev = e["event_hash"]
        report(ok and prev == c["chain_head"], "custody: chain recomputed independently in Python")

        p = subprocess.run(["openssl", "pkeyutl", "-verify", "-pubin", "-inkey", str(lab.pub), "-rawin",
                            "-in", f"{lab.evidence}.manifest.json", "-sigfile", f"{lab.evidence}.manifest.sig"],
                           capture_output=True, text=True)
        report(p.returncode == 0, "custody: signature checks with stock OpenSSL", p.stderr.strip())

        rc, r = verify(lab.evidence, lab.pub)
        report(rc == 0 and r["status"] == "verified_signed_pinned", "verify: intact signed evidence passes", str(r.get("issues")))
        rc, r = verify(lab.evidence)
        report(rc == 0 and r["status"] == "verified_signed_unpinned", "verify: without a pinned key, reports signer as unproven")

        # ---- record-level findings: the verifier must name the record ---------------
        path = lab.copy()
        d = load(path)
        d["events"][middle]["target"] = "/tmp/innocent"
        save(path, d)
        rc, r = verify(path, lab.pub)
        hit = [i for i in r["issues"] if i["kind"] == "record_modified"]
        report(rc == 1 and len(hit) == 1 and hit[0]["first_event"] == middle_id,
               "attack: one field edited -> names exactly that record", str(r.get("issues")))

        path = lab.copy()
        d = load(path)
        del d["events"][middle]
        save(path, d)
        rc, r = verify(path, lab.pub)
        hit = [i for i in r["issues"] if i["kind"] == "record_missing"]
        report(rc == 1 and hit and hit[0]["first_event"] == middle_id and "chain_break" in kinds(r),
               "attack: record deleted -> names the missing record", str(r.get("issues")))

        path = lab.copy()
        d = load(path)
        d["events"] = d["events"][:-5]
        save(path, d)
        rc, r = verify(path, lab.pub)
        hit = [i for i in r["issues"] if i["kind"] == "record_missing"]
        report(rc == 1 and hit and hit[0]["first_event"] == len(events) - 4 and hit[0]["last_event"] == len(events),
               "attack: tail cut off -> names the missing range", str(r.get("issues")))

        path = lab.copy()
        d = load(path)
        d["events"][middle], d["events"][middle + 1] = d["events"][middle + 1], d["events"][middle]
        save(path, d)
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "record_out_of_order" in kinds(r), "attack: records swapped -> reported out of order", str(r.get("issues")))

        path = lab.copy()
        d = load(path)
        d["events"].insert(middle, dict(d["events"][middle]))
        save(path, d)
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "record_duplicate" in kinds(r), "attack: record duplicated -> reported", str(r.get("issues")))

        path = lab.copy()
        raw = Path(path).read_text(encoding="utf-8", errors="surrogateescape")
        needle = f'"detail": "{events[0]["detail"]}",'
        report(needle in raw, "attack setup: duplicate-key text found")
        Path(path).write_text(raw.replace(needle, needle + ' "detail": "forged",', 1), encoding="utf-8", errors="surrogateescape")
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "record_modified" in kinds(r), "attack: duplicate JSON key cannot hide an edit", str(r.get("issues")))

        path = lab.copy()
        d = load(path)
        d["custody"]["investigator"] = "Someone Else"
        save(path, d)
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "header_modified" in kinds(r), "attack: investigator changed -> header flagged", str(r.get("issues")))

        path = lab.copy()
        Path(path).write_text("{ this is no longer evidence")
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "not_json" in kinds(r), "attack: file destroyed -> reported, verifier survives", str(r.get("issues")))

        # ---- the limitation in the original report: rewrite file AND sidecar --------
        path = lab.copy()
        d = load(path)
        d["events"][middle]["target"] = "/tmp/innocent"
        rechain(d)
        save(path, d)
        rewrite_sidecar(path)
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "chain_rewritten" in kinds(r) and "sidecar_mismatch" not in kinds(r),
               "attack: file, sidecar and whole chain rewritten -> caught by signed manifest", str(r.get("issues")))

        # ... and the manifest too, re-signed with a key the attacker controls
        path = lab.copy()
        d = load(path)
        d["events"][middle]["target"] = "/tmp/innocent"
        rechain(d)
        save(path, d)
        rewrite_sidecar(path)
        manifest_path = Path(f"{path}.manifest.json")
        m = json.loads(manifest_path.read_text())
        m["evidence"].update(sha256=sha256(path), bytes=Path(path).stat().st_size,
                             chain_head=d["custody"]["chain_head"], chain_genesis=d["custody"]["chain_genesis"])
        manifest_path.write_text(json.dumps(m))
        subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey", str(lab.attacker_key), "-rawin", "-in", str(manifest_path),
                        "-out", f"{path}.manifest.sig"], check=True)
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "signature_invalid" in kinds(r), "attack: everything rewritten and re-signed -> pinned key rejects it", str(r.get("issues")))

        # ... and the same attacker removes the signature instead
        path = lab.copy()
        manifest_path = Path(f"{path}.manifest.json")
        m = json.loads(manifest_path.read_text())
        m["signature"] = None
        manifest_path.write_text(json.dumps(m))
        Path(f"{path}.manifest.sig").unlink()
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "signature_missing" in kinds(r), "attack: signature stripped -> pinned key still requires one", str(r.get("issues")))

        # ... or disguises it as old schema 2 evidence with no custody files at all
        path = lab.copy()
        d = load(path)
        del d["custody"]
        d["schema_version"] = 2
        save(path, d)
        rewrite_sidecar(path)
        for suffix in (".manifest.json", ".manifest.sig", ".audit.jsonl"):
            Path(f"{path}{suffix}").unlink()
        rc, r = verify(path, lab.pub)
        report(rc == 1, "attack: disguised as schema 2 -> pinned key rejects it", str(r.get("issues")))

        # ---- custody files -----------------------------------------------------------
        path = lab.copy()
        Path(f"{path}.manifest.sig").write_bytes(b"\0" * 64)
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "signature_invalid" in kinds(r), "attack: signature replaced -> rejected", str(r.get("issues")))

        path = lab.copy()
        Path(f"{path}.manifest.json").unlink()
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "manifest_missing" in kinds(r), "attack: manifest deleted -> reported", str(r.get("issues")))

        path = lab.copy()
        Path(Path(path).parent / "run.md").write_text("# edited report\n")
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "report_modified" in kinds(r), "attack: report edited -> reported", str(r.get("issues")))

        path = lab.copy()
        Path(f"{path}.audit.jsonl").write_text(
            Path(f"{path}.audit.jsonl").read_text().replace('"outcome":"signed"', '"outcome":"unsigned"'))
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "audit_broken" in kinds(r), "attack: audit entry edited -> reported", str(r.get("issues")))

        path = lab.copy()
        Path(f"{path}.audit.jsonl").unlink()
        rc, r = verify(path, lab.pub)
        report(rc == 1 and "audit_missing" in kinds(r), "attack: audit log deleted -> reported", str(r.get("issues")))

        # ---- audit log and export ------------------------------------------------------
        path = lab.copy()
        subprocess.run([BIN, "verify", str(path), "--pubkey", str(lab.pub), "--investigator", "Second Analyst"],
                       check=True, capture_output=True)
        bundle = Path(lab.tmp) / "bundle"
        p = subprocess.run([BIN, "export", str(path), "--to", str(bundle), "--pubkey", str(lab.pub), "--investigator", "Third Analyst"],
                           capture_output=True, text=True)
        entries = [json.loads(x) for x in Path(f"{path}.audit.jsonl").read_text().splitlines()]
        report(p.returncode == 0 and [e["action"] for e in entries] == ["generated", "verified", "exported"]
               and entries[1]["investigator"] == "Second Analyst" and entries[2]["investigator"] == "Third Analyst",
               "audit: generation, verification and export logged with who", p.stderr.strip())
        rc, r = verify(bundle / "run.json", lab.pub)
        report(rc == 0 and r["status"] == "verified_signed_pinned", "export: bundle verifies on its own", str(r.get("issues")))
        p = subprocess.run(["sha256sum", "-c", "run.json.sha256"], capture_output=True, cwd=bundle)
        report(p.returncode == 0, "export: sidecar works from inside the bundle")
        p = subprocess.run([BIN, "export", str(path), "--to", str(bundle), "--pubkey", str(lab.pub)], capture_output=True, text=True)
        report(p.returncode != 0, "export: refuses to overwrite an existing bundle")

        # ---- keys and formats -----------------------------------------------------------
        report(lab.key.stat().st_mode & 0o077 == 0, "keygen: private key readable by the owner only")
        p = subprocess.run([BIN, "keygen", "--key", str(lab.key)], capture_output=True, text=True)
        report(p.returncode != 0, "keygen: refuses to overwrite an existing key")
        out = lab.tmp / "unsigned.json"
        subprocess.run([BIN, "--config", "A", "--quiet", "--output", str(out), "--", "/bin/true"], check=True, capture_output=True)
        rc, r = verify(out)
        report(rc == 0 and r["status"] == "verified_unsigned", "verify: unsigned evidence passes but says so")
        p = subprocess.run([BIN, "--config", "A", "--quiet", "--sign-key", str(lab.tmp / "no_such.key"), "--output",
                            str(lab.tmp / "x.json"), "--", "/bin/true"], capture_output=True, text=True)
        report(p.returncode != 0 and not (lab.tmp / "x.json").exists(), "signing: bad key fails before tracing starts")
        out = lab.tmp / "baseline.json"
        subprocess.run([BIN, "--config", "C", "--quiet", "--baseline-format", "--output", str(out), "--", "/bin/true"],
                       check=True, capture_output=True)
        d = load(out)
        extras = [f"{out}{x}" for x in (".manifest.json", ".manifest.sig", ".audit.jsonl")]
        report(d["schema_version"] == 2 and "custody" not in d and "event_hash" not in d["events"][0]
               and not any(Path(x).exists() for x in extras), "baseline format: schema 2 with no custody files")
        rc, r = verify(out)
        report(rc == 0 and r["status"] == "legacy_sidecar_ok", "verify: schema 2 evidence reported as sidecar only")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
