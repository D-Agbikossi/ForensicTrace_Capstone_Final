# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | C |
| Events recorded | 1307 |
| Failed exec attempts removed | 12 |
| Duration | 750.719 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_C_r3.json` (486532 bytes) |
| SHA-256 | `1c44580ee95887c3848e458a01ef842cba0456efd1ba0f83552a8ac6b25fec2c` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_C_r3.json.sha256`

## 1. Process tree

- `8329` /usr/bin/bash
  - `8330` /usr/bin/rm
  - `8331` /usr/bin/mkdir
  - `8332` /usr/bin/cat
  - `8333` /usr/bin/python3
  - `8334` /usr/bin/sleep
  - `8335` /usr/bin/curl
  - `8336` /usr/bin/python3
  - `8337` /usr/bin/chmod
  - `8338` /tmp/ft_scenario01/downloaded.sh
    - `8339` /usr/bin/date
    - `8340` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8329 (?) executed `/usr/bin/bash`
- +5.398 ms pid 8330 (bash) executed `/usr/bin/rm`
- +11.152 ms pid 8331 (bash) executed `/usr/bin/mkdir`
- +15.089 ms pid 8332 (bash) executed `/usr/bin/cat`
- +18.033 ms pid 8334 (bash) executed `/usr/bin/sleep`
- +18.068 ms pid 8333 (bash) executed `/usr/bin/python3`
- +521.636 ms pid 8335 (bash) executed `/usr/bin/curl`
- +536.852 ms pid 8337 (bash) executed `/usr/bin/chmod`
- +539.034 ms pid 8338 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +539.788 ms pid 8339 (downloaded.sh) executed `/usr/bin/date`
- +542.345 ms pid 8340 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +67.544 ms pid 8333 (python3) connected to `unix:/var/run/nscd/socket`
- +67.618 ms pid 8333 (python3) connected to `ipv6:[...]`
- +67.653 ms pid 8333 (python3) connected to `sockfd=3`
- +67.677 ms pid 8333 (python3) connected to `0.0.0.0:8765`
- +69.403 ms pid 8333 (python3) connected to `unix:/var/run/nscd/socket`
- +531.784 ms pid 8335 (curl) connected to `unix:/var/run/nscd/socket`
- +531.838 ms pid 8335 (curl) connected to `unix:/var/run/nscd/socket`
- +532.234 ms pid 8335 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +14.932 ms by pid 8332 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +535.458 ms by pid 8335 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +538.680 ms pid 8337 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +10.070 ms pid 8330 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +10.163 ms pid 8330 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +10.261 ms pid 8330 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +531.991 ms pid 8335 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +539.034 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8338 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +10.163 ms #138 `unlinkat` by pid 8330 (rm)
    - +535.458 ms #1048 `openat` by pid 8335 (curl)
    - +535.616 ms #1053 `write` by pid 8335 (curl)
    - +535.659 ms #1054 `close` by pid 8335 (curl)
    - +538.680 ms #1123 `fchmodat` by pid 8337 (chmod)
    - +539.034 ms #1130 `execve` by pid 8338 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8329 | ? | execve | `/usr/bin/bash` |
| 15 | 1.740 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.831 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 2.048 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 2.131 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 2.242 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 2.325 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.435 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.516 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.625 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.704 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.830 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 2.914 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 3.047 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 3.124 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 3.204 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 3.309 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 3.389 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 3.489 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 3.567 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 3.681 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.773 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 3.876 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 3.951 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 4.059 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 4.133 | 8329 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 4.690 | 8329 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 5.070 | 8329 | bash | clone | `` |
| 73 | 5.398 | 8330 | bash | execve | `/usr/bin/rm` |
| 83 | 6.682 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 6.788 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 7.034 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 7.128 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 7.253 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 7.349 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 7.474 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 7.745 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 7.922 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 8.091 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 8.322 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 8.455 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 8.618 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 8.717 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 8.846 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 8.960 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 9.033 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 9.128 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 9.201 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 9.324 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 9.411 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 9.544 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 9.628 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 9.776 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 9.854 | 8330 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 9.961 | 8330 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 10.070 | 8330 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 10.163 | 8330 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 10.261 | 8330 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 10.475 | 8330 | rm | exit_group | `code=0` |
| 145 | 10.816 | 8329 | bash | clone | `` |
| 147 | 11.152 | 8331 | bash | execve | `/usr/bin/mkdir` |
| 167 | 12.558 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 12.612 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 12.750 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 12.800 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 12.866 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 12.915 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 12.977 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 13.027 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 13.087 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 13.136 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 13.199 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 13.245 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 13.318 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 13.365 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 13.417 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 13.479 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 13.525 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 13.588 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 13.635 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 13.706 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 13.763 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 13.837 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 13.983 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 14.096 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 14.155 | 8331 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 14.409 | 8331 | mkdir | exit_group | `code=0` |
| 223 | 14.704 | 8329 | bash | clone | `` |
| 225 | 14.932 | 8332 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 15.089 | 8332 | bash | execve | `/usr/bin/cat` |
| 240 | 15.779 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 15.825 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 15.961 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 15.999 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 16.068 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 16.125 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 16.393 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 16.477 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 16.565 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 16.617 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 16.672 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 16.706 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 16.774 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 16.809 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 16.847 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 16.894 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 16.928 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 16.978 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 17.011 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 17.066 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 17.115 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 17.169 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 17.215 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 17.262 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 17.297 | 8332 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 17.378 | 8332 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 17.500 | 8332 | cat | exit_group | `code=0` |
| 300 | 17.654 | 8329 | bash | clone | `` |
| 303 | 17.865 | 8329 | bash | clone | `` |
| 308 | 18.033 | 8334 | bash | execve | `/usr/bin/sleep` |
| 310 | 18.068 | 8333 | bash | execve | `/usr/bin/python3` |
| 330 | 18.722 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 332 | 18.781 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 339 | 18.904 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 19.034 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 19.104 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 19.156 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 19.215 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 351 | 19.268 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 355 | 19.337 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 358 | 19.385 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 359 | 19.398 | 8333 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 362 | 19.439 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 363 | 19.456 | 8333 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 365 | 19.489 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 369 | 19.549 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 372 | 19.595 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 374 | 19.637 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 19.697 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 19.754 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 19.813 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 19.864 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 19.931 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 19.981 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 20.043 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 20.090 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 20.152 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 20.201 | 8334 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 22.211 | 8333 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 22.268 | 8333 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 22.312 | 8333 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 22.343 | 8333 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 22.370 | 8333 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 23.149 | 8333 | python3 | openat | `/etc/localtime` |
| 434 | 26.383 | 8333 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 26.472 | 8333 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 26.611 | 8333 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 27.324 | 8333 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 27.399 | 8333 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 27.458 | 8333 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 33.637 | 8333 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 67.390 | 8333 | python3 | openat | `/etc/gai.conf` |
| 798 | 67.501 | 8333 | python3 | sendto | `socket:[52434]` |
| 799 | 67.544 | 8333 | python3 | connect | `unix:/var/run/nscd/socket` |
| 802 | 67.618 | 8333 | python3 | connect | `ipv6:[...]` |
| 803 | 67.653 | 8333 | python3 | connect | `sockfd=3` |
| 804 | 67.677 | 8333 | python3 | connect | `0.0.0.0:8765` |
| 814 | 69.403 | 8333 | python3 | connect | `unix:/var/run/nscd/socket` |
| 816 | 69.493 | 8333 | python3 | openat | `/etc/nsswitch.conf` |
| 820 | 69.612 | 8333 | python3 | openat | `/etc/host.conf` |
| 824 | 69.709 | 8333 | python3 | openat | `/etc/resolv.conf` |
| 828 | 69.819 | 8333 | python3 | openat | `/etc/hosts` |
| 832 | 69.923 | 8333 | python3 | openat | `/etc/hosts` |
| 837 | 521.004 | 8334 | sleep | exit_group | `code=0` |
| 839 | 521.391 | 8329 | bash | clone | `` |
| 841 | 521.636 | 8335 | bash | execve | `/usr/bin/curl` |
| 937 | 529.312 | 8335 | curl | openat | `/etc/gnutls/config` |
| 955 | 530.333 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 957 | 530.375 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 961 | 530.489 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 963 | 530.525 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 965 | 530.584 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 967 | 530.625 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 969 | 530.681 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 971 | 530.723 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 973 | 530.787 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 975 | 530.831 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 977 | 530.888 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 530.932 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 981 | 531.160 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 983 | 531.197 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 985 | 531.237 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 987 | 531.293 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 989 | 531.327 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 991 | 531.379 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 993 | 531.412 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 995 | 531.466 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 997 | 531.500 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 999 | 531.546 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1001 | 531.581 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1003 | 531.627 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1005 | 531.662 | 8335 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1007 | 531.717 | 8335 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1008 | 531.745 | 8335 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1009 | 531.784 | 8335 | curl | connect | `unix:/var/run/nscd/socket` |
| 1011 | 531.838 | 8335 | curl | connect | `unix:/var/run/nscd/socket` |
| 1013 | 531.882 | 8335 | curl | openat | `/etc/nsswitch.conf` |
| 1017 | 531.991 | 8335 | curl | openat | `/etc/passwd` |
| 1020 | 532.078 | 8335 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1021 | 532.234 | 8335 | curl | connect | `127.0.0.1:8765` |
| 1022 | 532.346 | 8335 | curl | sendto | `socket:[52444]` |
| 1023 | 532.383 | 8333 | python3 | accept4 | `sockfd=3` |
| 1024 | 532.532 | 8333 | python3 | clone3 | `` |
| 1025 | 532.706 | 8336 | python3 | recvfrom | `socket:[51026]` |
| 1026 | 532.975 | 8336 | python3 | openat | `/etc/mime.types` |
| 1039 | 535.136 | 8336 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1041 | 535.283 | 8336 | python3 | sendto | `socket:[51026]` |
| 1043 | 535.355 | 8335 | curl | recvfrom | `socket:[52444]` |
| 1045 | 535.401 | 8336 | python3 | sendto | `socket:[51026]` |
| 1046 | 535.427 | 8335 | curl | recvfrom | `socket:[52444]` |
| 1048 | 535.458 | 8335 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1052 | 535.591 | 8336 | python3 | exit | `code=0` |
| 1053 | 535.616 | 8335 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1057 | 536.037 | 8335 | curl | exit_group | `code=0` |
| 1059 | 536.644 | 8329 | bash | clone | `` |
| 1061 | 536.852 | 8337 | bash | execve | `/usr/bin/chmod` |
| 1071 | 537.548 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1073 | 537.592 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1077 | 537.698 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1079 | 537.744 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1081 | 537.812 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1083 | 537.850 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1085 | 537.895 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1087 | 537.929 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1089 | 537.974 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1091 | 538.008 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1093 | 538.057 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1095 | 538.090 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1097 | 538.146 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1099 | 538.179 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1101 | 538.216 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1103 | 538.262 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1105 | 538.295 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1107 | 538.346 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1109 | 538.380 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1111 | 538.433 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1113 | 538.468 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1115 | 538.513 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1117 | 538.547 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1119 | 538.593 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1121 | 538.627 | 8337 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1123 | 538.680 | 8337 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1126 | 538.755 | 8337 | chmod | exit_group | `code=0` |
| 1128 | 538.882 | 8329 | bash | clone | `` |
| 1130 | 539.034 | 8338 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1136 | 539.514 | 8338 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1139 | 539.588 | 8338 | downloaded.sh | clone | `` |
| 1145 | 539.788 | 8339 | downloaded.sh | execve | `/usr/bin/date` |
| 1155 | 540.307 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1157 | 540.344 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1161 | 540.434 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1163 | 540.468 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1165 | 540.513 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1167 | 540.547 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1169 | 540.593 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1171 | 540.627 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1173 | 540.673 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1175 | 540.706 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1177 | 540.762 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1179 | 540.856 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1181 | 540.926 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1183 | 540.961 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1185 | 540.997 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1187 | 541.066 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1189 | 541.114 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1191 | 541.476 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1193 | 541.539 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1195 | 541.609 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1197 | 541.655 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1199 | 541.711 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1201 | 541.763 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1203 | 541.822 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1205 | 541.866 | 8339 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1207 | 541.935 | 8339 | date | openat | `/etc/localtime` |
| 1216 | 542.141 | 8339 | date | exit_group | `code=0` |
| 1218 | 542.295 | 8338 | downloaded.sh | vfork | `` |
| 1219 | 542.345 | 8340 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1229 | 542.880 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1231 | 542.916 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1235 | 543.003 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1237 | 543.038 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1239 | 543.083 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1241 | 543.118 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1243 | 543.163 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1245 | 543.196 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1247 | 543.240 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1249 | 543.273 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1251 | 543.317 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1253 | 543.355 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1255 | 543.408 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1257 | 543.443 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1259 | 543.478 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1261 | 543.522 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1263 | 543.556 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1265 | 543.601 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1267 | 543.635 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1269 | 543.687 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1271 | 543.720 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1273 | 543.770 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1275 | 543.803 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1277 | 543.850 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1279 | 543.884 | 8340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1296 | 744.880 | 8340 | sleep | exit_group | `code=0` |
| 1298 | 745.618 | 8338 | downloaded.sh | exit_group | `code=0` |
| 1307 | 749.192 | 8329 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 33.782 ms |
| Workload CPU (user+sys) | 72.403 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 5.472 ms |
| Evidence size | 486532 bytes |

