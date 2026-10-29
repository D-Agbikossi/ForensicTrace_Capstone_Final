# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | D |
| Events recorded | 3630 |
| Failed exec attempts removed | 12 |
| Duration | 573.882 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_D_r1.json` (1224183 bytes) |
| SHA-256 | `5a9cc295df807647f18ad5cc7505758f852afdb10bc04f7b8fe3b6b161fef6fb` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_D_r1.json.sha256`

## 1. Process tree

- `8020` /usr/bin/bash
  - `8021` /usr/bin/rm
  - `8023` /usr/bin/mkdir
  - `8024` /usr/bin/python3
  - `8025` /usr/bin/sleep
  - `8028` /usr/bin/curl
  - `8029` /usr/bin/python3
  - `8030` /usr/bin/cat
  - `8031` /usr/bin/chmod
  - `8032` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8020 (?) executed `/usr/bin/bash`
- +7.087 ms pid 8021 (bash) executed `/usr/bin/rm`
- +20.074 ms pid 8023 (bash) executed `/usr/bin/mkdir`
- +31.136 ms pid 8025 (bash) executed `/usr/bin/sleep`
- +36.159 ms pid 8024 (bash) executed `/usr/bin/python3`
- +539.029 ms pid 8028 (bash) executed `/usr/bin/curl`
- +559.095 ms pid 8030 (bash) executed `/usr/bin/cat`
- +564.381 ms pid 8031 (bash) executed `/usr/bin/chmod`
- +569.526 ms pid 8032 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +119.761 ms pid 8024 (python3) connected to `unix:/var/run/nscd/socket`
- +119.848 ms pid 8024 (python3) connected to `ipv6:[...]`
- +119.891 ms pid 8024 (python3) connected to `sockfd=3`
- +119.908 ms pid 8024 (python3) connected to `0.0.0.0:8766`
- +121.822 ms pid 8024 (python3) connected to `unix:/var/run/nscd/socket`
- +552.161 ms pid 8028 (curl) connected to `unix:/var/run/nscd/socket`
- +552.229 ms pid 8028 (curl) connected to `unix:/var/run/nscd/socket`
- +552.987 ms pid 8028 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +27.075 ms by pid 8020 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +538.916 ms by pid 8028 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +558.869 ms by pid 8030 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +568.081 ms pid 8031 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +17.908 ms pid 8021 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +17.971 ms pid 8021 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +18.004 ms pid 8021 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +18.061 ms pid 8021 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +552.413 ms pid 8028 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +569.526 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8032 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +17.971 ms #386 `unlinkat` by pid 8021 (rm)
    - +558.869 ms #3188 `openat` by pid 8030 (bash)
    - +558.948 ms #3190 `close` by pid 8030 (bash)
    - +562.711 ms #3319 `write` by pid 8030 (cat)
    - +562.832 ms #3323 `close` by pid 8030 (cat)
    - +568.081 ms #3497 `fchmodat` by pid 8031 (chmod)
    - +569.526 ms #3527 `execve` by pid 8032 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8020 | ? | execve | `/usr/bin/bash` |
| 49 | 1.318 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.354 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.522 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.554 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.634 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.667 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 1.741 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 1.775 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 1.850 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 1.885 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 1.963 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 1.998 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.082 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.115 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.166 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.253 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.298 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.372 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.406 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.491 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.525 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 2.599 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 2.633 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 2.709 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 2.742 | 8020 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 4.304 | 8020 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 239 | 6.438 | 8020 | bash | clone | `` |
| 256 | 7.087 | 8021 | bash | execve | `/usr/bin/rm` |
| 293 | 11.648 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 11.713 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 12.019 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 12.073 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 12.251 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 12.339 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 12.508 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 12.568 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 12.698 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 12.753 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 12.868 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 12.922 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 13.059 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 13.113 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 13.192 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 16.312 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 16.368 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 16.928 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 16.980 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 17.094 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 17.139 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 17.253 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 17.302 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 17.447 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 17.500 | 8021 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 17.691 | 8021 | rm | openat | `/tmp/ft_scenario03` |
| 385 | 17.908 | 8021 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 386 | 17.971 | 8021 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 387 | 18.004 | 8021 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 389 | 18.061 | 8021 | rm | unlinkat | `/tmp/ft_scenario03` |
| 394 | 18.235 | 8021 | rm | exit_group | `code=0` |
| 428 | 19.189 | 8020 | bash | clone | `` |
| 445 | 20.074 | 8023 | bash | execve | `/usr/bin/mkdir` |
| 509 | 23.250 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 511 | 23.310 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 520 | 23.586 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 522 | 23.642 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 526 | 23.770 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 528 | 23.827 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 532 | 23.950 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 534 | 24.004 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 538 | 24.132 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 540 | 24.187 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 544 | 24.330 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 546 | 24.389 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 550 | 24.531 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 552 | 24.590 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 555 | 24.673 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 559 | 24.803 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 561 | 24.862 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 565 | 24.990 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 567 | 25.047 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 571 | 25.186 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 573 | 25.246 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 577 | 25.379 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 579 | 25.440 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 583 | 25.573 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 585 | 25.633 | 8023 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 596 | 26.182 | 8023 | mkdir | exit_group | `code=0` |
| 606 | 27.075 | 8020 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 614 | 27.341 | 8020 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 621 | 27.548 | 8020 | bash | clone | `` |
| 670 | 30.602 | 8020 | bash | clone | `` |
| 687 | 31.136 | 8025 | bash | execve | `/usr/bin/sleep` |
| 731 | 32.649 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 733 | 32.696 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 742 | 32.930 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 744 | 32.978 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 748 | 33.134 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 751 | 33.215 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 760 | 33.914 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 763 | 34.092 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 771 | 34.657 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 775 | 34.753 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 782 | 34.893 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 785 | 34.953 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 791 | 35.092 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 795 | 35.155 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 799 | 35.603 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 803 | 35.800 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 807 | 35.899 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 814 | 36.031 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 818 | 36.098 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 822 | 36.159 | 8024 | bash | execve | `/usr/bin/python3` |
| 824 | 36.231 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 826 | 36.278 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 830 | 36.392 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 832 | 36.446 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 836 | 36.575 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 839 | 36.632 | 8025 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 921 | 38.920 | 8024 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 923 | 38.956 | 8024 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 953 | 41.824 | 8024 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 954 | 41.852 | 8024 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 957 | 41.918 | 8024 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 958 | 41.938 | 8024 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 959 | 41.957 | 8024 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 970 | 42.939 | 8024 | python3 | openat | `/etc/localtime` |
| 1125 | 49.191 | 8024 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1131 | 49.521 | 8024 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1140 | 49.822 | 8024 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1171 | 51.821 | 8024 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1179 | 51.990 | 8024 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1187 | 52.153 | 8024 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1435 | 65.567 | 8024 | python3 | openat | `/tmp/ft_scenario03` |
| 2370 | 119.479 | 8024 | python3 | openat | `/etc/gai.conf` |
| 2380 | 119.674 | 8024 | python3 | sendto | `socket:[50565]` |
| 2384 | 119.761 | 8024 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2388 | 119.848 | 8024 | python3 | connect | `ipv6:[...]` |
| 2390 | 119.891 | 8024 | python3 | connect | `sockfd=3` |
| 2391 | 119.908 | 8024 | python3 | connect | `0.0.0.0:8766` |
| 2432 | 121.822 | 8024 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2436 | 121.903 | 8024 | python3 | openat | `/etc/nsswitch.conf` |
| 2443 | 122.034 | 8024 | python3 | openat | `/etc/host.conf` |
| 2449 | 122.132 | 8024 | python3 | openat | `/etc/resolv.conf` |
| 2455 | 122.247 | 8024 | python3 | openat | `/etc/hosts` |
| 2463 | 122.387 | 8024 | python3 | openat | `/etc/hosts` |
| 2473 | 537.635 | 8025 | sleep | exit_group | `code=0` |
| 2509 | 538.492 | 8020 | bash | clone | `` |
| 2526 | 538.916 | 8028 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 2529 | 539.029 | 8028 | bash | execve | `/usr/bin/curl` |
| 2845 | 549.169 | 8028 | curl | openat | `/etc/gnutls/config` |
| 2892 | 550.595 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 2894 | 550.631 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 2903 | 550.801 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 2905 | 550.835 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 2909 | 550.911 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 2911 | 550.943 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 2915 | 551.019 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 2917 | 551.051 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 2921 | 551.123 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 2923 | 551.158 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 2927 | 551.238 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 2929 | 551.273 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 2933 | 551.356 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 2935 | 551.390 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 2938 | 551.440 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 2942 | 551.521 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 2944 | 551.554 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 2948 | 551.630 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 2950 | 551.662 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 2954 | 551.744 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 2956 | 551.779 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 2960 | 551.853 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 2962 | 551.887 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 2966 | 551.961 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 2968 | 551.995 | 8028 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 2972 | 552.075 | 8028 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 2973 | 552.095 | 8028 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 2976 | 552.161 | 8028 | curl | connect | `unix:/var/run/nscd/socket` |
| 2979 | 552.229 | 8028 | curl | connect | `unix:/var/run/nscd/socket` |
| 2983 | 552.299 | 8028 | curl | openat | `/etc/nsswitch.conf` |
| 2989 | 552.413 | 8028 | curl | openat | `/etc/passwd` |
| 2994 | 552.500 | 8028 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3019 | 552.987 | 8028 | curl | connect | `127.0.0.1:8766` |
| 3022 | 553.114 | 8024 | python3 | accept4 | `sockfd=3` |
| 3038 | 553.377 | 8028 | curl | sendto | `socket:[49623]` |
| 3040 | 553.425 | 8024 | python3 | clone3 | `` |
| 3059 | 553.804 | 8029 | python3 | recvfrom | `socket:[50576]` |
| 3069 | 554.163 | 8029 | python3 | openat | `/etc/mime.types` |
| 3094 | 556.346 | 8029 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 3100 | 556.532 | 8029 | python3 | sendto | `socket:[50576]` |
| 3106 | 556.641 | 8029 | python3 | sendto | `socket:[50576]` |
| 3107 | 556.658 | 8028 | curl | recvfrom | `socket:[49623]` |
| 3118 | 556.846 | 8028 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 3120 | 556.883 | 8029 | python3 | exit | `code=0` |
| 3135 | 557.370 | 8028 | curl | exit_group | `code=0` |
| 3171 | 558.448 | 8020 | bash | clone | `` |
| 3188 | 558.869 | 8030 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 3197 | 559.095 | 8030 | bash | execve | `/usr/bin/cat` |
| 3234 | 560.337 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3236 | 560.379 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3245 | 560.578 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3247 | 560.618 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3251 | 560.714 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3253 | 560.754 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3257 | 560.847 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3259 | 560.889 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3263 | 560.978 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3265 | 561.020 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3269 | 561.108 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3271 | 561.150 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3275 | 561.258 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3277 | 561.299 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3280 | 561.359 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3284 | 561.450 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3286 | 561.491 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3290 | 561.582 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3292 | 561.624 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3296 | 561.728 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3298 | 561.873 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3302 | 562.012 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3304 | 562.071 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3308 | 562.250 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3310 | 562.469 | 8030 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3319 | 562.711 | 8030 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 3325 | 562.897 | 8030 | cat | exit_group | `code=0` |
| 3361 | 563.898 | 8020 | bash | clone | `` |
| 3378 | 564.381 | 8031 | bash | execve | `/usr/bin/chmod` |
| 3415 | 565.837 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3417 | 565.893 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3426 | 566.127 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3428 | 566.177 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3432 | 566.290 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3434 | 566.339 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3438 | 566.441 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3440 | 566.489 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3444 | 566.595 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3446 | 566.642 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3450 | 566.745 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3452 | 566.793 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3456 | 566.906 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3458 | 566.954 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3461 | 567.028 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3465 | 567.130 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3467 | 567.179 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3471 | 567.288 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3473 | 567.336 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3477 | 567.448 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3479 | 567.491 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3483 | 567.587 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3485 | 567.727 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3489 | 567.889 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3491 | 567.935 | 8031 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3497 | 568.081 | 8031 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 3500 | 568.183 | 8031 | chmod | exit_group | `code=0` |
| 3510 | 568.762 | 8020 | bash | clone | `` |
| 3527 | 569.526 | 8032 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 3567 | 570.840 | 8032 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 3582 | 571.144 | 8032 | runme.sh | exit_group | `code=0` |
| 3630 | 573.238 | 8020 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 60.913 ms |
| Workload CPU (user+sys) | 82.746 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 3.903 ms |
| Evidence size | 1224183 bytes |

