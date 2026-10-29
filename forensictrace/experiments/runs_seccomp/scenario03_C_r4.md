# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | C |
| Events recorded | 1155 |
| Failed exec attempts removed | 12 |
| Duration | 533.573 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_C_r4.json` (428526 bytes) |
| SHA-256 | `0e708f386eb02ba5829b0598af6fe18396a5bafbdf7113d1cc466106a77e9652` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_C_r4.json.sha256`

## 1. Process tree

- `8650` /usr/bin/bash
  - `8651` /usr/bin/rm
  - `8652` /usr/bin/mkdir
  - `8653` /usr/bin/python3
  - `8654` /usr/bin/sleep
  - `8665` /usr/bin/curl
  - `8666` /usr/bin/python3
  - `8667` /usr/bin/cat
  - `8668` /usr/bin/chmod
  - `8669` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8650 (?) executed `/usr/bin/bash`
- +2.441 ms pid 8651 (bash) executed `/usr/bin/rm`
- +4.784 ms pid 8652 (bash) executed `/usr/bin/mkdir`
- +7.462 ms pid 8654 (bash) executed `/usr/bin/sleep`
- +7.509 ms pid 8653 (bash) executed `/usr/bin/python3`
- +513.594 ms pid 8665 (bash) executed `/usr/bin/curl`
- +526.029 ms pid 8667 (bash) executed `/usr/bin/cat`
- +528.882 ms pid 8668 (bash) executed `/usr/bin/chmod`
- +531.042 ms pid 8669 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +58.306 ms pid 8653 (python3) connected to `unix:/var/run/nscd/socket`
- +58.408 ms pid 8653 (python3) connected to `ipv6:[...]`
- +58.444 ms pid 8653 (python3) connected to `sockfd=3`
- +58.463 ms pid 8653 (python3) connected to `0.0.0.0:8766`
- +59.718 ms pid 8653 (python3) connected to `unix:/var/run/nscd/socket`
- +520.939 ms pid 8665 (curl) connected to `unix:/var/run/nscd/socket`
- +520.989 ms pid 8665 (curl) connected to `unix:/var/run/nscd/socket`
- +521.296 ms pid 8665 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +7.022 ms by pid 8650 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +511.049 ms by pid 8665 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +525.893 ms by pid 8667 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +530.702 ms pid 8668 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +4.278 ms pid 8651 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +4.324 ms pid 8651 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +4.351 ms pid 8651 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +4.392 ms pid 8651 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +521.113 ms pid 8665 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +531.042 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8669 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +4.324 ms #138 `unlinkat` by pid 8651 (rm)
    - +525.893 ms #989 `openat` by pid 8667 (bash)
    - +525.951 ms #990 `close` by pid 8667 (bash)
    - +528.276 ms #1057 `write` by pid 8667 (cat)
    - +528.380 ms #1060 `close` by pid 8667 (cat)
    - +530.702 ms #1128 `fchmodat` by pid 8668 (chmod)
    - +531.042 ms #1135 `execve` by pid 8669 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8650 | ? | execve | `/usr/bin/bash` |
| 15 | 0.795 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 0.833 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 0.925 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 0.960 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.008 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.043 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.090 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.123 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.169 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.203 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.249 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.284 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.338 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.372 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.407 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.453 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.488 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 1.532 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 1.569 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 1.625 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 1.660 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 1.705 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 1.738 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 1.787 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 1.821 | 8650 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.069 | 8650 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 2.263 | 8650 | bash | clone | `` |
| 73 | 2.441 | 8651 | bash | execve | `/usr/bin/rm` |
| 83 | 3.064 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.109 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 3.258 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 3.298 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 3.349 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 3.383 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 3.430 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 3.464 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 3.508 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 3.543 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 3.594 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 3.630 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 3.685 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 3.723 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 3.761 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 3.805 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 3.840 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 3.887 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 3.921 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 3.973 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 4.006 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 4.052 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 4.086 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 4.132 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 4.166 | 8651 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 4.219 | 8651 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 4.278 | 8651 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 4.324 | 8651 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 4.351 | 8651 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 4.392 | 8651 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 4.510 | 8651 | rm | exit_group | `code=0` |
| 146 | 4.646 | 8650 | bash | clone | `` |
| 148 | 4.784 | 8652 | bash | execve | `/usr/bin/mkdir` |
| 168 | 5.731 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 5.768 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 5.857 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 5.895 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 5.939 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 5.974 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 6.020 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 6.054 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 6.099 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 6.131 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 6.177 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 6.211 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 6.263 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 6.297 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 6.332 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 6.376 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 6.410 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 6.455 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 6.489 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 6.536 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 6.577 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 6.628 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 6.661 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 6.707 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 6.740 | 8652 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 6.883 | 8652 | mkdir | exit_group | `code=0` |
| 224 | 7.022 | 8650 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 7.081 | 8650 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 7.135 | 8650 | bash | clone | `` |
| 231 | 7.290 | 8650 | bash | clone | `` |
| 236 | 7.462 | 8654 | bash | execve | `/usr/bin/sleep` |
| 238 | 7.509 | 8653 | bash | execve | `/usr/bin/python3` |
| 256 | 8.053 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 260 | 8.108 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 267 | 8.226 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 269 | 8.271 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 8.326 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 8.374 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 8.434 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 278 | 8.482 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 280 | 8.541 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 283 | 8.595 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 287 | 8.655 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 290 | 8.708 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 291 | 8.720 | 8653 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 294 | 8.775 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 295 | 8.785 | 8653 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 297 | 8.819 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 300 | 8.863 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 8.920 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 8.964 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 9.024 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 9.074 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 9.138 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 9.187 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 9.248 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 9.298 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 9.359 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 9.408 | 8654 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 11.762 | 8653 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 11.833 | 8653 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 11.885 | 8653 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 11.914 | 8653 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 11.940 | 8653 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 12.849 | 8653 | python3 | openat | `/etc/localtime` |
| 362 | 17.348 | 8653 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 17.464 | 8653 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 17.650 | 8653 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 18.469 | 8653 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 18.545 | 8653 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 18.630 | 8653 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 24.849 | 8653 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 58.136 | 8653 | python3 | openat | `/etc/gai.conf` |
| 726 | 58.240 | 8653 | python3 | sendto | `socket:[52135]` |
| 727 | 58.306 | 8653 | python3 | connect | `unix:/var/run/nscd/socket` |
| 730 | 58.408 | 8653 | python3 | connect | `ipv6:[...]` |
| 731 | 58.444 | 8653 | python3 | connect | `sockfd=3` |
| 732 | 58.463 | 8653 | python3 | connect | `0.0.0.0:8766` |
| 742 | 59.718 | 8653 | python3 | connect | `unix:/var/run/nscd/socket` |
| 744 | 59.772 | 8653 | python3 | openat | `/etc/nsswitch.conf` |
| 748 | 59.858 | 8653 | python3 | openat | `/etc/host.conf` |
| 752 | 59.930 | 8653 | python3 | openat | `/etc/resolv.conf` |
| 756 | 60.007 | 8653 | python3 | openat | `/etc/hosts` |
| 760 | 60.087 | 8653 | python3 | openat | `/etc/hosts` |
| 765 | 510.128 | 8654 | sleep | exit_group | `code=0` |
| 767 | 510.672 | 8650 | bash | clone | `` |
| 769 | 511.049 | 8665 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 771 | 513.594 | 8665 | bash | execve | `/usr/bin/curl` |
| 867 | 518.893 | 8665 | curl | openat | `/etc/gnutls/config` |
| 885 | 519.795 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 887 | 519.833 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 891 | 519.927 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 893 | 519.961 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 895 | 520.009 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 897 | 520.044 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 899 | 520.089 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 901 | 520.124 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 903 | 520.167 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 905 | 520.202 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 907 | 520.247 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 909 | 520.281 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 911 | 520.336 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 913 | 520.368 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 915 | 520.406 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 520.458 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 520.491 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 921 | 520.538 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 923 | 520.576 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 925 | 520.632 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 927 | 520.667 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 929 | 520.712 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 931 | 520.749 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 933 | 520.797 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 935 | 520.833 | 8665 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 937 | 520.885 | 8665 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 938 | 520.904 | 8665 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 939 | 520.939 | 8665 | curl | connect | `unix:/var/run/nscd/socket` |
| 941 | 520.989 | 8665 | curl | connect | `unix:/var/run/nscd/socket` |
| 943 | 521.030 | 8665 | curl | openat | `/etc/nsswitch.conf` |
| 947 | 521.113 | 8665 | curl | openat | `/etc/passwd` |
| 950 | 521.175 | 8665 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 951 | 521.296 | 8665 | curl | connect | `127.0.0.1:8766` |
| 952 | 521.392 | 8665 | curl | sendto | `socket:[54528]` |
| 953 | 521.415 | 8653 | python3 | accept4 | `sockfd=3` |
| 954 | 521.557 | 8653 | python3 | clone3 | `` |
| 955 | 521.711 | 8666 | python3 | recvfrom | `socket:[52147]` |
| 956 | 521.958 | 8666 | python3 | openat | `/etc/mime.types` |
| 969 | 524.324 | 8666 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 971 | 524.487 | 8666 | python3 | sendto | `socket:[52147]` |
| 973 | 524.605 | 8665 | curl | recvfrom | `socket:[54528]` |
| 975 | 524.658 | 8666 | python3 | sendto | `socket:[52147]` |
| 976 | 524.713 | 8665 | curl | recvfrom | `socket:[54528]` |
| 980 | 524.812 | 8665 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 984 | 524.905 | 8666 | python3 | exit | `code=0` |
| 985 | 525.105 | 8665 | curl | exit_group | `code=0` |
| 987 | 525.665 | 8650 | bash | clone | `` |
| 989 | 525.893 | 8667 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 994 | 526.029 | 8667 | bash | execve | `/usr/bin/cat` |
| 1004 | 526.660 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1006 | 526.696 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1010 | 526.793 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1012 | 526.826 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1014 | 526.874 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1016 | 526.907 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1018 | 526.954 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1020 | 526.989 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1022 | 527.033 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1024 | 527.068 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1026 | 527.111 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1028 | 527.181 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1030 | 527.301 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1032 | 527.376 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1034 | 527.429 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1036 | 527.499 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1038 | 527.550 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1040 | 527.615 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1042 | 527.664 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1044 | 527.735 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1046 | 527.781 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1048 | 527.847 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1050 | 527.898 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1052 | 528.005 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1054 | 528.116 | 8667 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1057 | 528.276 | 8667 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1062 | 528.437 | 8667 | cat | exit_group | `code=0` |
| 1064 | 528.687 | 8650 | bash | clone | `` |
| 1066 | 528.882 | 8668 | bash | execve | `/usr/bin/chmod` |
| 1076 | 529.623 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1078 | 529.664 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1082 | 529.753 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1084 | 529.787 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1086 | 529.833 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1088 | 529.867 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1090 | 529.917 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1092 | 529.950 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1094 | 529.995 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1096 | 530.028 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1098 | 530.074 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1100 | 530.108 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1102 | 530.161 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1104 | 530.195 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1106 | 530.231 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1108 | 530.277 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1110 | 530.311 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1112 | 530.357 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1114 | 530.392 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1116 | 530.442 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1118 | 530.477 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1120 | 530.522 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1122 | 530.555 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1124 | 530.616 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1126 | 530.649 | 8668 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1128 | 530.702 | 8668 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1131 | 530.771 | 8668 | chmod | exit_group | `code=0` |
| 1133 | 530.898 | 8650 | bash | clone | `` |
| 1135 | 531.042 | 8669 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1141 | 531.527 | 8669 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1146 | 531.650 | 8669 | runme.sh | exit_group | `code=0` |
| 1155 | 532.954 | 8650 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 21.322 ms |
| Workload CPU (user+sys) | 62.476 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.411 ms |
| Evidence size | 428526 bytes |

