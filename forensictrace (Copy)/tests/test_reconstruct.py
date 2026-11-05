#!/usr/bin/env python3
"""Check incident reconstruction against what each scenario script really does.

Runs every scenario under the engine and looks for the expected relations, then
checks the negative controls: benign commands must raise no suspicion, and missing
evidence must produce "not collected", never a guess.

Prints one "[PASS] name" or "[FAIL] name" per check; run_tests.sh counts them.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import evaluate  # noqa: E402
import reconstruct  # noqa: E402

BIN = str(ROOT / "forensictrace")
failures = 0


def report(ok, name, note=""):
    global failures
    failures += 0 if ok else 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{f' ({note})' if note and not ok else ''}")


def trace(tmp, name, config, *cmd):
    out = Path(tmp) / f"{name}_{config}.json"
    subprocess.run([BIN, "--config", config, "--quiet", "--scenario", name, "--output", str(out), "--", *cmd],
                   capture_output=True, cwd=ROOT, check=False)
    doc = reconstruct.load_evidence(out)
    return doc, reconstruct.reconstruct(doc)


def scenario(tmp, script, config="C"):
    return trace(tmp, script.split("_")[0], config, "bash", f"scenarios/{script}")


def has(result, kind, src_exe=None, dst_suffix=None):
    nodes = {n["id"]: n for n in result["graph"]["nodes"]}
    for e in result["graph"]["edges"]:
        if e["kind"] != kind:
            continue
        src, dst = nodes[e["src"]], nodes[e["dst"]]
        if src_exe and src.get("label") != src_exe:
            continue
        if dst_suffix and not (dst.get("path") or dst.get("label") or "").endswith(dst_suffix):
            continue
        return e
    return None


def rules(result):
    return {f["rule"] for f in result["findings"]}


def evidence_real(doc, result):
    ids = {e["id"] for e in doc["events"]}
    return all(e["evidence"] and set(e["evidence"]) <= ids for e in result["graph"]["edges"])


def scores_valid(result):
    return all(0 < e["confidence"] < 1 and e["factors"] for e in result["graph"]["edges"])


def main():
    with tempfile.TemporaryDirectory(prefix="ft_recon_") as tmp:
        # ---- scenario 5: the full multi-stage chain ----------------------------------
        doc, r = scenario(tmp, "scenario05_multistage_intrusion.sh")
        a = r["answers"]
        report(a["initiator"] and "scenario05" in a["initiator"]["command"] and a["initiator"]["pid"] == doc["events"][0]["pid"],
               "scenario 5: initiating process identified")
        d = [x for x in a["downloads"] if x["file"].endswith("/ft_scenario05/update.sh")]
        report(len(a["downloads"]) == 1 and d and base(d[0]["exe"]) == "curl" and d[0]["endpoint"] == "127.0.0.1:8767",
               "scenario 5: downloading process, payload and source identified", str(a["downloads"]))
        report(any(x["file"].endswith("/update.sh") for x in a["executions"]), "scenario 5: payload execution linked to the download")
        paths = {f["path"] for f in a["affected_files"]}
        report({"/tmp/ft_scenario05/victim/persistence.cron", "/tmp/ft_scenario05/victim/settings.conf"} <= paths and "/dev/null" not in paths,
               "scenario 5: files changed by the payload identified", str(paths))
        e = has(r, "wrote", "update.sh", "/settings.conf")
        report(e is not None, "scenario 5: the payload process itself linked to the file change")
        ends = {n["endpoint"]: n for n in a["endpoints"]}
        report(set(ends) == {"127.0.0.1:8767", "127.0.0.1:8768"} and all(n["state"] == "established" for n in ends.values()),
               "scenario 5: contacted endpoints identified, probes excluded", str(list(ends)))
        report(all(n["proto"] == "tcp" and n["scope"] == "loopback" for n in ends.values()), "scenario 5: protocol and scope recorded")
        outbound = [c for c in r["connections"] if c["direction"] == "outbound" and not c["probe"]]
        report(all(c["src_host"] == "127.0.0.1" and c["src_port"] for c in outbound), "scenario 5: source address and port recorded")
        report(all("peer_pid" in c for c in outbound), "scenario 5: both ends of each connection paired")
        report({"FT-DOWNLOAD-EXEC", "FT-PAYLOAD-OUTBOUND"} <= rules(r), "scenario 5: suspicious activity flagged", str(rules(r)))
        chain = {x["id"]: x for x in r["graph"]["edges"]}
        steps = [chain[i] for i in a["chain"]]
        kinds = [x["kind"] for x in steps]
        report(kinds.count("downloaded") == 1 and "executed" in kinds and "connected" in kinds and "wrote" in kinds,
               "scenario 5: chain covers download, execution, file change, connection", str(kinds))
        order = [next(i for i, x in enumerate(steps) if x["kind"] == k) for k in ("downloaded", "executed")]
        report(order[0] < order[1] and [x["ms"] for x in steps] == sorted(x["ms"] for x in steps), "scenario 5: chain is in time order")
        report(evidence_real(doc, r), "scenario 5: every relation cites real events")
        report(scores_valid(r), "scenario 5: every relation has a score and its reasons")
        inferred = has(r, "downloaded")
        report(inferred["tier"] == "inferred" and inferred["confidence"] <= 0.9
               and any("not proven" in f["label"] for f in inferred["factors"]),
               "scenario 5: inferred download is labelled and capped below certainty")
        scores = evaluate.evaluate(doc, evaluate.load(ROOT / "scenarios/ground_truth/scenario05.json")) \
            if hasattr(evaluate, "evaluate") else None
        if scores is not None:
            report(scores["coverage_pct"] == 100, "scenario 5: ground truth fully covered", str(scores))

        # ---- the four study scenarios ----------------------------------------------------
        doc, r = scenario(tmp, "scenario01_download_execute.sh")
        report(has(r, "downloaded", "curl", "/downloaded.sh") and has(r, "executed", dst_suffix=None)
               and "FT-DOWNLOAD-EXEC" in rules(r), "scenario 1: download then execute reconstructed")
        report(evidence_real(doc, r), "scenario 1: every relation cites real events")

        doc, r = scenario(tmp, "scenario02_privilege_escalation.sh")
        report(has(r, "read_denied", "cat", "/etc/shadow") or has(r, "read", "cat", "/etc/shadow"),
               "scenario 2: /etc/shadow attempt attributed to cat")
        report(has(r, "deleted", "rm", "/fake_passwd_entry") and "FT-CREATE-DELETE" in rules(r), "scenario 2: fake record deletion attributed to rm")
        report(not r["answers"]["downloads"], "scenario 2: no download invented")

        doc, r = scenario(tmp, "scenario03_network_payload.sh")
        report(has(r, "downloaded", "curl", "/fetched.txt") and has(r, "executed", dst_suffix=None), "scenario 3: fetch and payload execution reconstructed")
        report(not has(r, "downloaded", dst_suffix="/runme.sh"), "scenario 3: runme.sh, written locally, is not called a download")

        doc, r = scenario(tmp, "scenario04_file_corruption.sh")
        report("FT-OVERWRITE" in rules(r) and has(r, "overwritten", dst_suffix="/important.txt"), "scenario 4: overwrite of important.txt reconstructed")

        # ---- missing evidence must stay unknown -------------------------------------------
        doc, r = scenario(tmp, "scenario05_multistage_intrusion.sh", "A")
        a = r["answers"]
        report(not r["collected"]["file"] and not a["affected_files"] and "not collected" in a["affected_files_note"]
               and not a["downloads"] and "not collected" in a["downloads_note"] and "not collected" in a["endpoints_note"],
               "config A: file and network answers say not collected")
        doc, r = scenario(tmp, "scenario05_multistage_intrusion.sh", "B")
        a = r["answers"]
        report(not a["downloads"] and "not collected" in a["downloads_note"] and not a["endpoints"] and a["affected_files"],
               "config B: files known, download and endpoints not collected")

        # ---- negative controls: benign activity raises no suspicion ------------------------
        doc, r = trace(tmp, "ls", "C", "/bin/ls", "/tmp")
        report(not [f for f in r["findings"] if f["severity"] in ("critical", "high", "medium")]
               and not r["answers"]["chain"], "control: ls raises no finding", str(r["findings"]))
        out_file = Path(tmp) / "note.txt"
        doc, r = trace(tmp, "write", "C", "/bin/sh", "-c", f"echo hello > {out_file}")
        report(not r["answers"]["downloads"] and not r["answers"]["executions"]
               and not [f for f in r["findings"] if f["severity"] in ("critical", "high")],
               "control: writing a file is not called a download")
        doc, r = trace(tmp, "refused", "C", "/bin/sh", "-c", f"curl -s -m 2 http://127.0.0.1:1/ ; echo done > {out_file}")
        report(not r["answers"]["downloads"] and all(n["state"] in ("failed", "attempted") for n in r["answers"]["endpoints"]),
               "control: a refused connection followed by a write is not a download", str(r["answers"]["endpoints"]))
        doc, r = trace(tmp, "devnull", "C", "/bin/sh", "-c", "curl -s -m 2 -o /dev/null http://127.0.0.1:1/")
        report(not r["answers"]["affected_files"] and not r["answers"]["downloads"], "control: /dev/null is not an affected file")

        # ---- schema 2 study runs still reconstruct ---------------------------------------
        old = reconstruct.load_evidence(ROOT / "experiments/runs/scenario01_C_r1.json")
        r = reconstruct.reconstruct(old)
        down = has(r, "downloaded", "curl", "/downloaded.sh")
        report(down and down["confidence"] < 0.8, "schema 2: reconstructs, with lower confidence without socket ids")

    return 1 if failures else 0


def base(path):
    return path.rsplit("/", 1)[-1]


if __name__ == "__main__":
    sys.exit(main())
