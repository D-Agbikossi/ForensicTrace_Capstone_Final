# ForensicTrace (final product)

**Evidence sufficiency and resource trade-offs in Linux incident reconstruction**

## 1. Project overview

This repository is the **final ForensicTrace product**: a C11 Linux command-line tool that implements the approved capstone scope (FR1–FR11, four evidence configurations, four controlled scenarios, and the evaluation pipeline). It is not an unfinished prototype and not an enterprise SIEM.

The tool runs a command under observation, records only the system calls that the chosen **evidence configuration** allows, correlates the events, prints an incident timeline, writes a Markdown forensic report, and stores each experiment as one JSON file with a SHA-256 integrity sidecar.

It is also the experimental instrument for the study. Four evidence configurations (A process, B + file, C + network, D all syscalls) were run against four scripted incidents (download and execute, privilege-related activity, network payload, file corruption), 64 runs per collection mode, and scored against ground truth for event coverage, reconstruction accuracy, ordering, explainability, CPU, memory, storage and processing time.

**Main finding:** process + file + network events (configuration C) were the smallest set that reconstructed all four incidents accurately and explainably; recording every syscall (D) added no quality and about 2.6x the storage. A seccomp-filtered collection mode was added so that CPU cost follows the evidence set (tracer CPU 2.4 ms for A against 40.0 ms for D). See [`forensictrace/results/summary.md`](forensictrace/results/summary.md) and [`forensictrace/docs/limitations.md`](forensictrace/docs/limitations.md).

## 2. Technical requirements

| Item | Requirement | Tested with |
|---|---|---|
| OS | Linux x86_64, kernel 5.x or newer (ptrace and seccomp) | Ubuntu 24.04.4, kernel 7.0.0 |
| Compiler | gcc or clang with C11 | gcc 13.3 (no warnings, including `-Wpedantic`) |
| Build | GNU make | make 4.3 |
| Libraries | OpenSSL development files (`libssl-dev`) for SHA-256 | OpenSSL 3.0.13 |
| Scripts | Python 3.10+, `pandas`, `numpy`, `scipy`; charts are SVG written with the standard library (`scripts/svgchart.py`), no plotting package needed | Python 3.12.3, pandas 2.2.2, scipy 1.17.1 |
| Scenarios | `bash`, `curl`, `python3` (local HTTP server) | |
| Optional | `valgrind` | 3.22 |
| Hardware | Any x86_64 machine | HP Laptop 14, Intel Core i3-1115G4 (4 threads), 3.5 GiB RAM |
| Permissions | A process may trace its own children; no root needed. In Docker add `--cap-add=SYS_PTRACE`. | |


## 3. Installation and first run

```bash
git clone https://github.com/D-Agbikossi/ForensicTrace_Capstone_Final.git
cd ForensicTrace_Capstone_Final/forensictrace
bash scripts/setup.sh          # installs dependencies (sudo), builds, runs the 23 tests
```

Manual steps:

```bash
sudo apt install -y build-essential libssl-dev python3 curl valgrind \
     python3-pandas python3-numpy python3-scipy
make clean && make             # builds ./forensictrace with -Wall -Wextra
make test                      # expect: 23 passed, 0 failed
```

Trace a command, verify the evidence and read the timeline:

```bash
./forensictrace --config B --output /tmp/run.json --report /tmp/run.md -- /bin/ls /tmp
sha256sum -c /tmp/run.json.sha256
python3 scripts/view_timeline.py /tmp/run.json
```

Command line: `forensictrace --config <A|B|C|D> --output <file.json> [--mode ptrace|seccomp] [--report <file.md>] [--scenario <label>] [--quiet] [--verbose] -- <command> [args]`

Run the experiment and the statistics (about 30 seconds per mode on the test laptop):

```bash
python3 scripts/run_experiments.py                 # 64 runs, plain ptrace  -> results/
python3 scripts/run_experiments.py --mode seccomp  # 64 runs, seccomp       -> results_seccomp/
python3 scripts/analyze.py                         # statistics, summary.md, tradeoff.svg
python3 scripts/analyze.py --results results_seccomp/results.csv --out-dir results_seccomp
```

Other helpers:

```bash
bash scripts/demo.sh                                          # build, test and a short guided demo
python3 scripts/visualize_events.py /tmp/run.json -o events.svg  # event counts by type (SVG chart)
python3 scripts/build_report.py                               # rebuild docs/technical_report.pdf
```

`build_report.py` needs `python3-markdown` or `markdown-it-py`, plus `playwright` or a Chromium/Chrome binary. Step-by-step setup and troubleshooting: [`forensictrace/docs/deployment.md`](forensictrace/docs/deployment.md).

## 4. Scope alignment

Planned features come from the approved proposal (functional requirements FR1 to FR11, the experimental design and the optional items). Status is Completed, Partial or Not implemented.

| Planned feature | Intended purpose | Status | Evidence |
|---|---|---|---|
| FR1 process events via ptrace | Who started which program, parent and child | Completed | `src/collector.c`; test "Config A produces valid JSON" |
| FR2 file events | What files were opened, written, changed, deleted | Completed | `collector.c` syscall table; "Config B includes file events" |
| FR3 network events | Where data came from or went | Completed (IPv4 and unix socket addresses decoded; IPv6 shown without address) | "Config C includes network events" |
| FR4 raw syscall trace | Upper-bound configuration D | Completed | "Config D > Config A" |
| FR5 normalised JSON events | One common event format | Completed | `src/normaliser.c`, `json_writer.c` |
| FR6 correlation by time, PID, PPID, resource | Link events into causal chains | Completed | `src/correlator.c`; tests "Correlation links events", "Cross-process correlation" |
| FR7 incident timeline | Readable reconstruction | Completed | `src/reconstructor.c`; `scripts/view_timeline.py` |
| FR8 four configurations A to D | The experimental variable | Completed | `ft_config_accepts()`; tests 4 to 8 |
| FR9 human-readable report | Analyst-facing summary | Completed | `src/report.c`, `docs/examples/` |
| FR10 CPU, memory, storage, processing time | The cost outcomes | Completed | `src/metrics.c`, JSON `resource_metrics` |
| FR11 one JSON file with integrity hash | Tamper detection | Completed, changed: SHA-256 stored in a sidecar file because a file cannot hold its own hash | `src/integrity.c`; "Sidecar verifies", "Tamper detection" |
| Four controlled scenarios with ground truth | Known answer to score against | Completed | `scenarios/`, `scenarios/ground_truth/` |
| Evaluation metrics and sufficiency threshold | Answer RQ1 to RQ4 | Completed | `scripts/evaluate.py` |
| Statistical analysis plan (Kruskal-Wallis, Dunn, eta-squared) | Compare configurations | Completed | `scripts/analyze.py`, `results/summary.md` |
| 64-run experiment | The dataset | Completed (and repeated for seccomp mode) | `scripts/run_experiments.py`, `results/results.csv` |
| Seccomp collection mode | Not planned. Added to explain and test why plain ptrace CPU cost did not depend on the configuration | Completed (scope change, justified in report) | `collector.c`; test "seccomp mode matches ptrace mode" |
| Linux kernel 5.x and Ubuntu 22.04 compatibility | Portability | Partial: tested on Ubuntu 24.04.4, kernel 7.0 only | Section 2 above |
| ProvSec external validation | Check approach on public data | Not implemented (optional in proposal) | |
| Expert scoring of explainability | Human check of the rubric | Not implemented (optional); rubric is scored automatically | `docs/limitations.md` |

## 5. Testing

- **Functional and integration tests:** `make test` runs 23 acceptance tests (build without warnings, CLI and validation, each configuration, correlation, integrity and tamper detection, end-to-end scenario, collection-mode equivalence).
- **Stress tests:** 150 concurrent processes traced without loss; the 20,000-event cap is enforced and flagged. This testing found and fixed a defect: processes beyond 64 concurrent were silently dropped.
- **Error handling:** invalid configuration or mode, missing command, unwritable output path.
- **Memory safety:** Valgrind and an AddressSanitizer/UBSan build (`make asan`) report no errors.
- **Compatibility:** gcc 13 builds cleanly with `-Wall -Wextra -Wpedantic`. clang is not installed on the test machine and was not re-checked.
- **Performance:** the 64-run experiments measure CPU, memory, wall time, storage and processing time against an unmonitored baseline.

Details and results are in the technical report.

## 6. Repository structure

```
ForensicTrace_Capstone_Final/
├── README.md                     this file
└── forensictrace/
    ├── Makefile                  build, test, asan targets
    ├── src/                      C11 source (one file per pipeline stage + forensictrace.h)
    │   ├── main.c                CLI, stage orchestration, timing
    │   ├── collector.c           ptrace and seccomp collection, syscall table, config filter
    │   ├── normaliser.c          common event form
    │   ├── correlator.c          parent_event / resource_event links
    │   ├── reconstructor.c       timeline
    │   ├── report.c              Markdown forensic report
    │   ├── metrics.c             CPU and memory (getrusage)
    │   ├── json_writer.c         one JSON file per experiment
    │   └── integrity.c           SHA-256 sidecar
    ├── scenarios/                four scenario scripts + ground_truth/*.json
    ├── scripts/                  setup, demo, evaluate, run_experiments, analyze, viewers
    ├── tests/run_tests.sh        23 acceptance, stress and error-handling tests
    ├── experiments/runs/, runs_seccomp/  64 raw experiment JSON files per mode, with sidecars and reports
    ├── results/, results_seccomp/  experiment summaries (CSV, summary, SVG chart)
    ├── README.md                 short guide to the application folder
    └── docs/                     technical report (PDF), limitations, deployment guide, example traces
```

## 7. Ethics and safety

The tool only traces commands you start yourself on a system you are authorised to use. Scenarios run in `/tmp` on a local machine, use a local HTTP server and contain no real malware or personal data. The seccomp mode sets `no_new_privs`, so set-uid programs lose privileges while traced.

## Deliverable
- Technical walkthrough video: 
- Technical report: 

# Author

Denaton Agbikossi 

# Supervisor

Junior Turatsinze