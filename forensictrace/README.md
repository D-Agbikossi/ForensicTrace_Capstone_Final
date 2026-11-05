# ForensicTrace (application)


Linux forensic tool (final product): `ptrace` or seccomp-filtered syscall collection → correlation → timeline → Markdown report → hash-chained JSON evidence with a signed manifest, plus a local web dashboard over that evidence.

## Quick start

```bash
make clean && make
chmod +x tests/run_tests.sh scenarios/*.sh scripts/*.sh
./tests/run_tests.sh
```

Record the demo:

```bash
bash scripts/demo.sh
```

## Dashboard

```bash
make dashboard  
```

See [docs/dashboard.md](docs/dashboard.md).

## Usage

```bash
./forensictrace --config B --output /tmp/run.json -- /bin/ls /tmp
sha256sum -c /tmp/run.json.sha256
python3 scripts/view_timeline.py /tmp/run.json
python3 scripts/reconstruct.py /tmp/run.json        # who, what, which files, which endpoints
./forensictrace verify /tmp/run.json                # names modified or missing records
```

Signing, investigator and case identifiers, export and the hash format: [docs/custody.md](docs/custody.md).

## Collection modes

```bash
./forensictrace --config B --mode ptrace  --output /tmp/p.json -- /bin/ls   # default: stop on every syscall
./forensictrace --config B --mode seccomp --output /tmp/s.json -- /bin/ls   # kernel filter: stop only on selected syscalls
python3 scripts/run_experiments.py --mode seccomp && python3 scripts/analyze.py --results results_seccomp/results.csv --out-dir results_seccomp
```

Both modes record identical events; `seccomp` makes CPU cost follow the evidence configuration. See [docs/limitations.md](docs/limitations.md).

## Evidence configurations

| Config | Records |
|--------|---------|
| A | Process syscalls only |
| B | A + file syscalls |
| C | B + network syscalls |
| D | All syscalls |

## Build

Use **`Makefile`** in this directory (`make`). There is only one build file.

## Project layout

```
src/              C source (collector, normaliser, correlator, reconstructor, report, metrics, JSON, integrity, custody, verify)
dashboard/        Local web dashboard: server.py + static/
tests/            run_tests.sh and the custody, reconstruction and dashboard suites (120 checks)
scenarios/        Four study scenarios, one reconstruction demo, ground_truth/*.json
scripts/          setup, demo, evaluate, run_experiments, analyze, reconstruct, svgchart, viewers, build_report
experiments/      Raw evidence of the 64-run experiments (runs/ = ptrace, runs_seccomp/ = seccomp)
results/          ptrace results: CSV, summary.md, tradeoff.svg, environment.json
results_seccomp/  seccomp results, same layout
docs/             Technical report (md + PDF), limitations, deployment guide, example trace
```

## Documentation

- [docs/deployment.md](docs/deployment.md) — step-by-step install, first trace, troubleshooting
- [docs/technical_report.md](docs/technical_report.md) ([PDF](docs/ForensicTrace_Final_Technical Report.pdf)) — design, testing, results
- [docs/limitations.md](docs/limitations.md) — threats to validity
- [docs/dashboard.md](docs/dashboard.md) — dashboard, reconstruction rules, confidence scores
- [docs/custody.md](docs/custody.md) — chain of custody, hash format, what it does not protect against
- [docs/examples/](docs/examples/) — a real scenario 4 trace, its report and timeline, and a signed scenario 5 case

## Ethics

Lab use only — controlled scenarios on authorised systems.
