# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | A |
| Events recorded | 27 |
| Failed exec attempts removed | 12 |
| Duration | 527.614 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_A_r3.json` (9471 bytes) |
| SHA-256 | `524ac17f304aa2aa8ef32698e31b143f0ca9a4492fffe3e301cefe1ee434b675` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_A_r3.json.sha256`

## 1. Process tree

- `8451` /usr/bin/bash
  - `8452` /usr/bin/rm
  - `8453` /usr/bin/mkdir
  - `8454` /usr/bin/python3
  - `8455` /usr/bin/sleep
  - `8456` /usr/bin/curl
  - `8457` /usr/bin/python3
  - `8458` /usr/bin/cat
  - `8459` /usr/bin/chmod
  - `8460` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8451 (?) executed `/usr/bin/bash`
- +1.198 ms pid 8452 (bash) executed `/usr/bin/rm`
- +2.180 ms pid 8453 (bash) executed `/usr/bin/mkdir`
- +3.277 ms pid 8454 (bash) executed `/usr/bin/python3`
- +3.302 ms pid 8455 (bash) executed `/usr/bin/sleep`
- +505.663 ms pid 8456 (bash) executed `/usr/bin/curl`
- +522.547 ms pid 8458 (bash) executed `/usr/bin/cat`
- +523.872 ms pid 8459 (bash) executed `/usr/bin/chmod`
- +525.042 ms pid 8460 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

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

- +525.042 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8460 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8451 | ? | execve | `/usr/bin/bash` |
| 2 | 1.071 | 8451 | bash | clone | `` |
| 3 | 1.198 | 8452 | bash | execve | `/usr/bin/rm` |
| 4 | 1.903 | 8452 | rm | exit_group | `code=0` |
| 5 | 2.052 | 8451 | bash | clone | `` |
| 6 | 2.180 | 8453 | bash | execve | `/usr/bin/mkdir` |
| 7 | 2.863 | 8453 | mkdir | exit_group | `code=0` |
| 8 | 3.038 | 8451 | bash | clone | `` |
| 9 | 3.181 | 8451 | bash | clone | `` |
| 10 | 3.277 | 8454 | bash | execve | `/usr/bin/python3` |
| 11 | 3.302 | 8455 | bash | execve | `/usr/bin/sleep` |
| 12 | 504.100 | 8455 | sleep | exit_group | `code=0` |
| 13 | 504.901 | 8451 | bash | clone | `` |
| 14 | 505.663 | 8456 | bash | execve | `/usr/bin/curl` |
| 15 | 516.438 | 8454 | python3 | clone3 | `` |
| 16 | 521.352 | 8457 | python3 | exit | `code=0` |
| 17 | 521.590 | 8456 | curl | exit_group | `code=0` |
| 18 | 522.237 | 8451 | bash | clone | `` |
| 19 | 522.547 | 8458 | bash | execve | `/usr/bin/cat` |
| 20 | 523.532 | 8458 | cat | exit_group | `code=0` |
| 21 | 523.724 | 8451 | bash | clone | `` |
| 22 | 523.872 | 8459 | bash | execve | `/usr/bin/chmod` |
| 23 | 524.703 | 8459 | chmod | exit_group | `code=0` |
| 24 | 524.879 | 8451 | bash | clone | `` |
| 25 | 525.042 | 8460 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 26 | 525.569 | 8460 | runme.sh | exit_group | `code=0` |
| 27 | 526.995 | 8451 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 2.584 ms |
| Workload CPU (user+sys) | 66.059 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.042 ms |
| Evidence size | 9471 bytes |

