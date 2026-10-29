# ForensicTrace experiment: results summary

**Runs analysed:** 64 (4 scenarios x 4 configurations, 4-4 repetitions per condition). Truncated traces: 0.

> With n = 4 repetitions per condition the study is adequate for descriptive comparison but not for confirmatory hypothesis testing; results are indicative, not conclusive (proposal 3.2.7).

## 1. Evidence sufficiency

Sufficient = **every** run in **all** scenarios meets all four thresholds (coverage >= 80 %, accuracy >= 80 %, ordering >= 70 %, explainability >= 10/15).

| Configuration | Coverage min/mean | Accuracy min/mean | Ordering min/mean | Explainability min/mean | Criteria met (of 4) | Verdict |
|---|---|---|---|---|---|---|
| A Minimal (process) | 0.00 / 24.02 FAIL | 0.00 / 12.60 FAIL | 0.00 / 0.00 FAIL | 0 / 3.00 FAIL | 0 | insufficient |
| B Standard (+file) | 87.50 / 94.38 OK | 80.00 / 91.25 OK | 71.43 / 87.86 OK | 8 / 11.50 FAIL | 3 | insufficient |
| C Extended (+network) | 100.00 / 100.00 OK | 100.00 / 100.00 OK | 100.00 / 100.00 OK | 15 / 15.00 OK | 4 | **SUFFICIENT** |
| D Full (all syscalls) | 100.00 / 100.00 OK | 100.00 / 100.00 OK | 100.00 / 100.00 OK | 15 / 15.00 OK | 4 | **SUFFICIENT** |

Per-scenario sufficiency (all repetitions meet all thresholds):

| Scenario | Config A | Config B | Config C | Config D | Smallest sufficient |
|---|---|---|---|---|---|
| S1 download+execute | no | no | yes | yes | C |
| S2 privilege-related | no | yes | yes | yes | B |
| S3 network payload | no | no | yes | yes | C |
| S4 file corruption | no | yes | yes | yes | B |

**Answer to RQ4:** the smallest sufficient configuration across all tested scenarios is **C (Extended (+network))**: process + file + network. 
Per scenario the smallest sufficient configuration is: S1 download+execute -> C, S2 privilege-related -> B, S3 network payload -> C, S4 file corruption -> B.

Config D adds no measured quality over C but stores 2.9x more events and 2.6x more storage.

## 2. Reconstruction quality by configuration

Descriptive statistics per configuration (n = scenarios x repetitions).

**Event coverage (%)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 24.02 | 14.74 | 29.29 | 0.00 | 37.50 | 10.45 | [16.16, 31.87] |
| B | 16 | 94.38 | 5.88 | 95.00 | 87.50 | 100.00 | 10.62 | [91.24, 97.51] |
| C | 16 | 100.00 | 0.00 | 100.00 | 100.00 | 100.00 | 0.00 | [100.00, 100.00] |
| D | 16 | 100.00 | 0.00 | 100.00 | 100.00 | 100.00 | 0.00 | [100.00, 100.00] |

**Reconstruction accuracy (%)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 12.60 | 7.78 | 15.19 | 0.00 | 20.00 | 5.29 | [8.45, 16.74] |
| B | 16 | 91.25 | 9.22 | 92.50 | 80.00 | 100.00 | 16.25 | [86.34, 96.16] |
| C | 16 | 100.00 | 0.00 | 100.00 | 100.00 | 100.00 | 0.00 | [100.00, 100.00] |
| D | 16 | 100.00 | 0.00 | 100.00 | 100.00 | 100.00 | 0.00 | [100.00, 100.00] |

**Ordering correctness (%)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | [0.00, 0.00] |
| B | 16 | 87.86 | 12.93 | 90.00 | 71.43 | 100.00 | 22.14 | [80.97, 94.74] |
| C | 16 | 100.00 | 0.00 | 100.00 | 100.00 | 100.00 | 0.00 | [100.00, 100.00] |
| D | 16 | 100.00 | 0.00 | 100.00 | 100.00 | 100.00 | 0.00 | [100.00, 100.00] |

**Explainability (0-15)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 3.00 | 1.79 | 4.00 | 0.00 | 4.00 | 1.00 | [2.05, 3.95] |
| B | 16 | 11.50 | 3.61 | 11.50 | 8.00 | 15.00 | 7.00 | [9.57, 13.43] |
| C | 16 | 15.00 | 0.00 | 15.00 | 15.00 | 15.00 | 0.00 | [15.00, 15.00] |
| D | 16 | 15.00 | 0.00 | 15.00 | 15.00 | 15.00 | 0.00 | [15.00, 15.00] |

Per-scenario means (rows: scenario, columns: configuration)

Event coverage (%)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 37.50 | 87.50 | 100.00 | 100.00 |
| S2 privilege-related | 28.57 | 100.00 | 100.00 | 100.00 |
| S3 network payload | 30.00 | 90.00 | 100.00 | 100.00 |
| S4 file corruption | 0.00 | 100.00 | 100.00 | 100.00 |

Reconstruction accuracy (%)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 20.00 | 80.00 | 100.00 | 100.00 |
| S2 privilege-related | 15.38 | 100.00 | 100.00 | 100.00 |
| S3 network payload | 15.00 | 85.00 | 100.00 | 100.00 |
| S4 file corruption | 0.00 | 100.00 | 100.00 | 100.00 |

Ordering correctness (%)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 0.00 | 71.43 | 100.00 | 100.00 |
| S2 privilege-related | 0.00 | 100.00 | 100.00 | 100.00 |
| S3 network payload | 0.00 | 80.00 | 100.00 | 100.00 |
| S4 file corruption | 0.00 | 100.00 | 100.00 | 100.00 |

Explainability (0-15)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 4.00 | 8.00 | 15.00 | 15.00 |
| S2 privilege-related | 4.00 | 15.00 | 15.00 | 15.00 |
| S3 network payload | 4.00 | 8.00 | 15.00 | 15.00 |
| S4 file corruption | 0.00 | 15.00 | 15.00 | 15.00 |

## 3. Resource cost by configuration

Overheads are measured against an unmonitored baseline run of the same scenario in the same repetition (CPU time of the traced tree plus the tracer's own CPU; memory = tracer peak RSS + change in workload peak RSS).

**CPU overhead (ms)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 46.31 | 26.72 | 41.72 | 11.02 | 99.79 | 44.10 | [32.07, 60.55] |
| B | 16 | 50.99 | 30.73 | 40.01 | 14.05 | 103.01 | 48.96 | [34.62, 67.37] |
| C | 16 | 45.66 | 23.51 | 43.36 | 11.91 | 74.11 | 47.36 | [33.13, 58.19] |
| D | 16 | 50.54 | 30.10 | 43.39 | 17.95 | 106.15 | 56.06 | [34.50, 66.57] |

**Memory overhead (KiB)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 12271.75 | 9387.44 | 11620.00 | 3248.00 | 29568.00 | 16427.00 | [7269.54, 17273.96] |
| B | 16 | 11794.00 | 8665.37 | 11630.00 | 3188.00 | 21916.00 | 16451.00 | [7176.55, 16411.45] |
| C | 16 | 11570.25 | 8352.59 | 11038.00 | 3296.00 | 20044.00 | 16172.00 | [7119.47, 16021.03] |
| D | 16 | 11891.50 | 8696.22 | 11648.00 | 3384.00 | 23040.00 | 16365.00 | [7257.61, 16525.39] |

**Storage volume (KiB)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 8.15 | 2.27 | 7.66 | 6.07 | 11.22 | 3.67 | [6.94, 9.36] |
| B | 16 | 303.45 | 143.99 | 290.14 | 163.76 | 469.74 | 260.92 | [226.72, 380.17] |
| C | 16 | 305.98 | 146.58 | 292.67 | 163.76 | 474.80 | 265.98 | [227.87, 384.08] |
| D | 16 | 809.66 | 452.98 | 783.38 | 372.08 | 1299.53 | 848.40 | [568.28, 1051.03] |

**Processing time (ms)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 0.06 | 0.05 | 0.04 | 0.03 | 0.20 | 0.02 | [0.04, 0.09] |
| B | 16 | 1.52 | 1.41 | 1.13 | 0.42 | 5.67 | 1.57 | [0.77, 2.27] |
| C | 16 | 1.63 | 1.64 | 0.99 | 0.42 | 5.47 | 1.62 | [0.76, 2.51] |
| D | 16 | 4.21 | 4.26 | 2.74 | 0.81 | 13.97 | 4.75 | [1.94, 6.48] |

**Wall-time overhead (ms)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 47.54 | 44.08 | 37.03 | 10.74 | 198.89 | 21.17 | [24.05, 71.02] |
| B | 16 | 46.87 | 30.43 | 31.35 | 19.21 | 119.49 | 30.01 | [30.65, 63.08] |
| C | 16 | 43.31 | 30.56 | 35.41 | 11.15 | 140.95 | 34.49 | [27.03, 59.59] |
| D | 16 | 38.59 | 21.17 | 35.11 | 16.53 | 83.04 | 25.77 | [27.31, 49.86] |

**Events stored**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 23.50 | 7.06 | 22.00 | 17.00 | 33.00 | 11.50 | [19.74, 27.26] |
| B | 16 | 833.00 | 398.42 | 797.00 | 447.00 | 1291.00 | 724.00 | [620.70, 1045.30] |
| C | 16 | 840.50 | 406.10 | 804.50 | 447.00 | 1306.00 | 739.00 | [624.11, 1056.89] |
| D | 16 | 2447.50 | 1377.35 | 2371.00 | 1118.00 | 3929.00 | 2585.75 | [1713.56, 3181.44] |

Per-scenario means (rows: scenario, columns: configuration)

CPU overhead (ms)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 70.51 | 79.20 | 71.77 | 83.64 |
| S2 privilege-related | 20.57 | 23.06 | 19.43 | 23.02 |
| S3 network payload | 68.41 | 76.07 | 63.50 | 71.59 |
| S4 file corruption | 25.76 | 25.63 | 27.94 | 23.90 |

Memory overhead (KiB)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 22345.00 | 20483.00 | 19501.00 | 20663.00 |
| S2 privilege-related | 3491.00 | 3444.00 | 3462.00 | 3535.00 |
| S3 network payload | 19799.00 | 19858.00 | 19800.00 | 19894.00 |
| S4 file corruption | 3452.00 | 3391.00 | 3518.00 | 3474.00 |

Storage volume (KiB)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 11.22 | 469.74 | 474.80 | 1298.27 |
| S2 privilege-related | 6.07 | 167.19 | 167.19 | 373.08 |
| S3 network payload | 9.25 | 413.09 | 418.15 | 1195.20 |
| S4 file corruption | 6.07 | 163.76 | 163.76 | 372.08 |

Processing time (ms)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 0.13 | 3.09 | 4.04 | 10.27 |
| S2 privilege-related | 0.04 | 0.56 | 0.46 | 0.96 |
| S3 network payload | 0.04 | 1.97 | 1.56 | 4.57 |
| S4 file corruption | 0.04 | 0.47 | 0.46 | 1.04 |

Wall-time overhead (ms)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 51.78 | 67.30 | 76.38 | 55.13 |
| S2 privilege-related | 20.41 | 29.96 | 17.48 | 21.61 |
| S3 network payload | 86.43 | 63.17 | 43.45 | 52.29 |
| S4 file corruption | 31.53 | 27.03 | 35.93 | 25.32 |

Events stored

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 33.00 | 1291.00 | 1306.00 | 3925.00 |
| S2 privilege-related | 17.00 | 455.00 | 455.00 | 1118.00 |
| S3 network payload | 27.00 | 1139.00 | 1154.00 | 3629.00 |
| S4 file corruption | 17.00 | 447.00 | 447.00 | 1118.00 |

## 4. Between-configuration tests

Kruskal-Wallis across configurations (pooled over scenarios). eta-squared = (H - k + 1)/(n - k). 'n/a' means every observation was identical so the test is undefined.

| Metric | H | p | eta2 | Effect | p < 0.05 |
|---|---|---|---|---|---|
| Event coverage (%) | 52.85 | <0.001 | 0.831 | large | yes |
| Reconstruction accuracy (%) | 52.85 | <0.001 | 0.831 | large | yes |
| Ordering correctness (%) | 53.89 | <0.001 | 0.848 | large | yes |
| Explainability (0-15) | 53.36 | <0.001 | 0.839 | large | yes |
| CPU overhead (ms) | 0.33 | 0.954 | 0.000 | negligible | no |
| Memory overhead (KiB) | 0.22 | 0.974 | 0.000 | negligible | no |
| Storage volume (KiB) | 40.06 | <0.001 | 0.618 | large | yes |
| Processing time (ms) | 39.50 | <0.001 | 0.608 | large | yes |
| Wall-time overhead (ms) | 0.51 | 0.918 | 0.000 | negligible | no |
| Events stored | 40.34 | <0.001 | 0.622 | large | yes |

Dunn's post-hoc (Bonferroni-adjusted p) for the significant metrics:

**Event coverage (%)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.20 | <0.001 | <0.001 | yes |
| A vs C | -6.30 | <0.001 | <0.001 | yes |
| A vs D | -6.30 | <0.001 | <0.001 | yes |
| B vs C | -2.10 | 0.036 | 0.215 | no |
| B vs D | -2.10 | 0.036 | 0.215 | no |
| C vs D | 0.00 | 1.000 | 1.000 | no |

**Reconstruction accuracy (%)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.20 | <0.001 | <0.001 | yes |
| A vs C | -6.30 | <0.001 | <0.001 | yes |
| A vs D | -6.30 | <0.001 | <0.001 | yes |
| B vs C | -2.10 | 0.036 | 0.215 | no |
| B vs D | -2.10 | 0.036 | 0.215 | no |
| C vs D | 0.00 | 1.000 | 1.000 | no |

**Ordering correctness (%)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.24 | <0.001 | <0.001 | yes |
| A vs C | -6.36 | <0.001 | <0.001 | yes |
| A vs D | -6.36 | <0.001 | <0.001 | yes |
| B vs C | -2.12 | 0.034 | 0.204 | no |
| B vs D | -2.12 | 0.034 | 0.204 | no |
| C vs D | 0.00 | 1.000 | 1.000 | no |

**Explainability (0-15)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.22 | <0.001 | <0.001 | yes |
| A vs C | -6.33 | <0.001 | <0.001 | yes |
| A vs D | -6.33 | <0.001 | <0.001 | yes |
| B vs C | -2.11 | 0.035 | 0.210 | no |
| B vs D | -2.11 | 0.035 | 0.210 | no |
| C vs D | 0.00 | 1.000 | 1.000 | no |

**Storage volume (KiB)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.10 | <0.001 | <0.001 | yes |
| A vs C | -4.41 | <0.001 | <0.001 | yes |
| A vs D | -6.08 | <0.001 | <0.001 | yes |
| B vs C | -0.31 | 0.754 | 1.000 | no |
| B vs D | -1.98 | 0.048 | 0.285 | no |
| C vs D | -1.67 | 0.095 | 0.572 | no |

**Processing time (ms)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.37 | <0.001 | <0.001 | yes |
| A vs C | -4.20 | <0.001 | <0.001 | yes |
| A vs D | -6.02 | <0.001 | <0.001 | yes |
| B vs C | 0.17 | 0.864 | 1.000 | no |
| B vs D | -1.65 | 0.099 | 0.591 | no |
| C vs D | -1.82 | 0.068 | 0.410 | no |

**Events stored**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.12 | <0.001 | <0.001 | yes |
| A vs C | -4.43 | <0.001 | <0.001 | yes |
| A vs D | -6.10 | <0.001 | <0.001 | yes |
| B vs C | -0.31 | 0.760 | 1.000 | no |
| B vs D | -1.98 | 0.047 | 0.284 | no |
| C vs D | -1.68 | 0.093 | 0.559 | no |

Per-scenario Kruskal-Wallis p-values (n = repetitions per group):

| Metric | S1 download+execute | S2 privilege-related | S3 network payload | S4 file corruption |
|---|---|---|---|---|
| Event coverage (%) | 0.002 | 0.002 | 0.002 | 0.002 |
| Reconstruction accuracy (%) | 0.002 | 0.002 | 0.002 | 0.002 |
| Ordering correctness (%) | 0.002 | 0.002 | 0.002 | 0.002 |
| Explainability (0-15) | 0.002 | 0.002 | 0.002 | 0.002 |
| CPU overhead (ms) | 0.382 | 0.907 | 0.835 | 0.553 |
| Memory overhead (KiB) | 0.222 | 0.343 | 0.916 | 0.446 |
| Storage volume (KiB) | 0.003 | 0.004 | 0.003 | 0.003 |
| Processing time (ms) | 0.005 | 0.005 | 0.004 | 0.005 |

## 5. Comparison against the reference configurations

Mean difference of each configuration versus the baseline A (effect of adding evidence) and versus the full configuration D (effect of removing evidence).

| Metric (vs A / vs D) | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| Event coverage (%) | +0.00 / -75.98 | +70.36 / -5.62 | +75.98 / +0.00 | +75.98 / +0.00 |
| Reconstruction accuracy (%) | +0.00 / -87.41 | +78.66 / -8.75 | +87.41 / +0.00 | +87.41 / +0.00 |
| Ordering correctness (%) | +0.00 / -100.00 | +87.86 / -12.14 | +100.00 / +0.00 | +100.00 / +0.00 |
| Explainability (0-15) | +0.00 / -12.00 | +8.50 / -3.50 | +12.00 / +0.00 | +12.00 / +0.00 |
| CPU overhead (ms) | +0.00 / -4.23 | +4.68 / +0.46 | -0.65 / -4.88 | +4.23 / +0.00 |
| Memory overhead (KiB) | +0.00 / +380.25 | -477.75 / -97.50 | -701.50 / -321.25 | -380.25 / +0.00 |
| Storage volume (KiB) | +0.00 / -801.51 | +295.29 / -506.21 | +297.82 / -503.68 | +801.51 / +0.00 |
| Processing time (ms) | +0.00 / -4.15 | +1.46 / -2.69 | +1.57 / -2.58 | +4.15 / +0.00 |

## 6. Evidence-versus-cost trade-off

| Configuration | Explainability | Coverage % | Events | Storage KiB | CPU overhead ms | Memory overhead KiB | Processing ms | Sufficient |
|---|---|---|---|---|---|---|---|---|
| A Minimal (process) | 3.00 | 24.02 | 24 | 8.15 | 46.31 | 12272 | 0.06 | no |
| B Standard (+file) | 11.50 | 94.38 | 833 | 303.45 | 50.99 | 11794 | 1.52 | no |
| C Extended (+network) | 15.00 | 100.00 | 840 | 305.98 | 45.66 | 11570 | 1.63 | yes |
| D Full (all syscalls) | 15.00 | 100.00 | 2448 | 809.66 | 50.54 | 11892 | 4.21 | yes |

## 7. Evidence integrity

Each run: the SHA-256 sidecar must verify, and three controlled modifications (bit flip, appended byte, truncated tail) must all be detected.

| Config | Runs | Sidecar verified | Tamper detected |
|---|---|---|---|
| A | 16 | 16/16 | 16/16 |
| B | 16 | 16/16 | 16/16 |
| C | 16 | 16/16 | 16/16 |
| D | 16 | 16/16 | 16/16 |
| all | 64 | 64/64 | 64/64 |

## Notes on measurement

- **Ground truth** is the per-scenario action list in `scenarios/ground_truth/*.json`; a step is covered when a recorded event matches its syscall/target pattern.
- **Accuracy** = (covered steps + reconstructed relationships) / (expected steps + expected relationships); a causal relationship counts only if the correlator's `parent_event` / `resource_event` links connect the two events.
- **Explainability** is scored automatically from the evidence with the Table 6 rubric (see `scripts/evaluate.py`); it is a proxy for, not a replacement of, expert judgement. Use `--make-manual-template` to record researcher scores and obtain agreement statistics.
- Event timestamps come from one monotonic clock, so ordering is exact whenever both events are captured; ordering loss therefore reflects missing evidence, not clock error.
- Overheads use `getrusage`; CPU of very short runs has ~10 ms granularity.
