# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | D |
| Events recorded | 3630 |
| Failed exec attempts removed | 12 |
| Duration | 559.223 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_D_r1.json` (1224173 bytes) |
| SHA-256 | `54d3a7fad11666e973855713706c27584ae0c8e85ebdf9b84337e3feac527a4c` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_D_r1.json.sha256`

## 1. Process tree

- `7242` /usr/bin/bash
  - `7243` /usr/bin/rm
  - `7244` /usr/bin/mkdir
  - `7245` /usr/bin/python3
  - `7246` /usr/bin/sleep
  - `7247` /usr/bin/curl
  - `7248` /usr/bin/python3
  - `7249` /usr/bin/cat
  - `7250` /usr/bin/chmod
  - `7251` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7242 (?) executed `/usr/bin/bash`
- +8.448 ms pid 7243 (bash) executed `/usr/bin/rm`
- +12.989 ms pid 7244 (bash) executed `/usr/bin/mkdir`
- +18.849 ms pid 7246 (bash) executed `/usr/bin/sleep`
- +19.015 ms pid 7245 (bash) executed `/usr/bin/python3`
- +524.443 ms pid 7247 (bash) executed `/usr/bin/curl`
- +544.537 ms pid 7249 (bash) executed `/usr/bin/cat`
- +548.366 ms pid 7250 (bash) executed `/usr/bin/chmod`
- +553.807 ms pid 7251 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +94.631 ms pid 7245 (python3) connected to `unix:/var/run/nscd/socket`
- +94.771 ms pid 7245 (python3) connected to `ipv6:[...]`
- +94.816 ms pid 7245 (python3) connected to `sockfd=3`
- +94.838 ms pid 7245 (python3) connected to `0.0.0.0:8766`
- +96.559 ms pid 7245 (python3) connected to `unix:/var/run/nscd/socket`
- +537.373 ms pid 7247 (curl) connected to `unix:/var/run/nscd/socket`
- +537.437 ms pid 7247 (curl) connected to `unix:/var/run/nscd/socket`
- +538.201 ms pid 7247 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +16.574 ms by pid 7242 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +524.331 ms by pid 7247 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +544.270 ms by pid 7249 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +552.634 ms pid 7250 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +11.557 ms pid 7243 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +11.628 ms pid 7243 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +11.659 ms pid 7243 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +11.710 ms pid 7243 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +537.621 ms pid 7247 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +553.807 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7251 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +11.628 ms #386 `unlinkat` by pid 7243 (rm)
    - +544.270 ms #3188 `openat` by pid 7249 (bash)
    - +544.351 ms #3190 `close` by pid 7249 (bash)
    - +547.179 ms #3319 `write` by pid 7249 (cat)
    - +547.266 ms #3323 `close` by pid 7249 (cat)
    - +552.634 ms #3497 `fchmodat` by pid 7250 (chmod)
    - +553.807 ms #3527 `execve` by pid 7251 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7242 | ? | execve | `/usr/bin/bash` |
| 49 | 2.842 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 2.898 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 3.167 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 3.213 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 3.334 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 3.386 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 3.496 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 3.553 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 3.682 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 3.752 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 3.871 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 3.930 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 4.070 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 4.123 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 4.197 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 4.322 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 4.380 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 4.494 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 4.677 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 4.803 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 4.871 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 4.989 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 5.038 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 5.148 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 5.195 | 7242 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 7.059 | 7242 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 239 | 8.049 | 7242 | bash | clone | `` |
| 256 | 8.448 | 7243 | bash | execve | `/usr/bin/rm` |
| 293 | 9.515 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 9.552 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 9.733 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 9.780 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 9.879 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 9.913 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 10.035 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 10.075 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 10.161 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 10.194 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 10.273 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 10.315 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 10.414 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 10.448 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 10.505 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 10.590 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 10.632 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 10.734 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 10.774 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 10.886 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 10.919 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 11.014 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 11.056 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 11.155 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 11.197 | 7243 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 11.365 | 7243 | rm | openat | `/tmp/ft_scenario03` |
| 385 | 11.557 | 7243 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 386 | 11.628 | 7243 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 387 | 11.659 | 7243 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 389 | 11.710 | 7243 | rm | unlinkat | `/tmp/ft_scenario03` |
| 394 | 11.843 | 7243 | rm | exit_group | `code=0` |
| 428 | 12.629 | 7242 | bash | clone | `` |
| 445 | 12.989 | 7244 | bash | execve | `/usr/bin/mkdir` |
| 509 | 14.532 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 511 | 14.627 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 520 | 14.850 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 522 | 14.892 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 526 | 14.968 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 528 | 15.002 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 532 | 15.075 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 534 | 15.108 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 538 | 15.184 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 540 | 15.216 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 544 | 15.290 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 546 | 15.324 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 550 | 15.405 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 552 | 15.439 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 555 | 15.489 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 559 | 15.561 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 561 | 15.596 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 565 | 15.668 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 567 | 15.709 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 571 | 15.793 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 573 | 15.826 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 577 | 15.899 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 579 | 15.932 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 583 | 16.011 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 585 | 16.045 | 7244 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 596 | 16.292 | 7244 | mkdir | exit_group | `code=0` |
| 606 | 16.574 | 7242 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 614 | 16.729 | 7242 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 621 | 16.934 | 7242 | bash | clone | `` |
| 692 | 18.310 | 7242 | bash | clone | `` |
| 718 | 18.849 | 7246 | bash | execve | `/usr/bin/sleep` |
| 725 | 19.015 | 7245 | bash | execve | `/usr/bin/python3` |
| 795 | 20.242 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 799 | 20.293 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 815 | 20.527 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 818 | 20.571 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 826 | 20.669 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 828 | 20.722 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 834 | 20.828 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 837 | 20.880 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 844 | 20.982 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 847 | 21.031 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 852 | 21.124 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 855 | 21.173 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 861 | 21.322 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 865 | 21.373 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 870 | 21.447 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 874 | 21.506 | 7245 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 877 | 21.547 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 878 | 21.564 | 7245 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 881 | 21.600 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 889 | 21.722 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 893 | 21.773 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 898 | 21.882 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 901 | 21.929 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 906 | 22.033 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 909 | 22.078 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 915 | 22.173 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 917 | 22.223 | 7246 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 953 | 24.929 | 7245 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 954 | 24.962 | 7245 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 957 | 25.045 | 7245 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 958 | 25.071 | 7245 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 959 | 25.096 | 7245 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 970 | 26.120 | 7245 | python3 | openat | `/etc/localtime` |
| 1125 | 32.146 | 7245 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1131 | 32.395 | 7245 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1140 | 32.666 | 7245 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1171 | 34.033 | 7245 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1179 | 34.246 | 7245 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1187 | 34.440 | 7245 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1435 | 44.101 | 7245 | python3 | openat | `/tmp/ft_scenario03` |
| 2370 | 94.356 | 7245 | python3 | openat | `/etc/gai.conf` |
| 2380 | 94.544 | 7245 | python3 | sendto | `socket:[44647]` |
| 2384 | 94.631 | 7245 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2388 | 94.771 | 7245 | python3 | connect | `ipv6:[...]` |
| 2390 | 94.816 | 7245 | python3 | connect | `sockfd=3` |
| 2391 | 94.838 | 7245 | python3 | connect | `0.0.0.0:8766` |
| 2431 | 96.559 | 7245 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2435 | 96.707 | 7245 | python3 | openat | `/etc/nsswitch.conf` |
| 2442 | 96.947 | 7245 | python3 | openat | `/etc/host.conf` |
| 2448 | 97.086 | 7245 | python3 | openat | `/etc/resolv.conf` |
| 2454 | 97.226 | 7245 | python3 | openat | `/etc/hosts` |
| 2462 | 97.403 | 7245 | python3 | openat | `/etc/hosts` |
| 2472 | 522.947 | 7246 | sleep | exit_group | `code=0` |
| 2508 | 523.898 | 7242 | bash | clone | `` |
| 2525 | 524.331 | 7247 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 2528 | 524.443 | 7247 | bash | execve | `/usr/bin/curl` |
| 2844 | 533.947 | 7247 | curl | openat | `/etc/gnutls/config` |
| 2891 | 535.453 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 2893 | 535.494 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 2902 | 535.694 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 2904 | 535.746 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 2908 | 535.847 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 2910 | 535.890 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 2914 | 536.010 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 2916 | 536.059 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 2920 | 536.170 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 2922 | 536.227 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 2926 | 536.341 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 2928 | 536.387 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 2932 | 536.488 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 2934 | 536.521 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 2937 | 536.573 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 2941 | 536.650 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 2943 | 536.690 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 2947 | 536.768 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 2949 | 536.802 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 2953 | 536.884 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 2955 | 536.919 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 2959 | 536.993 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 2961 | 537.026 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 2965 | 537.165 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 2967 | 537.201 | 7247 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 2971 | 537.287 | 7247 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 2972 | 537.307 | 7247 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 2975 | 537.373 | 7247 | curl | connect | `unix:/var/run/nscd/socket` |
| 2978 | 537.437 | 7247 | curl | connect | `unix:/var/run/nscd/socket` |
| 2982 | 537.507 | 7247 | curl | openat | `/etc/nsswitch.conf` |
| 2988 | 537.621 | 7247 | curl | openat | `/etc/passwd` |
| 2993 | 537.717 | 7247 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3018 | 538.201 | 7247 | curl | connect | `127.0.0.1:8766` |
| 3022 | 538.332 | 7245 | python3 | accept4 | `sockfd=3` |
| 3034 | 538.537 | 7247 | curl | sendto | `socket:[44655]` |
| 3042 | 538.669 | 7245 | python3 | clone3 | `` |
| 3058 | 539.035 | 7248 | python3 | recvfrom | `socket:[45340]` |
| 3068 | 539.390 | 7248 | python3 | openat | `/etc/mime.types` |
| 3094 | 541.610 | 7248 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 3100 | 541.811 | 7248 | python3 | sendto | `socket:[45340]` |
| 3106 | 541.952 | 7248 | python3 | sendto | `socket:[45340]` |
| 3107 | 541.960 | 7247 | curl | recvfrom | `socket:[44655]` |
| 3116 | 542.122 | 7247 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 3122 | 542.219 | 7248 | python3 | exit | `code=0` |
| 3135 | 542.624 | 7247 | curl | exit_group | `code=0` |
| 3171 | 543.820 | 7242 | bash | clone | `` |
| 3188 | 544.270 | 7249 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 3197 | 544.537 | 7249 | bash | execve | `/usr/bin/cat` |
| 3234 | 545.588 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3236 | 545.624 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3245 | 545.798 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3247 | 545.831 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3251 | 545.908 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3253 | 545.941 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3257 | 546.014 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3259 | 546.048 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3263 | 546.120 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3265 | 546.154 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3269 | 546.226 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3271 | 546.261 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3275 | 546.343 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3277 | 546.376 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3280 | 546.427 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3284 | 546.502 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3286 | 546.536 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3290 | 546.609 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3292 | 546.644 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3296 | 546.728 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3298 | 546.763 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3302 | 546.845 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3304 | 546.891 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3308 | 546.976 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3310 | 547.015 | 7249 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3319 | 547.179 | 7249 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 3325 | 547.306 | 7249 | cat | exit_group | `code=0` |
| 3361 | 547.990 | 7242 | bash | clone | `` |
| 3378 | 548.366 | 7250 | bash | execve | `/usr/bin/chmod` |
| 3415 | 549.681 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3417 | 549.743 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3426 | 550.047 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3428 | 550.097 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3432 | 550.229 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3434 | 550.288 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3438 | 550.554 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3440 | 550.762 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3444 | 550.873 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3446 | 550.961 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3450 | 551.073 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3452 | 551.117 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3456 | 551.408 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3458 | 551.504 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3461 | 551.578 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3465 | 551.683 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3467 | 551.933 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3471 | 552.039 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3473 | 552.078 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3477 | 552.181 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3479 | 552.221 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3483 | 552.320 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3485 | 552.359 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3489 | 552.452 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3491 | 552.494 | 7250 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3497 | 552.634 | 7250 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 3500 | 552.744 | 7250 | chmod | exit_group | `code=0` |
| 3510 | 553.184 | 7242 | bash | clone | `` |
| 3527 | 553.807 | 7251 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 3567 | 555.309 | 7251 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 3582 | 555.679 | 7251 | runme.sh | exit_group | `code=0` |
| 3630 | 558.073 | 7242 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 57.950 ms |
| Workload CPU (user+sys) | 76.506 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 4.327 ms |
| Evidence size | 1224173 bytes |

