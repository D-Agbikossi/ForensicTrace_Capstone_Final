# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 6.027 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_A_r1.json` (6214 bytes) |
| SHA-256 | `eb3e0c6abdfc605fc3e13da5b1996e301255ce42cb89fc3598fcb78f852dd47b` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_A_r1.json.sha256`

## 1. Process tree

- `7983` /usr/bin/bash
  - `7984` /usr/bin/rm
  - `7985` /usr/bin/mkdir
  - `7986` /usr/bin/cat
  - `7987` /usr/bin/cat
  - `7988` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7983 (?) executed `/usr/bin/bash`
- +1.244 ms pid 7984 (bash) executed `/usr/bin/rm`
- +2.162 ms pid 7985 (bash) executed `/usr/bin/mkdir`
- +3.172 ms pid 7986 (bash) executed `/usr/bin/cat`
- +4.012 ms pid 7987 (bash) executed `/usr/bin/cat`
- +4.772 ms pid 7988 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 7983 | ? | execve | `/usr/bin/bash` |
| 2 | 1.109 | 7983 | bash | clone | `` |
| 3 | 1.244 | 7984 | bash | execve | `/usr/bin/rm` |
| 4 | 1.903 | 7984 | rm | exit_group | `code=0` |
| 5 | 2.036 | 7983 | bash | clone | `` |
| 6 | 2.162 | 7985 | bash | execve | `/usr/bin/mkdir` |
| 7 | 2.872 | 7985 | mkdir | exit_group | `code=0` |
| 8 | 3.016 | 7983 | bash | clone | `` |
| 9 | 3.172 | 7986 | bash | execve | `/usr/bin/cat` |
| 10 | 3.736 | 7986 | cat | exit_group | `code=1` |
| 11 | 3.905 | 7983 | bash | clone | `` |
| 12 | 4.012 | 7987 | bash | execve | `/usr/bin/cat` |
| 13 | 4.548 | 7987 | cat | exit_group | `code=0` |
| 14 | 4.667 | 7983 | bash | clone | `` |
| 15 | 4.772 | 7988 | bash | execve | `/usr/bin/rm` |
| 16 | 5.300 | 7988 | rm | exit_group | `code=0` |
| 17 | 5.423 | 7983 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 1.666 ms |
| Workload CPU (user+sys) | 5.388 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.027 ms |
| Evidence size | 6214 bytes |

