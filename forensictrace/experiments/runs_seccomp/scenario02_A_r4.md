# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 6.404 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_A_r4.json` (6213 bytes) |
| SHA-256 | `3300fdeed619627af666f5bdfdbd3b5b2c953098a24994b0941ce4a6c643cc3d` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_A_r4.json.sha256`

## 1. Process tree

- `8596` /usr/bin/bash
  - `8597` /usr/bin/rm
  - `8598` /usr/bin/mkdir
  - `8599` /usr/bin/cat
  - `8600` /usr/bin/cat
  - `8601` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8596 (?) executed `/usr/bin/bash`
- +1.303 ms pid 8597 (bash) executed `/usr/bin/rm`
- +2.297 ms pid 8598 (bash) executed `/usr/bin/mkdir`
- +3.531 ms pid 8599 (bash) executed `/usr/bin/cat`
- +4.375 ms pid 8600 (bash) executed `/usr/bin/cat`
- +5.130 ms pid 8601 (bash) executed `/usr/bin/rm`

## 3. Network activity

Not available: configuration A does not record network events.

## 4. Files created or modified

Not available: configuration A does not record file events.

## 5. Permission changes

Not available: configuration A does not record file events.

## 6. Deletions

Not available: configuration A does not record file events.

## 7. Access to sensitive resources

Not available: configuration A does not record file events.

## 8. Provenance of files executed from temporary directories

None.

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8596 | ? | execve | `/usr/bin/bash` |
| 2 | 1.148 | 8596 | bash | clone | `` |
| 3 | 1.303 | 8597 | bash | execve | `/usr/bin/rm` |
| 4 | 2.044 | 8597 | rm | exit_group | `code=0` |
| 5 | 2.176 | 8596 | bash | clone | `` |
| 6 | 2.297 | 8598 | bash | execve | `/usr/bin/mkdir` |
| 7 | 3.173 | 8598 | mkdir | exit_group | `code=0` |
| 8 | 3.342 | 8596 | bash | clone | `` |
| 9 | 3.531 | 8599 | bash | execve | `/usr/bin/cat` |
| 10 | 4.120 | 8599 | cat | exit_group | `code=1` |
| 11 | 4.268 | 8596 | bash | clone | `` |
| 12 | 4.375 | 8600 | bash | execve | `/usr/bin/cat` |
| 13 | 4.933 | 8600 | cat | exit_group | `code=0` |
| 14 | 5.025 | 8596 | bash | clone | `` |
| 15 | 5.130 | 8601 | bash | execve | `/usr/bin/rm` |
| 16 | 5.644 | 8601 | rm | exit_group | `code=0` |
| 17 | 5.737 | 8596 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 1.609 ms |
| Workload CPU (user+sys) | 5.740 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.028 ms |
| Evidence size | 6213 bytes |

