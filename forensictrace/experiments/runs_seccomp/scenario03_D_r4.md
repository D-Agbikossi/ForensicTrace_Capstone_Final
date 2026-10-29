# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | D |
| Events recorded | 3630 |
| Failed exec attempts removed | 12 |
| Duration | 560.849 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_D_r4.json` (1224173 bytes) |
| SHA-256 | `dd4fa040a8ea41ea36b55ef67eb662bdd85c16f28f0b20df4833e7e22ed126d1` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_D_r4.json.sha256`

## 1. Process tree

- `8639` /usr/bin/bash
  - `8640` /usr/bin/rm
  - `8641` /usr/bin/mkdir
  - `8642` /usr/bin/python3
  - `8643` /usr/bin/sleep
  - `8644` /usr/bin/curl
  - `8645` /usr/bin/python3
  - `8646` /usr/bin/cat
  - `8647` /usr/bin/chmod
  - `8648` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8639 (?) executed `/usr/bin/bash`
- +5.519 ms pid 8640 (bash) executed `/usr/bin/rm`
- +9.512 ms pid 8641 (bash) executed `/usr/bin/mkdir`
- +14.769 ms pid 8643 (bash) executed `/usr/bin/sleep`
- +14.787 ms pid 8642 (bash) executed `/usr/bin/python3`
- +525.660 ms pid 8644 (bash) executed `/usr/bin/curl`
- +549.677 ms pid 8646 (bash) executed `/usr/bin/cat`
- +553.892 ms pid 8647 (bash) executed `/usr/bin/chmod`
- +557.208 ms pid 8648 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +88.469 ms pid 8642 (python3) connected to `unix:/var/run/nscd/socket`
- +88.554 ms pid 8642 (python3) connected to `ipv6:[...]`
- +88.601 ms pid 8642 (python3) connected to `sockfd=3`
- +88.618 ms pid 8642 (python3) connected to `0.0.0.0:8766`
- +90.369 ms pid 8642 (python3) connected to `unix:/var/run/nscd/socket`
- +542.910 ms pid 8644 (curl) connected to `unix:/var/run/nscd/socket`
- +542.980 ms pid 8644 (curl) connected to `unix:/var/run/nscd/socket`
- +543.737 ms pid 8644 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +12.917 ms by pid 8639 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +525.301 ms by pid 8644 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +549.490 ms by pid 8646 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +556.520 ms pid 8647 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +8.139 ms pid 8640 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +8.183 ms pid 8640 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +8.209 ms pid 8640 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +8.253 ms pid 8640 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +543.164 ms pid 8644 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +557.208 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8648 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +8.183 ms #386 `unlinkat` by pid 8640 (rm)
    - +549.490 ms #3188 `openat` by pid 8646 (bash)
    - +549.558 ms #3190 `close` by pid 8646 (bash)
    - +552.765 ms #3319 `write` by pid 8646 (cat)
    - +552.854 ms #3323 `close` by pid 8646 (cat)
    - +556.520 ms #3497 `fchmodat` by pid 8647 (chmod)
    - +557.208 ms #3527 `execve` by pid 8648 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8639 | ? | execve | `/usr/bin/bash` |
| 49 | 1.391 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.427 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.593 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.626 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.703 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.736 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 1.811 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 1.845 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 1.938 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 1.975 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.049 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.083 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.167 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.199 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.253 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.328 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.362 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.435 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.469 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.551 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.585 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 2.658 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 2.692 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 2.768 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 2.801 | 8639 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 4.234 | 8639 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 239 | 5.158 | 8639 | bash | clone | `` |
| 256 | 5.519 | 8640 | bash | execve | `/usr/bin/rm` |
| 293 | 6.467 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 6.504 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 6.663 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 6.697 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 6.774 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 6.808 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 6.880 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 6.913 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 6.993 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 7.026 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 7.097 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 7.131 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 7.219 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 7.253 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 7.304 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 7.379 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 7.414 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 7.491 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 7.524 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 7.603 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 7.636 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 7.708 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 7.742 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 7.815 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 7.849 | 8640 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 7.980 | 8640 | rm | openat | `/tmp/ft_scenario03` |
| 385 | 8.139 | 8640 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 386 | 8.183 | 8640 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 387 | 8.209 | 8640 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 389 | 8.253 | 8640 | rm | unlinkat | `/tmp/ft_scenario03` |
| 394 | 8.377 | 8640 | rm | exit_group | `code=0` |
| 428 | 9.160 | 8639 | bash | clone | `` |
| 445 | 9.512 | 8641 | bash | execve | `/usr/bin/mkdir` |
| 509 | 10.979 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 511 | 11.020 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 520 | 11.181 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 522 | 11.214 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 526 | 11.289 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 528 | 11.323 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 532 | 11.396 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 534 | 11.429 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 538 | 11.503 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 540 | 11.535 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 544 | 11.609 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 546 | 11.643 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 550 | 11.724 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 552 | 11.758 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 555 | 11.809 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 559 | 11.881 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 561 | 11.915 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 565 | 11.993 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 567 | 12.026 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 571 | 12.106 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 573 | 12.139 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 577 | 12.211 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 579 | 12.245 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 583 | 12.324 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 585 | 12.359 | 8641 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 596 | 12.604 | 8641 | mkdir | exit_group | `code=0` |
| 606 | 12.917 | 8639 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 614 | 13.118 | 8639 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 621 | 13.294 | 8639 | bash | clone | `` |
| 695 | 14.361 | 8639 | bash | clone | `` |
| 724 | 14.769 | 8643 | bash | execve | `/usr/bin/sleep` |
| 725 | 14.787 | 8642 | bash | execve | `/usr/bin/python3` |
| 794 | 16.026 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 798 | 16.080 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 815 | 16.319 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 818 | 16.366 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 826 | 16.463 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 828 | 16.506 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 835 | 16.609 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 838 | 16.656 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 844 | 16.750 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 847 | 16.797 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 852 | 16.887 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 856 | 16.938 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 863 | 17.048 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 866 | 17.098 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 871 | 17.168 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 872 | 17.180 | 8642 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 876 | 17.236 | 8642 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 879 | 17.277 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 883 | 17.328 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 890 | 17.428 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 894 | 17.480 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 899 | 17.582 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 901 | 17.627 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 907 | 17.732 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 909 | 17.778 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 913 | 17.873 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 915 | 17.924 | 8643 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 953 | 22.132 | 8642 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 954 | 22.179 | 8642 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 957 | 22.275 | 8642 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 958 | 22.303 | 8642 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 959 | 22.330 | 8642 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 970 | 23.776 | 8642 | python3 | openat | `/etc/localtime` |
| 1125 | 29.982 | 8642 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1131 | 30.158 | 8642 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1140 | 30.424 | 8642 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1171 | 31.676 | 8642 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1179 | 31.887 | 8642 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1187 | 32.092 | 8642 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1435 | 41.577 | 8642 | python3 | openat | `/tmp/ft_scenario03` |
| 2370 | 88.189 | 8642 | python3 | openat | `/etc/gai.conf` |
| 2380 | 88.381 | 8642 | python3 | sendto | `socket:[53550]` |
| 2384 | 88.469 | 8642 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2388 | 88.554 | 8642 | python3 | connect | `ipv6:[...]` |
| 2390 | 88.601 | 8642 | python3 | connect | `sockfd=3` |
| 2391 | 88.618 | 8642 | python3 | connect | `0.0.0.0:8766` |
| 2431 | 90.369 | 8642 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2435 | 90.450 | 8642 | python3 | openat | `/etc/nsswitch.conf` |
| 2442 | 90.579 | 8642 | python3 | openat | `/etc/host.conf` |
| 2448 | 90.680 | 8642 | python3 | openat | `/etc/resolv.conf` |
| 2454 | 90.788 | 8642 | python3 | openat | `/etc/hosts` |
| 2462 | 90.932 | 8642 | python3 | openat | `/etc/hosts` |
| 2472 | 520.866 | 8643 | sleep | exit_group | `code=0` |
| 2508 | 523.870 | 8639 | bash | clone | `` |
| 2525 | 525.301 | 8644 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 2528 | 525.660 | 8644 | bash | execve | `/usr/bin/curl` |
| 2844 | 539.912 | 8644 | curl | openat | `/etc/gnutls/config` |
| 2891 | 541.226 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 2893 | 541.264 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 2902 | 541.434 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 2904 | 541.467 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 2908 | 541.545 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 2910 | 541.580 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 2914 | 541.654 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 2916 | 541.688 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 2920 | 541.761 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 2922 | 541.795 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 2926 | 541.870 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 2928 | 541.902 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 2932 | 542.042 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 2934 | 542.089 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 2937 | 542.183 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 2941 | 542.267 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 2943 | 542.302 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 2947 | 542.376 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 2949 | 542.411 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 2953 | 542.492 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 2955 | 542.527 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 2959 | 542.601 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 2961 | 542.634 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 2965 | 542.712 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 2967 | 542.745 | 8644 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 2971 | 542.825 | 8644 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 2972 | 542.846 | 8644 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 2975 | 542.910 | 8644 | curl | connect | `unix:/var/run/nscd/socket` |
| 2978 | 542.980 | 8644 | curl | connect | `unix:/var/run/nscd/socket` |
| 2982 | 543.050 | 8644 | curl | openat | `/etc/nsswitch.conf` |
| 2988 | 543.164 | 8644 | curl | openat | `/etc/passwd` |
| 2993 | 543.255 | 8644 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3018 | 543.737 | 8644 | curl | connect | `127.0.0.1:8766` |
| 3022 | 543.860 | 8642 | python3 | accept4 | `sockfd=3` |
| 3035 | 544.048 | 8644 | curl | sendto | `socket:[54501]` |
| 3042 | 544.142 | 8642 | python3 | clone3 | `` |
| 3058 | 544.515 | 8645 | python3 | recvfrom | `socket:[53554]` |
| 3068 | 544.871 | 8645 | python3 | openat | `/etc/mime.types` |
| 3094 | 547.071 | 8645 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 3100 | 547.257 | 8645 | python3 | sendto | `socket:[53554]` |
| 3106 | 547.396 | 8645 | python3 | sendto | `socket:[53554]` |
| 3107 | 547.412 | 8644 | curl | recvfrom | `socket:[54501]` |
| 3116 | 547.574 | 8644 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 3124 | 547.705 | 8645 | python3 | exit | `code=0` |
| 3135 | 548.057 | 8644 | curl | exit_group | `code=0` |
| 3171 | 549.094 | 8639 | bash | clone | `` |
| 3188 | 549.490 | 8646 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 3197 | 549.677 | 8646 | bash | execve | `/usr/bin/cat` |
| 3234 | 550.923 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3236 | 550.963 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3245 | 551.131 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3247 | 551.386 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3251 | 551.465 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3253 | 551.499 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3257 | 551.573 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3259 | 551.607 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3263 | 551.685 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3265 | 551.719 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3269 | 551.792 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3271 | 551.827 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3275 | 551.910 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3277 | 551.947 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3280 | 551.998 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3284 | 552.075 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3286 | 552.108 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3290 | 552.184 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3292 | 552.225 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3296 | 552.323 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3298 | 552.362 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3302 | 552.451 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3304 | 552.490 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3308 | 552.567 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3310 | 552.600 | 8646 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3319 | 552.765 | 8646 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 3325 | 552.896 | 8646 | cat | exit_group | `code=0` |
| 3361 | 553.558 | 8639 | bash | clone | `` |
| 3378 | 553.892 | 8647 | bash | execve | `/usr/bin/chmod` |
| 3415 | 555.028 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3417 | 555.064 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3426 | 555.224 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3428 | 555.258 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3432 | 555.332 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3434 | 555.366 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3438 | 555.439 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3440 | 555.472 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3444 | 555.549 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3446 | 555.582 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3450 | 555.654 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3452 | 555.687 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3456 | 555.769 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3458 | 555.803 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3461 | 555.854 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3465 | 555.942 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3467 | 555.978 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3471 | 556.053 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3473 | 556.086 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3477 | 556.165 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3479 | 556.198 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3483 | 556.270 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3485 | 556.304 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3489 | 556.377 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3491 | 556.411 | 8647 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3497 | 556.520 | 8647 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 3500 | 556.588 | 8647 | chmod | exit_group | `code=0` |
| 3510 | 556.861 | 8639 | bash | clone | `` |
| 3527 | 557.208 | 8648 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 3567 | 558.183 | 8648 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 3582 | 558.426 | 8648 | runme.sh | exit_group | `code=0` |
| 3630 | 560.295 | 8639 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 56.898 ms |
| Workload CPU (user+sys) | 75.527 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 3.804 ms |
| Evidence size | 1224173 bytes |

