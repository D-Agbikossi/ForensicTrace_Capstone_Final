# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | A |
| Events recorded | 33 |
| Failed exec attempts removed | 12 |
| Duration | 733.604 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_A_r3.json` (11488 bytes) |
| SHA-256 | `9fbb21be2d53f38fd5b766456af0d0d95ddec7573e85c6791a4cbf5b614adc1b` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_A_r3.json.sha256`

## 1. Process tree

- `8316` /usr/bin/bash
  - `8317` /usr/bin/rm
  - `8318` /usr/bin/mkdir
  - `8319` /usr/bin/cat
  - `8320` /usr/bin/python3
  - `8321` /usr/bin/sleep
  - `8322` /usr/bin/curl
  - `8323` /usr/bin/python3
  - `8324` /usr/bin/chmod
  - `8325` /tmp/ft_scenario01/downloaded.sh
    - `8326` /usr/bin/date
    - `8327` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8316 (?) executed `/usr/bin/bash`
- +1.499 ms pid 8317 (bash) executed `/usr/bin/rm`
- +2.772 ms pid 8318 (bash) executed `/usr/bin/mkdir`
- +4.540 ms pid 8319 (bash) executed `/usr/bin/cat`
- +5.844 ms pid 8320 (bash) executed `/usr/bin/python3`
- +5.931 ms pid 8321 (bash) executed `/usr/bin/sleep`
- +508.404 ms pid 8322 (bash) executed `/usr/bin/curl`
- +525.545 ms pid 8324 (bash) executed `/usr/bin/chmod`
- +526.796 ms pid 8325 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +527.586 ms pid 8326 (downloaded.sh) executed `/usr/bin/date`
- +528.602 ms pid 8327 (downloaded.sh) executed `/usr/bin/sleep`

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

- +526.796 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8325 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8316 | ? | execve | `/usr/bin/bash` |
| 2 | 1.254 | 8316 | bash | clone | `` |
| 3 | 1.499 | 8317 | bash | execve | `/usr/bin/rm` |
| 4 | 2.405 | 8317 | rm | exit_group | `code=0` |
| 5 | 2.610 | 8316 | bash | clone | `` |
| 6 | 2.772 | 8318 | bash | execve | `/usr/bin/mkdir` |
| 7 | 4.052 | 8318 | mkdir | exit_group | `code=0` |
| 8 | 4.330 | 8316 | bash | clone | `` |
| 9 | 4.540 | 8319 | bash | execve | `/usr/bin/cat` |
| 10 | 5.261 | 8319 | cat | exit_group | `code=0` |
| 11 | 5.502 | 8316 | bash | clone | `` |
| 12 | 5.750 | 8316 | bash | clone | `` |
| 13 | 5.844 | 8320 | bash | execve | `/usr/bin/python3` |
| 14 | 5.931 | 8321 | bash | execve | `/usr/bin/sleep` |
| 15 | 506.851 | 8321 | sleep | exit_group | `code=0` |
| 16 | 507.842 | 8316 | bash | clone | `` |
| 17 | 508.404 | 8322 | bash | execve | `/usr/bin/curl` |
| 18 | 519.189 | 8320 | python3 | clone3 | `` |
| 19 | 524.101 | 8323 | python3 | exit | `code=0` |
| 20 | 524.438 | 8322 | curl | exit_group | `code=0` |
| 21 | 525.224 | 8316 | bash | clone | `` |
| 22 | 525.545 | 8324 | bash | execve | `/usr/bin/chmod` |
| 23 | 526.487 | 8324 | chmod | exit_group | `code=0` |
| 24 | 526.637 | 8316 | bash | clone | `` |
| 25 | 526.796 | 8325 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 26 | 527.416 | 8325 | downloaded.sh | clone | `` |
| 27 | 527.586 | 8326 | downloaded.sh | execve | `/usr/bin/date` |
| 28 | 528.418 | 8326 | date | exit_group | `code=0` |
| 29 | 528.554 | 8325 | downloaded.sh | vfork | `` |
| 30 | 528.602 | 8327 | downloaded.sh | execve | `/usr/bin/sleep` |
| 31 | 729.363 | 8327 | sleep | exit_group | `code=0` |
| 32 | 729.915 | 8325 | downloaded.sh | exit_group | `code=0` |
| 33 | 732.646 | 8316 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 3.182 ms |
| Workload CPU (user+sys) | 70.814 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.123 ms |
| Evidence size | 11488 bytes |

