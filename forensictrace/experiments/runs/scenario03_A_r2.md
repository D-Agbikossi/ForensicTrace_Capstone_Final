# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | A |
| Events recorded | 27 |
| Failed exec attempts removed | 12 |
| Duration | 728.603 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_A_r2.json` (9472 bytes) |
| SHA-256 | `e947469084378f371bc933ed7aa3ca2d1d52e0aac5bc87769ef141524cf31535` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_A_r2.json.sha256`

## 1. Process tree

- `7446` /usr/bin/bash
  - `7447` /usr/bin/rm
  - `7448` /usr/bin/mkdir
  - `7450` /usr/bin/sleep
  - `7449` /usr/bin/python3
  - `7452` /usr/bin/curl
  - `7453` /usr/bin/python3
  - `7454` /usr/bin/cat
  - `7455` /usr/bin/chmod
  - `7456` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7446 (?) executed `/usr/bin/bash`
- +5.617 ms pid 7447 (bash) executed `/usr/bin/rm`
- +10.068 ms pid 7448 (bash) executed `/usr/bin/mkdir`
- +16.056 ms pid 7450 (bash) executed `/usr/bin/sleep`
- +16.074 ms pid 7449 (bash) executed `/usr/bin/python3`
- +560.946 ms pid 7452 (bash) executed `/usr/bin/curl`
- +659.612 ms pid 7454 (bash) executed `/usr/bin/cat`
- +690.389 ms pid 7455 (bash) executed `/usr/bin/chmod`
- +715.086 ms pid 7456 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

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

- +715.086 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7456 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7446 | ? | execve | `/usr/bin/bash` |
| 2 | 5.241 | 7446 | bash | clone | `` |
| 3 | 5.617 | 7447 | bash | execve | `/usr/bin/rm` |
| 4 | 8.804 | 7447 | rm | exit_group | `code=0` |
| 5 | 9.718 | 7446 | bash | clone | `` |
| 6 | 10.068 | 7448 | bash | execve | `/usr/bin/mkdir` |
| 7 | 13.889 | 7448 | mkdir | exit_group | `code=0` |
| 8 | 14.626 | 7446 | bash | clone | `` |
| 9 | 15.669 | 7446 | bash | clone | `` |
| 10 | 16.056 | 7450 | bash | execve | `/usr/bin/sleep` |
| 11 | 16.074 | 7449 | bash | execve | `/usr/bin/python3` |
| 12 | 524.614 | 7450 | sleep | exit_group | `code=0` |
| 13 | 554.345 | 7446 | bash | clone | `` |
| 14 | 560.946 | 7452 | bash | execve | `/usr/bin/curl` |
| 15 | 619.886 | 7449 | python3 | clone3 | `` |
| 16 | 643.551 | 7452 | curl | exit_group | `code=0` |
| 17 | 644.733 | 7453 | python3 | exit | `code=0` |
| 18 | 650.033 | 7446 | bash | clone | `` |
| 19 | 659.612 | 7454 | bash | execve | `/usr/bin/cat` |
| 20 | 685.426 | 7454 | cat | exit_group | `code=0` |
| 21 | 688.754 | 7446 | bash | clone | `` |
| 22 | 690.389 | 7455 | bash | execve | `/usr/bin/chmod` |
| 23 | 708.949 | 7455 | chmod | exit_group | `code=0` |
| 24 | 713.424 | 7446 | bash | clone | `` |
| 25 | 715.086 | 7456 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 26 | 720.026 | 7456 | runme.sh | exit_group | `code=0` |
| 27 | 727.458 | 7446 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 58.928 ms |
| Workload CPU (user+sys) | 85.237 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.045 ms |
| Evidence size | 9472 bytes |

