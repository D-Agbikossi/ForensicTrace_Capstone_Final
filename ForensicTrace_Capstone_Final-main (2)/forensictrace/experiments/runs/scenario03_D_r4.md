# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | D |
| Events recorded | 3624 |
| Failed exec attempts removed | 12 |
| Duration | 600.307 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_D_r4.json` (1222339 bytes) |
| SHA-256 | `925668c427d5b94e059a35e4d4428045cdbe461cf1de1b3f281b4820e5bbec7c` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_D_r4.json.sha256`

## 1. Process tree

- `7834` /usr/bin/bash
  - `7835` /usr/bin/rm
  - `7836` /usr/bin/mkdir
  - `7837` /usr/bin/python3
  - `7838` /usr/bin/sleep
  - `7839` /usr/bin/curl
  - `7840` /usr/bin/python3
  - `7841` /usr/bin/cat
  - `7842` /usr/bin/chmod
  - `7843` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7834 (?) executed `/usr/bin/bash`
- +8.995 ms pid 7835 (bash) executed `/usr/bin/rm`
- +16.388 ms pid 7836 (bash) executed `/usr/bin/mkdir`
- +25.363 ms pid 7838 (bash) executed `/usr/bin/sleep`
- +25.424 ms pid 7837 (bash) executed `/usr/bin/python3`
- +535.990 ms pid 7839 (bash) executed `/usr/bin/curl`
- +571.075 ms pid 7841 (bash) executed `/usr/bin/cat`
- +583.652 ms pid 7842 (bash) executed `/usr/bin/chmod`
- +592.490 ms pid 7843 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +100.397 ms pid 7837 (python3) connected to `unix:/var/run/nscd/socket`
- +100.503 ms pid 7837 (python3) connected to `ipv6:[...]`
- +100.556 ms pid 7837 (python3) connected to `sockfd=3`
- +100.578 ms pid 7837 (python3) connected to `0.0.0.0:8766`
- +102.529 ms pid 7837 (python3) connected to `unix:/var/run/nscd/socket`
- +560.734 ms pid 7839 (curl) connected to `unix:/var/run/nscd/socket`
- +560.852 ms pid 7839 (curl) connected to `unix:/var/run/nscd/socket`
- +561.952 ms pid 7839 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +22.833 ms by pid 7834 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +535.812 ms by pid 7839 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +570.835 ms by pid 7841 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +591.198 ms pid 7842 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +14.378 ms pid 7835 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +14.496 ms pid 7835 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +14.538 ms pid 7835 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +14.606 ms pid 7835 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +561.107 ms pid 7839 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +592.490 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7843 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +14.496 ms #386 `unlinkat` by pid 7835 (rm)
    - +570.835 ms #3188 `openat` by pid 7841 (bash)
    - +570.927 ms #3190 `close` by pid 7841 (bash)
    - +577.666 ms #3319 `write` by pid 7841 (cat)
    - +577.848 ms #3323 `close` by pid 7841 (cat)
    - +591.198 ms #3497 `fchmodat` by pid 7842 (chmod)
    - +592.490 ms #3527 `execve` by pid 7843 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7834 | ? | execve | `/usr/bin/bash` |
| 49 | 1.458 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.524 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.749 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.792 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.892 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.935 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 2.031 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 2.076 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 2.171 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 2.216 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.312 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.357 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.511 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.549 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.606 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.926 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.969 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 3.070 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 3.116 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 3.227 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 3.303 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 4.566 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 4.622 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 4.755 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 4.804 | 7834 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 6.973 | 7834 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 239 | 8.271 | 7834 | bash | clone | `` |
| 256 | 8.995 | 7835 | bash | execve | `/usr/bin/rm` |
| 293 | 10.870 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 10.931 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 11.202 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 11.259 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 11.385 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 11.467 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 11.612 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 11.666 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 11.943 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 12.127 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 12.254 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 12.309 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 12.438 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 12.489 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 12.577 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 12.685 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 12.735 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 12.855 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 12.905 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 13.030 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 13.082 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 13.206 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 13.262 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 13.419 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 13.484 | 7835 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 13.672 | 7835 | rm | openat | `/tmp/ft_scenario03` |
| 385 | 14.378 | 7835 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 386 | 14.496 | 7835 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 387 | 14.538 | 7835 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 389 | 14.606 | 7835 | rm | unlinkat | `/tmp/ft_scenario03` |
| 394 | 14.814 | 7835 | rm | exit_group | `code=0` |
| 428 | 15.958 | 7834 | bash | clone | `` |
| 445 | 16.388 | 7836 | bash | execve | `/usr/bin/mkdir` |
| 509 | 18.438 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 511 | 18.476 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 520 | 18.642 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 522 | 18.679 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 526 | 18.756 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 528 | 18.790 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 532 | 18.864 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 534 | 18.897 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 538 | 18.972 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 540 | 19.005 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 544 | 19.080 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 546 | 19.115 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 550 | 19.202 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 552 | 19.238 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 555 | 19.290 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 559 | 19.365 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 561 | 19.403 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 565 | 19.479 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 567 | 19.513 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 571 | 19.596 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 573 | 19.629 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 577 | 19.703 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 579 | 19.737 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 583 | 19.812 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 585 | 19.871 | 7836 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 596 | 20.297 | 7836 | mkdir | exit_group | `code=0` |
| 606 | 22.833 | 7834 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 614 | 23.134 | 7834 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 621 | 23.422 | 7834 | bash | clone | `` |
| 694 | 24.791 | 7834 | bash | clone | `` |
| 723 | 25.363 | 7838 | bash | execve | `/usr/bin/sleep` |
| 725 | 25.424 | 7837 | bash | execve | `/usr/bin/python3` |
| 801 | 27.147 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 804 | 27.206 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 819 | 27.484 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 822 | 27.544 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 829 | 27.673 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 832 | 27.729 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 839 | 27.860 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 842 | 27.918 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 848 | 28.038 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 851 | 28.096 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 859 | 28.236 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 862 | 28.298 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 863 | 28.311 | 7837 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 867 | 28.384 | 7837 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 871 | 28.573 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 874 | 28.627 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 880 | 28.710 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 886 | 28.827 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 889 | 28.879 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 894 | 29.003 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 897 | 29.055 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 903 | 29.176 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 905 | 29.367 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 909 | 30.653 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 911 | 30.851 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 915 | 30.999 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 917 | 31.044 | 7838 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 953 | 33.276 | 7837 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 954 | 33.306 | 7837 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 957 | 33.375 | 7837 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 958 | 33.402 | 7837 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 959 | 33.422 | 7837 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 970 | 34.373 | 7837 | python3 | openat | `/etc/localtime` |
| 1125 | 40.141 | 7837 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1131 | 40.322 | 7837 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1140 | 40.592 | 7837 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1171 | 41.849 | 7837 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1179 | 42.062 | 7837 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1187 | 42.258 | 7837 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1435 | 52.506 | 7837 | python3 | openat | `/tmp/ft_scenario03` |
| 2370 | 100.040 | 7837 | python3 | openat | `/etc/gai.conf` |
| 2380 | 100.282 | 7837 | python3 | sendto | `socket:[48003]` |
| 2384 | 100.397 | 7837 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2388 | 100.503 | 7837 | python3 | connect | `ipv6:[...]` |
| 2390 | 100.556 | 7837 | python3 | connect | `sockfd=3` |
| 2391 | 100.578 | 7837 | python3 | connect | `0.0.0.0:8766` |
| 2431 | 102.529 | 7837 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2435 | 102.633 | 7837 | python3 | openat | `/etc/nsswitch.conf` |
| 2442 | 102.798 | 7837 | python3 | openat | `/etc/host.conf` |
| 2448 | 102.928 | 7837 | python3 | openat | `/etc/resolv.conf` |
| 2454 | 103.067 | 7837 | python3 | openat | `/etc/hosts` |
| 2462 | 103.243 | 7837 | python3 | openat | `/etc/hosts` |
| 2472 | 533.608 | 7838 | sleep | exit_group | `code=0` |
| 2508 | 535.243 | 7834 | bash | clone | `` |
| 2525 | 535.812 | 7839 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 2528 | 535.990 | 7839 | bash | execve | `/usr/bin/curl` |
| 2844 | 550.559 | 7839 | curl | openat | `/etc/gnutls/config` |
| 2891 | 552.283 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 2893 | 552.439 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 2902 | 552.935 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 2904 | 552.983 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 2908 | 553.089 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 2910 | 553.139 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 2914 | 553.405 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 2916 | 553.568 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 2920 | 553.773 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 2922 | 554.496 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 2926 | 554.632 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 2928 | 554.681 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 2932 | 554.815 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 2934 | 554.866 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 2937 | 554.946 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 2941 | 555.110 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 2943 | 558.427 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 2947 | 559.854 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 2949 | 559.914 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 2953 | 560.047 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 2955 | 560.106 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 2959 | 560.239 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 2961 | 560.297 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 2965 | 560.445 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 2967 | 560.491 | 7839 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 2971 | 560.616 | 7839 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 2972 | 560.647 | 7839 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 2975 | 560.734 | 7839 | curl | connect | `unix:/var/run/nscd/socket` |
| 2978 | 560.852 | 7839 | curl | connect | `unix:/var/run/nscd/socket` |
| 2982 | 560.951 | 7839 | curl | openat | `/etc/nsswitch.conf` |
| 2988 | 561.107 | 7839 | curl | openat | `/etc/passwd` |
| 2993 | 561.232 | 7839 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3018 | 561.952 | 7839 | curl | connect | `127.0.0.1:8766` |
| 3020 | 562.133 | 7837 | python3 | accept4 | `sockfd=3` |
| 3034 | 562.472 | 7837 | python3 | clone3 | `` |
| 3043 | 562.667 | 7839 | curl | sendto | `socket:[48726]` |
| 3058 | 563.066 | 7840 | python3 | recvfrom | `socket:[48727]` |
| 3068 | 563.523 | 7840 | python3 | openat | `/etc/mime.types` |
| 3094 | 567.870 | 7840 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 3100 | 568.179 | 7840 | python3 | sendto | `socket:[48727]` |
| 3106 | 568.389 | 7840 | python3 | sendto | `socket:[48727]` |
| 3107 | 568.410 | 7839 | curl | recvfrom | `socket:[48726]` |
| 3116 | 568.615 | 7839 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 3124 | 568.766 | 7840 | python3 | exit | `code=0` |
| 3135 | 569.135 | 7839 | curl | exit_group | `code=0` |
| 3171 | 570.338 | 7834 | bash | clone | `` |
| 3188 | 570.835 | 7841 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 3197 | 571.075 | 7841 | bash | execve | `/usr/bin/cat` |
| 3234 | 572.981 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3236 | 573.035 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3245 | 573.446 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3247 | 573.756 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3251 | 574.049 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3253 | 574.101 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3257 | 574.206 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3259 | 574.261 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3263 | 574.385 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3265 | 574.462 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3269 | 574.587 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3271 | 574.648 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3275 | 574.794 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3277 | 574.851 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3280 | 574.934 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3284 | 575.244 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3286 | 576.486 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3290 | 576.752 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3292 | 576.819 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3296 | 576.964 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3298 | 577.017 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3302 | 577.139 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3304 | 577.190 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3308 | 577.320 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3310 | 577.374 | 7841 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3319 | 577.666 | 7841 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 3325 | 577.935 | 7841 | cat | exit_group | `code=0` |
| 3361 | 581.239 | 7834 | bash | clone | `` |
| 3378 | 583.652 | 7842 | bash | execve | `/usr/bin/chmod` |
| 3415 | 585.869 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3417 | 585.911 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3426 | 586.099 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3428 | 586.138 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3432 | 586.223 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3434 | 586.267 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3438 | 586.374 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3440 | 586.419 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3444 | 586.502 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3446 | 586.542 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3450 | 586.638 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3452 | 586.680 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3456 | 586.845 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3458 | 586.890 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3461 | 586.987 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3465 | 587.094 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3467 | 587.146 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3471 | 587.271 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3473 | 587.322 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3477 | 590.586 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3479 | 590.711 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3483 | 590.853 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3485 | 590.899 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3489 | 590.999 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3491 | 591.044 | 7842 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3497 | 591.198 | 7842 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 3500 | 591.310 | 7842 | chmod | exit_group | `code=0` |
| 3510 | 591.952 | 7834 | bash | clone | `` |
| 3527 | 592.490 | 7843 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 3567 | 594.140 | 7843 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 3582 | 594.519 | 7843 | runme.sh | exit_group | `code=0` |
| 3624 | 599.038 | 7834 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 66.608 ms |
| Workload CPU (user+sys) | 84.096 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 4.655 ms |
| Evidence size | 1222339 bytes |

