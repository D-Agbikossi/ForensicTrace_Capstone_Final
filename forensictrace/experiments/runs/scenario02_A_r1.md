# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 25.363 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_A_r1.json` (6218 bytes) |
| SHA-256 | `b6ed4bc90f1702f9d41c69ff6d3618c82af179eee06c4dcdc99f278419cd2e2d` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_A_r1.json.sha256`

## 1. Process tree

- `7206` /usr/bin/bash
  - `7207` /usr/bin/rm
  - `7208` /usr/bin/mkdir
  - `7209` /usr/bin/cat
  - `7210` /usr/bin/cat
  - `7211` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7206 (?) executed `/usr/bin/bash`
- +4.917 ms pid 7207 (bash) executed `/usr/bin/rm`
- +8.616 ms pid 7208 (bash) executed `/usr/bin/mkdir`
- +14.175 ms pid 7209 (bash) executed `/usr/bin/cat`
- +17.724 ms pid 7210 (bash) executed `/usr/bin/cat`
- +21.511 ms pid 7211 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 7206 | ? | execve | `/usr/bin/bash` |
| 2 | 4.546 | 7206 | bash | clone | `` |
| 3 | 4.917 | 7207 | bash | execve | `/usr/bin/rm` |
| 4 | 7.657 | 7207 | rm | exit_group | `code=0` |
| 5 | 8.269 | 7206 | bash | clone | `` |
| 6 | 8.616 | 7208 | bash | execve | `/usr/bin/mkdir` |
| 7 | 12.742 | 7208 | mkdir | exit_group | `code=0` |
| 8 | 13.719 | 7206 | bash | clone | `` |
| 9 | 14.175 | 7209 | bash | execve | `/usr/bin/cat` |
| 10 | 16.889 | 7209 | cat | exit_group | `code=1` |
| 11 | 17.372 | 7206 | bash | clone | `` |
| 12 | 17.724 | 7210 | bash | execve | `/usr/bin/cat` |
| 13 | 20.961 | 7210 | cat | exit_group | `code=0` |
| 14 | 21.176 | 7206 | bash | clone | `` |
| 15 | 21.511 | 7211 | bash | execve | `/usr/bin/rm` |
| 16 | 24.613 | 7211 | rm | exit_group | `code=0` |
| 17 | 24.879 | 7206 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 14.776 ms |
| Workload CPU (user+sys) | 10.496 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.035 ms |
| Evidence size | 6218 bytes |

