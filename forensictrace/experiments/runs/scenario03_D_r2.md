# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | D |
| Events recorded | 3632 |
| Failed exec attempts removed | 12 |
| Duration | 590.858 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_D_r2.json` (1224875 bytes) |
| SHA-256 | `59d02766c3f7cea4be5998d0cf10a21c480e8c1a7d2d59eb36f1ebf414c2e772` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_D_r2.json.sha256`

## 1. Process tree

- `7458` /usr/bin/bash
  - `7459` /usr/bin/rm
  - `7460` /usr/bin/mkdir
  - `7461` /usr/bin/python3
  - `7462` /usr/bin/sleep
  - `7464` /usr/bin/curl
  - `7465` /usr/bin/python3
  - `7466` /usr/bin/cat
  - `7467` /usr/bin/chmod
  - `7468` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7458 (?) executed `/usr/bin/bash`
- +11.703 ms pid 7459 (bash) executed `/usr/bin/rm`
- +21.054 ms pid 7460 (bash) executed `/usr/bin/mkdir`
- +30.285 ms pid 7461 (bash) executed `/usr/bin/python3`
- +30.422 ms pid 7462 (bash) executed `/usr/bin/sleep`
- +537.386 ms pid 7464 (bash) executed `/usr/bin/curl`
- +575.171 ms pid 7466 (bash) executed `/usr/bin/cat`
- +579.830 ms pid 7467 (bash) executed `/usr/bin/chmod`
- +584.025 ms pid 7468 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +113.978 ms pid 7461 (python3) connected to `unix:/var/run/nscd/socket`
- +114.091 ms pid 7461 (python3) connected to `ipv6:[...]`
- +114.150 ms pid 7461 (python3) connected to `sockfd=3`
- +114.172 ms pid 7461 (python3) connected to `0.0.0.0:8766`
- +116.974 ms pid 7461 (python3) connected to `unix:/var/run/nscd/socket`
- +563.120 ms pid 7464 (curl) connected to `unix:/var/run/nscd/socket`
- +563.204 ms pid 7464 (curl) connected to `unix:/var/run/nscd/socket`
- +564.329 ms pid 7464 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +26.900 ms by pid 7458 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +537.278 ms by pid 7464 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +574.932 ms by pid 7466 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +582.641 ms pid 7467 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +17.956 ms pid 7459 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +18.050 ms pid 7459 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +18.110 ms pid 7459 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +18.213 ms pid 7459 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +563.449 ms pid 7464 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +584.025 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7468 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +18.050 ms #386 `unlinkat` by pid 7459 (rm)
    - +574.932 ms #3190 `openat` by pid 7466 (bash)
    - +575.024 ms #3192 `close` by pid 7466 (bash)
    - +578.503 ms #3321 `write` by pid 7466 (cat)
    - +578.615 ms #3325 `close` by pid 7466 (cat)
    - +582.641 ms #3499 `fchmodat` by pid 7467 (chmod)
    - +584.025 ms #3529 `execve` by pid 7468 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7458 | ? | execve | `/usr/bin/bash` |
| 49 | 2.393 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 2.454 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 2.769 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 2.824 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 2.957 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 3.013 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 3.140 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 3.197 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 3.319 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 3.373 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 3.496 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 3.651 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 3.877 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 3.930 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 4.014 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 4.137 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 4.193 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 4.312 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 4.366 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 4.503 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 4.561 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 4.688 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 4.743 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 4.880 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 4.935 | 7458 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 6.828 | 7458 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 239 | 7.947 | 7458 | bash | clone | `` |
| 256 | 11.703 | 7459 | bash | execve | `/usr/bin/rm` |
| 293 | 13.609 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 13.704 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 13.973 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 14.022 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 14.143 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 14.203 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 14.325 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 14.375 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 14.568 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 14.616 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 14.734 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 14.796 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 14.916 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 14.973 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 15.044 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 15.155 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 15.209 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 15.423 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 15.473 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 15.598 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 15.693 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 15.822 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 15.876 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 16.010 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 16.059 | 7459 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 16.974 | 7459 | rm | openat | `/tmp/ft_scenario03` |
| 385 | 17.956 | 7459 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 386 | 18.050 | 7459 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 387 | 18.110 | 7459 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 389 | 18.213 | 7459 | rm | unlinkat | `/tmp/ft_scenario03` |
| 394 | 18.423 | 7459 | rm | exit_group | `code=0` |
| 428 | 19.542 | 7458 | bash | clone | `` |
| 445 | 21.054 | 7460 | bash | execve | `/usr/bin/mkdir` |
| 509 | 23.704 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 511 | 23.765 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 520 | 24.027 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 522 | 24.086 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 526 | 24.208 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 528 | 24.261 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 532 | 24.387 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 534 | 24.440 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 538 | 24.566 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 540 | 24.617 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 544 | 24.765 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 546 | 24.819 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 550 | 24.950 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 552 | 25.003 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 555 | 25.081 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 559 | 25.199 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 561 | 25.252 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 565 | 25.370 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 567 | 25.423 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 571 | 25.549 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 573 | 25.600 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 577 | 25.722 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 579 | 25.777 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 583 | 25.885 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 585 | 25.934 | 7460 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 596 | 26.312 | 7460 | mkdir | exit_group | `code=0` |
| 606 | 26.900 | 7458 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 614 | 27.223 | 7458 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 621 | 27.435 | 7458 | bash | clone | `` |
| 701 | 29.880 | 7458 | bash | clone | `` |
| 719 | 30.285 | 7461 | bash | execve | `/usr/bin/python3` |
| 725 | 30.422 | 7462 | bash | execve | `/usr/bin/sleep` |
| 797 | 32.297 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 801 | 32.356 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 817 | 32.767 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 821 | 32.826 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 828 | 32.963 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 831 | 33.050 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 838 | 33.195 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 841 | 33.261 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 847 | 33.383 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 851 | 33.436 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 858 | 33.569 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 861 | 33.617 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 865 | 33.690 | 7461 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 868 | 33.775 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 869 | 33.784 | 7461 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 872 | 33.830 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 877 | 33.909 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 885 | 34.147 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 888 | 34.226 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 893 | 34.348 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 896 | 34.435 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 903 | 34.566 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 905 | 34.731 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 909 | 34.848 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 911 | 34.885 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 915 | 34.988 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 917 | 35.027 | 7462 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 953 | 37.528 | 7461 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 954 | 37.564 | 7461 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 957 | 37.641 | 7461 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 958 | 37.668 | 7461 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 959 | 37.716 | 7461 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 970 | 38.820 | 7461 | python3 | openat | `/etc/localtime` |
| 1125 | 45.313 | 7461 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1131 | 45.482 | 7461 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1140 | 45.749 | 7461 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1171 | 47.229 | 7461 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1179 | 47.425 | 7461 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1187 | 47.606 | 7461 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1435 | 59.736 | 7461 | python3 | openat | `/tmp/ft_scenario03` |
| 2370 | 113.582 | 7461 | python3 | openat | `/etc/gai.conf` |
| 2380 | 113.850 | 7461 | python3 | sendto | `socket:[46757]` |
| 2384 | 113.978 | 7461 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2388 | 114.091 | 7461 | python3 | connect | `ipv6:[...]` |
| 2390 | 114.150 | 7461 | python3 | connect | `sockfd=3` |
| 2391 | 114.172 | 7461 | python3 | connect | `0.0.0.0:8766` |
| 2432 | 116.974 | 7461 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2436 | 117.083 | 7461 | python3 | openat | `/etc/nsswitch.conf` |
| 2443 | 117.248 | 7461 | python3 | openat | `/etc/host.conf` |
| 2449 | 117.371 | 7461 | python3 | openat | `/etc/resolv.conf` |
| 2455 | 117.507 | 7461 | python3 | openat | `/etc/hosts` |
| 2463 | 117.686 | 7461 | python3 | openat | `/etc/hosts` |
| 2473 | 535.828 | 7462 | sleep | exit_group | `code=0` |
| 2509 | 536.813 | 7458 | bash | clone | `` |
| 2526 | 537.278 | 7464 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 2529 | 537.386 | 7464 | bash | execve | `/usr/bin/curl` |
| 2845 | 558.399 | 7464 | curl | openat | `/etc/gnutls/config` |
| 2892 | 561.062 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 2894 | 561.110 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 2903 | 561.340 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 2905 | 561.385 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 2909 | 561.488 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 2911 | 561.529 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 2915 | 561.630 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 2917 | 561.670 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 2921 | 561.777 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 2923 | 561.820 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 2927 | 561.920 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 2929 | 561.963 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 2933 | 562.075 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 2935 | 562.115 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 2938 | 562.176 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 2942 | 562.283 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 2944 | 562.323 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 2948 | 562.421 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 2950 | 562.460 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 2954 | 562.567 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 2956 | 562.609 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 2960 | 562.712 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 2962 | 562.754 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 2966 | 562.861 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 2968 | 562.903 | 7464 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 2972 | 563.014 | 7464 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 2973 | 563.037 | 7464 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 2976 | 563.120 | 7464 | curl | connect | `unix:/var/run/nscd/socket` |
| 2979 | 563.204 | 7464 | curl | connect | `unix:/var/run/nscd/socket` |
| 2983 | 563.297 | 7464 | curl | openat | `/etc/nsswitch.conf` |
| 2989 | 563.449 | 7464 | curl | openat | `/etc/passwd` |
| 2994 | 563.562 | 7464 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3019 | 564.329 | 7464 | curl | connect | `127.0.0.1:8766` |
| 3021 | 564.482 | 7461 | python3 | accept4 | `sockfd=3` |
| 3038 | 564.830 | 7464 | curl | sendto | `socket:[45005]` |
| 3040 | 564.880 | 7461 | python3 | clone3 | `` |
| 3061 | 567.913 | 7465 | python3 | recvfrom | `socket:[46762]` |
| 3071 | 568.451 | 7465 | python3 | openat | `/etc/mime.types` |
| 3096 | 570.973 | 7465 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 3102 | 571.374 | 7465 | python3 | sendto | `socket:[46762]` |
| 3108 | 571.563 | 7465 | python3 | sendto | `socket:[46762]` |
| 3109 | 571.571 | 7464 | curl | recvfrom | `socket:[45005]` |
| 3117 | 571.834 | 7464 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 3127 | 572.039 | 7465 | python3 | exit | `code=0` |
| 3137 | 572.889 | 7464 | curl | exit_group | `code=0` |
| 3173 | 574.410 | 7458 | bash | clone | `` |
| 3190 | 574.932 | 7466 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 3199 | 575.171 | 7466 | bash | execve | `/usr/bin/cat` |
| 3236 | 576.538 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3238 | 576.584 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3247 | 576.805 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3249 | 576.848 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3253 | 576.941 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3255 | 576.984 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3259 | 577.076 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3261 | 577.118 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3265 | 577.215 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3267 | 577.256 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3271 | 577.348 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3273 | 577.389 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3277 | 577.492 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3279 | 577.534 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3282 | 577.597 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3286 | 577.707 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3288 | 577.751 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3292 | 577.845 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3294 | 577.888 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3298 | 577.988 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3300 | 578.029 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3304 | 578.121 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3306 | 578.162 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3310 | 578.258 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3312 | 578.301 | 7466 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3321 | 578.503 | 7466 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 3327 | 578.670 | 7466 | cat | exit_group | `code=0` |
| 3363 | 579.461 | 7458 | bash | clone | `` |
| 3380 | 579.830 | 7467 | bash | execve | `/usr/bin/chmod` |
| 3417 | 580.836 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3419 | 580.873 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3428 | 581.041 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3430 | 581.075 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3434 | 581.152 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3436 | 581.186 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3440 | 581.261 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3442 | 581.296 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3446 | 581.400 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3448 | 581.446 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3452 | 581.535 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3454 | 581.577 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3458 | 581.686 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3460 | 581.729 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3463 | 581.788 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3467 | 581.888 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3469 | 581.928 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3473 | 582.030 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3475 | 582.075 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3479 | 582.180 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3481 | 582.222 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3485 | 582.315 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3487 | 582.360 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3491 | 582.452 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3493 | 582.496 | 7467 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3499 | 582.641 | 7467 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 3502 | 582.743 | 7467 | chmod | exit_group | `code=0` |
| 3512 | 583.015 | 7458 | bash | clone | `` |
| 3529 | 584.025 | 7468 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 3569 | 585.996 | 7468 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 3584 | 586.935 | 7468 | runme.sh | exit_group | `code=0` |
| 3632 | 589.627 | 7458 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 66.020 ms |
| Workload CPU (user+sys) | 90.471 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 5.372 ms |
| Evidence size | 1224875 bytes |

