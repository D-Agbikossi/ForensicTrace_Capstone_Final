# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | C |
| Events recorded | 1307 |
| Failed exec attempts removed | 12 |
| Duration | 750.242 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_C_r1.json` (486532 bytes) |
| SHA-256 | `612d1fdc1a62aabce9d3e805513078e3b67720ba6bb7cfcde127af3deb53eba2` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_C_r1.json.sha256`

## 1. Process tree

- `7907` /usr/bin/bash
  - `7908` /usr/bin/rm
  - `7909` /usr/bin/mkdir
  - `7910` /usr/bin/cat
  - `7911` /usr/bin/python3
  - `7912` /usr/bin/sleep
  - `7917` /usr/bin/curl
  - `7918` /usr/bin/python3
  - `7919` /usr/bin/chmod
  - `7920` /tmp/ft_scenario01/downloaded.sh
    - `7921` /usr/bin/date
    - `7922` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7907 (?) executed `/usr/bin/bash`
- +4.627 ms pid 7908 (bash) executed `/usr/bin/rm`
- +7.375 ms pid 7909 (bash) executed `/usr/bin/mkdir`
- +10.197 ms pid 7910 (bash) executed `/usr/bin/cat`
- +12.911 ms pid 7912 (bash) executed `/usr/bin/sleep`
- +13.445 ms pid 7911 (bash) executed `/usr/bin/python3`
- +517.888 ms pid 7917 (bash) executed `/usr/bin/curl`
- +535.342 ms pid 7919 (bash) executed `/usr/bin/chmod`
- +537.729 ms pid 7920 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +538.603 ms pid 7921 (downloaded.sh) executed `/usr/bin/date`
- +540.573 ms pid 7922 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +67.264 ms pid 7911 (python3) connected to `unix:/var/run/nscd/socket`
- +67.358 ms pid 7911 (python3) connected to `ipv6:[...]`
- +67.394 ms pid 7911 (python3) connected to `sockfd=3`
- +67.418 ms pid 7911 (python3) connected to `0.0.0.0:8765`
- +68.865 ms pid 7911 (python3) connected to `unix:/var/run/nscd/socket`
- +527.010 ms pid 7917 (curl) connected to `unix:/var/run/nscd/socket`
- +527.074 ms pid 7917 (curl) connected to `unix:/var/run/nscd/socket`
- +527.469 ms pid 7917 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +10.068 ms by pid 7910 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +533.910 ms by pid 7917 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +537.360 ms pid 7919 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +6.814 ms pid 7908 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +6.870 ms pid 7908 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +6.929 ms pid 7908 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +527.251 ms pid 7917 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +537.729 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7920 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +6.870 ms #138 `unlinkat` by pid 7908 (rm)
    - +533.910 ms #1048 `openat` by pid 7917 (curl)
    - +534.147 ms #1052 `write` by pid 7917 (curl)
    - +534.253 ms #1054 `close` by pid 7917 (curl)
    - +537.360 ms #1123 `fchmodat` by pid 7919 (chmod)
    - +537.729 ms #1130 `execve` by pid 7920 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7907 | ? | execve | `/usr/bin/bash` |
| 15 | 2.415 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 2.470 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 2.587 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 2.627 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 2.688 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 2.731 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.791 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.830 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.901 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 3.003 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 3.117 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 3.154 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 3.210 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 3.258 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 3.295 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 3.372 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 3.417 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 3.463 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 3.501 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 3.568 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.603 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 3.659 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 3.693 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 3.748 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 3.782 | 7907 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 4.152 | 7907 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 4.412 | 7907 | bash | clone | `` |
| 73 | 4.627 | 7908 | bash | execve | `/usr/bin/rm` |
| 83 | 5.375 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 5.424 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 5.543 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 5.587 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 5.646 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 5.690 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 5.749 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 5.794 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 5.851 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 5.896 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 5.952 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 5.997 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 6.063 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 6.107 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 6.154 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 6.211 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 6.262 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 6.322 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 6.365 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 6.429 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 6.472 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 6.530 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 6.575 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 6.632 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 6.676 | 7908 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 6.742 | 7908 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 6.814 | 7908 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 6.870 | 7908 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 6.929 | 7908 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 7.058 | 7908 | rm | exit_group | `code=0` |
| 145 | 7.212 | 7907 | bash | clone | `` |
| 147 | 7.375 | 7909 | bash | execve | `/usr/bin/mkdir` |
| 167 | 8.269 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 8.306 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 8.396 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 8.429 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 8.475 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 8.523 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 8.588 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 8.637 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 8.694 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 8.741 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 8.801 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 8.845 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 8.912 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 8.956 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 9.003 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 9.060 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 9.103 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 9.160 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 9.203 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 9.276 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 9.321 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 9.378 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 9.422 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 9.483 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 9.528 | 7909 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 9.693 | 7909 | mkdir | exit_group | `code=0` |
| 223 | 9.884 | 7907 | bash | clone | `` |
| 225 | 10.068 | 7910 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 10.197 | 7910 | bash | execve | `/usr/bin/cat` |
| 240 | 10.830 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 10.880 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 10.992 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 11.040 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 11.094 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 11.136 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 11.190 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 11.238 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 11.294 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 11.336 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 11.391 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 11.441 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 11.505 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 11.538 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 11.587 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 11.647 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 11.681 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 11.740 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 11.773 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 11.830 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 11.886 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 11.930 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 11.963 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 12.023 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 12.058 | 7910 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 12.148 | 7910 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 12.355 | 7910 | cat | exit_group | `code=0` |
| 300 | 12.524 | 7907 | bash | clone | `` |
| 303 | 12.737 | 7907 | bash | clone | `` |
| 307 | 12.911 | 7912 | bash | execve | `/usr/bin/sleep` |
| 311 | 13.445 | 7911 | bash | execve | `/usr/bin/python3` |
| 334 | 14.437 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 336 | 14.500 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 342 | 14.669 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 345 | 14.719 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 348 | 14.777 | 7911 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 349 | 14.789 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 352 | 14.840 | 7911 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 353 | 14.849 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 357 | 14.921 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 360 | 14.982 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 362 | 15.057 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 364 | 15.114 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 366 | 15.189 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 368 | 15.256 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 370 | 15.348 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 372 | 15.405 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 374 | 15.464 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 15.542 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 15.598 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 15.681 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 15.749 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 15.847 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 15.915 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 15.997 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 16.052 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 16.134 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 16.190 | 7912 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 18.095 | 7911 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 18.167 | 7911 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 18.212 | 7911 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 18.263 | 7911 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 18.289 | 7911 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 19.262 | 7911 | python3 | openat | `/etc/localtime` |
| 434 | 22.653 | 7911 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 22.766 | 7911 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 22.936 | 7911 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 23.716 | 7911 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 23.810 | 7911 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 23.885 | 7911 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 30.935 | 7911 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 67.019 | 7911 | python3 | openat | `/etc/gai.conf` |
| 798 | 67.194 | 7911 | python3 | sendto | `socket:[48115]` |
| 799 | 67.264 | 7911 | python3 | connect | `unix:/var/run/nscd/socket` |
| 802 | 67.358 | 7911 | python3 | connect | `ipv6:[...]` |
| 803 | 67.394 | 7911 | python3 | connect | `sockfd=3` |
| 804 | 67.418 | 7911 | python3 | connect | `0.0.0.0:8765` |
| 814 | 68.865 | 7911 | python3 | connect | `unix:/var/run/nscd/socket` |
| 816 | 68.950 | 7911 | python3 | openat | `/etc/nsswitch.conf` |
| 820 | 69.076 | 7911 | python3 | openat | `/etc/host.conf` |
| 824 | 69.171 | 7911 | python3 | openat | `/etc/resolv.conf` |
| 828 | 69.283 | 7911 | python3 | openat | `/etc/hosts` |
| 832 | 69.434 | 7911 | python3 | openat | `/etc/hosts` |
| 837 | 517.047 | 7912 | sleep | exit_group | `code=0` |
| 839 | 517.562 | 7907 | bash | clone | `` |
| 841 | 517.888 | 7917 | bash | execve | `/usr/bin/curl` |
| 937 | 524.407 | 7917 | curl | openat | `/etc/gnutls/config` |
| 955 | 525.499 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 957 | 525.547 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 961 | 525.668 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 963 | 525.711 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 965 | 525.771 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 967 | 525.817 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 969 | 525.873 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 971 | 525.919 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 973 | 525.976 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 975 | 526.021 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 977 | 526.087 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 526.155 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 981 | 526.252 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 983 | 526.303 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 985 | 526.355 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 987 | 526.418 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 989 | 526.462 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 991 | 526.521 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 993 | 526.564 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 995 | 526.629 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 997 | 526.674 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 999 | 526.731 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1001 | 526.776 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1003 | 526.833 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1005 | 526.878 | 7917 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1007 | 526.942 | 7917 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1008 | 526.967 | 7917 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1009 | 527.010 | 7917 | curl | connect | `unix:/var/run/nscd/socket` |
| 1011 | 527.074 | 7917 | curl | connect | `unix:/var/run/nscd/socket` |
| 1013 | 527.129 | 7917 | curl | openat | `/etc/nsswitch.conf` |
| 1017 | 527.251 | 7917 | curl | openat | `/etc/passwd` |
| 1020 | 527.330 | 7917 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1021 | 527.469 | 7917 | curl | connect | `127.0.0.1:8765` |
| 1022 | 527.582 | 7917 | curl | sendto | `socket:[48125]` |
| 1023 | 527.620 | 7911 | python3 | accept4 | `sockfd=3` |
| 1024 | 527.804 | 7911 | python3 | clone3 | `` |
| 1025 | 527.989 | 7918 | python3 | recvfrom | `socket:[49437]` |
| 1026 | 528.310 | 7918 | python3 | openat | `/etc/mime.types` |
| 1039 | 533.502 | 7918 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1041 | 533.671 | 7918 | python3 | sendto | `socket:[49437]` |
| 1042 | 533.770 | 7917 | curl | recvfrom | `socket:[48125]` |
| 1045 | 533.860 | 7918 | python3 | sendto | `socket:[49437]` |
| 1046 | 533.883 | 7917 | curl | recvfrom | `socket:[48125]` |
| 1048 | 533.910 | 7917 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1052 | 534.147 | 7917 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1053 | 534.173 | 7918 | python3 | exit | `code=0` |
| 1057 | 534.573 | 7917 | curl | exit_group | `code=0` |
| 1059 | 535.133 | 7907 | bash | clone | `` |
| 1061 | 535.342 | 7919 | bash | execve | `/usr/bin/chmod` |
| 1071 | 535.988 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1073 | 536.026 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1077 | 536.127 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1079 | 536.183 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1081 | 536.257 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1083 | 536.305 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1085 | 536.364 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1087 | 536.408 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1089 | 536.464 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1091 | 536.509 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1093 | 536.564 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1095 | 536.607 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1097 | 536.677 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1099 | 536.720 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1101 | 536.768 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1103 | 536.826 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1105 | 536.869 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1107 | 536.932 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1109 | 536.975 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1111 | 537.039 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1113 | 537.084 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1115 | 537.141 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1117 | 537.199 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1119 | 537.270 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1121 | 537.305 | 7919 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1123 | 537.360 | 7919 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1126 | 537.434 | 7919 | chmod | exit_group | `code=0` |
| 1128 | 537.578 | 7907 | bash | clone | `` |
| 1130 | 537.729 | 7920 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1136 | 538.299 | 7920 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1139 | 538.401 | 7920 | downloaded.sh | clone | `` |
| 1145 | 538.603 | 7921 | downloaded.sh | execve | `/usr/bin/date` |
| 1155 | 539.137 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1157 | 539.175 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1161 | 539.275 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1163 | 539.310 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1165 | 539.357 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1167 | 539.391 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1169 | 539.436 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1171 | 539.471 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1173 | 539.516 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1175 | 539.549 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1177 | 539.594 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1179 | 539.626 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1181 | 539.682 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1183 | 539.716 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1185 | 539.752 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1187 | 539.798 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1189 | 539.832 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1191 | 539.879 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1193 | 539.913 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1195 | 539.963 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1197 | 539.998 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1199 | 540.042 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1201 | 540.077 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1203 | 540.126 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1205 | 540.163 | 7921 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1207 | 540.220 | 7921 | date | openat | `/etc/localtime` |
| 1216 | 540.395 | 7921 | date | exit_group | `code=0` |
| 1218 | 540.526 | 7920 | downloaded.sh | vfork | `` |
| 1219 | 540.573 | 7922 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1229 | 541.025 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1231 | 541.061 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1235 | 541.155 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1237 | 541.253 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1239 | 541.314 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1241 | 541.350 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1243 | 541.396 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1245 | 541.429 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1247 | 541.475 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1249 | 541.508 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1251 | 541.552 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1253 | 541.586 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1255 | 541.640 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1257 | 541.675 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1259 | 541.710 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1261 | 541.754 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1263 | 541.789 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1265 | 541.834 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1267 | 541.869 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1269 | 541.918 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1271 | 541.952 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1273 | 541.996 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1275 | 542.029 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1277 | 542.076 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1279 | 542.110 | 7922 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1296 | 742.746 | 7922 | sleep | exit_group | `code=0` |
| 1298 | 743.098 | 7920 | downloaded.sh | exit_group | `code=0` |
| 1307 | 745.706 | 7907 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 31.357 ms |
| Workload CPU (user+sys) | 74.342 ms |
| Tracer peak memory | 18004 KiB |
| Processing time (normalise+correlate+reconstruct) | 4.041 ms |
| Evidence size | 486532 bytes |

