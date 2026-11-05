# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | A |
| Events recorded | 27 |
| Failed exec attempts removed | 12 |
| Duration | 522.352 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_A_r4.json` (9468 bytes) |
| SHA-256 | `94c92a3167bd996ff1407d49ee402f292575dce51c75b8e82ef4c5bd278a6298` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_A_r4.json.sha256`

## 1. Process tree

- `8613` /usr/bin/bash
  - `8614` /usr/bin/rm
  - `8615` /usr/bin/mkdir
  - `8616` /usr/bin/python3
  - `8617` /usr/bin/sleep
  - `8618` /usr/bin/curl
  - `8619` /usr/bin/python3
  - `8620` /usr/bin/cat
  - `8621` /usr/bin/chmod
  - `8622` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8613 (?) executed `/usr/bin/bash`
- +2.461 ms pid 8614 (bash) executed `/usr/bin/rm`
- +4.031 ms pid 8615 (bash) executed `/usr/bin/mkdir`
- +5.290 ms pid 8616 (bash) executed `/usr/bin/python3`
- +5.323 ms pid 8617 (bash) executed `/usr/bin/sleep`
- +507.060 ms pid 8618 (bash) executed `/usr/bin/curl`
- +515.852 ms pid 8620 (bash) executed `/usr/bin/cat`
- +517.849 ms pid 8621 (bash) executed `/usr/bin/chmod`
- +519.234 ms pid 8622 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

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

- +519.234 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8622 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8613 | ? | execve | `/usr/bin/bash` |
| 2 | 2.252 | 8613 | bash | clone | `` |
| 3 | 2.461 | 8614 | bash | execve | `/usr/bin/rm` |
| 4 | 3.698 | 8614 | rm | exit_group | `code=0` |
| 5 | 3.886 | 8613 | bash | clone | `` |
| 6 | 4.031 | 8615 | bash | execve | `/usr/bin/mkdir` |
| 7 | 4.847 | 8615 | mkdir | exit_group | `code=0` |
| 8 | 5.025 | 8613 | bash | clone | `` |
| 9 | 5.188 | 8613 | bash | clone | `` |
| 10 | 5.290 | 8616 | bash | execve | `/usr/bin/python3` |
| 11 | 5.323 | 8617 | bash | execve | `/usr/bin/sleep` |
| 12 | 506.256 | 8617 | sleep | exit_group | `code=0` |
| 13 | 506.724 | 8613 | bash | clone | `` |
| 14 | 507.060 | 8618 | bash | execve | `/usr/bin/curl` |
| 15 | 511.564 | 8616 | python3 | clone3 | `` |
| 16 | 514.564 | 8619 | python3 | exit | `code=0` |
| 17 | 514.754 | 8618 | curl | exit_group | `code=0` |
| 18 | 515.540 | 8613 | bash | clone | `` |
| 19 | 515.852 | 8620 | bash | execve | `/usr/bin/cat` |
| 20 | 516.809 | 8620 | cat | exit_group | `code=0` |
| 21 | 517.561 | 8613 | bash | clone | `` |
| 22 | 517.849 | 8621 | bash | execve | `/usr/bin/chmod` |
| 23 | 518.830 | 8621 | chmod | exit_group | `code=0` |
| 24 | 519.058 | 8613 | bash | clone | `` |
| 25 | 519.234 | 8622 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 26 | 519.794 | 8622 | runme.sh | exit_group | `code=0` |
| 27 | 521.359 | 8613 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 3.082 ms |
| Workload CPU (user+sys) | 58.658 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.070 ms |
| Evidence size | 9468 bytes |

