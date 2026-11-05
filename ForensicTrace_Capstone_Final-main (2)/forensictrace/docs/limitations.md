# Limitations and Threats to Validity

Figures below come from the 64-run experiments stored in `results/` (plain ptrace)
and `results_seccomp/` (seccomp-filtered collection). They were measured on
the author's laptop: Ubuntu 24.04.4, kernel 7.0, HP Laptop 14 (Intel Core i3-1115G4, 4 threads, 3.5 GiB RAM).

## 1. Why the resource-cost result depends on how evidence is collected

The study's hypothesis is that a smaller evidence configuration lowers resource
cost. In the baseline `ptrace` collector this was **not** observed for CPU or
memory. Mean tracer CPU was 38.1, 41.7, 39.3 and 43.1 ms for configurations A–D
(Kruskal–Wallis p = 0.63), and CPU overhead did not differ either (p = 0.95).

The cause is how `ptrace(PTRACE_SYSCALL)` works. The kernel stops the traced
process at the entry and exit of **every** system call and wakes the tracer, two
context switches per call, whether or not the configuration records it. The
configuration filter (`ft_config_accepts()`) only decides what is *stored*, so
the stop cost is the same for A and D. Only the cost that follows the stop
(parsing arguments, storing events, writing JSON, processing) varies with the
configuration, and that is small beside the cost of the stops.

To test whether evidence selection can reduce collection cost at all, a second
collection mode was added (`--mode seccomp`). It is still `ptrace`-based, but the
child installs a kernel seccomp-bpf filter that returns `SECCOMP_RET_TRACE` only
for the syscalls in the active configuration; other syscalls run without a stop
(`PTRACE_O_TRACESECCOMP`). The recorded events are identical to the baseline
mode (verified by an automated test and by repeating all 64 runs), so
reconstruction quality is unchanged, but the cost now follows the configuration:

| Config | Tracer CPU, ptrace (ms) | Tracer CPU, seccomp (ms) | Wall overhead, ptrace (ms) | Wall overhead, seccomp (ms) |
|---|---|---|---|---|
| A | 38.1 | 2.4 | 47.5 | -0.4 |
| B | 41.7 | 19.0 | 46.9 | 25.0 |
| C | 39.3 | 19.0 | 43.3 | 15.7 |
| D | 43.1 | 40.0 | 38.6 | 31.8 |

In seccomp mode the differences between configurations are significant
(Kruskal–Wallis p < 0.001 for tracer CPU, CPU overhead and wall overhead).
Config D, which must stop on every syscall, costs about the same tracer CPU as
the baseline mode (40.0 against 43.1 ms), as expected. Wall overhead is noisy at
this scale: B's mean (25.0 ms) is above C's only because of a few slow runs
(SD 34 ms), and A's small negative value means the monitored runs were within
noise of the unmonitored ones.

## 2. Construct validity: the quality result is partly built into the design

The ground-truth steps are process, file and network actions, and the
configurations are defined as adding exactly those categories. Config A scoring
near 0% on file-based steps is therefore close to guaranteed by construction. The
informative comparisons are B against C (does network evidence change
explainability?) and C against D (does recording every other syscall add
anything?). In these runs B misses the network `connect` step in scenarios 1 and
3, and D adds nothing over C.

## 3. External validity

- Only four short, deterministic, scripted scenarios on one host were tested.
  The conclusion "C is the smallest sufficient configuration" applies to these
  scenarios, not to Linux incidents in general. Real intrusions are noisier,
  longer, and may use syscalls outside the categories defined here
  (for example `mmap`, `ptrace`, `setuid`, `execve` through a shell built-in).
- The incidents are simulated and run by the experimenter. No adversary tried to
  evade the collector.
- A kernel-level or privileged attacker can defeat any user-space ptrace tracer.
  The tool also assumes `x86_64`; the 32-bit and x32 syscall ABIs are not traced.
- The thresholds (80/80/70/10) are researcher-chosen. Config C meets all of them
  with margin, so they separate A and B from C but cannot separate C from D.

## 4. Measurement validity of explainability

Explainability is scored **automatically** by `scripts/evaluate.py` from the
rubric in Table 6, not by human judges. The scores are therefore consistent and
repeatable, but they measure what the rubric's author encoded, and rule-based
scores can differ from how an analyst would rate the output. The proposal lists
expert scoring as optional; to strengthen the result, have at least two people
score a sample of reports and report agreement
(`scripts/analyze.py --make-manual-template` creates the sheet, `--manual`
imports it).

## 5. Statistical power

Each condition has n = 4 repetitions. This supports descriptive comparison but
not confirmatory hypothesis testing; p-values are indicative. Because the
scenarios are deterministic, quality metrics have almost no variance (C and D
are always exactly 100%), so some Kruskal–Wallis tests are undefined and
effect sizes are inflated. Repetitions mostly capture timing noise, not
behavioural variation.

## 6. Environment and measurement noise

- Overhead is the difference between a monitored and an unmonitored run of the
  same script. The scripts run for tens to hundreds of milliseconds and include
  process start-up, so CPU measurements carry noticeable noise, and the
  scenarios with a Python HTTP server and curl (1 and 3) have much larger
  absolute overhead than scenarios 2 and 4.
- Run order is randomised per repetition with a fixed seed, but nothing else
  is controlled: CPU frequency scaling and other desktop load affect the
  numbers. The results in this repository were produced on one laptop with a
  normal desktop session running; absolute timings will differ on other
  machines. The environment is recorded in `results/environment.json` and
  `results_seccomp/environment.json`.
- Seccomp mode sets `PR_SET_NO_NEW_PRIVS` on the traced process, so set-uid
  binaries (for example `sudo`) lose their privileges inside the experiment.
  The four scenarios do not use any.

## 7. Evidence integrity

Integrity uses a SHA-256 sidecar. It detects accidental or later modification of
the JSON file (a flipped bit, an appended byte and a truncated tail were all
detected in every run), but it does not protect against an attacker who
rewrites both the file and its sidecar. Tamper-evident logging schemes
(hash chains, signing, remote anchoring) are outside the scope of this study,
as the proposal states.

## 8. Other scope limits (as stated in the proposal)

Single host, no enterprise-scale monitoring, no deleted-file recovery, no
memory forensics, no courtroom admissibility, event cap of 20,000 per run
(no run was truncated).
