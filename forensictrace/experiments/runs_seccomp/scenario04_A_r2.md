# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 6.336 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_A_r2.json` (6208 bytes) |
| SHA-256 | `d79fb1a961d4caae8011bedaf55c26738b9f0d13ffe498eb3c9fa3921fdcf4a4` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_A_r2.json.sha256`

## 1. Process tree

- `8290` /usr/bin/bash
  - `8291` /usr/bin/rm
  - `8292` /usr/bin/mkdir
  - `8293` /usr/bin/cat
  - `8294` /usr/bin/cat
  - `8295` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8290 (?) executed `/usr/bin/bash`
- +1.319 ms pid 8291 (bash) executed `/usr/bin/rm`
- +2.443 ms pid 8292 (bash) executed `/usr/bin/mkdir`
- +3.486 ms pid 8293 (bash) executed `/usr/bin/cat`
- +4.337 ms pid 8294 (bash) executed `/usr/bin/cat`
- +5.103 ms pid 8295 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 8290 | ? | execve | `/usr/bin/bash` |
| 2 | 1.145 | 8290 | bash | clone | `` |
| 3 | 1.319 | 8291 | bash | execve | `/usr/bin/rm` |
| 4 | 2.181 | 8291 | rm | exit_group | `code=0` |
| 5 | 2.332 | 8290 | bash | clone | `` |
| 6 | 2.443 | 8292 | bash | execve | `/usr/bin/mkdir` |
| 7 | 3.175 | 8292 | mkdir | exit_group | `code=0` |
| 8 | 3.369 | 8290 | bash | clone | `` |
| 9 | 3.486 | 8293 | bash | execve | `/usr/bin/cat` |
| 10 | 4.051 | 8293 | cat | exit_group | `code=0` |
| 11 | 4.220 | 8290 | bash | clone | `` |
| 12 | 4.337 | 8294 | bash | execve | `/usr/bin/cat` |
| 13 | 4.883 | 8294 | cat | exit_group | `code=0` |
| 14 | 4.980 | 8290 | bash | clone | `` |
| 15 | 5.103 | 8295 | bash | execve | `/usr/bin/rm` |
| 16 | 5.650 | 8295 | rm | exit_group | `code=0` |
| 17 | 5.755 | 8290 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 1.622 ms |
| Workload CPU (user+sys) | 5.699 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.030 ms |
| Evidence size | 6208 bytes |

