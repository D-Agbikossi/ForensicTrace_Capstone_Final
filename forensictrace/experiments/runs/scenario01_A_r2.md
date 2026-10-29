# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | A |
| Events recorded | 33 |
| Failed exec attempts removed | 12 |
| Duration | 799.232 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_A_r2.json` (11488 bytes) |
| SHA-256 | `790f4e24d80d53731c45fdd385fbc670a4957da63d8885b1e86add74823540d5` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_A_r2.json.sha256`

## 1. Process tree

- `7363` /usr/bin/bash
  - `7364` /usr/bin/rm
  - `7365` /usr/bin/mkdir
  - `7366` /usr/bin/cat
  - `7367` /usr/bin/python3
  - `7368` /usr/bin/sleep
  - `7369` /usr/bin/curl
  - `7370` /usr/bin/python3
  - `7371` /usr/bin/chmod
  - `7372` /tmp/ft_scenario01/downloaded.sh
    - `7373` /usr/bin/date
    - `7374` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7363 (?) executed `/usr/bin/bash`
- +8.899 ms pid 7364 (bash) executed `/usr/bin/rm`
- +14.954 ms pid 7365 (bash) executed `/usr/bin/mkdir`
- +21.910 ms pid 7366 (bash) executed `/usr/bin/cat`
- +32.322 ms pid 7367 (bash) executed `/usr/bin/python3`
- +33.385 ms pid 7368 (bash) executed `/usr/bin/sleep`
- +552.027 ms pid 7369 (bash) executed `/usr/bin/curl`
- +577.859 ms pid 7371 (bash) executed `/usr/bin/chmod`
- +581.451 ms pid 7372 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +583.250 ms pid 7373 (downloaded.sh) executed `/usr/bin/date`
- +586.782 ms pid 7374 (downloaded.sh) executed `/usr/bin/sleep`

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

- +581.451 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7372 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7363 | ? | execve | `/usr/bin/bash` |
| 2 | 8.439 | 7363 | bash | clone | `` |
| 3 | 8.899 | 7364 | bash | execve | `/usr/bin/rm` |
| 4 | 13.268 | 7364 | rm | exit_group | `code=0` |
| 5 | 14.245 | 7363 | bash | clone | `` |
| 6 | 14.954 | 7365 | bash | execve | `/usr/bin/mkdir` |
| 7 | 19.937 | 7365 | mkdir | exit_group | `code=0` |
| 8 | 21.241 | 7363 | bash | clone | `` |
| 9 | 21.910 | 7366 | bash | execve | `/usr/bin/cat` |
| 10 | 25.961 | 7366 | cat | exit_group | `code=0` |
| 11 | 26.335 | 7363 | bash | clone | `` |
| 12 | 32.322 | 7367 | bash | execve | `/usr/bin/python3` |
| 13 | 32.453 | 7363 | bash | clone | `` |
| 14 | 33.385 | 7368 | bash | execve | `/usr/bin/sleep` |
| 15 | 547.888 | 7368 | sleep | exit_group | `code=0` |
| 16 | 550.993 | 7363 | bash | clone | `` |
| 17 | 552.027 | 7369 | bash | execve | `/usr/bin/curl` |
| 18 | 571.961 | 7367 | python3 | clone3 | `` |
| 19 | 576.093 | 7370 | python3 | exit | `code=0` |
| 20 | 576.496 | 7369 | curl | exit_group | `code=0` |
| 21 | 577.517 | 7363 | bash | clone | `` |
| 22 | 577.859 | 7371 | bash | execve | `/usr/bin/chmod` |
| 23 | 580.732 | 7371 | chmod | exit_group | `code=0` |
| 24 | 581.127 | 7363 | bash | clone | `` |
| 25 | 581.451 | 7372 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 26 | 582.834 | 7372 | downloaded.sh | clone | `` |
| 27 | 583.250 | 7373 | downloaded.sh | execve | `/usr/bin/date` |
| 28 | 586.277 | 7373 | date | exit_group | `code=0` |
| 29 | 586.695 | 7372 | downloaded.sh | vfork | `` |
| 30 | 586.782 | 7374 | downloaded.sh | execve | `/usr/bin/sleep` |
| 31 | 790.768 | 7374 | sleep | exit_group | `code=0` |
| 32 | 791.518 | 7372 | downloaded.sh | exit_group | `code=0` |
| 33 | 798.238 | 7363 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 65.071 ms |
| Workload CPU (user+sys) | 100.991 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.125 ms |
| Evidence size | 11488 bytes |

