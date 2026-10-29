#!/usr/bin/env python3
"""Run the controlled experiment of the proposal.

  4 scenarios x 4 evidence configurations x N repetitions (default 4) = 64 runs

For every repetition and scenario an UNMONITORED baseline run is measured first
(the reference for CPU / memory / wall-time overhead), then the four
configurations are run in random order (seeded, so the order is reproducible and
slow drift on the machine is not confounded with a configuration).

Per run it records: reconstruction quality (evaluate.py), resource overhead
(CPU, memory, wall time), storage volume, processing time and an integrity
check (sidecar verifies; any modification of the JSON is detected).

Outputs
  experiments/runs/*.json|.sha256|.md   raw evidence per run (runs_seccomp/ for --mode seccomp)
  results/results.csv                   one row per monitored run
  results/baseline_runs.csv             one row per unmonitored run
  results/environment.json              machine / tool versions for reproducibility

Then run:  python3 scripts/analyze.py
"""
import argparse
import csv
import hashlib
import json
import os
import platform
import random
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import evaluate  # noqa: E402

SCENARIOS = {
    "scenario01": "scenario01_download_execute.sh",
    "scenario02": "scenario02_privilege_escalation.sh",
    "scenario03": "scenario03_network_payload.sh",
    "scenario04": "scenario04_file_corruption.sh",
}
CONFIGS = ["A", "B", "C", "D"]


def run_baseline(script):
    """Unmonitored run: wall time, CPU (incl. waited descendants) and peak RSS."""
    t0 = time.monotonic_ns()
    p = subprocess.Popen(["bash", str(script)], stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL, cwd=str(ROOT))
    _, status, ru = os.wait4(p.pid, 0)
    wall = time.monotonic_ns() - t0
    p.returncode = os.waitstatus_to_exitcode(status)
    return {
        "rc": p.returncode,
        "wall_ns": wall,
        "cpu_us": int((ru.ru_utime + ru.ru_stime) * 1e6),
        "maxrss_kb": ru.ru_maxrss,
    }


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def integrity_check(json_path):
    """(sidecar verifies, every controlled modification is detected)."""
    sidecar = Path(str(json_path) + ".sha256")
    try:
        expected = sidecar.read_text().split()[0]
    except (OSError, IndexError):
        return False, False
    verified = sha256_file(json_path) == expected
    data = Path(json_path).read_bytes()
    mods = []
    flipped = bytearray(data)
    flipped[len(flipped) // 2] ^= 0x01            # one bit flipped mid-file
    mods.append(bytes(flipped))
    mods.append(data + b" ")                       # appended byte
    mods.append(data[:-2])                         # truncated tail
    detected = all(hashlib.sha256(m).hexdigest() != expected for m in mods)
    return verified, detected


def run_monitored(binary, cfg, sid, script, runs_dir, rep, mode):
    run_id = f"{sid}_{cfg}_r{rep}"
    out = runs_dir / f"{run_id}.json"
    rep_md = runs_dir / f"{run_id}.md"
    for f in (out, Path(str(out) + ".sha256"), rep_md):
        if f.exists():
            f.unlink()
    cmd = [str(binary), "--config", cfg, "--output", str(out), "--report", str(rep_md),
           "--mode", mode, "--scenario", sid, "--quiet", "--", "bash", str(script)]
    p = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                       cwd=str(ROOT), text=True)
    return run_id, out, p.returncode, p.stderr


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reps", type=int, default=4, help="repetitions per condition (default 4)")
    ap.add_argument("--scenarios", nargs="*", default=list(SCENARIOS), help="subset of scenarios")
    ap.add_argument("--configs", nargs="*", default=CONFIGS, help="subset of configurations")
    ap.add_argument("--seed", type=int, default=42, help="seed for run-order randomisation")
    ap.add_argument("--mode", choices=["ptrace", "seccomp"], default="ptrace",
                    help="collection mode (default ptrace); seccomp results go to results_seccomp/")
    ap.add_argument("--binary", default=str(ROOT / "forensictrace"))
    ap.add_argument("--results-dir", default=None)
    ap.add_argument("--runs-dir", default=None)
    args = ap.parse_args()
    suffix = "" if args.mode == "ptrace" else "_" + args.mode
    if args.results_dir is None:
        args.results_dir = str(ROOT / ("results" + suffix))
    if args.runs_dir is None:
        args.runs_dir = str(ROOT / "experiments" / ("runs" + suffix))

    binary = Path(args.binary)
    if not binary.exists():
        print(f"binary not found: {binary} (run make first)", file=sys.stderr)
        return 1
    results_dir = Path(args.results_dir)
    runs_dir = Path(args.runs_dir)
    results_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)

    gts = {sid: evaluate.load(ROOT / "scenarios" / "ground_truth" / f"{sid}.json")
           for sid in args.scenarios}
    rng = random.Random(args.seed)

    base_rows, rows = [], []
    total = args.reps * len(args.scenarios) * len(args.configs)
    done = 0
    t_start = time.time()

    for rep in range(1, args.reps + 1):
        for sid in args.scenarios:
            script = ROOT / "scenarios" / SCENARIOS[sid]
            base = run_baseline(script)
            base_rows.append({"scenario": sid, "rep": rep, **base})

            order = list(args.configs)
            rng.shuffle(order)
            for cfg in order:
                done += 1
                run_id, out, rc, err = run_monitored(binary, cfg, sid, script, runs_dir, rep, args.mode)
                if rc != 0 or not out.exists():
                    print(f"[{done}/{total}] {run_id}: FAILED rc={rc} {err.strip()[:200]}", file=sys.stderr)
                    continue

                trace = evaluate.load(out)
                q = evaluate.evaluate(trace, gts[sid])
                res = trace["resource_metrics"]
                proc = trace["processing"]
                tracer_us = res["tracer_user_us"] + res["tracer_sys_us"]
                work_us = res["workload_user_us"] + res["workload_sys_us"]
                mon_cpu_us = tracer_us + work_us
                wall_ns = res["wall_ns"]
                util_mon = mon_cpu_us * 1000.0 / wall_ns if wall_ns else 0.0
                util_base = base["cpu_us"] * 1000.0 / base["wall_ns"] if base["wall_ns"] else 0.0
                verified, detected = integrity_check(out)

                rows.append({
                    "run_id": run_id, "mode": args.mode, "scenario": sid, "config": cfg, "rep": rep,
                    "events": trace["event_count"], "raw_events": trace["raw_event_count"],
                    "dropped_failed_exec": trace["dropped_failed_exec"],
                    "truncated": int(trace["truncated"]),
                    "coverage_pct": q["coverage_pct"], "accuracy_pct": q["accuracy_pct"],
                    "ordering_pct": q["ordering_pct"], "explainability": q["explainability"],
                    "exp_actor": q["explain_dims"]["actor"], "exp_action": q["explain_dims"]["action"],
                    "exp_resource": q["explain_dims"]["resource"],
                    "exp_temporal": q["explain_dims"]["temporal"],
                    "exp_causal": q["explain_dims"]["causal"],
                    "cpu_overhead_ms": round((mon_cpu_us - base["cpu_us"]) / 1000.0, 3),
                    "cpu_util_overhead_pct": round((util_mon - util_base) * 100.0, 3),
                    "wall_overhead_ms": round((wall_ns - base["wall_ns"]) / 1e6, 3),
                    "memory_overhead_kb": res["tracer_maxrss_kb"] + (res["workload_maxrss_kb"] - base["maxrss_kb"]),
                    "tracer_cpu_ms": round(tracer_us / 1000.0, 3),
                    "workload_cpu_ms": round(work_us / 1000.0, 3),
                    "baseline_cpu_ms": round(base["cpu_us"] / 1000.0, 3),
                    "baseline_wall_ms": round(base["wall_ns"] / 1e6, 3),
                    "storage_bytes": trace["storage_bytes"],
                    "storage_kb": round(trace["storage_bytes"] / 1024.0, 3),
                    "processing_ms": round(proc["total_ns"] / 1e6, 3),
                    "normalise_ms": round(proc["normalise_ns"] / 1e6, 3),
                    "correlate_ms": round(proc["correlate_ns"] / 1e6, 3),
                    "reconstruct_ms": round(proc["reconstruct_ns"] / 1e6, 3),
                    "integrity_verified": int(verified), "tamper_detected": int(detected),
                    "missing_steps": " ".join(map(str, q["missing_steps"])),
                })
                r = rows[-1]
                print(f"[{done}/{total}] {run_id:<18} events={r['events']:<5} "
                      f"cov={r['coverage_pct']:<6} acc={r['accuracy_pct']:<6} "
                      f"ord={r['ordering_pct']:<6} expl={r['explainability']:<2} "
                      f"cpu+{r['cpu_overhead_ms']}ms  {r['storage_kb']}KB")

    def dump(path, data):
        if not data:
            return
        with open(path, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0].keys()))
            w.writeheader()
            w.writerows(data)

    dump(results_dir / "results.csv", rows)
    dump(results_dir / "baseline_runs.csv", base_rows)

    try:
        commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                                capture_output=True, text=True).stdout.strip()
    except OSError:
        commit = ""
    env = {
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "kernel": platform.release(), "machine": platform.machine(),
        "python": platform.python_version(), "cpu_count": os.cpu_count(),
        "git_commit": commit, "mode": args.mode, "reps": args.reps, "seed": args.seed,
        "scenarios": args.scenarios, "configs": args.configs,
        "runs_completed": len(rows), "runs_expected": total,
        "elapsed_s": round(time.time() - t_start, 1),
    }
    (results_dir / "environment.json").write_text(json.dumps(env, indent=2) + "\n")

    print(f"\n{len(rows)}/{total} runs recorded -> {results_dir / 'results.csv'}")
    return 0 if len(rows) == total else 2


if __name__ == "__main__":
    sys.exit(main())
