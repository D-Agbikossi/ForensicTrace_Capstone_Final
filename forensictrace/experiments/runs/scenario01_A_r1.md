# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | A |
| Events recorded | 33 |
| Failed exec attempts removed | 12 |
| Duration | 778.511 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_A_r1.json` (11489 bytes) |
| SHA-256 | `b70b8287271fd4d9f5511027a2d345e95c6ca9b014d650700530e8a368802ebc` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_A_r1.json.sha256`

## 1. Process tree

- `7173` /usr/bin/bash
  - `7174` /usr/bin/rm
  - `7175` /usr/bin/mkdir
  - `7176` /usr/bin/cat
  - `7178` /usr/bin/sleep
  - `7177` /usr/bin/python3
  - `7179` /usr/bin/curl
  - `7180` /usr/bin/python3
  - `7181` /usr/bin/chmod
  - `7182` /tmp/ft_scenario01/downloaded.sh
    - `7183` /usr/bin/date
    - `7184` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7173 (?) executed `/usr/bin/bash`
- +6.446 ms pid 7174 (bash) executed `/usr/bin/rm`
- +10.291 ms pid 7175 (bash) executed `/usr/bin/mkdir`
- +15.723 ms pid 7176 (bash) executed `/usr/bin/cat`
- +20.161 ms pid 7178 (bash) executed `/usr/bin/sleep`
- +20.207 ms pid 7177 (bash) executed `/usr/bin/python3`
- +528.630 ms pid 7179 (bash) executed `/usr/bin/curl`
- +560.598 ms pid 7181 (bash) executed `/usr/bin/chmod`
- +563.713 ms pid 7182 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +565.562 ms pid 7183 (downloaded.sh) executed `/usr/bin/date`
- +568.664 ms pid 7184 (downloaded.sh) executed `/usr/bin/sleep`

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

- +563.713 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7182 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7173 | ? | execve | `/usr/bin/bash` |
| 2 | 6.048 | 7173 | bash | clone | `` |
| 3 | 6.446 | 7174 | bash | execve | `/usr/bin/rm` |
| 4 | 9.345 | 7174 | rm | exit_group | `code=0` |
| 5 | 9.953 | 7173 | bash | clone | `` |
| 6 | 10.291 | 7175 | bash | execve | `/usr/bin/mkdir` |
| 7 | 14.276 | 7175 | mkdir | exit_group | `code=0` |
| 8 | 15.156 | 7173 | bash | clone | `` |
| 9 | 15.723 | 7176 | bash | execve | `/usr/bin/cat` |
| 10 | 18.496 | 7176 | cat | exit_group | `code=0` |
| 11 | 18.782 | 7173 | bash | clone | `` |
| 12 | 19.801 | 7173 | bash | clone | `` |
| 13 | 20.161 | 7178 | bash | execve | `/usr/bin/sleep` |
| 14 | 20.207 | 7177 | bash | execve | `/usr/bin/python3` |
| 15 | 524.927 | 7178 | sleep | exit_group | `code=0` |
| 16 | 527.442 | 7173 | bash | clone | `` |
| 17 | 528.630 | 7179 | bash | execve | `/usr/bin/curl` |
| 18 | 555.377 | 7177 | python3 | clone3 | `` |
| 19 | 558.803 | 7180 | python3 | exit | `code=0` |
| 20 | 559.259 | 7179 | curl | exit_group | `code=0` |
| 21 | 560.248 | 7173 | bash | clone | `` |
| 22 | 560.598 | 7181 | bash | execve | `/usr/bin/chmod` |
| 23 | 563.117 | 7181 | chmod | exit_group | `code=0` |
| 24 | 563.383 | 7173 | bash | clone | `` |
| 25 | 563.713 | 7182 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 26 | 565.130 | 7182 | downloaded.sh | clone | `` |
| 27 | 565.562 | 7183 | downloaded.sh | execve | `/usr/bin/date` |
| 28 | 568.210 | 7183 | date | exit_group | `code=0` |
| 29 | 568.595 | 7182 | downloaded.sh | vfork | `` |
| 30 | 568.664 | 7184 | downloaded.sh | execve | `/usr/bin/sleep` |
| 31 | 772.235 | 7184 | sleep | exit_group | `code=0` |
| 32 | 772.942 | 7182 | downloaded.sh | exit_group | `code=0` |
| 33 | 777.801 | 7173 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 62.434 ms |
| Workload CPU (user+sys) | 84.180 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.122 ms |
| Evidence size | 11489 bytes |

