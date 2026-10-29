# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | A |
| Events recorded | 33 |
| Failed exec attempts removed | 12 |
| Duration | 727.640 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_A_r4.json` (11483 bytes) |
| SHA-256 | `7bdd8c1c2157db86ff0acfc133b0427701f75c3523131580bfd7147a71dbd200` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_A_r4.json.sha256`

## 1. Process tree

- `8543` /usr/bin/bash
  - `8544` /usr/bin/rm
  - `8545` /usr/bin/mkdir
  - `8546` /usr/bin/cat
  - `8547` /usr/bin/python3
  - `8548` /usr/bin/sleep
  - `8549` /usr/bin/curl
  - `8550` /usr/bin/python3
  - `8551` /usr/bin/chmod
  - `8552` /tmp/ft_scenario01/downloaded.sh
    - `8553` /usr/bin/date
    - `8554` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8543 (?) executed `/usr/bin/bash`
- +1.464 ms pid 8544 (bash) executed `/usr/bin/rm`
- +2.422 ms pid 8545 (bash) executed `/usr/bin/mkdir`
- +3.915 ms pid 8546 (bash) executed `/usr/bin/cat`
- +6.426 ms pid 8547 (bash) executed `/usr/bin/python3`
- +6.570 ms pid 8548 (bash) executed `/usr/bin/sleep`
- +509.499 ms pid 8549 (bash) executed `/usr/bin/curl`
- +522.095 ms pid 8551 (bash) executed `/usr/bin/chmod`
- +523.233 ms pid 8552 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +523.897 ms pid 8553 (downloaded.sh) executed `/usr/bin/date`
- +524.774 ms pid 8554 (downloaded.sh) executed `/usr/bin/sleep`

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

- +523.233 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8552 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8543 | ? | execve | `/usr/bin/bash` |
| 2 | 1.307 | 8543 | bash | clone | `` |
| 3 | 1.464 | 8544 | bash | execve | `/usr/bin/rm` |
| 4 | 2.144 | 8544 | rm | exit_group | `code=0` |
| 5 | 2.296 | 8543 | bash | clone | `` |
| 6 | 2.422 | 8545 | bash | execve | `/usr/bin/mkdir` |
| 7 | 3.146 | 8545 | mkdir | exit_group | `code=0` |
| 8 | 3.429 | 8543 | bash | clone | `` |
| 9 | 3.915 | 8546 | bash | execve | `/usr/bin/cat` |
| 10 | 5.420 | 8546 | cat | exit_group | `code=0` |
| 11 | 5.753 | 8543 | bash | clone | `` |
| 12 | 6.155 | 8543 | bash | clone | `` |
| 13 | 6.426 | 8547 | bash | execve | `/usr/bin/python3` |
| 14 | 6.570 | 8548 | bash | execve | `/usr/bin/sleep` |
| 15 | 508.480 | 8548 | sleep | exit_group | `code=0` |
| 16 | 509.053 | 8543 | bash | clone | `` |
| 17 | 509.499 | 8549 | bash | execve | `/usr/bin/curl` |
| 18 | 517.466 | 8547 | python3 | clone3 | `` |
| 19 | 520.769 | 8550 | python3 | exit | `code=0` |
| 20 | 521.040 | 8549 | curl | exit_group | `code=0` |
| 21 | 521.889 | 8543 | bash | clone | `` |
| 22 | 522.095 | 8551 | bash | execve | `/usr/bin/chmod` |
| 23 | 522.919 | 8551 | chmod | exit_group | `code=0` |
| 24 | 523.085 | 8543 | bash | clone | `` |
| 25 | 523.233 | 8552 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 26 | 523.762 | 8552 | downloaded.sh | clone | `` |
| 27 | 523.897 | 8553 | downloaded.sh | execve | `/usr/bin/date` |
| 28 | 524.599 | 8553 | date | exit_group | `code=0` |
| 29 | 524.721 | 8552 | downloaded.sh | vfork | `` |
| 30 | 524.774 | 8554 | downloaded.sh | execve | `/usr/bin/sleep` |
| 31 | 725.468 | 8554 | sleep | exit_group | `code=0` |
| 32 | 725.661 | 8552 | downloaded.sh | exit_group | `code=0` |
| 33 | 727.025 | 8543 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 2.864 ms |
| Workload CPU (user+sys) | 81.471 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.068 ms |
| Evidence size | 11483 bytes |

