# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | A |
| Events recorded | 33 |
| Failed exec attempts removed | 12 |
| Duration | 724.121 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_A_r2.json` (11485 bytes) |
| SHA-256 | `53898fa20b4d61c2f55ea4ef5f610ecbcba3fd314b80fb743bb2ca4ce3c42d8e` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_A_r2.json.sha256`

## 1. Process tree

- `8163` /usr/bin/bash
  - `8164` /usr/bin/rm
  - `8165` /usr/bin/mkdir
  - `8166` /usr/bin/cat
  - `8167` /usr/bin/python3
  - `8168` /usr/bin/sleep
  - `8169` /usr/bin/curl
  - `8170` /usr/bin/python3
  - `8171` /usr/bin/chmod
  - `8172` /tmp/ft_scenario01/downloaded.sh
    - `8173` /usr/bin/date
    - `8174` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8163 (?) executed `/usr/bin/bash`
- +1.236 ms pid 8164 (bash) executed `/usr/bin/rm`
- +2.331 ms pid 8165 (bash) executed `/usr/bin/mkdir`
- +3.346 ms pid 8166 (bash) executed `/usr/bin/cat`
- +4.272 ms pid 8167 (bash) executed `/usr/bin/python3`
- +4.305 ms pid 8168 (bash) executed `/usr/bin/sleep`
- +505.639 ms pid 8169 (bash) executed `/usr/bin/curl`
- +518.196 ms pid 8171 (bash) executed `/usr/bin/chmod`
- +519.463 ms pid 8172 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +520.296 ms pid 8173 (downloaded.sh) executed `/usr/bin/date`
- +521.313 ms pid 8174 (downloaded.sh) executed `/usr/bin/sleep`

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

- +519.463 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8172 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8163 | ? | execve | `/usr/bin/bash` |
| 2 | 1.066 | 8163 | bash | clone | `` |
| 3 | 1.236 | 8164 | bash | execve | `/usr/bin/rm` |
| 4 | 2.021 | 8164 | rm | exit_group | `code=0` |
| 5 | 2.185 | 8163 | bash | clone | `` |
| 6 | 2.331 | 8165 | bash | execve | `/usr/bin/mkdir` |
| 7 | 3.026 | 8165 | mkdir | exit_group | `code=0` |
| 8 | 3.179 | 8163 | bash | clone | `` |
| 9 | 3.346 | 8166 | bash | execve | `/usr/bin/cat` |
| 10 | 3.940 | 8166 | cat | exit_group | `code=0` |
| 11 | 4.050 | 8163 | bash | clone | `` |
| 12 | 4.174 | 8163 | bash | clone | `` |
| 13 | 4.272 | 8167 | bash | execve | `/usr/bin/python3` |
| 14 | 4.305 | 8168 | bash | execve | `/usr/bin/sleep` |
| 15 | 505.041 | 8168 | sleep | exit_group | `code=0` |
| 16 | 505.434 | 8163 | bash | clone | `` |
| 17 | 505.639 | 8169 | bash | execve | `/usr/bin/curl` |
| 18 | 512.533 | 8167 | python3 | clone3 | `` |
| 19 | 516.951 | 8170 | python3 | exit | `code=0` |
| 20 | 517.282 | 8169 | curl | exit_group | `code=0` |
| 21 | 517.982 | 8163 | bash | clone | `` |
| 22 | 518.196 | 8171 | bash | execve | `/usr/bin/chmod` |
| 23 | 519.158 | 8171 | chmod | exit_group | `code=0` |
| 24 | 519.305 | 8163 | bash | clone | `` |
| 25 | 519.463 | 8172 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 26 | 520.120 | 8172 | downloaded.sh | clone | `` |
| 27 | 520.296 | 8173 | downloaded.sh | execve | `/usr/bin/date` |
| 28 | 521.116 | 8173 | date | exit_group | `code=0` |
| 29 | 521.250 | 8172 | downloaded.sh | vfork | `` |
| 30 | 521.313 | 8174 | downloaded.sh | execve | `/usr/bin/sleep` |
| 31 | 722.062 | 8174 | sleep | exit_group | `code=0` |
| 32 | 722.299 | 8172 | downloaded.sh | exit_group | `code=0` |
| 33 | 723.524 | 8163 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 2.437 ms |
| Workload CPU (user+sys) | 61.482 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.043 ms |
| Evidence size | 11485 bytes |

