# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 6.339 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_A_r3.json` (6207 bytes) |
| SHA-256 | `bab50bc0a14bd8432390658f2c79fb57da8e87957067e18738fd86c0fdbc4d33` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_A_r3.json.sha256`

## 1. Process tree

- `8490` /usr/bin/bash
  - `8491` /usr/bin/rm
  - `8492` /usr/bin/mkdir
  - `8493` /usr/bin/cat
  - `8494` /usr/bin/cat
  - `8495` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8490 (?) executed `/usr/bin/bash`
- +1.214 ms pid 8491 (bash) executed `/usr/bin/rm`
- +2.270 ms pid 8492 (bash) executed `/usr/bin/mkdir`
- +3.326 ms pid 8493 (bash) executed `/usr/bin/cat`
- +4.193 ms pid 8494 (bash) executed `/usr/bin/cat`
- +5.009 ms pid 8495 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 8490 | ? | execve | `/usr/bin/bash` |
| 2 | 1.080 | 8490 | bash | clone | `` |
| 3 | 1.214 | 8491 | bash | execve | `/usr/bin/rm` |
| 4 | 1.954 | 8491 | rm | exit_group | `code=0` |
| 5 | 2.142 | 8490 | bash | clone | `` |
| 6 | 2.270 | 8492 | bash | execve | `/usr/bin/mkdir` |
| 7 | 3.001 | 8492 | mkdir | exit_group | `code=0` |
| 8 | 3.199 | 8490 | bash | clone | `` |
| 9 | 3.326 | 8493 | bash | execve | `/usr/bin/cat` |
| 10 | 3.893 | 8493 | cat | exit_group | `code=0` |
| 11 | 4.076 | 8490 | bash | clone | `` |
| 12 | 4.193 | 8494 | bash | execve | `/usr/bin/cat` |
| 13 | 4.739 | 8494 | cat | exit_group | `code=0` |
| 14 | 4.862 | 8490 | bash | clone | `` |
| 15 | 5.009 | 8495 | bash | execve | `/usr/bin/rm` |
| 16 | 5.644 | 8495 | rm | exit_group | `code=0` |
| 17 | 5.774 | 8490 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 1.584 ms |
| Workload CPU (user+sys) | 5.714 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.033 ms |
| Evidence size | 6207 bytes |

