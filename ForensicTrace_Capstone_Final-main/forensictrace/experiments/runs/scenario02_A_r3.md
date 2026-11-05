# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 31.171 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_A_r3.json` (6218 bytes) |
| SHA-256 | `64d61ef48ceb90fe6d0f406975dd7f8b062dca9b925a17ff537fdd7f1cc5973e` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_A_r3.json.sha256`

## 1. Process tree

- `7592` /usr/bin/bash
  - `7593` /usr/bin/rm
  - `7594` /usr/bin/mkdir
  - `7595` /usr/bin/cat
  - `7596` /usr/bin/cat
  - `7597` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7592 (?) executed `/usr/bin/bash`
- +5.507 ms pid 7593 (bash) executed `/usr/bin/rm`
- +11.849 ms pid 7594 (bash) executed `/usr/bin/mkdir`
- +18.544 ms pid 7595 (bash) executed `/usr/bin/cat`
- +22.876 ms pid 7596 (bash) executed `/usr/bin/cat`
- +26.843 ms pid 7597 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 7592 | ? | execve | `/usr/bin/bash` |
| 2 | 5.061 | 7592 | bash | clone | `` |
| 3 | 5.507 | 7593 | bash | execve | `/usr/bin/rm` |
| 4 | 10.360 | 7593 | rm | exit_group | `code=0` |
| 5 | 11.276 | 7592 | bash | clone | `` |
| 6 | 11.849 | 7594 | bash | execve | `/usr/bin/mkdir` |
| 7 | 16.395 | 7594 | mkdir | exit_group | `code=0` |
| 8 | 17.613 | 7592 | bash | clone | `` |
| 9 | 18.544 | 7595 | bash | execve | `/usr/bin/cat` |
| 10 | 21.945 | 7595 | cat | exit_group | `code=1` |
| 11 | 22.504 | 7592 | bash | clone | `` |
| 12 | 22.876 | 7596 | bash | execve | `/usr/bin/cat` |
| 13 | 26.001 | 7596 | cat | exit_group | `code=0` |
| 14 | 26.375 | 7592 | bash | clone | `` |
| 15 | 26.843 | 7597 | bash | execve | `/usr/bin/rm` |
| 16 | 30.398 | 7597 | rm | exit_group | `code=0` |
| 17 | 30.680 | 7592 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 17.441 ms |
| Workload CPU (user+sys) | 12.447 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.032 ms |
| Evidence size | 6218 bytes |

