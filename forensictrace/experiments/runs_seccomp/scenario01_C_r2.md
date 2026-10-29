# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | C |
| Events recorded | 1307 |
| Failed exec attempts removed | 12 |
| Duration | 743.718 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_C_r2.json` (486533 bytes) |
| SHA-256 | `05c775e425129a980b5e3a72dfc7d736c2a7002be513516e4bedf2b3b0ead8a1` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_C_r2.json.sha256`

## 1. Process tree

- `8132` /usr/bin/bash
  - `8133` /usr/bin/rm
  - `8134` /usr/bin/mkdir
  - `8135` /usr/bin/cat
  - `8136` /usr/bin/python3
  - `8137` /usr/bin/sleep
  - `8139` /usr/bin/curl
  - `8140` /usr/bin/python3
  - `8141` /usr/bin/chmod
  - `8142` /tmp/ft_scenario01/downloaded.sh
    - `8143` /usr/bin/date
    - `8144` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8132 (?) executed `/usr/bin/bash`
- +2.479 ms pid 8133 (bash) executed `/usr/bin/rm`
- +6.020 ms pid 8134 (bash) executed `/usr/bin/mkdir`
- +9.734 ms pid 8135 (bash) executed `/usr/bin/cat`
- +12.640 ms pid 8137 (bash) executed `/usr/bin/sleep`
- +12.674 ms pid 8136 (bash) executed `/usr/bin/python3`
- +516.235 ms pid 8139 (bash) executed `/usr/bin/curl`
- +531.059 ms pid 8141 (bash) executed `/usr/bin/chmod`
- +533.109 ms pid 8142 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +533.863 ms pid 8143 (downloaded.sh) executed `/usr/bin/date`
- +535.759 ms pid 8144 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +77.527 ms pid 8136 (python3) connected to `unix:/var/run/nscd/socket`
- +77.619 ms pid 8136 (python3) connected to `ipv6:[...]`
- +77.654 ms pid 8136 (python3) connected to `sockfd=3`
- +77.678 ms pid 8136 (python3) connected to `0.0.0.0:8765`
- +79.084 ms pid 8136 (python3) connected to `unix:/var/run/nscd/socket`
- +524.639 ms pid 8139 (curl) connected to `unix:/var/run/nscd/socket`
- +524.718 ms pid 8139 (curl) connected to `unix:/var/run/nscd/socket`
- +525.236 ms pid 8139 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +9.552 ms by pid 8135 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +529.923 ms by pid 8139 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +532.767 ms pid 8141 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +5.253 ms pid 8133 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +5.315 ms pid 8133 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +5.377 ms pid 8133 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +524.938 ms pid 8139 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +533.109 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8142 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +5.315 ms #138 `unlinkat` by pid 8133 (rm)
    - +529.923 ms #1048 `openat` by pid 8139 (curl)
    - +530.038 ms #1052 `write` by pid 8139 (curl)
    - +530.082 ms #1054 `close` by pid 8139 (curl)
    - +532.767 ms #1123 `fchmodat` by pid 8141 (chmod)
    - +533.109 ms #1130 `execve` by pid 8142 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8132 | ? | execve | `/usr/bin/bash` |
| 15 | 0.816 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 0.894 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 0.999 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.033 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.080 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.115 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.166 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.205 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.252 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.285 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.332 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.366 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.421 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.455 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.491 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.538 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.573 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 1.617 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 1.651 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 1.704 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 1.738 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 1.784 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 1.817 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 1.865 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 1.898 | 8132 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.148 | 8132 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 2.321 | 8132 | bash | clone | `` |
| 73 | 2.479 | 8133 | bash | execve | `/usr/bin/rm` |
| 83 | 3.099 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.145 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 3.264 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 3.308 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 3.368 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 3.411 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 3.469 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 3.517 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 3.573 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 3.618 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 3.673 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 3.717 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 3.784 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 3.827 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 3.874 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 3.933 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 3.980 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 4.048 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 4.093 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 4.225 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 4.272 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 4.333 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 4.395 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 4.964 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 5.031 | 8133 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 5.160 | 8133 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 5.253 | 8133 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 5.315 | 8133 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 5.377 | 8133 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 5.543 | 8133 | rm | exit_group | `code=0` |
| 145 | 5.778 | 8132 | bash | clone | `` |
| 147 | 6.020 | 8134 | bash | execve | `/usr/bin/mkdir` |
| 167 | 7.313 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 7.360 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 7.478 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 7.523 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 7.593 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 7.671 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 7.759 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 7.817 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 7.881 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 7.932 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 8.009 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 8.057 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 8.128 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 8.183 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 8.237 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 8.299 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 8.347 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 8.408 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 8.452 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 8.521 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 8.571 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 8.638 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 8.688 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 8.756 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 8.805 | 8134 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 9.001 | 8134 | mkdir | exit_group | `code=0` |
| 223 | 9.301 | 8132 | bash | clone | `` |
| 225 | 9.552 | 8135 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 9.734 | 8135 | bash | execve | `/usr/bin/cat` |
| 240 | 10.515 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 10.562 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 10.677 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 10.720 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 10.780 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 10.825 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 10.882 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 10.927 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 10.983 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 11.028 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 11.085 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 11.128 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 11.212 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 11.257 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 11.304 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 11.368 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 11.412 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 11.472 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 11.515 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 11.579 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 11.624 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 11.680 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 11.725 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 11.782 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 11.828 | 8135 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 11.922 | 8135 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 12.067 | 8135 | cat | exit_group | `code=0` |
| 300 | 12.250 | 8132 | bash | clone | `` |
| 303 | 12.473 | 8132 | bash | clone | `` |
| 308 | 12.640 | 8137 | bash | execve | `/usr/bin/sleep` |
| 310 | 12.674 | 8136 | bash | execve | `/usr/bin/python3` |
| 330 | 13.325 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 334 | 13.379 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 340 | 13.503 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 13.552 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 346 | 13.822 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 349 | 13.905 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 352 | 13.973 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 353 | 13.984 | 8136 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 356 | 14.036 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 358 | 14.092 | 8136 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 359 | 14.108 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 362 | 14.161 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 366 | 14.240 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 368 | 14.283 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 370 | 14.431 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 372 | 14.485 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 374 | 14.534 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 14.596 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 14.643 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 14.702 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 14.748 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 14.812 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 14.858 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 14.916 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 14.960 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 15.020 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 15.063 | 8137 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 17.212 | 8136 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 17.260 | 8136 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 17.305 | 8136 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 17.332 | 8136 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 17.356 | 8136 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 18.499 | 8136 | python3 | openat | `/etc/localtime` |
| 434 | 22.588 | 8136 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 22.711 | 8136 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 22.889 | 8136 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 23.962 | 8136 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 24.081 | 8136 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 24.157 | 8136 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 32.012 | 8136 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 77.335 | 8136 | python3 | openat | `/etc/gai.conf` |
| 798 | 77.472 | 8136 | python3 | sendto | `socket:[49118]` |
| 799 | 77.527 | 8136 | python3 | connect | `unix:/var/run/nscd/socket` |
| 802 | 77.619 | 8136 | python3 | connect | `ipv6:[...]` |
| 803 | 77.654 | 8136 | python3 | connect | `sockfd=3` |
| 804 | 77.678 | 8136 | python3 | connect | `0.0.0.0:8765` |
| 814 | 79.084 | 8136 | python3 | connect | `unix:/var/run/nscd/socket` |
| 816 | 79.309 | 8136 | python3 | openat | `/etc/nsswitch.conf` |
| 820 | 79.422 | 8136 | python3 | openat | `/etc/host.conf` |
| 824 | 79.518 | 8136 | python3 | openat | `/etc/resolv.conf` |
| 828 | 79.618 | 8136 | python3 | openat | `/etc/hosts` |
| 832 | 79.719 | 8136 | python3 | openat | `/etc/hosts` |
| 837 | 515.708 | 8137 | sleep | exit_group | `code=0` |
| 839 | 516.007 | 8132 | bash | clone | `` |
| 841 | 516.235 | 8139 | bash | execve | `/usr/bin/curl` |
| 937 | 521.626 | 8139 | curl | openat | `/etc/gnutls/config` |
| 955 | 522.756 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 957 | 522.804 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 961 | 522.926 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 963 | 522.974 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 965 | 523.051 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 967 | 523.111 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 969 | 523.195 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 971 | 523.310 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 973 | 523.386 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 975 | 523.444 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 977 | 523.516 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 523.569 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 981 | 523.653 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 983 | 523.706 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 985 | 523.771 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 987 | 523.848 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 989 | 523.901 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 991 | 523.973 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 993 | 524.030 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 995 | 524.122 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 997 | 524.190 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 999 | 524.268 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1001 | 524.330 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1003 | 524.406 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1005 | 524.468 | 8139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1007 | 524.553 | 8139 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1008 | 524.587 | 8139 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1009 | 524.639 | 8139 | curl | connect | `unix:/var/run/nscd/socket` |
| 1011 | 524.718 | 8139 | curl | connect | `unix:/var/run/nscd/socket` |
| 1013 | 524.792 | 8139 | curl | openat | `/etc/nsswitch.conf` |
| 1017 | 524.938 | 8139 | curl | openat | `/etc/passwd` |
| 1020 | 525.043 | 8139 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1021 | 525.236 | 8139 | curl | connect | `127.0.0.1:8765` |
| 1022 | 525.372 | 8139 | curl | sendto | `socket:[51468]` |
| 1023 | 525.402 | 8136 | python3 | accept4 | `sockfd=3` |
| 1024 | 525.557 | 8136 | python3 | clone3 | `` |
| 1025 | 525.741 | 8140 | python3 | recvfrom | `socket:[49123]` |
| 1026 | 526.102 | 8140 | python3 | openat | `/etc/mime.types` |
| 1039 | 529.571 | 8140 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1041 | 529.734 | 8140 | python3 | sendto | `socket:[49123]` |
| 1042 | 529.781 | 8139 | curl | recvfrom | `socket:[51468]` |
| 1045 | 529.866 | 8140 | python3 | sendto | `socket:[49123]` |
| 1046 | 529.893 | 8139 | curl | recvfrom | `socket:[51468]` |
| 1048 | 529.923 | 8139 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1052 | 530.038 | 8139 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1053 | 530.067 | 8140 | python3 | exit | `code=0` |
| 1057 | 530.328 | 8139 | curl | exit_group | `code=0` |
| 1059 | 530.886 | 8132 | bash | clone | `` |
| 1061 | 531.059 | 8141 | bash | execve | `/usr/bin/chmod` |
| 1071 | 531.694 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1073 | 531.731 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1077 | 531.823 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1079 | 531.856 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1081 | 531.904 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1083 | 531.938 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1085 | 531.983 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1087 | 532.017 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1089 | 532.062 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1091 | 532.096 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1093 | 532.141 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1095 | 532.179 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1097 | 532.234 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1099 | 532.268 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1101 | 532.305 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1103 | 532.352 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1105 | 532.385 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1107 | 532.432 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1109 | 532.465 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1111 | 532.518 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1113 | 532.552 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1115 | 532.596 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1117 | 532.630 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1119 | 532.677 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1121 | 532.714 | 8141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1123 | 532.767 | 8141 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1126 | 532.835 | 8141 | chmod | exit_group | `code=0` |
| 1128 | 532.960 | 8132 | bash | clone | `` |
| 1130 | 533.109 | 8142 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1136 | 533.589 | 8142 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1139 | 533.664 | 8142 | downloaded.sh | clone | `` |
| 1145 | 533.863 | 8143 | downloaded.sh | execve | `/usr/bin/date` |
| 1155 | 534.372 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1157 | 534.408 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1161 | 534.498 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1163 | 534.533 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1165 | 534.579 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1167 | 534.613 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1169 | 534.657 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1171 | 534.692 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1173 | 534.737 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1175 | 534.770 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1177 | 534.814 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1179 | 534.846 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1181 | 534.901 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1183 | 534.936 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1185 | 534.971 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1187 | 535.016 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1189 | 535.049 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1191 | 535.096 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1193 | 535.133 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1195 | 535.187 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1197 | 535.223 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1199 | 535.267 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1201 | 535.301 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1203 | 535.348 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1205 | 535.381 | 8143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1207 | 535.435 | 8143 | date | openat | `/etc/localtime` |
| 1216 | 535.597 | 8143 | date | exit_group | `code=0` |
| 1218 | 535.722 | 8142 | downloaded.sh | vfork | `` |
| 1219 | 535.759 | 8144 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1229 | 536.208 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1231 | 536.244 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1235 | 536.329 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1237 | 536.363 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1239 | 536.406 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1241 | 536.441 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1243 | 536.485 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1245 | 536.517 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1247 | 536.561 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1249 | 536.594 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1251 | 536.638 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1253 | 536.672 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1255 | 536.724 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1257 | 536.758 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1259 | 536.793 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1261 | 536.837 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1263 | 536.872 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1265 | 536.916 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1267 | 536.950 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1269 | 536.999 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1271 | 537.032 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1273 | 537.076 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1275 | 537.108 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1277 | 537.154 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1279 | 537.193 | 8144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1296 | 738.274 | 8144 | sleep | exit_group | `code=0` |
| 1298 | 739.010 | 8142 | downloaded.sh | exit_group | `code=0` |
| 1307 | 742.746 | 8132 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 32.962 ms |
| Workload CPU (user+sys) | 82.442 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 8.385 ms |
| Evidence size | 486533 bytes |

