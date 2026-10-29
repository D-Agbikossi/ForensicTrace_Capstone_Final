# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 6.798 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_A_r4.json` (6208 bytes) |
| SHA-256 | `8ced6d5024f8a9f5110810e858a51370c9e06f143efc162a06b11b07d04b8809` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_A_r4.json.sha256`

## 1. Process tree

- `8684` /usr/bin/bash
  - `8685` /usr/bin/rm
  - `8686` /usr/bin/mkdir
  - `8687` /usr/bin/cat
  - `8688` /usr/bin/cat
  - `8689` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8684 (?) executed `/usr/bin/bash`
- +1.669 ms pid 8685 (bash) executed `/usr/bin/rm`
- +2.671 ms pid 8686 (bash) executed `/usr/bin/mkdir`
- +3.791 ms pid 8687 (bash) executed `/usr/bin/cat`
- +4.647 ms pid 8688 (bash) executed `/usr/bin/cat`
- +5.373 ms pid 8689 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 8684 | ? | execve | `/usr/bin/bash` |
| 2 | 1.499 | 8684 | bash | clone | `` |
| 3 | 1.669 | 8685 | bash | execve | `/usr/bin/rm` |
| 4 | 2.421 | 8685 | rm | exit_group | `code=0` |
| 5 | 2.554 | 8684 | bash | clone | `` |
| 6 | 2.671 | 8686 | bash | execve | `/usr/bin/mkdir` |
| 7 | 3.450 | 8686 | mkdir | exit_group | `code=0` |
| 8 | 3.642 | 8684 | bash | clone | `` |
| 9 | 3.791 | 8687 | bash | execve | `/usr/bin/cat` |
| 10 | 4.350 | 8687 | cat | exit_group | `code=0` |
| 11 | 4.531 | 8684 | bash | clone | `` |
| 12 | 4.647 | 8688 | bash | execve | `/usr/bin/cat` |
| 13 | 5.168 | 8688 | cat | exit_group | `code=0` |
| 14 | 5.262 | 8684 | bash | clone | `` |
| 15 | 5.373 | 8689 | bash | execve | `/usr/bin/rm` |
| 16 | 5.902 | 8689 | rm | exit_group | `code=0` |
| 17 | 6.028 | 8684 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 1.837 ms |
| Workload CPU (user+sys) | 6.057 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.028 ms |
| Evidence size | 6208 bytes |

