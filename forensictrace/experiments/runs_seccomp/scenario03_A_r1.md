# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | A |
| Events recorded | 27 |
| Failed exec attempts removed | 12 |
| Duration | 522.082 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_A_r1.json` (9471 bytes) |
| SHA-256 | `03a333f13d200294a37074a2800781cba68977269730c2c1b8883991e9a84b2b` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_A_r1.json.sha256`

## 1. Process tree

- `8053` /usr/bin/bash
  - `8054` /usr/bin/rm
  - `8055` /usr/bin/mkdir
  - `8056` /usr/bin/python3
  - `8057` /usr/bin/sleep
  - `8059` /usr/bin/curl
  - `8060` /usr/bin/python3
  - `8061` /usr/bin/cat
  - `8062` /usr/bin/chmod
  - `8063` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8053 (?) executed `/usr/bin/bash`
- +1.424 ms pid 8054 (bash) executed `/usr/bin/rm`
- +3.067 ms pid 8055 (bash) executed `/usr/bin/mkdir`
- +5.499 ms pid 8056 (bash) executed `/usr/bin/python3`
- +5.798 ms pid 8057 (bash) executed `/usr/bin/sleep`
- +507.524 ms pid 8059 (bash) executed `/usr/bin/curl`
- +515.314 ms pid 8061 (bash) executed `/usr/bin/cat`
- +516.402 ms pid 8062 (bash) executed `/usr/bin/chmod`
- +517.335 ms pid 8063 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

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

- +517.335 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8063 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8053 | ? | execve | `/usr/bin/bash` |
| 2 | 1.260 | 8053 | bash | clone | `` |
| 3 | 1.424 | 8054 | bash | execve | `/usr/bin/rm` |
| 4 | 2.587 | 8054 | rm | exit_group | `code=0` |
| 5 | 2.887 | 8053 | bash | clone | `` |
| 6 | 3.067 | 8055 | bash | execve | `/usr/bin/mkdir` |
| 7 | 4.556 | 8055 | mkdir | exit_group | `code=0` |
| 8 | 4.938 | 8053 | bash | clone | `` |
| 9 | 5.499 | 8056 | bash | execve | `/usr/bin/python3` |
| 10 | 5.545 | 8053 | bash | clone | `` |
| 11 | 5.798 | 8057 | bash | execve | `/usr/bin/sleep` |
| 12 | 506.936 | 8057 | sleep | exit_group | `code=0` |
| 13 | 507.250 | 8053 | bash | clone | `` |
| 14 | 507.524 | 8059 | bash | execve | `/usr/bin/curl` |
| 15 | 511.741 | 8056 | python3 | clone3 | `` |
| 16 | 514.294 | 8060 | python3 | exit | `code=0` |
| 17 | 514.492 | 8059 | curl | exit_group | `code=0` |
| 18 | 515.061 | 8053 | bash | clone | `` |
| 19 | 515.314 | 8061 | bash | execve | `/usr/bin/cat` |
| 20 | 516.093 | 8061 | cat | exit_group | `code=0` |
| 21 | 516.262 | 8053 | bash | clone | `` |
| 22 | 516.402 | 8062 | bash | execve | `/usr/bin/chmod` |
| 23 | 517.060 | 8062 | chmod | exit_group | `code=0` |
| 24 | 517.190 | 8053 | bash | clone | `` |
| 25 | 517.335 | 8063 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 26 | 517.772 | 8063 | runme.sh | exit_group | `code=0` |
| 27 | 521.273 | 8053 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 2.552 ms |
| Workload CPU (user+sys) | 70.535 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.059 ms |
| Evidence size | 9471 bytes |

