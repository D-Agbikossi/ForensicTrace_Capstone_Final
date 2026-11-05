# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | D |
| Events recorded | 3628 |
| Failed exec attempts removed | 12 |
| Duration | 558.030 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_D_r3.json` (1223508 bytes) |
| SHA-256 | `46302e63687bc3e0bb65e7dfce206a8d655de46f07e687586deb617bd7426b66` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_D_r3.json.sha256`

## 1. Process tree

- `8440` /usr/bin/bash
  - `8441` /usr/bin/rm
  - `8442` /usr/bin/mkdir
  - `8443` /usr/bin/python3
  - `8444` /usr/bin/sleep
  - `8445` /usr/bin/curl
  - `8446` /usr/bin/python3
  - `8447` /usr/bin/cat
  - `8448` /usr/bin/chmod
  - `8449` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8440 (?) executed `/usr/bin/bash`
- +5.755 ms pid 8441 (bash) executed `/usr/bin/rm`
- +10.615 ms pid 8442 (bash) executed `/usr/bin/mkdir`
- +18.872 ms pid 8444 (bash) executed `/usr/bin/sleep`
- +18.889 ms pid 8443 (bash) executed `/usr/bin/python3`
- +526.836 ms pid 8445 (bash) executed `/usr/bin/curl`
- +546.317 ms pid 8447 (bash) executed `/usr/bin/cat`
- +550.879 ms pid 8448 (bash) executed `/usr/bin/chmod`
- +554.056 ms pid 8449 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +96.268 ms pid 8443 (python3) connected to `unix:/var/run/nscd/socket`
- +96.367 ms pid 8443 (python3) connected to `ipv6:[...]`
- +96.424 ms pid 8443 (python3) connected to `sockfd=3`
- +96.444 ms pid 8443 (python3) connected to `0.0.0.0:8766`
- +98.412 ms pid 8443 (python3) connected to `unix:/var/run/nscd/socket`
- +538.889 ms pid 8445 (curl) connected to `unix:/var/run/nscd/socket`
- +538.960 ms pid 8445 (curl) connected to `unix:/var/run/nscd/socket`
- +539.729 ms pid 8445 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +17.076 ms by pid 8440 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +526.622 ms by pid 8445 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +546.078 ms by pid 8447 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +553.374 ms pid 8448 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +9.256 ms pid 8441 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +9.309 ms pid 8441 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +9.342 ms pid 8441 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +9.399 ms pid 8441 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +539.150 ms pid 8445 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +554.056 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8449 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +9.309 ms #386 `unlinkat` by pid 8441 (rm)
    - +546.078 ms #3186 `openat` by pid 8447 (bash)
    - +546.170 ms #3188 `close` by pid 8447 (bash)
    - +549.504 ms #3317 `write` by pid 8447 (cat)
    - +549.609 ms #3321 `close` by pid 8447 (cat)
    - +553.374 ms #3495 `fchmodat` by pid 8448 (chmod)
    - +554.056 ms #3525 `execve` by pid 8449 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8440 | ? | execve | `/usr/bin/bash` |
| 49 | 1.746 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.783 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.960 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.993 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 2.071 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 2.104 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 2.179 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 2.213 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 2.287 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 2.322 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.396 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.430 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.514 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.547 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.599 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.675 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.709 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.783 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.820 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.901 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.949 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 3.032 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 3.081 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 3.158 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 3.191 | 8440 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 4.458 | 8440 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 239 | 5.363 | 8440 | bash | clone | `` |
| 256 | 5.755 | 8441 | bash | execve | `/usr/bin/rm` |
| 293 | 7.061 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 7.108 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 7.320 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 7.365 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 7.464 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 7.509 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 7.606 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 7.649 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 7.746 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 7.790 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 7.884 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 7.932 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 8.042 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 8.090 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 8.154 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 8.251 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 8.297 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 8.394 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 8.437 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 8.543 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 8.586 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 8.681 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 8.726 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 8.823 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 8.868 | 8441 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 9.047 | 8441 | rm | openat | `/tmp/ft_scenario03` |
| 385 | 9.256 | 8441 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 386 | 9.309 | 8441 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 387 | 9.342 | 8441 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 389 | 9.399 | 8441 | rm | unlinkat | `/tmp/ft_scenario03` |
| 394 | 9.553 | 8441 | rm | exit_group | `code=0` |
| 428 | 10.236 | 8440 | bash | clone | `` |
| 445 | 10.615 | 8442 | bash | execve | `/usr/bin/mkdir` |
| 509 | 14.263 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 511 | 14.318 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 520 | 14.547 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 522 | 14.604 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 526 | 14.707 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 528 | 14.756 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 532 | 14.859 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 534 | 14.905 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 538 | 15.144 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 540 | 15.191 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 544 | 15.294 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 546 | 15.343 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 550 | 15.453 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 552 | 15.499 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 555 | 15.560 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 559 | 15.682 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 561 | 15.738 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 565 | 15.881 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 567 | 15.927 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 571 | 16.038 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 573 | 16.077 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 577 | 16.171 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 579 | 16.216 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 583 | 16.319 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 585 | 16.356 | 8442 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 596 | 16.703 | 8442 | mkdir | exit_group | `code=0` |
| 606 | 17.076 | 8440 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 614 | 17.233 | 8440 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 621 | 17.375 | 8440 | bash | clone | `` |
| 694 | 18.464 | 8440 | bash | clone | `` |
| 724 | 18.872 | 8444 | bash | execve | `/usr/bin/sleep` |
| 725 | 18.889 | 8443 | bash | execve | `/usr/bin/python3` |
| 795 | 20.218 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 799 | 20.271 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 815 | 20.506 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 818 | 20.550 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 826 | 20.648 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 828 | 20.692 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 835 | 20.795 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 838 | 20.842 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 845 | 20.959 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 848 | 21.005 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 853 | 21.100 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 857 | 21.146 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 863 | 21.252 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 866 | 21.295 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 871 | 21.367 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 872 | 21.380 | 8443 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 876 | 21.435 | 8443 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 879 | 21.477 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 883 | 21.529 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 890 | 21.633 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 894 | 21.686 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 899 | 21.790 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 901 | 21.836 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 907 | 21.942 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 910 | 21.987 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 915 | 22.083 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 917 | 22.133 | 8444 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 953 | 24.764 | 8443 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 954 | 24.799 | 8443 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 957 | 24.884 | 8443 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 958 | 24.910 | 8443 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 959 | 24.942 | 8443 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 970 | 25.952 | 8443 | python3 | openat | `/etc/localtime` |
| 1125 | 31.810 | 8443 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1131 | 31.995 | 8443 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1140 | 32.264 | 8443 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1171 | 33.439 | 8443 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1179 | 33.669 | 8443 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1187 | 34.027 | 8443 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1435 | 42.706 | 8443 | python3 | openat | `/tmp/ft_scenario03` |
| 2370 | 95.943 | 8443 | python3 | openat | `/etc/gai.conf` |
| 2380 | 96.164 | 8443 | python3 | sendto | `socket:[52604]` |
| 2384 | 96.268 | 8443 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2388 | 96.367 | 8443 | python3 | connect | `ipv6:[...]` |
| 2390 | 96.424 | 8443 | python3 | connect | `sockfd=3` |
| 2391 | 96.444 | 8443 | python3 | connect | `0.0.0.0:8766` |
| 2432 | 98.412 | 8443 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2436 | 98.519 | 8443 | python3 | openat | `/etc/nsswitch.conf` |
| 2443 | 98.684 | 8443 | python3 | openat | `/etc/host.conf` |
| 2449 | 98.812 | 8443 | python3 | openat | `/etc/resolv.conf` |
| 2455 | 98.956 | 8443 | python3 | openat | `/etc/hosts` |
| 2463 | 99.136 | 8443 | python3 | openat | `/etc/hosts` |
| 2473 | 523.131 | 8444 | sleep | exit_group | `code=0` |
| 2509 | 525.696 | 8440 | bash | clone | `` |
| 2526 | 526.622 | 8445 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 2529 | 526.836 | 8445 | bash | execve | `/usr/bin/curl` |
| 2845 | 535.505 | 8445 | curl | openat | `/etc/gnutls/config` |
| 2892 | 537.012 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 2894 | 537.057 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 2903 | 537.265 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 2905 | 537.307 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 2909 | 537.398 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 2911 | 537.439 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 2915 | 537.531 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 2917 | 537.572 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 2921 | 537.659 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 2923 | 537.703 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 2927 | 537.792 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 2929 | 537.833 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 2933 | 537.938 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 2935 | 537.980 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 2938 | 538.122 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 2942 | 538.230 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 2944 | 538.266 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 2948 | 538.345 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 2950 | 538.378 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 2954 | 538.462 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 2956 | 538.498 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 2960 | 538.572 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 2962 | 538.610 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 2966 | 538.686 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 2968 | 538.720 | 8445 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 2972 | 538.803 | 8445 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 2973 | 538.823 | 8445 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 2976 | 538.889 | 8445 | curl | connect | `unix:/var/run/nscd/socket` |
| 2979 | 538.960 | 8445 | curl | connect | `unix:/var/run/nscd/socket` |
| 2983 | 539.033 | 8445 | curl | openat | `/etc/nsswitch.conf` |
| 2989 | 539.150 | 8445 | curl | openat | `/etc/passwd` |
| 2994 | 539.240 | 8445 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3019 | 539.729 | 8445 | curl | connect | `127.0.0.1:8766` |
| 3021 | 539.849 | 8443 | python3 | accept4 | `sockfd=3` |
| 3039 | 540.111 | 8445 | curl | sendto | `socket:[53275]` |
| 3040 | 540.130 | 8443 | python3 | clone3 | `` |
| 3059 | 540.471 | 8446 | python3 | recvfrom | `socket:[52608]` |
| 3067 | 540.788 | 8446 | python3 | openat | `/etc/mime.types` |
| 3092 | 542.979 | 8446 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 3098 | 543.167 | 8446 | python3 | sendto | `socket:[52608]` |
| 3104 | 543.273 | 8446 | python3 | sendto | `socket:[52608]` |
| 3105 | 543.292 | 8445 | curl | recvfrom | `socket:[53275]` |
| 3116 | 543.478 | 8445 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 3118 | 543.520 | 8446 | python3 | exit | `code=0` |
| 3133 | 543.995 | 8445 | curl | exit_group | `code=0` |
| 3169 | 545.507 | 8440 | bash | clone | `` |
| 3186 | 546.078 | 8447 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 3195 | 546.317 | 8447 | bash | execve | `/usr/bin/cat` |
| 3232 | 547.608 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3234 | 547.654 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3243 | 547.852 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3245 | 547.894 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3249 | 547.991 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3251 | 548.034 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3255 | 548.124 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3257 | 548.164 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3261 | 548.255 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3263 | 548.295 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3267 | 548.384 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3269 | 548.426 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3273 | 548.526 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3275 | 548.569 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3278 | 548.629 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3282 | 548.719 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3284 | 548.762 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3288 | 548.853 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3290 | 548.893 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3294 | 549.000 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3296 | 549.041 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3300 | 549.130 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3302 | 549.172 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3306 | 549.263 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3308 | 549.304 | 8447 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3317 | 549.504 | 8447 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 3323 | 549.656 | 8447 | cat | exit_group | `code=0` |
| 3359 | 550.499 | 8440 | bash | clone | `` |
| 3376 | 550.879 | 8448 | bash | execve | `/usr/bin/chmod` |
| 3413 | 551.875 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3415 | 551.912 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3424 | 552.085 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3426 | 552.118 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3430 | 552.193 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3432 | 552.227 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3436 | 552.301 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3438 | 552.335 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3442 | 552.409 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3444 | 552.443 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3448 | 552.515 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3450 | 552.549 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3454 | 552.632 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3456 | 552.666 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3459 | 552.716 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3463 | 552.790 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3465 | 552.826 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3469 | 552.899 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3471 | 552.936 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3475 | 553.018 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3477 | 553.053 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3481 | 553.125 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3483 | 553.158 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3487 | 553.233 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3489 | 553.266 | 8448 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3495 | 553.374 | 8448 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 3498 | 553.446 | 8448 | chmod | exit_group | `code=0` |
| 3508 | 553.706 | 8440 | bash | clone | `` |
| 3525 | 554.056 | 8449 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 3565 | 555.212 | 8449 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 3580 | 555.517 | 8449 | runme.sh | exit_group | `code=0` |
| 3628 | 557.427 | 8440 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 54.816 ms |
| Workload CPU (user+sys) | 79.248 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 3.838 ms |
| Evidence size | 1223508 bytes |

