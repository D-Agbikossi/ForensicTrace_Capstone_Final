# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | D |
| Events recorded | 3628 |
| Failed exec attempts removed | 12 |
| Duration | 574.158 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_D_r2.json` (1223497 bytes) |
| SHA-256 | `d0d2246dc3d5d785b2f49862fd9ad1877829b98fb38081aa34b355bc47475696` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_D_r2.json.sha256`

## 1. Process tree

- `8258` /usr/bin/bash
  - `8259` /usr/bin/rm
  - `8260` /usr/bin/mkdir
  - `8261` /usr/bin/python3
  - `8262` /usr/bin/sleep
  - `8264` /usr/bin/curl
  - `8265` /usr/bin/python3
  - `8266` /usr/bin/cat
  - `8267` /usr/bin/chmod
  - `8268` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8258 (?) executed `/usr/bin/bash`
- +6.298 ms pid 8259 (bash) executed `/usr/bin/rm`
- +11.444 ms pid 8260 (bash) executed `/usr/bin/mkdir`
- +18.421 ms pid 8262 (bash) executed `/usr/bin/sleep`
- +18.470 ms pid 8261 (bash) executed `/usr/bin/python3`
- +524.445 ms pid 8264 (bash) executed `/usr/bin/curl`
- +553.912 ms pid 8266 (bash) executed `/usr/bin/cat`
- +562.856 ms pid 8267 (bash) executed `/usr/bin/chmod`
- +570.315 ms pid 8268 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +84.866 ms pid 8261 (python3) connected to `unix:/var/run/nscd/socket`
- +84.972 ms pid 8261 (python3) connected to `ipv6:[...]`
- +85.026 ms pid 8261 (python3) connected to `sockfd=3`
- +85.047 ms pid 8261 (python3) connected to `0.0.0.0:8766`
- +86.986 ms pid 8261 (python3) connected to `unix:/var/run/nscd/socket`
- +545.397 ms pid 8264 (curl) connected to `unix:/var/run/nscd/socket`
- +545.637 ms pid 8264 (curl) connected to `unix:/var/run/nscd/socket`
- +546.546 ms pid 8264 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +16.242 ms by pid 8258 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +524.328 ms by pid 8264 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +553.662 ms by pid 8266 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +569.513 ms pid 8267 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +9.738 ms pid 8259 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +9.788 ms pid 8259 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +9.821 ms pid 8259 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +9.878 ms pid 8259 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +545.858 ms pid 8264 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +570.315 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8268 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +9.788 ms #386 `unlinkat` by pid 8259 (rm)
    - +553.662 ms #3186 `openat` by pid 8266 (bash)
    - +553.764 ms #3188 `close` by pid 8266 (bash)
    - +557.334 ms #3317 `write` by pid 8266 (cat)
    - +557.448 ms #3321 `close` by pid 8266 (cat)
    - +569.513 ms #3495 `fchmodat` by pid 8267 (chmod)
    - +570.315 ms #3525 `execve` by pid 8268 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8258 | ? | execve | `/usr/bin/bash` |
| 49 | 2.187 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 2.233 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 2.447 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 2.490 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 2.642 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 2.678 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 2.753 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 2.788 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 2.863 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 2.898 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.973 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 3.007 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 3.091 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 3.125 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 3.177 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 3.255 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 3.289 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 3.363 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 3.397 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 3.479 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 3.514 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 3.603 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 3.639 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 3.722 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 3.755 | 8258 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 5.094 | 8258 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 239 | 5.907 | 8258 | bash | clone | `` |
| 256 | 6.298 | 8259 | bash | execve | `/usr/bin/rm` |
| 293 | 7.562 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 7.610 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 7.824 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 7.869 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 7.966 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 8.011 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 8.107 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 8.151 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 8.247 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 8.290 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 8.383 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 8.428 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 8.538 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 8.583 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 8.648 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 8.744 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 8.789 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 8.890 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 8.933 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 9.037 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 9.081 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 9.176 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 9.221 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 9.317 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 9.362 | 8259 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 9.529 | 8259 | rm | openat | `/tmp/ft_scenario03` |
| 385 | 9.738 | 8259 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 386 | 9.788 | 8259 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 387 | 9.821 | 8259 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 389 | 9.878 | 8259 | rm | unlinkat | `/tmp/ft_scenario03` |
| 394 | 10.028 | 8259 | rm | exit_group | `code=0` |
| 428 | 11.012 | 8258 | bash | clone | `` |
| 445 | 11.444 | 8260 | bash | execve | `/usr/bin/mkdir` |
| 509 | 13.510 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 511 | 13.562 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 520 | 13.769 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 522 | 13.810 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 526 | 13.905 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 528 | 13.946 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 532 | 14.038 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 534 | 14.077 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 538 | 14.171 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 540 | 14.210 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 544 | 14.303 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 546 | 14.343 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 550 | 14.449 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 552 | 14.489 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 555 | 14.555 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 559 | 14.647 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 561 | 14.688 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 565 | 14.780 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 567 | 14.819 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 571 | 14.918 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 573 | 14.963 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 577 | 15.134 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 579 | 15.215 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 583 | 15.324 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 585 | 15.372 | 8260 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 596 | 15.855 | 8260 | mkdir | exit_group | `code=0` |
| 606 | 16.242 | 8258 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 614 | 16.396 | 8258 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 621 | 16.806 | 8258 | bash | clone | `` |
| 696 | 17.991 | 8258 | bash | clone | `` |
| 722 | 18.421 | 8262 | bash | execve | `/usr/bin/sleep` |
| 725 | 18.470 | 8261 | bash | execve | `/usr/bin/python3` |
| 800 | 19.706 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 804 | 19.754 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 819 | 19.943 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 822 | 19.981 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 829 | 20.079 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 832 | 20.120 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 839 | 20.213 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 842 | 20.253 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 848 | 20.345 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 851 | 20.384 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 859 | 20.485 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 862 | 20.533 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 863 | 20.545 | 8261 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 867 | 20.596 | 8261 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 871 | 20.645 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 874 | 20.687 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 880 | 20.751 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 886 | 20.844 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 889 | 20.886 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 894 | 20.987 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 897 | 21.026 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 903 | 21.123 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 905 | 21.166 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 909 | 21.257 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 911 | 21.297 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 915 | 21.390 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 917 | 21.430 | 8262 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 953 | 23.772 | 8261 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 954 | 23.801 | 8261 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 957 | 23.867 | 8261 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 958 | 23.887 | 8261 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 959 | 23.906 | 8261 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 970 | 24.829 | 8261 | python3 | openat | `/etc/localtime` |
| 1125 | 29.900 | 8261 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1131 | 30.053 | 8261 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1140 | 30.269 | 8261 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1171 | 31.338 | 8261 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1179 | 31.505 | 8261 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1187 | 31.661 | 8261 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1435 | 40.200 | 8261 | python3 | openat | `/tmp/ft_scenario03` |
| 2370 | 84.509 | 8261 | python3 | openat | `/etc/gai.conf` |
| 2380 | 84.757 | 8261 | python3 | sendto | `socket:[49916]` |
| 2384 | 84.866 | 8261 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2388 | 84.972 | 8261 | python3 | connect | `ipv6:[...]` |
| 2390 | 85.026 | 8261 | python3 | connect | `sockfd=3` |
| 2391 | 85.047 | 8261 | python3 | connect | `0.0.0.0:8766` |
| 2432 | 86.986 | 8261 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2436 | 87.090 | 8261 | python3 | openat | `/etc/nsswitch.conf` |
| 2443 | 87.254 | 8261 | python3 | openat | `/etc/host.conf` |
| 2449 | 87.382 | 8261 | python3 | openat | `/etc/resolv.conf` |
| 2455 | 87.521 | 8261 | python3 | openat | `/etc/hosts` |
| 2463 | 87.707 | 8261 | python3 | openat | `/etc/hosts` |
| 2473 | 522.698 | 8262 | sleep | exit_group | `code=0` |
| 2509 | 523.838 | 8258 | bash | clone | `` |
| 2526 | 524.328 | 8264 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 2529 | 524.445 | 8264 | bash | execve | `/usr/bin/curl` |
| 2845 | 541.302 | 8264 | curl | openat | `/etc/gnutls/config` |
| 2892 | 543.232 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 2894 | 543.283 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 2903 | 543.516 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 2905 | 543.568 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 2909 | 543.677 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 2911 | 543.725 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 2915 | 543.831 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 2917 | 543.879 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 2921 | 544.003 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 2923 | 544.053 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 2927 | 544.176 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 2929 | 544.224 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 2933 | 544.333 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 2935 | 544.378 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 2938 | 544.444 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 2942 | 544.551 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 2944 | 544.595 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 2948 | 544.695 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 2950 | 544.740 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 2954 | 544.843 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 2956 | 544.889 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 2960 | 544.985 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 2962 | 545.031 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 2966 | 545.131 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 2968 | 545.178 | 8264 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 2972 | 545.286 | 8264 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 2973 | 545.313 | 8264 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 2976 | 545.397 | 8264 | curl | connect | `unix:/var/run/nscd/socket` |
| 2979 | 545.637 | 8264 | curl | connect | `unix:/var/run/nscd/socket` |
| 2983 | 545.725 | 8264 | curl | openat | `/etc/nsswitch.conf` |
| 2989 | 545.858 | 8264 | curl | openat | `/etc/passwd` |
| 2994 | 545.962 | 8264 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3019 | 546.546 | 8264 | curl | connect | `127.0.0.1:8766` |
| 3023 | 546.719 | 8261 | python3 | accept4 | `sockfd=3` |
| 3036 | 546.941 | 8264 | curl | sendto | `socket:[49925]` |
| 3043 | 547.060 | 8261 | python3 | clone3 | `` |
| 3059 | 547.491 | 8265 | python3 | recvfrom | `socket:[51609]` |
| 3067 | 547.876 | 8265 | python3 | openat | `/etc/mime.types` |
| 3092 | 550.313 | 8265 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 3098 | 550.596 | 8265 | python3 | sendto | `socket:[51609]` |
| 3104 | 550.783 | 8265 | python3 | sendto | `socket:[51609]` |
| 3105 | 550.805 | 8264 | curl | recvfrom | `socket:[49925]` |
| 3114 | 551.127 | 8264 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 3121 | 551.246 | 8265 | python3 | exit | `code=0` |
| 3133 | 551.714 | 8264 | curl | exit_group | `code=0` |
| 3169 | 553.204 | 8258 | bash | clone | `` |
| 3186 | 553.662 | 8266 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 3195 | 553.912 | 8266 | bash | execve | `/usr/bin/cat` |
| 3232 | 555.226 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3234 | 555.397 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3243 | 555.618 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3245 | 555.663 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3249 | 555.755 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3251 | 555.800 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3255 | 555.894 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3257 | 555.935 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3261 | 556.030 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3263 | 556.072 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3267 | 556.162 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3269 | 556.205 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3273 | 556.307 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3275 | 556.351 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3278 | 556.414 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3282 | 556.507 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3284 | 556.557 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3288 | 556.651 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3290 | 556.694 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3294 | 556.802 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3296 | 556.844 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3300 | 556.936 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3302 | 556.981 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3306 | 557.074 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3308 | 557.118 | 8266 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3317 | 557.334 | 8266 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 3323 | 557.501 | 8266 | cat | exit_group | `code=0` |
| 3359 | 562.338 | 8258 | bash | clone | `` |
| 3376 | 562.856 | 8267 | bash | execve | `/usr/bin/chmod` |
| 3413 | 566.421 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3415 | 566.825 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3424 | 567.058 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3426 | 567.125 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3430 | 567.453 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3432 | 567.505 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3436 | 568.315 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3438 | 568.355 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3442 | 568.435 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3444 | 568.472 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3448 | 568.564 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3450 | 568.601 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3454 | 568.692 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3456 | 568.728 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3459 | 568.785 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3463 | 568.866 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3465 | 568.903 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3469 | 568.991 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3471 | 569.028 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3475 | 569.116 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3477 | 569.153 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3481 | 569.232 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3483 | 569.268 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3487 | 569.353 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3489 | 569.388 | 8267 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3495 | 569.513 | 8267 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 3498 | 569.605 | 8267 | chmod | exit_group | `code=0` |
| 3508 | 569.924 | 8258 | bash | clone | `` |
| 3525 | 570.315 | 8268 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 3565 | 571.579 | 8268 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 3580 | 571.829 | 8268 | runme.sh | exit_group | `code=0` |
| 3628 | 573.501 | 8258 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 56.621 ms |
| Workload CPU (user+sys) | 74.912 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 4.036 ms |
| Evidence size | 1223497 bytes |

