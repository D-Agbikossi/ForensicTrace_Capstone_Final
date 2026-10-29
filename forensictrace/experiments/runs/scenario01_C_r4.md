# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | C |
| Events recorded | 1306 |
| Failed exec attempts removed | 12 |
| Duration | 871.184 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_C_r4.json` (486192 bytes) |
| SHA-256 | `20d6ead2f1afc912ad6826adabac7b8ef3ffa61ee66b10ef05e99d517dac4f0d` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_C_r4.json.sha256`

## 1. Process tree

- `7753` /usr/bin/bash
  - `7754` /usr/bin/rm
  - `7755` /usr/bin/mkdir
  - `7756` /usr/bin/cat
  - `7757` /usr/bin/python3
  - `7758` /usr/bin/sleep
  - `7760` /usr/bin/curl
  - `7761` /usr/bin/python3
  - `7762` /usr/bin/chmod
  - `7763` /tmp/ft_scenario01/downloaded.sh
    - `7764` /usr/bin/date
    - `7765` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7753 (?) executed `/usr/bin/bash`
- +5.975 ms pid 7754 (bash) executed `/usr/bin/rm`
- +10.658 ms pid 7755 (bash) executed `/usr/bin/mkdir`
- +15.270 ms pid 7756 (bash) executed `/usr/bin/cat`
- +21.234 ms pid 7757 (bash) executed `/usr/bin/python3`
- +21.245 ms pid 7758 (bash) executed `/usr/bin/sleep`
- +527.048 ms pid 7760 (bash) executed `/usr/bin/curl`
- +564.802 ms pid 7762 (bash) executed `/usr/bin/chmod`
- +572.647 ms pid 7763 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +575.798 ms pid 7764 (downloaded.sh) executed `/usr/bin/date`
- +582.775 ms pid 7765 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +98.277 ms pid 7757 (python3) connected to `unix:/var/run/nscd/socket`
- +98.391 ms pid 7757 (python3) connected to `ipv6:[...]`
- +98.570 ms pid 7757 (python3) connected to `sockfd=3`
- +98.606 ms pid 7757 (python3) connected to `0.0.0.0:8765`
- +100.945 ms pid 7757 (python3) connected to `unix:/var/run/nscd/socket`
- +549.695 ms pid 7760 (curl) connected to `unix:/var/run/nscd/socket`
- +549.830 ms pid 7760 (curl) connected to `unix:/var/run/nscd/socket`
- +553.651 ms pid 7760 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +14.914 ms by pid 7756 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +561.621 ms by pid 7760 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +569.121 ms pid 7762 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +9.153 ms pid 7754 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +9.204 ms pid 7754 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +9.261 ms pid 7754 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +550.161 ms pid 7760 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +572.647 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7763 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +9.204 ms #138 `unlinkat` by pid 7754 (rm)
    - +561.621 ms #1048 `openat` by pid 7760 (curl)
    - +562.212 ms #1052 `write` by pid 7760 (curl)
    - +562.262 ms #1053 `close` by pid 7760 (curl)
    - +569.121 ms #1122 `fchmodat` by pid 7762 (chmod)
    - +572.647 ms #1129 `execve` by pid 7763 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7753 | ? | execve | `/usr/bin/bash` |
| 15 | 2.204 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 2.275 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 2.441 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 2.476 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 2.556 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 2.590 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.664 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.697 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.770 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.804 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.878 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 2.912 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.994 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 3.028 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 3.077 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 3.152 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 3.187 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 3.259 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 3.293 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 3.374 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.408 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 3.482 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 3.526 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 3.602 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 3.635 | 7753 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 4.867 | 7753 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 5.597 | 7753 | bash | clone | `` |
| 73 | 5.975 | 7754 | bash | execve | `/usr/bin/rm` |
| 83 | 7.123 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 7.164 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 7.360 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 7.400 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 7.490 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 7.536 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 7.630 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 7.672 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 7.760 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 7.801 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 7.888 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 7.930 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 8.031 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 8.071 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 8.131 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 8.219 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 8.262 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 8.364 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 8.404 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 8.509 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 8.550 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 8.640 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 8.682 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 8.770 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 8.812 | 7754 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 8.963 | 7754 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 9.153 | 7754 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 9.204 | 7754 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 9.261 | 7754 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 9.471 | 7754 | rm | exit_group | `code=0` |
| 145 | 10.291 | 7753 | bash | clone | `` |
| 147 | 10.658 | 7755 | bash | execve | `/usr/bin/mkdir` |
| 167 | 12.103 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 12.139 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 12.298 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 12.331 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 12.404 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 12.439 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 12.518 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 12.560 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 12.642 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 12.676 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 12.750 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 12.783 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 12.866 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 12.898 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 12.949 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 13.022 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 13.056 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 13.131 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 13.165 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 13.242 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 13.276 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 13.348 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 13.383 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 13.456 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 13.491 | 7755 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 13.740 | 7755 | mkdir | exit_group | `code=0` |
| 223 | 14.563 | 7753 | bash | clone | `` |
| 225 | 14.914 | 7756 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 15.270 | 7756 | bash | execve | `/usr/bin/cat` |
| 240 | 16.568 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 16.618 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 16.834 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 16.876 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 17.008 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 17.056 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 17.156 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 17.200 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 17.293 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 17.335 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 17.428 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 17.467 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 17.606 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 17.646 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 17.708 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 17.807 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 17.851 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 17.945 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 17.986 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 18.089 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 18.135 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 18.236 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 18.285 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 18.395 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 18.451 | 7756 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 18.782 | 7756 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 19.005 | 7756 | cat | exit_group | `code=0` |
| 300 | 19.413 | 7753 | bash | clone | `` |
| 303 | 20.685 | 7753 | bash | clone | `` |
| 309 | 21.234 | 7757 | bash | execve | `/usr/bin/python3` |
| 310 | 21.245 | 7758 | bash | execve | `/usr/bin/sleep` |
| 333 | 23.016 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 335 | 23.067 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 340 | 23.281 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 23.325 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 23.423 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 23.467 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 23.575 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 23.623 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 352 | 23.717 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 354 | 23.759 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 356 | 23.853 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 358 | 23.894 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 363 | 24.006 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 366 | 24.052 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 367 | 24.064 | 7757 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 370 | 24.119 | 7757 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 371 | 24.127 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 375 | 24.237 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 377 | 24.286 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 24.388 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 24.439 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 24.557 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 24.605 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 24.697 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 24.745 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 24.847 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 24.895 | 7758 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 27.465 | 7757 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 27.502 | 7757 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 27.585 | 7757 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 27.612 | 7757 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 27.636 | 7757 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 28.626 | 7757 | python3 | openat | `/etc/localtime` |
| 434 | 34.989 | 7757 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 35.369 | 7757 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 35.672 | 7757 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 37.117 | 7757 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 37.281 | 7757 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 37.427 | 7757 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 47.246 | 7757 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 97.930 | 7757 | python3 | openat | `/etc/gai.conf` |
| 798 | 98.172 | 7757 | python3 | sendto | `socket:[47866]` |
| 799 | 98.277 | 7757 | python3 | connect | `unix:/var/run/nscd/socket` |
| 802 | 98.391 | 7757 | python3 | connect | `ipv6:[...]` |
| 803 | 98.570 | 7757 | python3 | connect | `sockfd=3` |
| 804 | 98.606 | 7757 | python3 | connect | `0.0.0.0:8765` |
| 814 | 100.945 | 7757 | python3 | connect | `unix:/var/run/nscd/socket` |
| 816 | 101.040 | 7757 | python3 | openat | `/etc/nsswitch.conf` |
| 820 | 101.194 | 7757 | python3 | openat | `/etc/host.conf` |
| 824 | 101.315 | 7757 | python3 | openat | `/etc/resolv.conf` |
| 828 | 101.444 | 7757 | python3 | openat | `/etc/hosts` |
| 832 | 101.649 | 7757 | python3 | openat | `/etc/hosts` |
| 837 | 525.599 | 7758 | sleep | exit_group | `code=0` |
| 839 | 526.585 | 7753 | bash | clone | `` |
| 841 | 527.048 | 7760 | bash | execve | `/usr/bin/curl` |
| 937 | 541.246 | 7760 | curl | openat | `/etc/gnutls/config` |
| 955 | 546.383 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 957 | 546.437 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 961 | 546.774 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 963 | 546.831 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 965 | 546.967 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 967 | 547.013 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 969 | 547.517 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 971 | 547.577 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 973 | 547.760 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 975 | 547.826 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 977 | 547.945 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 548.000 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 981 | 548.124 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 983 | 548.177 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 985 | 548.260 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 987 | 548.379 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 989 | 548.432 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 991 | 548.795 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 993 | 548.891 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 995 | 549.023 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 997 | 549.074 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 999 | 549.262 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1001 | 549.310 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1003 | 549.405 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1005 | 549.444 | 7760 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1007 | 549.567 | 7760 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1008 | 549.593 | 7760 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1009 | 549.695 | 7760 | curl | connect | `unix:/var/run/nscd/socket` |
| 1011 | 549.830 | 7760 | curl | connect | `unix:/var/run/nscd/socket` |
| 1013 | 549.941 | 7760 | curl | openat | `/etc/nsswitch.conf` |
| 1017 | 550.161 | 7760 | curl | openat | `/etc/passwd` |
| 1020 | 551.650 | 7760 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1021 | 553.651 | 7760 | curl | connect | `127.0.0.1:8765` |
| 1022 | 553.867 | 7757 | python3 | accept4 | `sockfd=3` |
| 1023 | 554.276 | 7757 | python3 | clone3 | `` |
| 1024 | 554.294 | 7760 | curl | sendto | `socket:[50227]` |
| 1025 | 554.996 | 7761 | python3 | recvfrom | `socket:[50228]` |
| 1026 | 555.413 | 7761 | python3 | openat | `/etc/mime.types` |
| 1039 | 561.062 | 7761 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1041 | 561.355 | 7761 | python3 | sendto | `socket:[50228]` |
| 1044 | 561.532 | 7761 | python3 | sendto | `socket:[50228]` |
| 1045 | 561.553 | 7760 | curl | recvfrom | `socket:[50227]` |
| 1048 | 561.621 | 7760 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1051 | 562.183 | 7761 | python3 | exit | `code=0` |
| 1052 | 562.212 | 7760 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1056 | 562.835 | 7760 | curl | exit_group | `code=0` |
| 1058 | 564.332 | 7753 | bash | clone | `` |
| 1060 | 564.802 | 7762 | bash | execve | `/usr/bin/chmod` |
| 1070 | 566.714 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1072 | 566.803 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1076 | 567.094 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1078 | 567.142 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1080 | 567.247 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1082 | 567.292 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1084 | 567.403 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1086 | 567.447 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1088 | 567.556 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1090 | 567.601 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1092 | 567.697 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1094 | 567.744 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1096 | 567.856 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1098 | 567.931 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1100 | 568.020 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1102 | 568.125 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1104 | 568.172 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1106 | 568.274 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1108 | 568.322 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1110 | 568.434 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1112 | 568.484 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1114 | 568.668 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1116 | 568.716 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1118 | 568.831 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1120 | 568.881 | 7762 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1122 | 569.121 | 7762 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1125 | 569.234 | 7762 | chmod | exit_group | `code=0` |
| 1127 | 569.846 | 7753 | bash | clone | `` |
| 1129 | 572.647 | 7763 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1135 | 574.666 | 7763 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1138 | 575.108 | 7763 | downloaded.sh | clone | `` |
| 1144 | 575.798 | 7764 | downloaded.sh | execve | `/usr/bin/date` |
| 1154 | 577.538 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1156 | 577.592 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1160 | 577.827 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1162 | 577.872 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1164 | 578.109 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1166 | 578.170 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1168 | 578.291 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1170 | 578.343 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1172 | 578.479 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1174 | 578.603 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1176 | 578.763 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1178 | 578.813 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1180 | 578.934 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1182 | 578.997 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1184 | 579.099 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1186 | 579.227 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1188 | 579.612 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1190 | 579.756 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1192 | 579.808 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1194 | 579.935 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1196 | 580.058 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1198 | 580.184 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1200 | 580.231 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1202 | 580.333 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1204 | 580.382 | 7764 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1206 | 580.516 | 7764 | date | openat | `/etc/localtime` |
| 1215 | 580.882 | 7764 | date | exit_group | `code=0` |
| 1217 | 581.462 | 7763 | downloaded.sh | vfork | `` |
| 1218 | 582.775 | 7765 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1228 | 584.147 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1230 | 584.198 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1234 | 584.438 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1236 | 584.486 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1238 | 584.607 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1240 | 584.656 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1242 | 584.756 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1244 | 584.803 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1246 | 584.904 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1248 | 584.950 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1250 | 585.053 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1252 | 585.099 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1254 | 585.215 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1256 | 585.266 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1258 | 585.342 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1260 | 585.453 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1262 | 585.508 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1264 | 585.631 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1266 | 585.682 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1268 | 585.798 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1270 | 585.850 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1272 | 585.957 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1274 | 586.008 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1276 | 586.117 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1278 | 586.166 | 7765 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1295 | 798.187 | 7765 | sleep | exit_group | `code=0` |
| 1297 | 799.037 | 7763 | downloaded.sh | exit_group | `code=0` |
| 1306 | 868.610 | 7753 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 66.203 ms |
| Workload CPU (user+sys) | 90.842 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 2.620 ms |
| Evidence size | 486192 bytes |

