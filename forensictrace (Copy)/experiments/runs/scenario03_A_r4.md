# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | A |
| Events recorded | 27 |
| Failed exec attempts removed | 12 |
| Duration | 601.356 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_A_r4.json` (9470 bytes) |
| SHA-256 | `cd1d684db12a8d1eac79f3727f18bab7b0410a12c13f022be6d6f6f2339e32b3` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_A_r4.json.sha256`

## 1. Process tree

- `7812` /usr/bin/bash
  - `7813` /usr/bin/rm
  - `7814` /usr/bin/mkdir
  - `7816` /usr/bin/sleep
  - `7815` /usr/bin/python3
  - `7817` /usr/bin/curl
  - `7818` /usr/bin/python3
  - `7819` /usr/bin/cat
  - `7820` /usr/bin/chmod
  - `7821` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7812 (?) executed `/usr/bin/bash`
- +7.811 ms pid 7813 (bash) executed `/usr/bin/rm`
- +12.066 ms pid 7814 (bash) executed `/usr/bin/mkdir`
- +18.125 ms pid 7816 (bash) executed `/usr/bin/sleep`
- +18.142 ms pid 7815 (bash) executed `/usr/bin/python3`
- +523.830 ms pid 7817 (bash) executed `/usr/bin/curl`
- +581.783 ms pid 7819 (bash) executed `/usr/bin/cat`
- +586.198 ms pid 7820 (bash) executed `/usr/bin/chmod`
- +597.251 ms pid 7821 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

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

- +597.251 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7821 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7812 | ? | execve | `/usr/bin/bash` |
| 2 | 7.433 | 7812 | bash | clone | `` |
| 3 | 7.811 | 7813 | bash | execve | `/usr/bin/rm` |
| 4 | 11.091 | 7813 | rm | exit_group | `code=0` |
| 5 | 11.712 | 7812 | bash | clone | `` |
| 6 | 12.066 | 7814 | bash | execve | `/usr/bin/mkdir` |
| 7 | 15.992 | 7814 | mkdir | exit_group | `code=0` |
| 8 | 16.663 | 7812 | bash | clone | `` |
| 9 | 17.757 | 7812 | bash | clone | `` |
| 10 | 18.125 | 7816 | bash | execve | `/usr/bin/sleep` |
| 11 | 18.142 | 7815 | bash | execve | `/usr/bin/python3` |
| 12 | 521.795 | 7816 | sleep | exit_group | `code=0` |
| 13 | 522.969 | 7812 | bash | clone | `` |
| 14 | 523.830 | 7817 | bash | execve | `/usr/bin/curl` |
| 15 | 568.305 | 7815 | python3 | clone3 | `` |
| 16 | 579.088 | 7818 | python3 | exit | `code=0` |
| 17 | 579.569 | 7817 | curl | exit_group | `code=0` |
| 18 | 581.061 | 7812 | bash | clone | `` |
| 19 | 581.783 | 7819 | bash | execve | `/usr/bin/cat` |
| 20 | 584.587 | 7819 | cat | exit_group | `code=0` |
| 21 | 585.389 | 7812 | bash | clone | `` |
| 22 | 586.198 | 7820 | bash | execve | `/usr/bin/chmod` |
| 23 | 596.450 | 7820 | chmod | exit_group | `code=0` |
| 24 | 596.822 | 7812 | bash | clone | `` |
| 25 | 597.251 | 7821 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 26 | 598.812 | 7821 | runme.sh | exit_group | `code=0` |
| 27 | 600.507 | 7812 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 57.850 ms |
| Workload CPU (user+sys) | 94.136 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.043 ms |
| Evidence size | 9470 bytes |

