# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | C |
| Events recorded | 1307 |
| Failed exec attempts removed | 12 |
| Duration | 739.185 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_C_r4.json` (486529 bytes) |
| SHA-256 | `396038470bf4447a8be049b2c05f2c854961bd0296814dd977e770b4cf8703bd` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_C_r4.json.sha256`

## 1. Process tree

- `8556` /usr/bin/bash
  - `8557` /usr/bin/rm
  - `8558` /usr/bin/mkdir
  - `8559` /usr/bin/cat
  - `8560` /usr/bin/python3
  - `8561` /usr/bin/sleep
  - `8562` /usr/bin/curl
  - `8563` /usr/bin/python3
  - `8564` /usr/bin/chmod
  - `8565` /tmp/ft_scenario01/downloaded.sh
    - `8566` /usr/bin/date
    - `8567` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8556 (?) executed `/usr/bin/bash`
- +2.860 ms pid 8557 (bash) executed `/usr/bin/rm`
- +5.078 ms pid 8558 (bash) executed `/usr/bin/mkdir`
- +7.519 ms pid 8559 (bash) executed `/usr/bin/cat`
- +10.038 ms pid 8561 (bash) executed `/usr/bin/sleep`
- +10.088 ms pid 8560 (bash) executed `/usr/bin/python3`
- +513.585 ms pid 8562 (bash) executed `/usr/bin/curl`
- +528.757 ms pid 8564 (bash) executed `/usr/bin/chmod`
- +531.415 ms pid 8565 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +532.253 ms pid 8566 (downloaded.sh) executed `/usr/bin/date`
- +534.700 ms pid 8567 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +62.653 ms pid 8560 (python3) connected to `unix:/var/run/nscd/socket`
- +62.741 ms pid 8560 (python3) connected to `ipv6:[...]`
- +62.774 ms pid 8560 (python3) connected to `sockfd=3`
- +62.798 ms pid 8560 (python3) connected to `0.0.0.0:8765`
- +64.047 ms pid 8560 (python3) connected to `unix:/var/run/nscd/socket`
- +522.551 ms pid 8562 (curl) connected to `unix:/var/run/nscd/socket`
- +522.644 ms pid 8562 (curl) connected to `unix:/var/run/nscd/socket`
- +523.094 ms pid 8562 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +7.339 ms by pid 8559 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +526.934 ms by pid 8562 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +531.008 ms pid 8564 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +4.608 ms pid 8557 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +4.652 ms pid 8557 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +4.696 ms pid 8557 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +522.829 ms pid 8562 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +531.415 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8565 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +4.652 ms #138 `unlinkat` by pid 8557 (rm)
    - +526.934 ms #1048 `openat` by pid 8562 (curl)
    - +527.119 ms #1052 `write` by pid 8562 (curl)
    - +527.191 ms #1054 `close` by pid 8562 (curl)
    - +531.008 ms #1123 `fchmodat` by pid 8564 (chmod)
    - +531.415 ms #1130 `execve` by pid 8565 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8556 | ? | execve | `/usr/bin/bash` |
| 15 | 0.967 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.009 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.124 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.167 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.221 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.264 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.327 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.360 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.407 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.449 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.527 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.569 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.630 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.672 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.711 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.762 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.803 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 1.856 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 1.893 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 1.962 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 1.997 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 2.049 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.096 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.152 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.186 | 8556 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.492 | 8556 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 2.674 | 8556 | bash | clone | `` |
| 73 | 2.860 | 8557 | bash | execve | `/usr/bin/rm` |
| 83 | 3.456 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.505 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 3.598 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 3.631 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 3.681 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 3.716 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 3.761 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 3.796 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 3.840 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 3.875 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 3.917 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 3.953 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 4.008 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 4.042 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 4.082 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 4.128 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 4.163 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 4.216 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 4.250 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 4.301 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 4.335 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 4.380 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 4.414 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 4.464 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 4.499 | 8557 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 4.552 | 8557 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 4.608 | 8557 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 4.652 | 8557 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 4.696 | 8557 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 4.807 | 8557 | rm | exit_group | `code=0` |
| 145 | 4.932 | 8556 | bash | clone | `` |
| 147 | 5.078 | 8558 | bash | execve | `/usr/bin/mkdir` |
| 167 | 5.865 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 5.901 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 5.989 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 6.022 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 6.068 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 6.103 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 6.147 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 6.183 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 6.226 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 6.260 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 6.306 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 6.339 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 6.392 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 6.426 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 6.472 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 6.519 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 6.552 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 6.598 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 6.631 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 6.682 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 6.717 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 6.761 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 6.795 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 6.843 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 6.880 | 8558 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 7.009 | 8558 | mkdir | exit_group | `code=0` |
| 223 | 7.170 | 8556 | bash | clone | `` |
| 225 | 7.339 | 8559 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 7.519 | 8559 | bash | execve | `/usr/bin/cat` |
| 240 | 8.024 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 8.070 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 8.178 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 8.225 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 8.288 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 8.339 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 8.409 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 8.479 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 8.533 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 8.574 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 8.624 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 8.665 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 8.731 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 8.775 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 8.817 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 8.867 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 8.905 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 8.961 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 8.999 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 9.054 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 9.093 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 9.140 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 9.182 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 9.232 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 9.270 | 8559 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 9.376 | 8559 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 9.553 | 8559 | cat | exit_group | `code=0` |
| 300 | 9.700 | 8556 | bash | clone | `` |
| 303 | 9.877 | 8556 | bash | clone | `` |
| 308 | 10.038 | 8561 | bash | execve | `/usr/bin/sleep` |
| 310 | 10.088 | 8560 | bash | execve | `/usr/bin/python3` |
| 329 | 10.661 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 332 | 10.705 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 339 | 10.812 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 10.857 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 10.914 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 10.954 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 11.009 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 11.049 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 354 | 11.104 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 357 | 11.145 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 360 | 11.197 | 8560 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 361 | 11.205 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 364 | 11.242 | 8560 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 365 | 11.252 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 369 | 11.319 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 372 | 11.359 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 374 | 11.400 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 11.461 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 11.609 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 11.667 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 11.707 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 11.769 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 11.809 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 11.865 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 11.904 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 11.964 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 12.003 | 8561 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 13.912 | 8560 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 13.948 | 8560 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 13.982 | 8560 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 14.004 | 8560 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 14.024 | 8560 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 14.920 | 8560 | python3 | openat | `/etc/localtime` |
| 434 | 18.122 | 8560 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 18.214 | 8560 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 18.347 | 8560 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 19.046 | 8560 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 19.121 | 8560 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 19.180 | 8560 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 25.354 | 8560 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 62.472 | 8560 | python3 | openat | `/etc/gai.conf` |
| 798 | 62.604 | 8560 | python3 | sendto | `socket:[53414]` |
| 799 | 62.653 | 8560 | python3 | connect | `unix:/var/run/nscd/socket` |
| 802 | 62.741 | 8560 | python3 | connect | `ipv6:[...]` |
| 803 | 62.774 | 8560 | python3 | connect | `sockfd=3` |
| 804 | 62.798 | 8560 | python3 | connect | `0.0.0.0:8765` |
| 814 | 64.047 | 8560 | python3 | connect | `unix:/var/run/nscd/socket` |
| 816 | 64.118 | 8560 | python3 | openat | `/etc/nsswitch.conf` |
| 820 | 64.286 | 8560 | python3 | openat | `/etc/host.conf` |
| 824 | 64.384 | 8560 | python3 | openat | `/etc/resolv.conf` |
| 828 | 64.489 | 8560 | python3 | openat | `/etc/hosts` |
| 832 | 64.594 | 8560 | python3 | openat | `/etc/hosts` |
| 837 | 512.839 | 8561 | sleep | exit_group | `code=0` |
| 839 | 513.382 | 8556 | bash | clone | `` |
| 841 | 513.585 | 8562 | bash | execve | `/usr/bin/curl` |
| 937 | 518.208 | 8562 | curl | openat | `/etc/gnutls/config` |
| 955 | 520.096 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 957 | 520.177 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 961 | 520.541 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 963 | 520.613 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 965 | 520.732 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 967 | 520.804 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 969 | 520.902 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 971 | 520.976 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 973 | 521.068 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 975 | 521.136 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 977 | 521.231 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 521.300 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 981 | 521.424 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 983 | 521.518 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 985 | 521.600 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 987 | 521.700 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 989 | 521.752 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 991 | 521.829 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 993 | 521.881 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 995 | 521.974 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 997 | 522.031 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 999 | 522.130 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1001 | 522.195 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1003 | 522.271 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1005 | 522.348 | 8562 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1007 | 522.439 | 8562 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1008 | 522.494 | 8562 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1009 | 522.551 | 8562 | curl | connect | `unix:/var/run/nscd/socket` |
| 1011 | 522.644 | 8562 | curl | connect | `unix:/var/run/nscd/socket` |
| 1013 | 522.719 | 8562 | curl | openat | `/etc/nsswitch.conf` |
| 1017 | 522.829 | 8562 | curl | openat | `/etc/passwd` |
| 1020 | 522.905 | 8562 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1021 | 523.094 | 8562 | curl | connect | `127.0.0.1:8765` |
| 1022 | 523.331 | 8560 | python3 | accept4 | `sockfd=3` |
| 1023 | 523.476 | 8562 | curl | sendto | `socket:[52761]` |
| 1024 | 523.535 | 8560 | python3 | clone3 | `` |
| 1025 | 523.690 | 8563 | python3 | recvfrom | `socket:[54404]` |
| 1026 | 523.952 | 8563 | python3 | openat | `/etc/mime.types` |
| 1039 | 526.438 | 8563 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1041 | 526.676 | 8563 | python3 | sendto | `socket:[54404]` |
| 1042 | 526.762 | 8562 | curl | recvfrom | `socket:[52761]` |
| 1045 | 526.861 | 8563 | python3 | sendto | `socket:[54404]` |
| 1046 | 526.894 | 8562 | curl | recvfrom | `socket:[52761]` |
| 1048 | 526.934 | 8562 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1052 | 527.119 | 8562 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1053 | 527.172 | 8563 | python3 | exit | `code=0` |
| 1057 | 527.598 | 8562 | curl | exit_group | `code=0` |
| 1059 | 528.520 | 8556 | bash | clone | `` |
| 1061 | 528.757 | 8564 | bash | execve | `/usr/bin/chmod` |
| 1071 | 529.543 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1073 | 529.589 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1077 | 529.705 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1079 | 529.744 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1081 | 529.803 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1083 | 529.843 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1085 | 529.896 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1087 | 529.933 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1089 | 529.991 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1091 | 530.036 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1093 | 530.123 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1095 | 530.194 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1097 | 530.298 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1099 | 530.343 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1101 | 530.391 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1103 | 530.451 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1105 | 530.502 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1107 | 530.562 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1109 | 530.605 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1111 | 530.678 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1113 | 530.718 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1115 | 530.766 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1117 | 530.817 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1119 | 530.898 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1121 | 530.942 | 8564 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1123 | 531.008 | 8564 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1126 | 531.085 | 8564 | chmod | exit_group | `code=0` |
| 1128 | 531.254 | 8556 | bash | clone | `` |
| 1130 | 531.415 | 8565 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1136 | 531.974 | 8565 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1139 | 532.050 | 8565 | downloaded.sh | clone | `` |
| 1145 | 532.253 | 8566 | downloaded.sh | execve | `/usr/bin/date` |
| 1155 | 532.884 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1157 | 532.933 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1161 | 533.028 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1163 | 533.077 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1165 | 533.130 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1167 | 533.173 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1169 | 533.232 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1171 | 533.273 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1173 | 533.328 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1175 | 533.367 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1177 | 533.419 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1179 | 533.488 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1181 | 533.545 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1183 | 533.580 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1185 | 533.648 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1187 | 533.703 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1189 | 533.750 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1191 | 533.804 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1193 | 533.847 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1195 | 533.914 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1197 | 533.961 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1199 | 534.074 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1201 | 534.136 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1203 | 534.202 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1205 | 534.243 | 8566 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1207 | 534.309 | 8566 | date | openat | `/etc/localtime` |
| 1216 | 534.511 | 8566 | date | exit_group | `code=0` |
| 1218 | 534.660 | 8565 | downloaded.sh | vfork | `` |
| 1219 | 534.700 | 8567 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1229 | 535.195 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1231 | 535.231 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1235 | 535.319 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1237 | 535.354 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1239 | 535.399 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1241 | 535.434 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1243 | 535.488 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1245 | 535.522 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1247 | 535.568 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1249 | 535.601 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1251 | 535.645 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1253 | 535.680 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1255 | 535.745 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1257 | 535.805 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1259 | 535.848 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1261 | 535.923 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1263 | 535.963 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1265 | 536.020 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1267 | 536.063 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1269 | 536.124 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1271 | 536.162 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1273 | 536.213 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1275 | 536.247 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1277 | 536.294 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1279 | 536.327 | 8567 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1296 | 736.850 | 8567 | sleep | exit_group | `code=0` |
| 1298 | 737.041 | 8565 | downloaded.sh | exit_group | `code=0` |
| 1307 | 738.560 | 8556 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 24.473 ms |
| Workload CPU (user+sys) | 69.359 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.652 ms |
| Evidence size | 486529 bytes |

