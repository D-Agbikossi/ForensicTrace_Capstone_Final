# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | A |
| Events recorded | 17 |
| Failed exec attempts removed | 12 |
| Duration | 50.729 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_A_r3.json` (6213 bytes) |
| SHA-256 | `61b2d94a2755a88578e71f1f57f4fa459fa2bb0793db626d7e639173fcc4a27c` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_A_r3.json.sha256`

## 1. Process tree

- `7691` /usr/bin/bash
  - `7693` /usr/bin/rm
  - `7694` /usr/bin/mkdir
  - `7695` /usr/bin/cat
  - `7696` /usr/bin/cat
  - `7697` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7691 (?) executed `/usr/bin/bash`
- +11.991 ms pid 7693 (bash) executed `/usr/bin/rm`
- +24.509 ms pid 7694 (bash) executed `/usr/bin/mkdir`
- +33.359 ms pid 7695 (bash) executed `/usr/bin/cat`
- +38.399 ms pid 7696 (bash) executed `/usr/bin/cat`
- +43.273 ms pid 7697 (bash) executed `/usr/bin/rm`

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
| 1 | 0.000 | 7691 | ? | execve | `/usr/bin/bash` |
| 2 | 11.322 | 7691 | bash | clone | `` |
| 3 | 11.991 | 7693 | bash | execve | `/usr/bin/rm` |
| 4 | 20.506 | 7693 | rm | exit_group | `code=0` |
| 5 | 22.408 | 7691 | bash | clone | `` |
| 6 | 24.509 | 7694 | bash | execve | `/usr/bin/mkdir` |
| 7 | 30.597 | 7694 | mkdir | exit_group | `code=0` |
| 8 | 32.502 | 7691 | bash | clone | `` |
| 9 | 33.359 | 7695 | bash | execve | `/usr/bin/cat` |
| 10 | 37.139 | 7695 | cat | exit_group | `code=0` |
| 11 | 37.960 | 7691 | bash | clone | `` |
| 12 | 38.399 | 7696 | bash | execve | `/usr/bin/cat` |
| 13 | 42.357 | 7696 | cat | exit_group | `code=0` |
| 14 | 42.786 | 7691 | bash | clone | `` |
| 15 | 43.273 | 7697 | bash | execve | `/usr/bin/rm` |
| 16 | 49.308 | 7697 | rm | exit_group | `code=0` |
| 17 | 49.671 | 7691 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 22.088 ms |
| Workload CPU (user+sys) | 17.366 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.035 ms |
| Evidence size | 6213 bytes |

