# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | A |
| Events recorded | 27 |
| Failed exec attempts removed | 12 |
| Duration | 563.040 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_A_r1.json` (9470 bytes) |
| SHA-256 | `7ff592653381b72be3496b3a7423668ab7c786f3bf73114e9c322c7f4672dbf3` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_A_r1.json.sha256`

## 1. Process tree

- `7264` /usr/bin/bash
  - `7265` /usr/bin/rm
  - `7266` /usr/bin/mkdir
  - `7268` /usr/bin/sleep
  - `7267` /usr/bin/python3
  - `7269` /usr/bin/curl
  - `7270` /usr/bin/python3
  - `7271` /usr/bin/cat
  - `7272` /usr/bin/chmod
  - `7273` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7264 (?) executed `/usr/bin/bash`
- +4.977 ms pid 7265 (bash) executed `/usr/bin/rm`
- +10.472 ms pid 7266 (bash) executed `/usr/bin/mkdir`
- +15.543 ms pid 7268 (bash) executed `/usr/bin/sleep`
- +15.559 ms pid 7267 (bash) executed `/usr/bin/python3`
- +522.868 ms pid 7269 (bash) executed `/usr/bin/curl`
- +550.206 ms pid 7271 (bash) executed `/usr/bin/cat`
- +555.286 ms pid 7272 (bash) executed `/usr/bin/chmod`
- +559.372 ms pid 7273 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

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

- +559.372 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7273 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7264 | ? | execve | `/usr/bin/bash` |
| 2 | 4.618 | 7264 | bash | clone | `` |
| 3 | 4.977 | 7265 | bash | execve | `/usr/bin/rm` |
| 4 | 9.317 | 7265 | rm | exit_group | `code=0` |
| 5 | 10.120 | 7264 | bash | clone | `` |
| 6 | 10.472 | 7266 | bash | execve | `/usr/bin/mkdir` |
| 7 | 13.638 | 7266 | mkdir | exit_group | `code=0` |
| 8 | 14.199 | 7264 | bash | clone | `` |
| 9 | 15.179 | 7264 | bash | clone | `` |
| 10 | 15.543 | 7268 | bash | execve | `/usr/bin/sleep` |
| 11 | 15.559 | 7267 | bash | execve | `/usr/bin/python3` |
| 12 | 519.384 | 7268 | sleep | exit_group | `code=0` |
| 13 | 521.524 | 7264 | bash | clone | `` |
| 14 | 522.868 | 7269 | bash | execve | `/usr/bin/curl` |
| 15 | 542.946 | 7267 | python3 | clone3 | `` |
| 16 | 547.504 | 7270 | python3 | exit | `code=0` |
| 17 | 548.040 | 7269 | curl | exit_group | `code=0` |
| 18 | 549.422 | 7264 | bash | clone | `` |
| 19 | 550.206 | 7271 | bash | execve | `/usr/bin/cat` |
| 20 | 554.033 | 7271 | cat | exit_group | `code=0` |
| 21 | 554.910 | 7264 | bash | clone | `` |
| 22 | 555.286 | 7272 | bash | execve | `/usr/bin/chmod` |
| 23 | 558.711 | 7272 | chmod | exit_group | `code=0` |
| 24 | 559.004 | 7264 | bash | clone | `` |
| 25 | 559.372 | 7273 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 26 | 560.935 | 7273 | runme.sh | exit_group | `code=0` |
| 27 | 562.510 | 7264 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 51.559 ms |
| Workload CPU (user+sys) | 76.529 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.039 ms |
| Evidence size | 9470 bytes |

