# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | C |
| Events recorded | 1155 |
| Failed exec attempts removed | 12 |
| Duration | 539.507 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_C_r3.json` (428526 bytes) |
| SHA-256 | `cc52f18d03829982031bd3149f028e934b83924343f7e8c7594fa589d1989a8e` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_C_r3.json.sha256`

## 1. Process tree

- `8417` /usr/bin/bash
  - `8418` /usr/bin/rm
  - `8419` /usr/bin/mkdir
  - `8420` /usr/bin/python3
  - `8421` /usr/bin/sleep
  - `8423` /usr/bin/curl
  - `8424` /usr/bin/python3
  - `8425` /usr/bin/cat
  - `8426` /usr/bin/chmod
  - `8427` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8417 (?) executed `/usr/bin/bash`
- +5.849 ms pid 8418 (bash) executed `/usr/bin/rm`
- +9.917 ms pid 8419 (bash) executed `/usr/bin/mkdir`
- +12.501 ms pid 8421 (bash) executed `/usr/bin/sleep`
- +12.530 ms pid 8420 (bash) executed `/usr/bin/python3`
- +515.775 ms pid 8423 (bash) executed `/usr/bin/curl`
- +531.607 ms pid 8425 (bash) executed `/usr/bin/cat`
- +534.226 ms pid 8426 (bash) executed `/usr/bin/chmod`
- +536.345 ms pid 8427 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +84.469 ms pid 8420 (python3) connected to `unix:/var/run/nscd/socket`
- +84.546 ms pid 8420 (python3) connected to `ipv6:[...]`
- +84.577 ms pid 8420 (python3) connected to `sockfd=3`
- +84.596 ms pid 8420 (python3) connected to `0.0.0.0:8766`
- +85.862 ms pid 8420 (python3) connected to `unix:/var/run/nscd/socket`
- +525.841 ms pid 8423 (curl) connected to `unix:/var/run/nscd/socket`
- +525.912 ms pid 8423 (curl) connected to `unix:/var/run/nscd/socket`
- +526.472 ms pid 8423 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +12.018 ms by pid 8417 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +515.679 ms by pid 8423 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +531.474 ms by pid 8425 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +535.966 ms pid 8426 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +9.402 ms pid 8418 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +9.447 ms pid 8418 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +9.472 ms pid 8418 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +9.513 ms pid 8418 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +526.077 ms pid 8423 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +536.345 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8427 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +9.447 ms #138 `unlinkat` by pid 8418 (rm)
    - +531.474 ms #989 `openat` by pid 8425 (bash)
    - +531.528 ms #990 `close` by pid 8425 (bash)
    - +533.718 ms #1057 `write` by pid 8425 (cat)
    - +533.828 ms #1060 `close` by pid 8425 (cat)
    - +535.966 ms #1128 `fchmodat` by pid 8426 (chmod)
    - +536.345 ms #1135 `execve` by pid 8427 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8417 | ? | execve | `/usr/bin/bash` |
| 15 | 1.798 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.908 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 2.137 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 2.226 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 2.343 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 2.430 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.546 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.629 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.744 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.837 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.955 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 3.042 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 3.178 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 3.265 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 3.354 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 3.472 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 3.564 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 3.676 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 3.765 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 3.902 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.992 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 4.107 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 4.193 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 4.314 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 4.399 | 8417 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 5.022 | 8417 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 5.485 | 8417 | bash | clone | `` |
| 73 | 5.849 | 8418 | bash | execve | `/usr/bin/rm` |
| 83 | 7.020 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 7.098 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 7.297 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 7.372 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 7.477 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 7.552 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 7.654 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 7.730 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 7.839 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 7.918 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 8.016 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 8.095 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 8.219 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 8.295 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 8.380 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 8.482 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 8.562 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 8.671 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 8.747 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 8.965 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 9.041 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 9.149 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 9.210 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 9.256 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 9.289 | 8418 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 9.342 | 8418 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 9.402 | 8418 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 9.447 | 8418 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 9.472 | 8418 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 9.513 | 8418 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 9.625 | 8418 | rm | exit_group | `code=0` |
| 146 | 9.751 | 8417 | bash | clone | `` |
| 148 | 9.917 | 8419 | bash | execve | `/usr/bin/mkdir` |
| 168 | 10.713 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 10.749 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 10.846 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 10.881 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 10.927 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 10.961 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 11.013 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 11.046 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 11.091 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 11.124 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 11.171 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 11.204 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 11.259 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 11.293 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 11.329 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 11.374 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 11.408 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 11.452 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 11.487 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 11.537 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 11.572 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 11.617 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 11.650 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 11.697 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 11.730 | 8419 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 11.875 | 8419 | mkdir | exit_group | `code=0` |
| 224 | 12.018 | 8417 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 12.079 | 8417 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 12.141 | 8417 | bash | clone | `` |
| 231 | 12.338 | 8417 | bash | clone | `` |
| 236 | 12.501 | 8421 | bash | execve | `/usr/bin/sleep` |
| 238 | 12.530 | 8420 | bash | execve | `/usr/bin/python3` |
| 258 | 13.141 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 260 | 13.186 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 267 | 13.297 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 13.348 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 13.412 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 13.460 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 13.520 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 278 | 13.565 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 281 | 13.626 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 284 | 13.673 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 288 | 13.723 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 290 | 13.758 | 8420 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 291 | 13.772 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 294 | 13.821 | 8420 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 295 | 13.841 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 298 | 13.886 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 301 | 13.933 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 13.988 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 14.036 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 14.100 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 14.148 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 14.213 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 14.262 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 14.321 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 14.368 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 14.429 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 14.477 | 8421 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 16.539 | 8420 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 16.590 | 8420 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 16.636 | 8420 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 16.663 | 8420 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 16.690 | 8420 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 17.551 | 8420 | python3 | openat | `/etc/localtime` |
| 362 | 21.383 | 8420 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 21.500 | 8420 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 21.647 | 8420 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 22.619 | 8420 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 22.740 | 8420 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 22.824 | 8420 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 30.925 | 8420 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 84.295 | 8420 | python3 | openat | `/etc/gai.conf` |
| 726 | 84.424 | 8420 | python3 | sendto | `socket:[52548]` |
| 727 | 84.469 | 8420 | python3 | connect | `unix:/var/run/nscd/socket` |
| 730 | 84.546 | 8420 | python3 | connect | `ipv6:[...]` |
| 731 | 84.577 | 8420 | python3 | connect | `sockfd=3` |
| 732 | 84.596 | 8420 | python3 | connect | `0.0.0.0:8766` |
| 742 | 85.862 | 8420 | python3 | connect | `unix:/var/run/nscd/socket` |
| 744 | 85.916 | 8420 | python3 | openat | `/etc/nsswitch.conf` |
| 748 | 86.001 | 8420 | python3 | openat | `/etc/host.conf` |
| 752 | 86.073 | 8420 | python3 | openat | `/etc/resolv.conf` |
| 756 | 86.151 | 8420 | python3 | openat | `/etc/hosts` |
| 760 | 86.231 | 8420 | python3 | openat | `/etc/hosts` |
| 765 | 515.074 | 8421 | sleep | exit_group | `code=0` |
| 767 | 515.342 | 8417 | bash | clone | `` |
| 769 | 515.679 | 8423 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 771 | 515.775 | 8423 | bash | execve | `/usr/bin/curl` |
| 867 | 520.632 | 8423 | curl | openat | `/etc/gnutls/config` |
| 885 | 521.650 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 887 | 521.698 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 891 | 521.842 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 893 | 521.890 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 895 | 521.952 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 897 | 522.061 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 899 | 522.154 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 901 | 522.206 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 903 | 522.263 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 905 | 522.313 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 907 | 522.375 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 909 | 524.920 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 911 | 525.018 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 913 | 525.066 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 915 | 525.121 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 525.191 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 525.239 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 921 | 525.302 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 923 | 525.351 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 925 | 525.418 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 927 | 525.467 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 929 | 525.528 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 931 | 525.581 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 933 | 525.640 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 935 | 525.688 | 8423 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 937 | 525.760 | 8423 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 938 | 525.787 | 8423 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 939 | 525.841 | 8423 | curl | connect | `unix:/var/run/nscd/socket` |
| 941 | 525.912 | 8423 | curl | connect | `unix:/var/run/nscd/socket` |
| 943 | 525.970 | 8423 | curl | openat | `/etc/nsswitch.conf` |
| 947 | 526.077 | 8423 | curl | openat | `/etc/passwd` |
| 950 | 526.159 | 8423 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 951 | 526.472 | 8423 | curl | connect | `127.0.0.1:8766` |
| 952 | 526.627 | 8423 | curl | sendto | `socket:[51124]` |
| 953 | 526.649 | 8420 | python3 | accept4 | `sockfd=3` |
| 954 | 526.891 | 8420 | python3 | clone3 | `` |
| 955 | 527.199 | 8424 | python3 | recvfrom | `socket:[52553]` |
| 956 | 527.488 | 8424 | python3 | openat | `/etc/mime.types` |
| 969 | 529.986 | 8424 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 971 | 530.136 | 8424 | python3 | sendto | `socket:[52553]` |
| 972 | 530.197 | 8423 | curl | recvfrom | `socket:[51124]` |
| 975 | 530.280 | 8424 | python3 | sendto | `socket:[52553]` |
| 976 | 530.304 | 8423 | curl | recvfrom | `socket:[51124]` |
| 980 | 530.394 | 8423 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 984 | 530.475 | 8424 | python3 | exit | `code=0` |
| 985 | 530.670 | 8423 | curl | exit_group | `code=0` |
| 987 | 531.252 | 8417 | bash | clone | `` |
| 989 | 531.474 | 8425 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 994 | 531.607 | 8425 | bash | execve | `/usr/bin/cat` |
| 1004 | 532.320 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1006 | 532.366 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1010 | 532.487 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1012 | 532.531 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1014 | 532.591 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1016 | 532.634 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1018 | 532.691 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1020 | 532.736 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1022 | 532.792 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1024 | 532.843 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1026 | 532.898 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1028 | 532.944 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1030 | 533.011 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1032 | 533.054 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1034 | 533.101 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1036 | 533.158 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1038 | 533.203 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1040 | 533.262 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1042 | 533.305 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1044 | 533.370 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1046 | 533.413 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1048 | 533.474 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1050 | 533.519 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1052 | 533.579 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1054 | 533.624 | 8425 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1057 | 533.718 | 8425 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1062 | 533.880 | 8425 | cat | exit_group | `code=0` |
| 1064 | 534.055 | 8417 | bash | clone | `` |
| 1066 | 534.226 | 8426 | bash | execve | `/usr/bin/chmod` |
| 1076 | 534.828 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1078 | 534.867 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1082 | 534.966 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1084 | 535.001 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1086 | 535.046 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1088 | 535.081 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1090 | 535.125 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1092 | 535.158 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1094 | 535.203 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1096 | 535.236 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1098 | 535.279 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1100 | 535.314 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1102 | 535.367 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1104 | 535.401 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1106 | 535.436 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1108 | 535.493 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1110 | 535.533 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1112 | 535.577 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1114 | 535.612 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1116 | 535.661 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1118 | 535.695 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1120 | 535.740 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1122 | 535.773 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1124 | 535.847 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1126 | 535.899 | 8426 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1128 | 535.966 | 8426 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1131 | 536.054 | 8426 | chmod | exit_group | `code=0` |
| 1133 | 536.201 | 8417 | bash | clone | `` |
| 1135 | 536.345 | 8427 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1141 | 536.836 | 8427 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1146 | 536.950 | 8427 | runme.sh | exit_group | `code=0` |
| 1155 | 538.283 | 8417 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 27.604 ms |
| Workload CPU (user+sys) | 76.861 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.509 ms |
| Evidence size | 428526 bytes |

