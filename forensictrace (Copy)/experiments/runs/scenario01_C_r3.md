# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | C |
| Events recorded | 1306 |
| Failed exec attempts removed | 12 |
| Duration | 790.844 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_C_r3.json` (486193 bytes) |
| SHA-256 | `b6848a3606d34e0b3a037bc644a354a469674b62517b259245967e6fe64a9f7a` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_C_r3.json.sha256`

## 1. Process tree

- `7532` /usr/bin/bash
  - `7533` /usr/bin/rm
  - `7534` /usr/bin/mkdir
  - `7535` /usr/bin/cat
  - `7536` /usr/bin/python3
  - `7537` /usr/bin/sleep
  - `7538` /usr/bin/curl
  - `7539` /usr/bin/python3
  - `7540` /usr/bin/chmod
  - `7541` /tmp/ft_scenario01/downloaded.sh
    - `7542` /usr/bin/date
    - `7543` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7532 (?) executed `/usr/bin/bash`
- +9.637 ms pid 7533 (bash) executed `/usr/bin/rm`
- +13.964 ms pid 7534 (bash) executed `/usr/bin/mkdir`
- +19.345 ms pid 7535 (bash) executed `/usr/bin/cat`
- +24.563 ms pid 7536 (bash) executed `/usr/bin/python3`
- +24.572 ms pid 7537 (bash) executed `/usr/bin/sleep`
- +532.366 ms pid 7538 (bash) executed `/usr/bin/curl`
- +567.118 ms pid 7540 (bash) executed `/usr/bin/chmod`
- +572.035 ms pid 7541 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +574.055 ms pid 7542 (downloaded.sh) executed `/usr/bin/date`
- +578.483 ms pid 7543 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +96.115 ms pid 7536 (python3) connected to `unix:/var/run/nscd/socket`
- +96.200 ms pid 7536 (python3) connected to `ipv6:[...]`
- +96.243 ms pid 7536 (python3) connected to `sockfd=3`
- +96.261 ms pid 7536 (python3) connected to `0.0.0.0:8765`
- +97.968 ms pid 7536 (python3) connected to `unix:/var/run/nscd/socket`
- +556.082 ms pid 7538 (curl) connected to `unix:/var/run/nscd/socket`
- +556.310 ms pid 7538 (curl) connected to `unix:/var/run/nscd/socket`
- +560.424 ms pid 7538 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +19.061 ms by pid 7535 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +564.823 ms by pid 7538 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +571.055 ms pid 7540 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +12.512 ms pid 7533 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +12.574 ms pid 7533 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +12.641 ms pid 7533 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +559.104 ms pid 7538 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +572.035 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7541 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +12.574 ms #138 `unlinkat` by pid 7533 (rm)
    - +564.823 ms #1048 `openat` by pid 7538 (curl)
    - +565.005 ms #1051 `write` by pid 7538 (curl)
    - +565.044 ms #1053 `close` by pid 7538 (curl)
    - +571.055 ms #1122 `fchmodat` by pid 7540 (chmod)
    - +572.035 ms #1129 `execve` by pid 7541 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7532 | ? | execve | `/usr/bin/bash` |
| 15 | 3.316 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 3.365 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 3.587 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 3.632 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 3.731 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 3.776 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 3.874 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 3.916 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 4.066 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 4.108 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 4.203 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 4.317 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 4.490 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 4.561 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 4.673 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 4.804 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 4.858 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 4.979 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 5.036 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 5.379 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 5.505 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 5.653 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 5.718 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 5.992 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 6.048 | 7532 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 8.428 | 7532 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 9.234 | 7532 | bash | clone | `` |
| 73 | 9.637 | 7533 | bash | execve | `/usr/bin/rm` |
| 83 | 10.705 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 10.742 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 10.906 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 10.940 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 11.017 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 11.051 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 11.126 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 11.161 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 11.234 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 11.269 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 11.344 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 11.378 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 11.478 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 11.514 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 11.565 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 11.643 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 11.679 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 11.755 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 11.789 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 11.873 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 11.906 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 11.981 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 12.015 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 12.089 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 12.130 | 7533 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 12.300 | 7533 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 12.512 | 7533 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 12.574 | 7533 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 12.641 | 7533 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 12.877 | 7533 | rm | exit_group | `code=0` |
| 145 | 13.591 | 7532 | bash | clone | `` |
| 147 | 13.964 | 7534 | bash | execve | `/usr/bin/mkdir` |
| 167 | 15.802 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 15.841 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 16.008 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 16.042 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 16.121 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 16.157 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 16.232 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 16.269 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 16.345 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 16.380 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 16.459 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 16.492 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 16.575 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 16.608 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 16.660 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 16.735 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 16.768 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 16.842 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 16.876 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 16.955 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 16.989 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 17.062 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 17.097 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 17.171 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 17.206 | 7534 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 17.447 | 7534 | mkdir | exit_group | `code=0` |
| 223 | 18.543 | 7532 | bash | clone | `` |
| 225 | 19.061 | 7535 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 19.345 | 7535 | bash | execve | `/usr/bin/cat` |
| 240 | 20.748 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 20.793 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 20.996 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 21.035 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 21.131 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 21.171 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 21.263 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 21.304 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 21.396 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 21.437 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 21.544 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 21.584 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 21.691 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 21.742 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 21.817 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 21.918 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 21.965 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 22.073 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 22.110 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 22.211 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 22.258 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 22.351 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 22.399 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 22.491 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 22.526 | 7535 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 22.693 | 7535 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 22.829 | 7535 | cat | exit_group | `code=0` |
| 300 | 23.118 | 7532 | bash | clone | `` |
| 303 | 24.178 | 7532 | bash | clone | `` |
| 309 | 24.563 | 7536 | bash | execve | `/usr/bin/python3` |
| 310 | 24.572 | 7537 | bash | execve | `/usr/bin/sleep` |
| 333 | 25.808 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 335 | 25.851 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 340 | 26.041 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 26.083 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 26.184 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 26.225 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 26.313 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 26.352 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 352 | 26.439 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 354 | 26.488 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 357 | 26.583 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 360 | 26.624 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 364 | 26.695 | 7536 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 366 | 26.733 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 367 | 26.741 | 7536 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 369 | 26.777 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 372 | 26.838 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 26.926 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 26.967 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 27.081 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 27.133 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 27.256 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 27.312 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 27.425 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 27.498 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 27.603 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 27.642 | 7537 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 30.206 | 7536 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 30.239 | 7536 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 30.308 | 7536 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 30.331 | 7536 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 30.351 | 7536 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 31.376 | 7536 | python3 | openat | `/etc/localtime` |
| 434 | 36.919 | 7536 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 37.135 | 7536 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 37.372 | 7536 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 38.484 | 7536 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 38.652 | 7536 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 38.806 | 7536 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 47.750 | 7536 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 95.839 | 7536 | python3 | openat | `/etc/gai.conf` |
| 798 | 96.026 | 7536 | python3 | sendto | `socket:[45707]` |
| 799 | 96.115 | 7536 | python3 | connect | `unix:/var/run/nscd/socket` |
| 802 | 96.200 | 7536 | python3 | connect | `ipv6:[...]` |
| 803 | 96.243 | 7536 | python3 | connect | `sockfd=3` |
| 804 | 96.261 | 7536 | python3 | connect | `0.0.0.0:8765` |
| 814 | 97.968 | 7536 | python3 | connect | `unix:/var/run/nscd/socket` |
| 816 | 98.047 | 7536 | python3 | openat | `/etc/nsswitch.conf` |
| 820 | 98.176 | 7536 | python3 | openat | `/etc/host.conf` |
| 824 | 98.277 | 7536 | python3 | openat | `/etc/resolv.conf` |
| 828 | 98.384 | 7536 | python3 | openat | `/etc/hosts` |
| 832 | 98.526 | 7536 | python3 | openat | `/etc/hosts` |
| 837 | 528.536 | 7537 | sleep | exit_group | `code=0` |
| 839 | 531.329 | 7532 | bash | clone | `` |
| 841 | 532.366 | 7538 | bash | execve | `/usr/bin/curl` |
| 937 | 548.889 | 7538 | curl | openat | `/etc/gnutls/config` |
| 955 | 550.728 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 957 | 550.894 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 961 | 551.133 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 963 | 551.171 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 965 | 551.266 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 967 | 551.306 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 969 | 551.403 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 971 | 551.487 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 973 | 551.610 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 975 | 551.664 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 977 | 551.832 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 551.893 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 981 | 553.747 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 983 | 553.837 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 985 | 554.196 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 987 | 554.567 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 989 | 554.682 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 991 | 554.885 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 993 | 555.013 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 995 | 555.256 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 997 | 555.335 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 999 | 555.475 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1001 | 555.524 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1003 | 555.742 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1005 | 555.800 | 7538 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1007 | 555.953 | 7538 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1008 | 555.985 | 7538 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1009 | 556.082 | 7538 | curl | connect | `unix:/var/run/nscd/socket` |
| 1011 | 556.310 | 7538 | curl | connect | `unix:/var/run/nscd/socket` |
| 1013 | 558.794 | 7538 | curl | openat | `/etc/nsswitch.conf` |
| 1017 | 559.104 | 7538 | curl | openat | `/etc/passwd` |
| 1020 | 559.276 | 7538 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1021 | 560.424 | 7538 | curl | connect | `127.0.0.1:8765` |
| 1022 | 560.634 | 7536 | python3 | accept4 | `sockfd=3` |
| 1023 | 561.015 | 7538 | curl | sendto | `socket:[47420]` |
| 1024 | 561.076 | 7536 | python3 | clone3 | `` |
| 1025 | 561.482 | 7539 | python3 | recvfrom | `socket:[47421]` |
| 1026 | 561.999 | 7539 | python3 | openat | `/etc/mime.types` |
| 1039 | 564.404 | 7539 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1041 | 564.603 | 7539 | python3 | sendto | `socket:[47421]` |
| 1044 | 564.737 | 7539 | python3 | sendto | `socket:[47421]` |
| 1045 | 564.776 | 7538 | curl | recvfrom | `socket:[47420]` |
| 1048 | 564.823 | 7538 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1051 | 565.005 | 7538 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1052 | 565.021 | 7539 | python3 | exit | `code=0` |
| 1056 | 565.480 | 7538 | curl | exit_group | `code=0` |
| 1058 | 566.715 | 7532 | bash | clone | `` |
| 1060 | 567.118 | 7540 | bash | execve | `/usr/bin/chmod` |
| 1070 | 568.624 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1072 | 568.678 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1076 | 568.910 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1078 | 568.959 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1080 | 569.062 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1082 | 569.117 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1084 | 569.303 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1086 | 569.343 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1088 | 569.470 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1090 | 569.525 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1092 | 569.669 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1094 | 569.721 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1096 | 569.841 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1098 | 569.899 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1100 | 569.978 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1102 | 570.086 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1104 | 570.139 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1106 | 570.252 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1108 | 570.303 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1110 | 570.419 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1112 | 570.514 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1114 | 570.617 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1116 | 570.661 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1118 | 570.759 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1120 | 570.804 | 7540 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1122 | 571.055 | 7540 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1125 | 571.173 | 7540 | chmod | exit_group | `code=0` |
| 1127 | 571.589 | 7532 | bash | clone | `` |
| 1129 | 572.035 | 7541 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1135 | 573.265 | 7541 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1138 | 573.504 | 7541 | downloaded.sh | clone | `` |
| 1144 | 574.055 | 7542 | downloaded.sh | execve | `/usr/bin/date` |
| 1154 | 575.556 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1156 | 575.606 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1160 | 575.827 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1162 | 575.871 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1164 | 575.973 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1166 | 576.043 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1168 | 576.149 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1170 | 576.196 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1172 | 576.292 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1174 | 576.337 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1176 | 576.433 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1178 | 576.485 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1180 | 576.596 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1182 | 576.642 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1184 | 576.711 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1186 | 576.817 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1188 | 576.863 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1190 | 576.972 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1192 | 577.016 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1194 | 577.136 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1196 | 577.182 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1198 | 577.278 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1200 | 577.324 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1202 | 577.420 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1204 | 577.473 | 7542 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1206 | 577.587 | 7542 | date | openat | `/etc/localtime` |
| 1215 | 577.878 | 7542 | date | exit_group | `code=0` |
| 1217 | 578.391 | 7541 | downloaded.sh | vfork | `` |
| 1218 | 578.483 | 7543 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1228 | 579.855 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1230 | 579.910 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1234 | 580.125 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1236 | 580.171 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1238 | 580.268 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1240 | 580.314 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1242 | 580.408 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1244 | 580.463 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1246 | 580.560 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1248 | 580.604 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1250 | 580.699 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1252 | 580.743 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1254 | 580.851 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1256 | 580.896 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1258 | 580.961 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1260 | 581.058 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1262 | 581.102 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1264 | 581.208 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1266 | 581.253 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1268 | 581.356 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1270 | 581.401 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1272 | 581.502 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1274 | 581.548 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1276 | 581.645 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1278 | 581.689 | 7543 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1295 | 782.601 | 7543 | sleep | exit_group | `code=0` |
| 1297 | 783.271 | 7541 | downloaded.sh | exit_group | `code=0` |
| 1306 | 789.812 | 7532 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 65.462 ms |
| Workload CPU (user+sys) | 86.364 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 5.054 ms |
| Evidence size | 486193 bytes |

