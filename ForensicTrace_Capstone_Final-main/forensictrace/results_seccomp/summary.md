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
| A | 16 | -1.10 | 10.45 | 0.66 | -29.48 | 13.19 | 5.86 | [-6.66, 4.47] |
| B | 16 | 19.52 | 11.55 | 14.52 | 5.97 | 45.41 | 13.05 | [13.36, 25.67] |
| C | 16 | 19.81 | 11.57 | 15.83 | 5.80 | 41.68 | 12.34 | [13.64, 25.97] |
| D | 16 | 45.10 | 24.12 | 37.60 | 19.86 | 84.66 | 47.27 | [32.24, 57.95] |

**Memory overhead (KiB)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 12388.75 | 9384.06 | 11830.00 | 3468.00 | 29320.00 | 16464.00 | [7388.34, 17389.16] |
| B | 16 | 11810.50 | 8574.65 | 11694.00 | 3348.00 | 21352.00 | 16444.00 | [7241.39, 16379.61] |
| C | 16 | 11614.75 | 8322.58 | 10726.00 | 3492.00 | 20256.00 | 16284.00 | [7179.96, 16049.54] |
| D | 16 | 11906.50 | 8647.08 | 11728.00 | 3404.00 | 22408.00 | 16396.00 | [7298.79, 16514.21] |

**Storage volume (KiB)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 8.15 | 2.27 | 7.66 | 6.06 | 11.22 | 3.68 | [6.94, 9.36] |
| B | 16 | 303.45 | 143.99 | 290.14 | 163.76 | 469.74 | 260.92 | [226.72, 380.17] |
| C | 16 | 306.12 | 146.73 | 292.67 | 163.76 | 475.13 | 266.31 | [227.93, 384.31] |
| D | 16 | 809.80 | 453.15 | 783.95 | 372.08 | 1298.90 | 848.51 | [568.34, 1051.27] |

**Processing time (ms)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 0.05 | 0.03 | 0.04 | 0.03 | 0.12 | 0.03 | [0.03, 0.07] |
| B | 16 | 1.51 | 1.59 | 1.02 | 0.41 | 5.37 | 1.26 | [0.67, 2.36] |
| C | 16 | 1.90 | 2.27 | 1.07 | 0.40 | 8.38 | 1.46 | [0.69, 3.10] |
| D | 16 | 3.41 | 3.42 | 2.54 | 0.81 | 13.46 | 3.16 | [1.59, 5.23] |

**Wall-time overhead (ms)**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | -0.37 | 7.02 | -1.37 | -14.21 | 13.62 | 6.38 | [-4.12, 3.37] |
| B | 16 | 25.00 | 34.39 | 13.96 | 6.74 | 140.32 | 4.65 | [6.68, 43.33] |
| C | 16 | 15.69 | 11.50 | 13.73 | 5.14 | 47.93 | 10.66 | [9.56, 21.82] |
| D | 16 | 31.81 | 10.77 | 29.77 | 18.65 | 53.53 | 16.59 | [26.07, 37.55] |

**Events stored**, pooled over scenarios

| Config | n | Mean | SD | Median | Min | Max | IQR | 95% CI of mean |
|---|---|---|---|---|---|---|---|---|
| A | 16 | 23.50 | 7.06 | 22.00 | 17.00 | 33.00 | 11.50 | [19.74, 27.26] |
| B | 16 | 833.00 | 398.42 | 797.00 | 447.00 | 1291.00 | 724.00 | [620.70, 1045.30] |
| C | 16 | 840.94 | 406.56 | 804.50 | 447.00 | 1307.00 | 740.00 | [624.30, 1057.58] |
| D | 16 | 2448.00 | 1377.92 | 2373.00 | 1118.00 | 3927.00 | 2586.25 | [1713.76, 3182.24] |

Per-scenario means (rows: scenario, columns: configuration)

CPU overhead (ms)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | -2.42 | 29.44 | 29.54 | 71.36 |
| S2 privilege-related | -0.14 | 11.42 | 10.94 | 22.69 |
| S3 network payload | -3.08 | 22.27 | 26.25 | 62.63 |
| S4 file corruption | 1.26 | 14.93 | 12.51 | 23.70 |

Memory overhead (KiB)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 22390.00 | 20257.00 | 19441.00 | 20547.00 |
| S2 privilege-related | 3593.00 | 3546.00 | 3582.00 | 3530.00 |
| S3 network payload | 20035.00 | 19954.00 | 19873.00 | 19971.00 |
| S4 file corruption | 3537.00 | 3485.00 | 3563.00 | 3578.00 |

Storage volume (KiB)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 11.22 | 469.74 | 475.13 | 1298.89 |
| S2 privilege-related | 6.07 | 167.19 | 167.19 | 373.08 |
| S3 network payload | 9.25 | 413.09 | 418.40 | 1195.16 |
| S4 file corruption | 6.06 | 163.76 | 163.76 | 372.08 |

Processing time (ms)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 0.09 | 3.61 | 4.89 | 7.78 |
| S2 privilege-related | 0.03 | 0.45 | 0.53 | 0.90 |
| S3 network payload | 0.06 | 1.51 | 1.75 | 3.90 |
| S4 file corruption | 0.03 | 0.48 | 0.42 | 1.07 |

Wall-time overhead (ms)

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | -1.56 | 27.43 | 13.38 | 35.83 |
| S2 privilege-related | -1.56 | 11.54 | 10.76 | 23.81 |
| S3 network payload | 2.11 | 15.67 | 25.85 | 42.36 |
| S4 file corruption | -0.48 | 45.37 | 12.78 | 25.24 |

Events stored

| Scenario | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| S1 download+execute | 33.00 | 1291.00 | 1307.00 | 3927.00 |
| S2 privilege-related | 17.00 | 455.00 | 455.00 | 1118.00 |
| S3 network payload | 27.00 | 1139.00 | 1154.75 | 3629.00 |
| S4 file corruption | 17.00 | 447.00 | 447.00 | 1118.00 |

## 4. Between-configuration tests

Kruskal-Wallis across configurations (pooled over scenarios). eta-squared = (H - k + 1)/(n - k). 'n/a' means every observation was identical so the test is undefined.

| Metric | H | p | eta2 | Effect | p < 0.05 |
|---|---|---|---|---|---|
| Event coverage (%) | 52.85 | <0.001 | 0.831 | large | yes |
| Reconstruction accuracy (%) | 52.85 | <0.001 | 0.831 | large | yes |
| Ordering correctness (%) | 53.89 | <0.001 | 0.848 | large | yes |
| Explainability (0-15) | 53.36 | <0.001 | 0.839 | large | yes |
| CPU overhead (ms) | 41.65 | <0.001 | 0.644 | large | yes |
| Memory overhead (KiB) | 1.44 | 0.695 | 0.000 | negligible | no |
| Storage volume (KiB) | 40.07 | <0.001 | 0.618 | large | yes |
| Processing time (ms) | 38.10 | <0.001 | 0.585 | large | yes |
| Wall-time overhead (ms) | 41.27 | <0.001 | 0.638 | large | yes |
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

**CPU overhead (ms)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -3.75 | <0.001 | 0.001 | yes |
| A vs C | -3.83 | <0.001 | <0.001 | yes |
| A vs D | -6.40 | <0.001 | <0.001 | yes |
| B vs C | -0.08 | 0.939 | 1.000 | no |
| B vs D | -2.65 | 0.008 | 0.048 | yes |
| C vs D | -2.57 | 0.010 | 0.060 | no |

**Storage volume (KiB)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.14 | <0.001 | <0.001 | yes |
| A vs C | -4.38 | <0.001 | <0.001 | yes |
| A vs D | -6.09 | <0.001 | <0.001 | yes |
| B vs C | -0.24 | 0.812 | 1.000 | no |
| B vs D | -1.94 | 0.052 | 0.311 | no |
| C vs D | -1.71 | 0.088 | 0.527 | no |

**Processing time (ms)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -4.41 | <0.001 | <0.001 | yes |
| A vs C | -4.38 | <0.001 | <0.001 | yes |
| A vs D | -5.80 | <0.001 | <0.001 | yes |
| B vs C | 0.03 | 0.977 | 1.000 | no |
| B vs D | -1.40 | 0.163 | 0.977 | no |
| C vs D | -1.42 | 0.154 | 0.926 | no |

**Wall-time overhead (ms)**

| Pair | z | p (raw) | p (Bonferroni) | Significant |
|---|---|---|---|---|
| A vs B | -3.77 | <0.001 | <0.001 | yes |
| A vs C | -3.40 | <0.001 | 0.004 | yes |
| A vs D | -6.39 | <0.001 | <0.001 | yes |
| B vs C | 0.37 | 0.711 | 1.000 | no |
| B vs D | -2.62 | 0.009 | 0.053 | no |
| C vs D | -2.99 | 0.003 | 0.017 | yes |

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
| CPU overhead (ms) | 0.005 | 0.005 | 0.006 | 0.005 |
| Memory overhead (KiB) | 0.364 | 0.388 | 0.102 | 0.392 |
| Storage volume (KiB) | 0.003 | 0.002 | 0.002 | 0.003 |
| Processing time (ms) | 0.024 | 0.005 | 0.005 | 0.004 |

## 5. Comparison against the reference configurations

Mean difference of each configuration versus the baseline A (effect of adding evidence) and versus the full configuration D (effect of removing evidence).

| Metric (vs A / vs D) | Config A | Config B | Config C | Config D |
|---|---|---|---|---|
| Event coverage (%) | +0.00 / -75.98 | +70.36 / -5.62 | +75.98 / +0.00 | +75.98 / +0.00 |
| Reconstruction accuracy (%) | +0.00 / -87.41 | +78.66 / -8.75 | +87.41 / +0.00 | +87.41 / +0.00 |
| Ordering correctness (%) | +0.00 / -100.00 | +87.86 / -12.14 | +100.00 / +0.00 | +100.00 / +0.00 |
| Explainability (0-15) | +0.00 / -12.00 | +8.50 / -3.50 | +12.00 / +0.00 | +12.00 / +0.00 |
| CPU overhead (ms) | +0.00 / -46.19 | +20.61 / -25.58 | +20.91 / -25.29 | +46.19 / +0.00 |
| Memory overhead (KiB) | +0.00 / +482.25 | -578.25 / -96.00 | -774.00 / -291.75 | -482.25 / +0.00 |
| Storage volume (KiB) | +0.00 / -801.65 | +295.30 / -506.36 | +297.97 / -503.68 | +801.65 / +0.00 |
| Processing time (ms) | +0.00 / -3.36 | +1.46 / -1.90 | +1.85 / -1.52 | +3.36 / +0.00 |

## 6. Evidence-versus-cost trade-off

| Configuration | Explainability | Coverage % | Events | Storage KiB | CPU overhead ms | Memory overhead KiB | Processing ms | Sufficient |
|---|---|---|---|---|---|---|---|---|
| A Minimal (process) | 3.00 | 24.02 | 24 | 8.15 | -1.10 | 12389 | 0.05 | no |
| B Standard (+file) | 11.50 | 94.38 | 833 | 303.45 | 19.52 | 11810 | 1.51 | no |
| C Extended (+network) | 15.00 | 100.00 | 841 | 306.12 | 19.81 | 11615 | 1.90 | yes |
| D Full (all syscalls) | 15.00 | 100.00 | 2448 | 809.80 | 45.10 | 11906 | 3.41 | yes |

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
