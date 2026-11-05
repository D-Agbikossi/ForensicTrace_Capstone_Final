# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 8.626 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_A_r3.json` (6212 bytes) |
| SHA-256 | `29ece73d2b22b110a670b21aeb0b7dcc2df8eda155c57967a59de17e2769fe54` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_A_r3.json.sha256`

## 1. Process tree

- `8392` /usr/bin/bash
  - `8393` /usr/bin/rm
  - `8394` /usr/bin/mkdir
  - `8395` /usr/bin/cat
  - `8396` /usr/bin/cat
  - `8397` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8392 (?) executed `/usr/bin/bash`
- +1.966 ms pid 8393 (bash) executed `/usr/bin/rm`
- +3.392 ms pid 8394 (bash) executed `/usr/bin/mkdir`
- +5.019 ms pid 8395 (bash) executed `/usr/bin/cat`
- +6.261 ms pid 8396 (bash) executed `/usr/bin/cat`
- +7.085 ms pid 8397 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 8392 | ? | execve | `/usr/bin/bash` |
| 2 | 1.602 | 8392 | bash | clone | `` |
| 3 | 1.966 | 8393 | bash | execve | `/usr/bin/rm` |
| 4 | 3.019 | 8393 | rm | exit_group | `code=0` |
| 5 | 3.219 | 8392 | bash | clone | `` |
| 6 | 3.392 | 8394 | bash | execve | `/usr/bin/mkdir` |
| 7 | 4.572 | 8394 | mkdir | exit_group | `code=0` |
| 8 | 4.793 | 8392 | bash | clone | `` |
| 9 | 5.019 | 8395 | bash | execve | `/usr/bin/cat` |
| 10 | 5.891 | 8395 | cat | exit_group | `code=1` |
| 11 | 6.110 | 8392 | bash | clone | `` |
| 12 | 6.261 | 8396 | bash | execve | `/usr/bin/cat` |
| 13 | 6.877 | 8396 | cat | exit_group | `code=0` |
| 14 | 6.985 | 8392 | bash | clone | `` |
| 15 | 7.085 | 8397 | bash | execve | `/usr/bin/rm` |
| 16 | 7.715 | 8397 | rm | exit_group | `code=0` |
| 17 | 7.816 | 8392 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 2.075 ms |
| Workload CPU (user+sys) | 7.655 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.029 ms |
| Evidence size | 6212 bytes |

