#!/usr/bin/env python3
"""End-to-end checks of the dashboard server against the real binary.

Prints one "[PASS] name" or "[FAIL] name" per check; run_tests.sh counts them.
"""
import http.client
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures = 0


def report(ok, name, note=""):
    global failures
    failures += 0 if ok else 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{f' ({note})' if note and not ok else ''}")


class Client:
    def __init__(self, port):
        self.port = port
        self.token = None

    def request(self, method, path, body=None, headers=None):
        c = http.client.HTTPConnection("127.0.0.1", self.port, timeout=180)
        hdrs = dict(headers or {})
        data = None
        if body is not None:
            data = json.dumps(body)
            hdrs.setdefault("Content-Type", "application/json")
            if self.token:
                hdrs.setdefault("X-FT-Token", self.token)
        c.request(method, path, data, hdrs)
        r = c.getresponse()
        raw = r.read()
        c.close()
        try:
            parsed = json.loads(raw)
        except ValueError:
            parsed = raw
        return r.status, parsed, dict(r.getheaders())


def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def main():
    with tempfile.TemporaryDirectory(prefix="ft_dash_") as tmp:
        evidence_dir = Path(tmp) / "evidence"
        evidence_dir.mkdir()
        key = Path(tmp) / "k" / "inv.key"
        subprocess.run([str(ROOT / "forensictrace"), "keygen", "--key", str(key)], check=True, capture_output=True)

        # hostile file name inside the evidence: the page must treat it as text
        hostile = Path(tmp) / "<img src=x onerror=alert(1)>.txt"
        subprocess.run([str(ROOT / "forensictrace"), "--config", "C", "--quiet", "--sign-key", str(key), "--output",
                        str(evidence_dir / "hostile.json"), "--", "/bin/sh", "-c", f"echo x > '{hostile}'"],
                       check=True, capture_output=True)

        port = free_port()
        server = subprocess.Popen([sys.executable, str(ROOT / "dashboard" / "server.py"), "--port", str(port),
                                   "--evidence-dir", str(evidence_dir), "--sign-key", str(key)],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        api = Client(port)
        try:
            for _ in range(50):
                try:
                    api.request("GET", "/api/session")
                    break
                except OSError:
                    time.sleep(0.1)

            status, body, headers = api.request("GET", "/")
            report(status == 200 and b"ForensicTrace" in body, "dashboard: page is served")
            csp = headers.get("Content-Security-Policy", "")
            report("script-src 'self'" in csp and "unsafe-inline" not in csp.split("style-src")[0],
                   "dashboard: content security policy forbids inline script")

            status, sess, _ = api.request("GET", "/api/session")
            api.token = sess["token"]
            report(status == 200 and sess["signing"] and sess["binary"], "dashboard: session reports signing and engine ready", str(sess))

            # ---- security boundaries ---------------------------------------------------
            status, _, _ = api.request("GET", "/api/cases", headers={"Host": f"evil.example:{port}"})
            report(status == 403, "security: foreign Host header rejected")
            status, _, _ = api.request("POST", "/api/verify", {"id": "x"}, headers={"X-FT-Token": "wrong"})
            report(status == 403, "security: state change without the token rejected")
            status, _, _ = api.request("POST", "/api/investigate", {}, headers={"Content-Type": "text/plain"})
            report(status == 415, "security: cross-site form content type rejected")
            for bad in ("runs/../../../../etc/passwd", "runs/../../README.md", "/etc/passwd", "nope/x.json"):
                status, _, _ = api.request("GET", f"/api/case?id={bad}")
                report(status == 404, f"security: path rejected: {bad}")
            status, body, _ = api.request("POST", "/api/investigate", {
                "scenario": "../../bin/sh", "config": "C", "mode": "ptrace", "case_id": "X", "investigator": "t"})
            report(status == 400, "security: only listed scenarios can be run")
            status, body, _ = api.request("POST", "/api/investigate", {
                "scenario": "scenario04", "config": "C", "mode": "ptrace", "case_id": "../evil", "investigator": "t"})
            report(status == 400, "security: case id cannot escape the cases folder")

            # ---- reading evidence -----------------------------------------------------
            status, body, _ = api.request("GET", "/api/cases")
            cases = body["cases"]
            ids = {c["id"] for c in cases}
            report(status == 200 and "examples/custody_demo/demo_scenario05.json" in ids and "runs/scenario01_C_r1.json" in ids
                   and not any(i.endswith(".manifest.json") for i in ids), "evidence: cases listed, custody files excluded")
            status, body, _ = api.request("GET", "/api/case?id=runs/scenario01_A_r1.json")
            report(status == 200 and body["analysis"]["collected"]["file"] is False, "evidence: schema 2 run opens")
            status, body, _ = api.request("GET", "/api/custody?id=runs/scenario01_A_r1.json")
            report(status == 200 and body["verification"]["status"] == "legacy_sidecar_ok", "custody: study run reported as sidecar only")
            status, body, _ = api.request("GET", "/api/custody?id=examples/demo_scenario04.json")
            report(status == 200 and body["verification"]["status"] == "legacy_sidecar_ok", "custody: old example reported as sidecar only")
            status, body, _ = api.request("GET", "/api/custody?id=examples/custody_demo/demo_scenario05.json")
            report(status == 200 and body["verification"]["status"] == "verified_signed_pinned", "custody: signed example verifies", str(body.get("verification")))
            hostile_id = next(i for i in ids if i.endswith("hostile.json"))
            status, body, _ = api.request("GET", f"/api/case?id={hostile_id}")
            names = [f["path"] for f in body["analysis"]["files"]]
            report(status == 200 and any("onerror" in n for n in names), "evidence: hostile file name delivered as JSON data")

            # ---- comparison matches the study's published conclusion -------------------
            status, body, _ = api.request("GET", "/api/compare?mode=ptrace&scenario=ALL")
            verdict = {c["config"]: c["sufficient"] for c in body["configs"]}
            report(verdict == {"A": False, "B": False, "C": True, "D": True}, "compare: smallest sufficient configuration is C, as published", str(verdict))
            status, body, _ = api.request("GET", "/api/compare?mode=seccomp&scenario=scenario02")
            report(status == 200 and {c["config"]: c["sufficient"] for c in body["configs"]}["B"], "compare: per-scenario view works")

            # ---- an analyst's full journey ----------------------------------------------
            status, body, _ = api.request("POST", "/api/investigate", {
                "scenario": "scenario05", "config": "C", "mode": "ptrace", "case_id": "TEST-DASH", "investigator": "Test Analyst"})
            case_id = body.get("id", "")
            report(status == 200 and body.get("signed"), "journey: investigation runs from the dashboard", str(body))
            produced = sorted(ROOT.glob("cases/TEST-DASH_*"))
            try:
                status, body, _ = api.request("GET", f"/api/case?id={case_id}")
                report(status == 200 and body["analysis"]["answers"]["downloads"], "journey: case shows the reconstruction")
                report(body["doc"]["custody"]["investigator"] == "Test Analyst", "journey: investigator recorded")
                status, body, _ = api.request("GET", f"/api/custody?id={case_id}")
                report(body["verification"]["status"] == "verified_signed_pinned" and len(body["audit"]) == 1, "journey: new evidence verifies, viewing adds no audit entry")
                status, body, _ = api.request("POST", "/api/verify", {"id": case_id, "investigator": "Test Analyst"})
                status, body, _ = api.request("GET", f"/api/custody?id={case_id}")
                report([a["action"] for a in body["audit"]] == ["generated", "verified"], "journey: explicit verification is logged")
                status, body, _ = api.request("GET", f"/api/report?id={case_id}")
                report(status == 200 and isinstance(body, (bytes, bytearray)) and b"Forensic" in body, "journey: report can be downloaded")
                status, body, _ = api.request("POST", "/api/export", {"id": case_id, "investigator": "Test Analyst"})
                exported = ROOT / body.get("directory", "missing")
                report(status == 200 and body["verified"] and exported.is_dir(), "journey: bundle exported", str(body))
                status, body, _ = api.request("POST", "/api/export", {"id": "runs/scenario01_C_r1.json"})
                report(status == 403, "journey: read-only study data cannot be exported or logged")
                # tampering with a case shows up in the dashboard
                evidence = ROOT / case_id
                text = evidence.read_text(encoding="utf-8", errors="surrogateescape")
                evidence.write_text(text.replace('"uid": 1000', '"uid": 0', 1) if '"uid": 1000' in text else text + " ",
                                    encoding="utf-8", errors="surrogateescape")
                status, body, _ = api.request("GET", f"/api/custody?id={case_id}")
                report(body["verification"]["status"] == "failed" and body["verification"]["issue_total"] > 0, "journey: tampering is reported")
                evidence.write_text("{ broken")
                status, body, _ = api.request("GET", f"/api/case?id={case_id}")
                st2, cust, _ = api.request("GET", f"/api/custody?id={case_id}")
                report(status == 422 and st2 == 200 and cust["verification"]["status"] == "failed", "journey: destroyed evidence fails cleanly")
            finally:
                for path in ROOT.glob("cases/TEST-DASH_*"):
                    path.unlink()
                for bundle in ROOT.glob("exports/TEST-DASH_*"):
                    for f in bundle.iterdir():
                        f.unlink()
                    bundle.rmdir()
                for d in (ROOT / "cases", ROOT / "exports"):
                    if d.is_dir() and not os.listdir(d):
                        d.rmdir()
            report(len(produced) >= 1, "journey: case files written under cases/")
        finally:
            server.terminate()
            _, err = server.communicate(timeout=5)
            report("Traceback" not in err and "internal" not in err, "dashboard: no server errors during the session", err[-300:])

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
