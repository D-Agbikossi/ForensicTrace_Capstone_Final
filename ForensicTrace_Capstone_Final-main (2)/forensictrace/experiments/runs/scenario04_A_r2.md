# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 40.404 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_A_r2.json` (6214 bytes) |
| SHA-256 | `a89cc08b2dbd2821474d1d8dc636ff69c41b6a1f4456ea8c665ab8cc79081f7a` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_A_r2.json.sha256`

## 1. Process tree

- `7493` /usr/bin/bash
  - `7494` /usr/bin/rm
  - `7495` /usr/bin/mkdir
  - `7496` /usr/bin/cat
  - `7497` /usr/bin/cat
  - `7498` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7493 (?) executed `/usr/bin/bash`
- +7.381 ms pid 7494 (bash) executed `/usr/bin/rm`
- +12.849 ms pid 7495 (bash) executed `/usr/bin/mkdir`
- +18.755 ms pid 7496 (bash) executed `/usr/bin/cat`
- +28.339 ms pid 7497 (bash) executed `/usr/bin/cat`
- +33.070 ms pid 7498 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 7493 | ? | execve | `/usr/bin/bash` |
| 2 | 6.919 | 7493 | bash | clone | `` |
| 3 | 7.381 | 7494 | bash | execve | `/usr/bin/rm` |
| 4 | 11.590 | 7494 | rm | exit_group | `code=0` |
| 5 | 12.430 | 7493 | bash | clone | `` |
| 6 | 12.849 | 7495 | bash | execve | `/usr/bin/mkdir` |
| 7 | 16.945 | 7495 | mkdir | exit_group | `code=0` |
| 8 | 18.289 | 7493 | bash | clone | `` |
| 9 | 18.755 | 7496 | bash | execve | `/usr/bin/cat` |
| 10 | 25.838 | 7496 | cat | exit_group | `code=0` |
| 11 | 27.884 | 7493 | bash | clone | `` |
| 12 | 28.339 | 7497 | bash | execve | `/usr/bin/cat` |
| 13 | 32.202 | 7497 | cat | exit_group | `code=0` |
| 14 | 32.638 | 7493 | bash | clone | `` |
| 15 | 33.070 | 7498 | bash | execve | `/usr/bin/rm` |
| 16 | 39.331 | 7498 | rm | exit_group | `code=0` |
| 17 | 39.723 | 7493 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 18.780 ms |
| Workload CPU (user+sys) | 13.639 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.041 ms |
| Evidence size | 6214 bytes |

