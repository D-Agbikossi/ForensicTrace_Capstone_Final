# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 35.188 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_A_r2.json` (6216 bytes) |
| SHA-256 | `c912d07f76b473536ad80d4e74c38b8f5183b981cdf9390d97d53b309ff8a601` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_A_r2.json.sha256`

## 1. Process tree

- `7403` /usr/bin/bash
  - `7404` /usr/bin/rm
  - `7405` /usr/bin/mkdir
  - `7406` /usr/bin/cat
  - `7407` /usr/bin/cat
  - `7408` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7403 (?) executed `/usr/bin/bash`
- +7.641 ms pid 7404 (bash) executed `/usr/bin/rm`
- +11.940 ms pid 7405 (bash) executed `/usr/bin/mkdir`
- +18.949 ms pid 7406 (bash) executed `/usr/bin/cat`
- +24.626 ms pid 7407 (bash) executed `/usr/bin/cat`
- +28.826 ms pid 7408 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 7403 | ? | execve | `/usr/bin/bash` |
| 2 | 6.888 | 7403 | bash | clone | `` |
| 3 | 7.641 | 7404 | bash | execve | `/usr/bin/rm` |
| 4 | 10.871 | 7404 | rm | exit_group | `code=0` |
| 5 | 11.542 | 7403 | bash | clone | `` |
| 6 | 11.940 | 7405 | bash | execve | `/usr/bin/mkdir` |
| 7 | 16.540 | 7405 | mkdir | exit_group | `code=0` |
| 8 | 18.310 | 7403 | bash | clone | `` |
| 9 | 18.949 | 7406 | bash | execve | `/usr/bin/cat` |
| 10 | 23.214 | 7406 | cat | exit_group | `code=1` |
| 11 | 24.138 | 7403 | bash | clone | `` |
| 12 | 24.626 | 7407 | bash | execve | `/usr/bin/cat` |
| 13 | 28.135 | 7407 | cat | exit_group | `code=0` |
| 14 | 28.450 | 7403 | bash | clone | `` |
| 15 | 28.826 | 7408 | bash | execve | `/usr/bin/rm` |
| 16 | 32.401 | 7408 | rm | exit_group | `code=0` |
| 17 | 34.413 | 7403 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 16.875 ms |
| Workload CPU (user+sys) | 13.902 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.040 ms |
| Evidence size | 6216 bytes |

