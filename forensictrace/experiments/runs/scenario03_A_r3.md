# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | A |
| Events recorded | 27 |
| Failed exec attempts removed | 12 |
| Duration | 560.262 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_A_r3.json` (9471 bytes) |
| SHA-256 | `5113bb2f76774f5711fce8d7a4cde5904aad3a8bed5fcb0541e6d4c175dc5af4` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_A_r3.json.sha256`

## 1. Process tree

- `7652` /usr/bin/bash
  - `7653` /usr/bin/rm
  - `7654` /usr/bin/mkdir
  - `7655` /usr/bin/python3
  - `7656` /usr/bin/sleep
  - `7657` /usr/bin/curl
  - `7658` /usr/bin/python3
  - `7659` /usr/bin/cat
  - `7660` /usr/bin/chmod
  - `7661` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7652 (?) executed `/usr/bin/bash`
- +8.726 ms pid 7653 (bash) executed `/usr/bin/rm`
- +14.513 ms pid 7654 (bash) executed `/usr/bin/mkdir`
- +20.207 ms pid 7655 (bash) executed `/usr/bin/python3`
- +20.250 ms pid 7656 (bash) executed `/usr/bin/sleep`
- +528.493 ms pid 7657 (bash) executed `/usr/bin/curl`
- +547.963 ms pid 7659 (bash) executed `/usr/bin/cat`
- +552.667 ms pid 7660 (bash) executed `/usr/bin/chmod`
- +556.443 ms pid 7661 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

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

- +556.443 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7661 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7652 | ? | execve | `/usr/bin/bash` |
| 2 | 8.196 | 7652 | bash | clone | `` |
| 3 | 8.726 | 7653 | bash | execve | `/usr/bin/rm` |
| 4 | 13.125 | 7653 | rm | exit_group | `code=0` |
| 5 | 14.005 | 7652 | bash | clone | `` |
| 6 | 14.513 | 7654 | bash | execve | `/usr/bin/mkdir` |
| 7 | 18.211 | 7654 | mkdir | exit_group | `code=0` |
| 8 | 18.814 | 7652 | bash | clone | `` |
| 9 | 19.863 | 7652 | bash | clone | `` |
| 10 | 20.207 | 7655 | bash | execve | `/usr/bin/python3` |
| 11 | 20.250 | 7656 | bash | execve | `/usr/bin/sleep` |
| 12 | 524.363 | 7656 | sleep | exit_group | `code=0` |
| 13 | 526.807 | 7652 | bash | clone | `` |
| 14 | 528.493 | 7657 | bash | execve | `/usr/bin/curl` |
| 15 | 541.288 | 7655 | python3 | clone3 | `` |
| 16 | 545.267 | 7658 | python3 | exit | `code=0` |
| 17 | 545.806 | 7657 | curl | exit_group | `code=0` |
| 18 | 547.183 | 7652 | bash | clone | `` |
| 19 | 547.963 | 7659 | bash | execve | `/usr/bin/cat` |
| 20 | 551.606 | 7659 | cat | exit_group | `code=0` |
| 21 | 552.298 | 7652 | bash | clone | `` |
| 22 | 552.667 | 7660 | bash | execve | `/usr/bin/chmod` |
| 23 | 555.819 | 7660 | chmod | exit_group | `code=0` |
| 24 | 556.104 | 7652 | bash | clone | `` |
| 25 | 556.443 | 7661 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 26 | 557.674 | 7661 | runme.sh | exit_group | `code=0` |
| 27 | 559.444 | 7652 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 54.951 ms |
| Workload CPU (user+sys) | 85.664 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.040 ms |
| Evidence size | 9471 bytes |

