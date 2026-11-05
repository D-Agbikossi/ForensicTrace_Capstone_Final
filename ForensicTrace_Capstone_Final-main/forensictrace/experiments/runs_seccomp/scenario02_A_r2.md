# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 8.121 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_A_r2.json` (6213 bytes) |
| SHA-256 | `ba2e0ac69853a12293b7c7cb3a8caa30fd31d78f71cde4aeed0412e2ef244f8c` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_A_r2.json.sha256`

## 1. Process tree

- `8203` /usr/bin/bash
  - `8204` /usr/bin/rm
  - `8205` /usr/bin/mkdir
  - `8206` /usr/bin/cat
  - `8207` /usr/bin/cat
  - `8208` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8203 (?) executed `/usr/bin/bash`
- +1.542 ms pid 8204 (bash) executed `/usr/bin/rm`
- +2.747 ms pid 8205 (bash) executed `/usr/bin/mkdir`
- +4.098 ms pid 8206 (bash) executed `/usr/bin/cat`
- +5.413 ms pid 8207 (bash) executed `/usr/bin/cat`
- +6.611 ms pid 8208 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 8203 | ? | execve | `/usr/bin/bash` |
| 2 | 1.347 | 8203 | bash | clone | `` |
| 3 | 1.542 | 8204 | bash | execve | `/usr/bin/rm` |
| 4 | 2.409 | 8204 | rm | exit_group | `code=0` |
| 5 | 2.598 | 8203 | bash | clone | `` |
| 6 | 2.747 | 8205 | bash | execve | `/usr/bin/mkdir` |
| 7 | 3.685 | 8205 | mkdir | exit_group | `code=0` |
| 8 | 3.896 | 8203 | bash | clone | `` |
| 9 | 4.098 | 8206 | bash | execve | `/usr/bin/cat` |
| 10 | 4.968 | 8206 | cat | exit_group | `code=1` |
| 11 | 5.225 | 8203 | bash | clone | `` |
| 12 | 5.413 | 8207 | bash | execve | `/usr/bin/cat` |
| 13 | 6.202 | 8207 | cat | exit_group | `code=0` |
| 14 | 6.446 | 8203 | bash | clone | `` |
| 15 | 6.611 | 8208 | bash | execve | `/usr/bin/rm` |
| 16 | 7.294 | 8208 | rm | exit_group | `code=0` |
| 17 | 7.434 | 8203 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 2.153 ms |
| Workload CPU (user+sys) | 7.177 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.029 ms |
| Evidence size | 6213 bytes |

