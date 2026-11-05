# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 24.623 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_A_r4.json` (6212 bytes) |
| SHA-256 | `a94a91ceff3a55e1d26c5e2c80d200f086872844f11becb0f09253c7dcb81d8d` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_A_r4.json.sha256`

## 1. Process tree

- `7869` /usr/bin/bash
  - `7870` /usr/bin/rm
  - `7871` /usr/bin/mkdir
  - `7872` /usr/bin/cat
  - `7873` /usr/bin/cat
  - `7874` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7869 (?) executed `/usr/bin/bash`
- +5.412 ms pid 7870 (bash) executed `/usr/bin/rm`
- +9.156 ms pid 7871 (bash) executed `/usr/bin/mkdir`
- +14.331 ms pid 7872 (bash) executed `/usr/bin/cat`
- +18.189 ms pid 7873 (bash) executed `/usr/bin/cat`
- +21.392 ms pid 7874 (bash) executed `/usr/bin/rm`

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

None.

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7869 | ? | execve | `/usr/bin/bash` |
| 2 | 5.056 | 7869 | bash | clone | `` |
| 3 | 5.412 | 7870 | bash | execve | `/usr/bin/rm` |
| 4 | 8.193 | 7870 | rm | exit_group | `code=0` |
| 5 | 8.814 | 7869 | bash | clone | `` |
| 6 | 9.156 | 7871 | bash | execve | `/usr/bin/mkdir` |
| 7 | 12.849 | 7871 | mkdir | exit_group | `code=0` |
| 8 | 14.005 | 7869 | bash | clone | `` |
| 9 | 14.331 | 7872 | bash | execve | `/usr/bin/cat` |
| 10 | 17.251 | 7872 | cat | exit_group | `code=0` |
| 11 | 17.872 | 7869 | bash | clone | `` |
| 12 | 18.189 | 7873 | bash | execve | `/usr/bin/cat` |
| 13 | 20.807 | 7873 | cat | exit_group | `code=0` |
| 14 | 21.057 | 7869 | bash | clone | `` |
| 15 | 21.392 | 7874 | bash | execve | `/usr/bin/rm` |
| 16 | 23.811 | 7874 | rm | exit_group | `code=0` |
| 17 | 24.124 | 7869 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 14.462 ms |
| Workload CPU (user+sys) | 10.228 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.031 ms |
| Evidence size | 6212 bytes |

