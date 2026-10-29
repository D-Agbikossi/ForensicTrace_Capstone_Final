# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | A |
| Events recorded | 33 |
| Failed exec attempts removed | 12 |
| Duration | 778.290 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_A_r3.json` (11489 bytes) |
| SHA-256 | `3a60b828e4eb20209fafe9f1765146c3e32039e55637e9c4b78ed57a259db03a` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_A_r3.json.sha256`

## 1. Process tree

- `7519` /usr/bin/bash
  - `7520` /usr/bin/rm
  - `7521` /usr/bin/mkdir
  - `7522` /usr/bin/cat
  - `7523` /usr/bin/python3
  - `7524` /usr/bin/sleep
  - `7525` /usr/bin/curl
  - `7526` /usr/bin/python3
  - `7527` /usr/bin/chmod
  - `7528` /tmp/ft_scenario01/downloaded.sh
    - `7529` /usr/bin/date
    - `7530` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7519 (?) executed `/usr/bin/bash`
- +7.497 ms pid 7520 (bash) executed `/usr/bin/rm`
- +11.927 ms pid 7521 (bash) executed `/usr/bin/mkdir`
- +16.961 ms pid 7522 (bash) executed `/usr/bin/cat`
- +21.811 ms pid 7523 (bash) executed `/usr/bin/python3`
- +22.046 ms pid 7524 (bash) executed `/usr/bin/sleep`
- +530.370 ms pid 7525 (bash) executed `/usr/bin/curl`
- +558.821 ms pid 7527 (bash) executed `/usr/bin/chmod`
- +562.564 ms pid 7528 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +564.245 ms pid 7529 (downloaded.sh) executed `/usr/bin/date`
- +567.364 ms pid 7530 (downloaded.sh) executed `/usr/bin/sleep`

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

- +562.564 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7528 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7519 | ? | execve | `/usr/bin/bash` |
| 2 | 7.121 | 7519 | bash | clone | `` |
| 3 | 7.497 | 7520 | bash | execve | `/usr/bin/rm` |
| 4 | 10.944 | 7520 | rm | exit_group | `code=0` |
| 5 | 11.557 | 7519 | bash | clone | `` |
| 6 | 11.927 | 7521 | bash | execve | `/usr/bin/mkdir` |
| 7 | 15.667 | 7521 | mkdir | exit_group | `code=0` |
| 8 | 16.442 | 7519 | bash | clone | `` |
| 9 | 16.961 | 7522 | bash | execve | `/usr/bin/cat` |
| 10 | 20.206 | 7522 | cat | exit_group | `code=0` |
| 11 | 20.472 | 7519 | bash | clone | `` |
| 12 | 21.478 | 7519 | bash | clone | `` |
| 13 | 21.811 | 7523 | bash | execve | `/usr/bin/python3` |
| 14 | 22.046 | 7524 | bash | execve | `/usr/bin/sleep` |
| 15 | 526.190 | 7524 | sleep | exit_group | `code=0` |
| 16 | 529.203 | 7519 | bash | clone | `` |
| 17 | 530.370 | 7525 | bash | execve | `/usr/bin/curl` |
| 18 | 553.521 | 7523 | python3 | clone3 | `` |
| 19 | 556.982 | 7526 | python3 | exit | `code=0` |
| 20 | 557.401 | 7525 | curl | exit_group | `code=0` |
| 21 | 558.435 | 7519 | bash | clone | `` |
| 22 | 558.821 | 7527 | bash | execve | `/usr/bin/chmod` |
| 23 | 561.899 | 7527 | chmod | exit_group | `code=0` |
| 24 | 562.158 | 7519 | bash | clone | `` |
| 25 | 562.564 | 7528 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 26 | 563.816 | 7528 | downloaded.sh | clone | `` |
| 27 | 564.245 | 7529 | downloaded.sh | execve | `/usr/bin/date` |
| 28 | 566.849 | 7529 | date | exit_group | `code=0` |
| 29 | 567.270 | 7528 | downloaded.sh | vfork | `` |
| 30 | 567.364 | 7530 | downloaded.sh | execve | `/usr/bin/sleep` |
| 31 | 770.526 | 7530 | sleep | exit_group | `code=0` |
| 32 | 771.287 | 7528 | downloaded.sh | exit_group | `code=0` |
| 33 | 777.359 | 7519 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 60.131 ms |
| Workload CPU (user+sys) | 80.988 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.197 ms |
| Evidence size | 11489 bytes |

