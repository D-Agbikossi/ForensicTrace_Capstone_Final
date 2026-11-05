# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | A |
| Events recorded | 33 |
| Failed exec attempts removed | 12 |
| Duration | 738.727 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_A_r1.json` (11485 bytes) |
| SHA-256 | `846e71df5763d92c47fb39d409a57023335bcfe53c09647404977dfda8d93bf9` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_A_r1.json.sha256`

## 1. Process tree

- `7950` /usr/bin/bash
  - `7951` /usr/bin/rm
  - `7952` /usr/bin/mkdir
  - `7953` /usr/bin/cat
  - `7954` /usr/bin/python3
  - `7955` /usr/bin/sleep
  - `7956` /usr/bin/curl
  - `7957` /usr/bin/python3
  - `7958` /usr/bin/chmod
  - `7959` /tmp/ft_scenario01/downloaded.sh
    - `7960` /usr/bin/date
    - `7961` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7950 (?) executed `/usr/bin/bash`
- +1.257 ms pid 7951 (bash) executed `/usr/bin/rm`
- +2.259 ms pid 7952 (bash) executed `/usr/bin/mkdir`
- +3.309 ms pid 7953 (bash) executed `/usr/bin/cat`
- +4.222 ms pid 7954 (bash) executed `/usr/bin/python3`
- +4.273 ms pid 7955 (bash) executed `/usr/bin/sleep`
- +506.611 ms pid 7956 (bash) executed `/usr/bin/curl`
- +531.638 ms pid 7958 (bash) executed `/usr/bin/chmod`
- +533.107 ms pid 7959 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +533.917 ms pid 7960 (downloaded.sh) executed `/usr/bin/date`
- +535.085 ms pid 7961 (downloaded.sh) executed `/usr/bin/sleep`

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

- +533.107 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7959 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7950 | ? | execve | `/usr/bin/bash` |
| 2 | 1.124 | 7950 | bash | clone | `` |
| 3 | 1.257 | 7951 | bash | execve | `/usr/bin/rm` |
| 4 | 2.001 | 7951 | rm | exit_group | `code=0` |
| 5 | 2.149 | 7950 | bash | clone | `` |
| 6 | 2.259 | 7952 | bash | execve | `/usr/bin/mkdir` |
| 7 | 2.987 | 7952 | mkdir | exit_group | `code=0` |
| 8 | 3.146 | 7950 | bash | clone | `` |
| 9 | 3.309 | 7953 | bash | execve | `/usr/bin/cat` |
| 10 | 3.869 | 7953 | cat | exit_group | `code=0` |
| 11 | 3.964 | 7950 | bash | clone | `` |
| 12 | 4.128 | 7950 | bash | clone | `` |
| 13 | 4.222 | 7954 | bash | execve | `/usr/bin/python3` |
| 14 | 4.273 | 7955 | bash | execve | `/usr/bin/sleep` |
| 15 | 505.244 | 7955 | sleep | exit_group | `code=0` |
| 16 | 506.119 | 7950 | bash | clone | `` |
| 17 | 506.611 | 7956 | bash | execve | `/usr/bin/curl` |
| 18 | 526.012 | 7954 | python3 | clone3 | `` |
| 19 | 529.279 | 7957 | python3 | exit | `code=0` |
| 20 | 529.606 | 7956 | curl | exit_group | `code=0` |
| 21 | 531.473 | 7950 | bash | clone | `` |
| 22 | 531.638 | 7958 | bash | execve | `/usr/bin/chmod` |
| 23 | 532.721 | 7958 | chmod | exit_group | `code=0` |
| 24 | 532.938 | 7950 | bash | clone | `` |
| 25 | 533.107 | 7959 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 26 | 533.749 | 7959 | downloaded.sh | clone | `` |
| 27 | 533.917 | 7960 | downloaded.sh | execve | `/usr/bin/date` |
| 28 | 534.884 | 7960 | date | exit_group | `code=0` |
| 29 | 535.030 | 7959 | downloaded.sh | vfork | `` |
| 30 | 535.085 | 7961 | downloaded.sh | execve | `/usr/bin/sleep` |
| 31 | 735.898 | 7961 | sleep | exit_group | `code=0` |
| 32 | 736.217 | 7959 | downloaded.sh | exit_group | `code=0` |
| 33 | 737.851 | 7950 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 2.848 ms |
| Workload CPU (user+sys) | 68.170 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.116 ms |
| Evidence size | 11485 bytes |

