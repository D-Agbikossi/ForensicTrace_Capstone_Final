# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | B |
| Events recorded | 1291 |
| Failed exec attempts removed | 12 |
| Duration | 752.061 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_B_r2.json` (481012 bytes) |
| SHA-256 | `91e4e77a0a3448c6b0d266044283739408269db1756037f0fc01558d150a6f53` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_B_r2.json.sha256`

## 1. Process tree

- `8116` /usr/bin/bash
  - `8117` /usr/bin/rm
  - `8118` /usr/bin/mkdir
  - `8119` /usr/bin/cat
  - `8120` /usr/bin/python3
  - `8121` /usr/bin/sleep
  - `8124` /usr/bin/curl
  - `8125` /usr/bin/python3
  - `8126` /usr/bin/chmod
  - `8127` /tmp/ft_scenario01/downloaded.sh
    - `8128` /usr/bin/date
    - `8129` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8116 (?) executed `/usr/bin/bash`
- +3.104 ms pid 8117 (bash) executed `/usr/bin/rm`
- +6.415 ms pid 8118 (bash) executed `/usr/bin/mkdir`
- +8.978 ms pid 8119 (bash) executed `/usr/bin/cat`
- +11.234 ms pid 8121 (bash) executed `/usr/bin/sleep`
- +11.270 ms pid 8120 (bash) executed `/usr/bin/python3`
- +515.733 ms pid 8124 (bash) executed `/usr/bin/curl`
- +539.475 ms pid 8126 (bash) executed `/usr/bin/chmod`
- +542.120 ms pid 8127 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +543.504 ms pid 8128 (downloaded.sh) executed `/usr/bin/date`
- +546.203 ms pid 8129 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +8.821 ms by pid 8119 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +537.840 ms by pid 8124 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +541.660 ms pid 8126 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +5.848 ms pid 8117 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +5.897 ms pid 8117 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +5.943 ms pid 8117 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +532.732 ms pid 8124 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +542.120 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8127 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +5.897 ms #138 `unlinkat` by pid 8117 (rm)
    - +537.840 ms #1032 `openat` by pid 8124 (curl)
    - +538.283 ms #1037 `write` by pid 8124 (curl)
    - +538.350 ms #1038 `close` by pid 8124 (curl)
    - +541.660 ms #1107 `fchmodat` by pid 8126 (chmod)
    - +542.120 ms #1114 `execve` by pid 8127 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8116 | ? | execve | `/usr/bin/bash` |
| 15 | 1.105 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.153 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.269 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.314 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.380 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.426 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.485 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.528 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.586 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.629 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.688 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.732 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.798 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.842 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.888 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.946 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.991 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.047 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.091 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 2.154 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 2.199 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 2.256 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.300 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.373 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.417 | 8116 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.702 | 8116 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 2.904 | 8116 | bash | clone | `` |
| 73 | 3.104 | 8117 | bash | execve | `/usr/bin/rm` |
| 83 | 3.753 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.797 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 4.571 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 4.648 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 4.714 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 4.758 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 4.817 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 4.862 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 4.918 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 4.963 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 5.019 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 5.064 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 5.131 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 5.175 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 5.223 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 5.280 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 5.326 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 5.428 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 5.468 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 5.524 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 5.559 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 5.606 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 5.642 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 5.690 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 5.726 | 8117 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 5.783 | 8117 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 5.848 | 8117 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 5.897 | 8117 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 5.943 | 8117 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 6.077 | 8117 | rm | exit_group | `code=0` |
| 145 | 6.236 | 8116 | bash | clone | `` |
| 147 | 6.415 | 8118 | bash | execve | `/usr/bin/mkdir` |
| 167 | 7.273 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 7.308 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 7.407 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 7.441 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 7.487 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 7.522 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 7.567 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 7.601 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 7.645 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 7.680 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 7.726 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 7.760 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 7.814 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 7.848 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 7.885 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 7.929 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 7.962 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 8.007 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 8.041 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 8.092 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 8.127 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 8.171 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 8.206 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 8.255 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 8.290 | 8118 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 8.447 | 8118 | mkdir | exit_group | `code=0` |
| 223 | 8.627 | 8116 | bash | clone | `` |
| 225 | 8.821 | 8119 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 8.978 | 8119 | bash | execve | `/usr/bin/cat` |
| 240 | 9.557 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 9.593 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 9.681 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 9.714 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 9.761 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 9.796 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 9.840 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 9.875 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 9.919 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 9.954 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 9.998 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 10.032 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 10.086 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 10.120 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 10.157 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 10.201 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 10.235 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 10.281 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 10.314 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 10.375 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 10.412 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 10.457 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 10.491 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 10.536 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 10.571 | 8119 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 10.642 | 8119 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 10.751 | 8119 | cat | exit_group | `code=0` |
| 300 | 10.882 | 8116 | bash | clone | `` |
| 303 | 11.066 | 8116 | bash | clone | `` |
| 308 | 11.234 | 8121 | bash | execve | `/usr/bin/sleep` |
| 310 | 11.270 | 8120 | bash | execve | `/usr/bin/python3` |
| 328 | 11.858 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 331 | 11.902 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 338 | 12.021 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 341 | 12.070 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 12.132 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 12.182 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 12.238 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 12.288 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 352 | 12.353 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 355 | 12.406 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 359 | 12.464 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 362 | 12.513 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 363 | 12.525 | 8120 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 366 | 12.580 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 367 | 12.588 | 8120 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 369 | 12.624 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 372 | 12.668 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 12.725 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 12.769 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 12.830 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 12.881 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 12.942 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 12.994 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 13.055 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 13.102 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 13.165 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 13.214 | 8121 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 15.364 | 8120 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 15.453 | 8120 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 15.507 | 8120 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 15.535 | 8120 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 15.559 | 8120 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 16.851 | 8120 | python3 | openat | `/etc/localtime` |
| 434 | 21.084 | 8120 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 21.226 | 8120 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 21.405 | 8120 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 22.141 | 8120 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 22.217 | 8120 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 22.278 | 8120 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 28.349 | 8120 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 61.937 | 8120 | python3 | openat | `/etc/gai.conf` |
| 810 | 63.514 | 8120 | python3 | openat | `/etc/nsswitch.conf` |
| 814 | 63.601 | 8120 | python3 | openat | `/etc/host.conf` |
| 818 | 63.673 | 8120 | python3 | openat | `/etc/resolv.conf` |
| 822 | 63.751 | 8120 | python3 | openat | `/etc/hosts` |
| 826 | 63.832 | 8120 | python3 | openat | `/etc/hosts` |
| 831 | 514.022 | 8121 | sleep | exit_group | `code=0` |
| 833 | 514.857 | 8116 | bash | clone | `` |
| 835 | 515.733 | 8124 | bash | execve | `/usr/bin/curl` |
| 931 | 527.815 | 8124 | curl | openat | `/etc/gnutls/config` |
| 949 | 530.578 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 951 | 530.635 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 955 | 530.768 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 957 | 530.814 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 959 | 530.874 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 961 | 530.920 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 963 | 530.982 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 965 | 531.028 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 967 | 531.085 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 969 | 531.129 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 971 | 531.187 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 973 | 531.230 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 975 | 531.299 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 977 | 531.345 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 979 | 531.609 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 981 | 531.680 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 983 | 531.726 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 985 | 531.787 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 987 | 531.832 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 989 | 531.897 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 991 | 531.943 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 993 | 532.000 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 995 | 532.046 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 997 | 532.105 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 999 | 532.149 | 8124 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1001 | 532.218 | 8124 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1002 | 532.244 | 8124 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1005 | 532.377 | 8124 | curl | openat | `/etc/nsswitch.conf` |
| 1009 | 532.732 | 8124 | curl | openat | `/etc/passwd` |
| 1012 | 532.820 | 8124 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1013 | 533.410 | 8120 | python3 | clone3 | `` |
| 1014 | 533.903 | 8125 | python3 | openat | `/etc/mime.types` |
| 1027 | 537.345 | 8125 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1032 | 537.840 | 8124 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1036 | 538.260 | 8125 | python3 | exit | `code=0` |
| 1037 | 538.283 | 8124 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1041 | 538.634 | 8124 | curl | exit_group | `code=0` |
| 1043 | 539.231 | 8116 | bash | clone | `` |
| 1045 | 539.475 | 8126 | bash | execve | `/usr/bin/chmod` |
| 1055 | 540.213 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1057 | 540.265 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1061 | 540.392 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1063 | 540.440 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1065 | 540.505 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1067 | 540.553 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1069 | 540.612 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1071 | 540.667 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1073 | 540.727 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1075 | 540.773 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1077 | 540.833 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1079 | 540.880 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1081 | 540.949 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1083 | 540.997 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1085 | 541.045 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1087 | 541.106 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1089 | 541.152 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1091 | 541.214 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1093 | 541.261 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1095 | 541.327 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1097 | 541.381 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1099 | 541.439 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1101 | 541.487 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1103 | 541.548 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1105 | 541.594 | 8126 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1107 | 541.660 | 8126 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1110 | 541.756 | 8126 | chmod | exit_group | `code=0` |
| 1112 | 541.903 | 8116 | bash | clone | `` |
| 1114 | 542.120 | 8127 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1120 | 543.122 | 8127 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1123 | 543.226 | 8127 | downloaded.sh | clone | `` |
| 1129 | 543.504 | 8128 | downloaded.sh | execve | `/usr/bin/date` |
| 1139 | 544.214 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1141 | 544.263 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1145 | 544.391 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1147 | 544.437 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1149 | 544.497 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1151 | 544.543 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1153 | 544.602 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1155 | 544.645 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1157 | 544.706 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1159 | 544.750 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1161 | 544.807 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1163 | 544.852 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1165 | 544.918 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1167 | 544.963 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1169 | 545.009 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1171 | 545.068 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1173 | 545.114 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1175 | 545.172 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1177 | 545.218 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1179 | 545.281 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1181 | 545.327 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1183 | 545.416 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1185 | 545.467 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1187 | 545.531 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1189 | 545.578 | 8128 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1191 | 545.653 | 8128 | date | openat | `/etc/localtime` |
| 1200 | 545.908 | 8128 | date | exit_group | `code=0` |
| 1202 | 546.141 | 8127 | downloaded.sh | vfork | `` |
| 1203 | 546.203 | 8129 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1213 | 546.963 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1215 | 547.018 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1219 | 547.159 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1221 | 547.209 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1223 | 547.280 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1225 | 547.331 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1227 | 547.410 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1229 | 547.460 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1231 | 547.689 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1233 | 547.742 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1235 | 547.811 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1237 | 547.863 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1239 | 547.945 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1241 | 547.998 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1243 | 548.054 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1245 | 548.123 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1247 | 548.175 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1249 | 548.246 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1251 | 548.298 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1253 | 548.419 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1255 | 548.486 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1257 | 548.578 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1259 | 548.646 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1261 | 548.743 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1263 | 548.796 | 8129 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1280 | 749.480 | 8129 | sleep | exit_group | `code=0` |
| 1282 | 749.688 | 8127 | downloaded.sh | exit_group | `code=0` |
| 1291 | 751.227 | 8116 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 28.942 ms |
| Workload CPU (user+sys) | 73.997 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.797 ms |
| Evidence size | 481012 bytes |

