# ForensicTrace (application)


C11 Linux command-line tool (final product): `ptrace` or seccomp-filtered syscall collection → correlation → timeline → Markdown report → JSON + SHA-256 sidecar.

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

## Usage

```bash
./forensictrace --config B --output /tmp/run.json -- /bin/ls /tmp
sha256sum -c /tmp/run.json.sha256
python3 scripts/view_timeline.py /tmp/run.json
```

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
src/              C source (collector, normaliser, correlator, reconstructor, report, metrics, JSON, integrity)
tests/            run_tests.sh — 23 acceptance, stress and error-handling tests
scenarios/        Four controlled incident scripts + ground_truth/*.json
scripts/          setup, demo, evaluate, run_experiments, analyze, svgchart, viewers, build_report
experiments/      Raw evidence of the 64-run experiments (runs/ = ptrace, runs_seccomp/ = seccomp)
results/          ptrace results: CSV, summary.md, tradeoff.svg, environment.json
results_seccomp/  seccomp results, same layout
docs/             Technical report (md + PDF), limitations, deployment guide, example trace
```

## Documentation

- [docs/deployment.md](docs/deployment.md) — step-by-step install, first trace, troubleshooting
- [docs/technical_report.md](docs/technical_report.md) ([PDF](docs/technical_report.pdf)) — design, testing, results
- [docs/limitations.md](docs/limitations.md) — threats to validity
- [docs/examples/](docs/examples/) — a real scenario 4 trace, its report and timeline

## Ethics

Lab use only — controlled scenarios on authorised systems.
