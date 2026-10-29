# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | A |
| Events recorded | 27 |
| Failed exec attempts removed | 12 |
| Duration | 533.893 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_A_r2.json` (9470 bytes) |
| SHA-256 | `814b003f8d65fee16a1f629be5419fbf3a28505689e9101784da467246f2a144` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_A_r2.json.sha256`

## 1. Process tree

- `8247` /usr/bin/bash
  - `8248` /usr/bin/rm
  - `8249` /usr/bin/mkdir
  - `8250` /usr/bin/python3
  - `8251` /usr/bin/sleep
  - `8252` /usr/bin/curl
  - `8253` /usr/bin/python3
  - `8254` /usr/bin/cat
  - `8255` /usr/bin/chmod
  - `8256` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8247 (?) executed `/usr/bin/bash`
- +1.432 ms pid 8248 (bash) executed `/usr/bin/rm`
- +2.794 ms pid 8249 (bash) executed `/usr/bin/mkdir`
- +4.409 ms pid 8250 (bash) executed `/usr/bin/python3`
- +4.444 ms pid 8251 (bash) executed `/usr/bin/sleep`
- +507.268 ms pid 8252 (bash) executed `/usr/bin/curl`
- +526.345 ms pid 8254 (bash) executed `/usr/bin/cat`
- +528.193 ms pid 8255 (bash) executed `/usr/bin/chmod`
- +529.936 ms pid 8256 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

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

- +529.936 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8256 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8247 | ? | execve | `/usr/bin/bash` |
| 2 | 1.247 | 8247 | bash | clone | `` |
| 3 | 1.432 | 8248 | bash | execve | `/usr/bin/rm` |
| 4 | 2.360 | 8248 | rm | exit_group | `code=0` |
| 5 | 2.643 | 8247 | bash | clone | `` |
| 6 | 2.794 | 8249 | bash | execve | `/usr/bin/mkdir` |
| 7 | 3.902 | 8249 | mkdir | exit_group | `code=0` |
| 8 | 4.142 | 8247 | bash | clone | `` |
| 9 | 4.305 | 8247 | bash | clone | `` |
| 10 | 4.409 | 8250 | bash | execve | `/usr/bin/python3` |
| 11 | 4.444 | 8251 | bash | execve | `/usr/bin/sleep` |
| 12 | 505.355 | 8251 | sleep | exit_group | `code=0` |
| 13 | 506.430 | 8247 | bash | clone | `` |
| 14 | 507.268 | 8252 | bash | execve | `/usr/bin/curl` |
| 15 | 518.171 | 8250 | python3 | clone3 | `` |
| 16 | 524.633 | 8253 | python3 | exit | `code=0` |
| 17 | 524.930 | 8252 | curl | exit_group | `code=0` |
| 18 | 525.834 | 8247 | bash | clone | `` |
| 19 | 526.345 | 8254 | bash | execve | `/usr/bin/cat` |
| 20 | 527.714 | 8254 | cat | exit_group | `code=0` |
| 21 | 527.957 | 8247 | bash | clone | `` |
| 22 | 528.193 | 8255 | bash | execve | `/usr/bin/chmod` |
| 23 | 529.412 | 8255 | chmod | exit_group | `code=0` |
| 24 | 529.648 | 8247 | bash | clone | `` |
| 25 | 529.936 | 8256 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 26 | 530.694 | 8256 | runme.sh | exit_group | `code=0` |
| 27 | 532.969 | 8247 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 3.292 ms |
| Workload CPU (user+sys) | 72.054 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.056 ms |
| Evidence size | 9470 bytes |

