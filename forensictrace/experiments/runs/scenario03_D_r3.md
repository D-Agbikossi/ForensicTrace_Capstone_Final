# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | D |
| Events recorded | 3630 |
| Failed exec attempts removed | 12 |
| Duration | 566.325 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_D_r3.json` (1224169 bytes) |
| SHA-256 | `40081dcc23490cc47f08791f14d3a93b2a48e6f664e727cdb1f34afd884bb35c` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_D_r3.json.sha256`

## 1. Process tree

- `7640` /usr/bin/bash
  - `7641` /usr/bin/rm
  - `7642` /usr/bin/mkdir
  - `7643` /usr/bin/python3
  - `7644` /usr/bin/sleep
  - `7645` /usr/bin/curl
  - `7646` /usr/bin/python3
  - `7647` /usr/bin/cat
  - `7648` /usr/bin/chmod
  - `7649` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7640 (?) executed `/usr/bin/bash`
- +8.219 ms pid 7641 (bash) executed `/usr/bin/rm`
- +12.100 ms pid 7642 (bash) executed `/usr/bin/mkdir`
- +18.007 ms pid 7643 (bash) executed `/usr/bin/python3`
- +18.016 ms pid 7644 (bash) executed `/usr/bin/sleep`
- +527.582 ms pid 7645 (bash) executed `/usr/bin/curl`
- +552.288 ms pid 7647 (bash) executed `/usr/bin/cat`
- +558.263 ms pid 7648 (bash) executed `/usr/bin/chmod`
- +562.360 ms pid 7649 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +89.833 ms pid 7643 (python3) connected to `unix:/var/run/nscd/socket`
- +89.948 ms pid 7643 (python3) connected to `ipv6:[...]`
- +90.003 ms pid 7643 (python3) connected to `sockfd=3`
- +90.024 ms pid 7643 (python3) connected to `0.0.0.0:8766`
- +91.882 ms pid 7643 (python3) connected to `unix:/var/run/nscd/socket`
- +545.027 ms pid 7645 (curl) connected to `unix:/var/run/nscd/socket`
- +545.091 ms pid 7645 (curl) connected to `unix:/var/run/nscd/socket`
- +545.871 ms pid 7645 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +16.213 ms by pid 7640 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +527.051 ms by pid 7645 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +551.879 ms by pid 7647 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +561.591 ms pid 7648 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +10.878 ms pid 7641 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +10.925 ms pid 7641 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +10.951 ms pid 7641 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +10.994 ms pid 7641 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +545.278 ms pid 7645 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +562.360 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7649 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +10.925 ms #386 `unlinkat` by pid 7641 (rm)
    - +551.879 ms #3188 `openat` by pid 7647 (bash)
    - +552.029 ms #3190 `close` by pid 7647 (bash)
    - +555.807 ms #3319 `write` by pid 7647 (cat)
    - +555.917 ms #3323 `close` by pid 7647 (cat)
    - +561.591 ms #3497 `fchmodat` by pid 7648 (chmod)
    - +562.360 ms #3527 `execve` by pid 7649 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7640 | ? | execve | `/usr/bin/bash` |
| 49 | 2.408 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 2.474 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 2.794 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 2.856 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 3.001 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 3.062 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 3.201 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 3.265 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 3.403 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 3.467 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 3.604 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 3.676 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 3.825 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 3.881 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 3.967 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 4.098 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 4.155 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 4.282 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 4.340 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 4.476 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 4.534 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 4.667 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 4.730 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 4.860 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 4.917 | 7640 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 6.946 | 7640 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 239 | 7.867 | 7640 | bash | clone | `` |
| 256 | 8.219 | 7641 | bash | execve | `/usr/bin/rm` |
| 293 | 9.199 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 9.236 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 9.395 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 9.430 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 9.504 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 9.539 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 9.612 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 9.650 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 9.726 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 9.759 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 9.831 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 9.865 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 9.948 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 9.983 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 10.033 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 10.108 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 10.143 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 10.219 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 10.252 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 10.335 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 10.368 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 10.441 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 10.476 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 10.551 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 10.585 | 7641 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 10.718 | 7641 | rm | openat | `/tmp/ft_scenario03` |
| 385 | 10.878 | 7641 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 386 | 10.925 | 7641 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 387 | 10.951 | 7641 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 389 | 10.994 | 7641 | rm | unlinkat | `/tmp/ft_scenario03` |
| 394 | 11.131 | 7641 | rm | exit_group | `code=0` |
| 428 | 11.760 | 7640 | bash | clone | `` |
| 445 | 12.100 | 7642 | bash | execve | `/usr/bin/mkdir` |
| 509 | 13.893 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 511 | 13.936 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 520 | 14.132 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 522 | 14.174 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 526 | 14.263 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 528 | 14.305 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 532 | 14.397 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 534 | 14.437 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 538 | 14.529 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 540 | 14.569 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 544 | 14.663 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 546 | 14.706 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 550 | 14.807 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 552 | 14.849 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 555 | 14.910 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 559 | 14.998 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 561 | 15.039 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 565 | 15.129 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 567 | 15.171 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 571 | 15.268 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 573 | 15.308 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 577 | 15.397 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 579 | 15.440 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 583 | 15.533 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 585 | 15.574 | 7642 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 596 | 15.899 | 7642 | mkdir | exit_group | `code=0` |
| 606 | 16.213 | 7640 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 614 | 16.400 | 7640 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 621 | 16.566 | 7640 | bash | clone | `` |
| 695 | 17.614 | 7640 | bash | clone | `` |
| 724 | 18.007 | 7643 | bash | execve | `/usr/bin/python3` |
| 725 | 18.016 | 7644 | bash | execve | `/usr/bin/sleep` |
| 793 | 19.223 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 797 | 19.277 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 815 | 19.515 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 818 | 19.561 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 825 | 19.659 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 828 | 19.703 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 834 | 19.805 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 837 | 19.848 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 844 | 19.948 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 847 | 19.993 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 852 | 20.086 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 856 | 20.138 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 863 | 20.246 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 866 | 20.296 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 871 | 20.365 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 872 | 20.377 | 7643 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 876 | 20.432 | 7643 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 879 | 20.472 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 883 | 20.522 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 890 | 20.622 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 894 | 20.678 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 899 | 20.777 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 901 | 20.825 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 907 | 20.922 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 910 | 20.967 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 915 | 21.060 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 917 | 21.109 | 7644 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 953 | 25.907 | 7643 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 954 | 25.958 | 7643 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 957 | 26.057 | 7643 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 958 | 26.084 | 7643 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 959 | 26.109 | 7643 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 970 | 27.685 | 7643 | python3 | openat | `/etc/localtime` |
| 1125 | 33.752 | 7643 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1131 | 33.898 | 7643 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1140 | 34.113 | 7643 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1171 | 35.183 | 7643 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1179 | 35.349 | 7643 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1187 | 35.498 | 7643 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1435 | 44.056 | 7643 | python3 | openat | `/tmp/ft_scenario03` |
| 2370 | 89.434 | 7643 | python3 | openat | `/etc/gai.conf` |
| 2380 | 89.680 | 7643 | python3 | sendto | `socket:[47663]` |
| 2384 | 89.833 | 7643 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2388 | 89.948 | 7643 | python3 | connect | `ipv6:[...]` |
| 2390 | 90.003 | 7643 | python3 | connect | `sockfd=3` |
| 2391 | 90.024 | 7643 | python3 | connect | `0.0.0.0:8766` |
| 2431 | 91.882 | 7643 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2435 | 91.988 | 7643 | python3 | openat | `/etc/nsswitch.conf` |
| 2442 | 92.166 | 7643 | python3 | openat | `/etc/host.conf` |
| 2448 | 92.336 | 7643 | python3 | openat | `/etc/resolv.conf` |
| 2454 | 92.601 | 7643 | python3 | openat | `/etc/hosts` |
| 2462 | 92.751 | 7643 | python3 | openat | `/etc/hosts` |
| 2472 | 522.241 | 7644 | sleep | exit_group | `code=0` |
| 2508 | 525.359 | 7640 | bash | clone | `` |
| 2520 | 527.051 | 7645 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 2525 | 527.582 | 7645 | bash | execve | `/usr/bin/curl` |
| 2844 | 540.143 | 7645 | curl | openat | `/etc/gnutls/config` |
| 2891 | 542.397 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 2893 | 542.447 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 2902 | 542.673 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 2904 | 542.717 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 2908 | 542.816 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 2910 | 542.863 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 2914 | 542.961 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 2916 | 543.011 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 2920 | 543.106 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 2922 | 543.151 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 2926 | 543.277 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 2928 | 543.322 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 2932 | 543.446 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 2934 | 543.491 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 2937 | 543.565 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 2941 | 543.676 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 2943 | 543.723 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 2947 | 544.359 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 2949 | 544.445 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 2953 | 544.588 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 2955 | 544.625 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 2959 | 544.714 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 2961 | 544.747 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 2965 | 544.823 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 2967 | 544.856 | 7645 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 2971 | 544.939 | 7645 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 2972 | 544.960 | 7645 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 2975 | 545.027 | 7645 | curl | connect | `unix:/var/run/nscd/socket` |
| 2978 | 545.091 | 7645 | curl | connect | `unix:/var/run/nscd/socket` |
| 2982 | 545.162 | 7645 | curl | openat | `/etc/nsswitch.conf` |
| 2988 | 545.278 | 7645 | curl | openat | `/etc/passwd` |
| 2993 | 545.367 | 7645 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3018 | 545.871 | 7645 | curl | connect | `127.0.0.1:8766` |
| 3022 | 546.004 | 7643 | python3 | accept4 | `sockfd=3` |
| 3034 | 546.202 | 7645 | curl | sendto | `socket:[47672]` |
| 3042 | 546.315 | 7643 | python3 | clone3 | `` |
| 3058 | 546.686 | 7646 | python3 | recvfrom | `socket:[45906]` |
| 3069 | 547.071 | 7646 | python3 | openat | `/etc/mime.types` |
| 3094 | 549.313 | 7646 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 3100 | 549.500 | 7646 | python3 | sendto | `socket:[45906]` |
| 3106 | 549.614 | 7646 | python3 | sendto | `socket:[45906]` |
| 3107 | 549.634 | 7645 | curl | recvfrom | `socket:[47672]` |
| 3118 | 549.836 | 7645 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 3120 | 549.875 | 7646 | python3 | exit | `code=0` |
| 3135 | 550.371 | 7645 | curl | exit_group | `code=0` |
| 3171 | 551.456 | 7640 | bash | clone | `` |
| 3188 | 551.879 | 7647 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 3197 | 552.288 | 7647 | bash | execve | `/usr/bin/cat` |
| 3234 | 553.785 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3236 | 553.833 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3245 | 554.051 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3247 | 554.094 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3251 | 554.193 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3253 | 554.236 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3257 | 554.332 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3259 | 554.377 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3263 | 554.472 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3265 | 554.517 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3269 | 554.610 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3271 | 554.660 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3275 | 554.768 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3277 | 554.811 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3280 | 554.876 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3284 | 554.975 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3286 | 555.018 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3290 | 555.118 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3292 | 555.164 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3296 | 555.268 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3298 | 555.314 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3302 | 555.409 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3304 | 555.454 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3308 | 555.550 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3310 | 555.593 | 7647 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3319 | 555.807 | 7647 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 3325 | 555.968 | 7647 | cat | exit_group | `code=0` |
| 3361 | 557.757 | 7640 | bash | clone | `` |
| 3378 | 558.263 | 7648 | bash | execve | `/usr/bin/chmod` |
| 3415 | 559.691 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3417 | 559.746 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3426 | 559.972 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3428 | 560.021 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3432 | 560.127 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3434 | 560.176 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3438 | 560.279 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3440 | 560.326 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3444 | 560.462 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3446 | 560.505 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3450 | 560.606 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3452 | 560.654 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3456 | 560.787 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3458 | 560.834 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3461 | 560.905 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3465 | 560.994 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3467 | 561.030 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3471 | 561.108 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3473 | 561.141 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3477 | 561.224 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3479 | 561.258 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3483 | 561.332 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3485 | 561.369 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3489 | 561.445 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3491 | 561.479 | 7648 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3497 | 561.591 | 7648 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 3500 | 561.702 | 7648 | chmod | exit_group | `code=0` |
| 3510 | 562.000 | 7640 | bash | clone | `` |
| 3527 | 562.360 | 7649 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 3567 | 563.400 | 7649 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 3582 | 563.659 | 7649 | runme.sh | exit_group | `code=0` |
| 3630 | 565.502 | 7640 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 59.558 ms |
| Workload CPU (user+sys) | 76.375 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 3.913 ms |
| Evidence size | 1224169 bytes |

