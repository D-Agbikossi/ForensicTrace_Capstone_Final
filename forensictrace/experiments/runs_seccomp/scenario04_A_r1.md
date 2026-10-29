# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 8.165 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_A_r1.json` (6208 bytes) |
| SHA-256 | `c7a0bfee077d5d0f154b05166b2207940c62e29e4129e7bbc7fcbf9321c9a497` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_A_r1.json.sha256`

## 1. Process tree

- `8086` /usr/bin/bash
  - `8087` /usr/bin/rm
  - `8088` /usr/bin/mkdir
  - `8089` /usr/bin/cat
  - `8090` /usr/bin/cat
  - `8091` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8086 (?) executed `/usr/bin/bash`
- +1.955 ms pid 8087 (bash) executed `/usr/bin/rm`
- +3.251 ms pid 8088 (bash) executed `/usr/bin/mkdir`
- +4.613 ms pid 8089 (bash) executed `/usr/bin/cat`
- +5.542 ms pid 8090 (bash) executed `/usr/bin/cat`
- +6.342 ms pid 8091 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 8086 | ? | execve | `/usr/bin/bash` |
| 2 | 1.748 | 8086 | bash | clone | `` |
| 3 | 1.955 | 8087 | bash | execve | `/usr/bin/rm` |
| 4 | 2.847 | 8087 | rm | exit_group | `code=0` |
| 5 | 3.070 | 8086 | bash | clone | `` |
| 6 | 3.251 | 8088 | bash | execve | `/usr/bin/mkdir` |
| 7 | 4.237 | 8088 | mkdir | exit_group | `code=0` |
| 8 | 4.473 | 8086 | bash | clone | `` |
| 9 | 4.613 | 8089 | bash | execve | `/usr/bin/cat` |
| 10 | 5.255 | 8089 | cat | exit_group | `code=0` |
| 11 | 5.420 | 8086 | bash | clone | `` |
| 12 | 5.542 | 8090 | bash | execve | `/usr/bin/cat` |
| 13 | 6.113 | 8090 | cat | exit_group | `code=0` |
| 14 | 6.208 | 8086 | bash | clone | `` |
| 15 | 6.342 | 8091 | bash | execve | `/usr/bin/rm` |
| 16 | 6.898 | 8091 | rm | exit_group | `code=0` |
| 17 | 7.002 | 8086 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 2.392 ms |
| Workload CPU (user+sys) | 6.756 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.030 ms |
| Evidence size | 6208 bytes |

