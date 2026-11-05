# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 38.688 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_A_r4.json` (6219 bytes) |
| SHA-256 | `7731ec0aa6e8540c031a067ea010eec02056aee019bdabf9624a385e7b9fde9f` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_A_r4.json.sha256`

## 1. Process tree

- `7795` /usr/bin/bash
  - `7796` /usr/bin/rm
  - `7797` /usr/bin/mkdir
  - `7798` /usr/bin/cat
  - `7799` /usr/bin/cat
  - `7800` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7795 (?) executed `/usr/bin/bash`
- +7.812 ms pid 7796 (bash) executed `/usr/bin/rm`
- +14.157 ms pid 7797 (bash) executed `/usr/bin/mkdir`
- +24.442 ms pid 7798 (bash) executed `/usr/bin/cat`
- +29.634 ms pid 7799 (bash) executed `/usr/bin/cat`
- +34.000 ms pid 7800 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 7795 | ? | execve | `/usr/bin/bash` |
| 2 | 7.093 | 7795 | bash | clone | `` |
| 3 | 7.812 | 7796 | bash | execve | `/usr/bin/rm` |
| 4 | 12.242 | 7796 | rm | exit_group | `code=0` |
| 5 | 13.474 | 7795 | bash | clone | `` |
| 6 | 14.157 | 7797 | bash | execve | `/usr/bin/mkdir` |
| 7 | 20.141 | 7797 | mkdir | exit_group | `code=0` |
| 8 | 22.379 | 7795 | bash | clone | `` |
| 9 | 24.442 | 7798 | bash | execve | `/usr/bin/cat` |
| 10 | 28.403 | 7798 | cat | exit_group | `code=1` |
| 11 | 29.162 | 7795 | bash | clone | `` |
| 12 | 29.634 | 7799 | bash | execve | `/usr/bin/cat` |
| 13 | 33.267 | 7799 | cat | exit_group | `code=0` |
| 14 | 33.581 | 7795 | bash | clone | `` |
| 15 | 34.000 | 7800 | bash | execve | `/usr/bin/rm` |
| 16 | 37.511 | 7800 | rm | exit_group | `code=0` |
| 17 | 38.070 | 7795 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 20.953 ms |
| Workload CPU (user+sys) | 14.794 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.049 ms |
| Evidence size | 6219 bytes |

