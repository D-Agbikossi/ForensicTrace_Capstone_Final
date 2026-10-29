# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | A |
| Events recorded | 33 |
| Failed exec attempts removed | 12 |
| Duration | 774.202 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_A_r4.json` (11488 bytes) |
| SHA-256 | `79cf3ffb1b8bab03b067ba38fc8741a082a3049846e07e7c41d45b20985dd3b3` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_A_r4.json.sha256`

## 1. Process tree

- `7738` /usr/bin/bash
  - `7739` /usr/bin/rm
  - `7740` /usr/bin/mkdir
  - `7741` /usr/bin/cat
  - `7743` /usr/bin/sleep
  - `7742` /usr/bin/python3
  - `7744` /usr/bin/curl
  - `7745` /usr/bin/python3
  - `7746` /usr/bin/chmod
  - `7747` /tmp/ft_scenario01/downloaded.sh
    - `7748` /usr/bin/date
    - `7750` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7738 (?) executed `/usr/bin/bash`
- +5.778 ms pid 7739 (bash) executed `/usr/bin/rm`
- +9.624 ms pid 7740 (bash) executed `/usr/bin/mkdir`
- +14.221 ms pid 7741 (bash) executed `/usr/bin/cat`
- +18.503 ms pid 7743 (bash) executed `/usr/bin/sleep`
- +18.511 ms pid 7742 (bash) executed `/usr/bin/python3`
- +526.146 ms pid 7744 (bash) executed `/usr/bin/curl`
- +547.632 ms pid 7746 (bash) executed `/usr/bin/chmod`
- +552.577 ms pid 7747 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +554.653 ms pid 7748 (downloaded.sh) executed `/usr/bin/date`
- +561.976 ms pid 7750 (downloaded.sh) executed `/usr/bin/sleep`

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

- +552.577 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7747 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7738 | ? | execve | `/usr/bin/bash` |
| 2 | 5.428 | 7738 | bash | clone | `` |
| 3 | 5.778 | 7739 | bash | execve | `/usr/bin/rm` |
| 4 | 8.668 | 7739 | rm | exit_group | `code=0` |
| 5 | 9.268 | 7738 | bash | clone | `` |
| 6 | 9.624 | 7740 | bash | execve | `/usr/bin/mkdir` |
| 7 | 12.775 | 7740 | mkdir | exit_group | `code=0` |
| 8 | 13.656 | 7738 | bash | clone | `` |
| 9 | 14.221 | 7741 | bash | execve | `/usr/bin/cat` |
| 10 | 16.834 | 7741 | cat | exit_group | `code=0` |
| 11 | 17.128 | 7738 | bash | clone | `` |
| 12 | 18.143 | 7738 | bash | clone | `` |
| 13 | 18.503 | 7743 | bash | execve | `/usr/bin/sleep` |
| 14 | 18.511 | 7742 | bash | execve | `/usr/bin/python3` |
| 15 | 522.418 | 7743 | sleep | exit_group | `code=0` |
| 16 | 525.090 | 7738 | bash | clone | `` |
| 17 | 526.146 | 7744 | bash | execve | `/usr/bin/curl` |
| 18 | 542.279 | 7742 | python3 | clone3 | `` |
| 19 | 545.660 | 7745 | python3 | exit | `code=0` |
| 20 | 546.090 | 7744 | curl | exit_group | `code=0` |
| 21 | 547.226 | 7738 | bash | clone | `` |
| 22 | 547.632 | 7746 | bash | execve | `/usr/bin/chmod` |
| 23 | 551.735 | 7746 | chmod | exit_group | `code=0` |
| 24 | 552.139 | 7738 | bash | clone | `` |
| 25 | 552.577 | 7747 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 26 | 554.174 | 7747 | downloaded.sh | clone | `` |
| 27 | 554.653 | 7748 | downloaded.sh | execve | `/usr/bin/date` |
| 28 | 561.352 | 7748 | date | exit_group | `code=0` |
| 29 | 561.883 | 7747 | downloaded.sh | vfork | `` |
| 30 | 561.976 | 7750 | downloaded.sh | execve | `/usr/bin/sleep` |
| 31 | 770.264 | 7750 | sleep | exit_group | `code=0` |
| 32 | 770.601 | 7747 | downloaded.sh | exit_group | `code=0` |
| 33 | 773.552 | 7738 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 56.525 ms |
| Workload CPU (user+sys) | 83.774 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.073 ms |
| Evidence size | 11488 bytes |

