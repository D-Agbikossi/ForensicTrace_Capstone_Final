# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 32.534 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_A_r1.json` (6213 bytes) |
| SHA-256 | `7f573e2ab46ad5dfc9f24606ef82580882b34675ee197c96db9008891b0c68f3` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_A_r1.json.sha256`

## 1. Process tree

- `7295` /usr/bin/bash
  - `7296` /usr/bin/rm
  - `7297` /usr/bin/mkdir
  - `7298` /usr/bin/cat
  - `7299` /usr/bin/cat
  - `7300` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7295 (?) executed `/usr/bin/bash`
- +5.993 ms pid 7296 (bash) executed `/usr/bin/rm`
- +9.979 ms pid 7297 (bash) executed `/usr/bin/mkdir`
- +15.547 ms pid 7298 (bash) executed `/usr/bin/cat`
- +19.344 ms pid 7299 (bash) executed `/usr/bin/cat`
- +28.385 ms pid 7300 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 7295 | ? | execve | `/usr/bin/bash` |
| 2 | 5.486 | 7295 | bash | clone | `` |
| 3 | 5.993 | 7296 | bash | execve | `/usr/bin/rm` |
| 4 | 8.963 | 7296 | rm | exit_group | `code=0` |
| 5 | 9.613 | 7295 | bash | clone | `` |
| 6 | 9.979 | 7297 | bash | execve | `/usr/bin/mkdir` |
| 7 | 14.224 | 7297 | mkdir | exit_group | `code=0` |
| 8 | 15.221 | 7295 | bash | clone | `` |
| 9 | 15.547 | 7298 | bash | execve | `/usr/bin/cat` |
| 10 | 18.348 | 7298 | cat | exit_group | `code=0` |
| 11 | 18.973 | 7295 | bash | clone | `` |
| 12 | 19.344 | 7299 | bash | execve | `/usr/bin/cat` |
| 13 | 27.496 | 7299 | cat | exit_group | `code=0` |
| 14 | 27.909 | 7295 | bash | clone | `` |
| 15 | 28.385 | 7300 | bash | execve | `/usr/bin/rm` |
| 16 | 31.704 | 7300 | rm | exit_group | `code=0` |
| 17 | 32.029 | 7295 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 16.029 ms |
| Workload CPU (user+sys) | 11.767 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.036 ms |
| Evidence size | 6213 bytes |

