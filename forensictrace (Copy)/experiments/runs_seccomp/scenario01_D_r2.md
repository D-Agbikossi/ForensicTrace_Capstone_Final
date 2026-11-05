# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | D |
| Events recorded | 3927 |
| Failed exec attempts removed | 12 |
| Duration | 766.320 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_D_r2.json` (1330062 bytes) |
| SHA-256 | `eaecaf05cae934ba7e22a7667b3ce1cc62fd964c401d0c2af27d501bfffd7c5c` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_D_r2.json.sha256`

## 1. Process tree

- `8146` /usr/bin/bash
  - `8147` /usr/bin/rm
  - `8148` /usr/bin/mkdir
  - `8149` /usr/bin/cat
  - `8150` /usr/bin/python3
  - `8151` /usr/bin/sleep
  - `8156` /usr/bin/curl
  - `8157` /usr/bin/python3
  - `8158` /usr/bin/chmod
  - `8159` /tmp/ft_scenario01/downloaded.sh
    - `8160` /usr/bin/date
    - `8161` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8146 (?) executed `/usr/bin/bash`
- +5.170 ms pid 8147 (bash) executed `/usr/bin/rm`
- +9.295 ms pid 8148 (bash) executed `/usr/bin/mkdir`
- +14.200 ms pid 8149 (bash) executed `/usr/bin/cat`
- +18.576 ms pid 8151 (bash) executed `/usr/bin/sleep`
- +18.664 ms pid 8150 (bash) executed `/usr/bin/python3`
- +526.157 ms pid 8156 (bash) executed `/usr/bin/curl`
- +545.992 ms pid 8158 (bash) executed `/usr/bin/chmod`
- +549.693 ms pid 8159 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +551.639 ms pid 8160 (downloaded.sh) executed `/usr/bin/date`
- +556.624 ms pid 8161 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +95.505 ms pid 8150 (python3) connected to `unix:/var/run/nscd/socket`
- +95.592 ms pid 8150 (python3) connected to `ipv6:[...]`
- +95.635 ms pid 8150 (python3) connected to `sockfd=3`
- +95.651 ms pid 8150 (python3) connected to `0.0.0.0:8765`
- +97.299 ms pid 8150 (python3) connected to `unix:/var/run/nscd/socket`
- +538.177 ms pid 8156 (curl) connected to `unix:/var/run/nscd/socket`
- +538.245 ms pid 8156 (curl) connected to `unix:/var/run/nscd/socket`
- +539.086 ms pid 8156 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +13.965 ms by pid 8149 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +543.496 ms by pid 8156 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +548.980 ms pid 8158 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +7.917 ms pid 8147 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +7.962 ms pid 8147 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +8.006 ms pid 8147 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +538.468 ms pid 8156 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +549.693 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8159 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +7.962 ms #386 `unlinkat` by pid 8147 (rm)
    - +543.496 ms #3282 `openat` by pid 8156 (curl)
    - +543.717 ms #3293 `write` by pid 8156 (curl)
    - +543.765 ms #3295 `close` by pid 8156 (curl)
    - +548.980 ms #3482 `fchmodat` by pid 8158 (chmod)
    - +549.693 ms #3512 `execve` by pid 8159 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8146 | ? | execve | `/usr/bin/bash` |
| 49 | 1.393 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.429 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.596 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.629 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.705 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.739 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 1.813 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 1.847 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 1.921 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 1.956 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.029 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.063 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.155 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.189 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.240 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.316 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.350 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.422 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.459 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.540 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.574 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 2.648 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 2.682 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 2.763 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 2.796 | 8146 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 4.055 | 8146 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 239 | 4.812 | 8146 | bash | clone | `` |
| 256 | 5.170 | 8147 | bash | execve | `/usr/bin/rm` |
| 293 | 6.241 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 6.279 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 6.442 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 6.477 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 6.552 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 6.586 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 6.664 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 6.696 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 6.770 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 6.803 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 6.876 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 6.910 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 6.993 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 7.028 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 7.078 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 7.158 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 7.194 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 7.268 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 7.301 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 7.382 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 7.414 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 7.487 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 7.522 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 7.596 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 7.631 | 8147 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 7.759 | 8147 | rm | openat | `/tmp/ft_scenario01` |
| 385 | 7.917 | 8147 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 386 | 7.962 | 8147 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 388 | 8.006 | 8147 | rm | unlinkat | `/tmp/ft_scenario01` |
| 393 | 8.140 | 8147 | rm | exit_group | `code=0` |
| 427 | 8.922 | 8146 | bash | clone | `` |
| 444 | 9.295 | 8148 | bash | execve | `/usr/bin/mkdir` |
| 508 | 10.933 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 510 | 10.978 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 519 | 11.194 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 521 | 11.239 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 525 | 11.336 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 527 | 11.379 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 531 | 11.475 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 533 | 11.518 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 537 | 11.612 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 539 | 11.657 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 543 | 11.751 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 545 | 11.796 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 549 | 11.901 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 551 | 11.946 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 554 | 12.009 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 558 | 12.113 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 560 | 12.181 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 564 | 12.279 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 566 | 12.314 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 570 | 12.398 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 572 | 12.433 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 576 | 12.511 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 578 | 12.544 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 582 | 12.620 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 584 | 12.653 | 8148 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 595 | 12.902 | 8148 | mkdir | exit_group | `code=0` |
| 634 | 13.627 | 8146 | bash | clone | `` |
| 651 | 13.965 | 8149 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 660 | 14.200 | 8149 | bash | execve | `/usr/bin/cat` |
| 697 | 15.125 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 699 | 15.161 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 708 | 15.321 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 710 | 15.355 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 714 | 15.430 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 716 | 15.462 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 720 | 15.535 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 722 | 15.570 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 726 | 15.644 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 728 | 15.678 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 732 | 15.749 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 734 | 15.783 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 738 | 15.867 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 740 | 15.900 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 743 | 15.950 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 747 | 16.024 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 749 | 16.059 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 753 | 16.137 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 755 | 16.172 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 759 | 16.251 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 761 | 16.285 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 765 | 16.359 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 767 | 16.393 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 771 | 16.467 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 773 | 16.500 | 8149 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 782 | 16.663 | 8149 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 788 | 16.789 | 8149 | cat | exit_group | `code=0` |
| 798 | 17.069 | 8146 | bash | clone | `` |
| 872 | 18.118 | 8146 | bash | clone | `` |
| 900 | 18.576 | 8151 | bash | execve | `/usr/bin/sleep` |
| 902 | 18.664 | 8150 | bash | execve | `/usr/bin/python3` |
| 939 | 20.032 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 941 | 20.090 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 950 | 20.372 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 952 | 20.416 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 956 | 20.516 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 958 | 20.562 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 962 | 20.659 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 964 | 20.705 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 968 | 20.804 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 970 | 20.853 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 974 | 20.955 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 976 | 21.002 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 980 | 21.121 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 982 | 21.166 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 986 | 21.579 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 993 | 21.739 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 997 | 21.798 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1005 | 21.945 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1009 | 22.007 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1016 | 22.158 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1020 | 22.224 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1028 | 22.355 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1031 | 22.404 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1038 | 22.516 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1041 | 22.562 | 8151 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1098 | 25.047 | 8150 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1100 | 25.103 | 8150 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1130 | 29.189 | 8150 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 1131 | 29.352 | 8150 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 1134 | 29.441 | 8150 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 1135 | 29.466 | 8150 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 1136 | 29.490 | 8150 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 1147 | 30.933 | 8150 | python3 | openat | `/etc/localtime` |
| 1302 | 37.465 | 8150 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1308 | 37.646 | 8150 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1317 | 37.912 | 8150 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1348 | 39.193 | 8150 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1356 | 39.409 | 8150 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1364 | 39.604 | 8150 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1612 | 48.849 | 8150 | python3 | openat | `/tmp/ft_scenario01` |
| 2547 | 95.226 | 8150 | python3 | openat | `/etc/gai.conf` |
| 2557 | 95.417 | 8150 | python3 | sendto | `socket:[49139]` |
| 2561 | 95.505 | 8150 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2565 | 95.592 | 8150 | python3 | connect | `ipv6:[...]` |
| 2567 | 95.635 | 8150 | python3 | connect | `sockfd=3` |
| 2568 | 95.651 | 8150 | python3 | connect | `0.0.0.0:8765` |
| 2609 | 97.299 | 8150 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2613 | 97.378 | 8150 | python3 | openat | `/etc/nsswitch.conf` |
| 2620 | 97.506 | 8150 | python3 | openat | `/etc/host.conf` |
| 2626 | 97.606 | 8150 | python3 | openat | `/etc/resolv.conf` |
| 2632 | 97.753 | 8150 | python3 | openat | `/etc/hosts` |
| 2640 | 97.940 | 8150 | python3 | openat | `/etc/hosts` |
| 2650 | 524.486 | 8151 | sleep | exit_group | `code=0` |
| 2686 | 525.584 | 8146 | bash | clone | `` |
| 2703 | 526.157 | 8156 | bash | execve | `/usr/bin/curl` |
| 3019 | 534.636 | 8156 | curl | openat | `/etc/gnutls/config` |
| 3066 | 536.431 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3068 | 536.481 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3077 | 536.714 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3079 | 536.749 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3083 | 536.827 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3085 | 536.862 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3089 | 536.946 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3091 | 536.984 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3095 | 537.059 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3097 | 537.092 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3101 | 537.180 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3103 | 537.214 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3107 | 537.302 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3109 | 537.337 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3112 | 537.389 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3116 | 537.466 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3118 | 537.500 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3122 | 537.576 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3124 | 537.609 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3128 | 537.692 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3130 | 537.726 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3134 | 537.801 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3136 | 537.836 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3140 | 537.911 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3142 | 537.946 | 8156 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3146 | 538.033 | 8156 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3147 | 538.052 | 8156 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 3150 | 538.177 | 8156 | curl | connect | `unix:/var/run/nscd/socket` |
| 3153 | 538.245 | 8156 | curl | connect | `unix:/var/run/nscd/socket` |
| 3157 | 538.325 | 8156 | curl | openat | `/etc/nsswitch.conf` |
| 3163 | 538.468 | 8156 | curl | openat | `/etc/passwd` |
| 3168 | 538.568 | 8156 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3192 | 539.086 | 8156 | curl | connect | `127.0.0.1:8765` |
| 3197 | 539.258 | 8150 | python3 | accept4 | `sockfd=3` |
| 3207 | 539.446 | 8156 | curl | sendto | `socket:[49147]` |
| 3216 | 539.661 | 8150 | python3 | clone3 | `` |
| 3232 | 540.088 | 8157 | python3 | recvfrom | `socket:[50759]` |
| 3242 | 540.602 | 8157 | python3 | openat | `/etc/mime.types` |
| 3267 | 543.023 | 8157 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 3273 | 543.306 | 8157 | python3 | sendto | `socket:[50759]` |
| 3279 | 543.446 | 8157 | python3 | sendto | `socket:[50759]` |
| 3280 | 543.456 | 8156 | curl | recvfrom | `socket:[49147]` |
| 3282 | 543.496 | 8156 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3293 | 543.717 | 8156 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 3294 | 543.729 | 8157 | python3 | exit | `code=0` |
| 3310 | 544.370 | 8156 | curl | exit_group | `code=0` |
| 3346 | 545.540 | 8146 | bash | clone | `` |
| 3363 | 545.992 | 8158 | bash | execve | `/usr/bin/chmod` |
| 3400 | 547.346 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3402 | 547.454 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3411 | 547.666 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3413 | 547.701 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3417 | 547.779 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3419 | 547.813 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3423 | 547.886 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3425 | 547.921 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3429 | 547.994 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3431 | 548.028 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3435 | 548.102 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3437 | 548.145 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3441 | 548.230 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3443 | 548.263 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3446 | 548.314 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3450 | 548.391 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3452 | 548.425 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3456 | 548.501 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3458 | 548.535 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3462 | 548.616 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3464 | 548.650 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3468 | 548.725 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3470 | 548.759 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3474 | 548.833 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3476 | 548.867 | 8158 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3482 | 548.980 | 8158 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 3485 | 549.058 | 8158 | chmod | exit_group | `code=0` |
| 3495 | 549.335 | 8146 | bash | clone | `` |
| 3512 | 549.693 | 8159 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 3552 | 550.932 | 8159 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3566 | 551.220 | 8159 | downloaded.sh | clone | `` |
| 3587 | 551.639 | 8160 | downloaded.sh | execve | `/usr/bin/date` |
| 3624 | 553.065 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3626 | 553.252 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3635 | 553.627 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3637 | 553.664 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3641 | 553.753 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3643 | 553.791 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3647 | 554.066 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3649 | 554.108 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3653 | 554.193 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3655 | 554.265 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3659 | 554.708 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3661 | 554.758 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3665 | 554.846 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3667 | 554.881 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3670 | 554.932 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3674 | 555.009 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3676 | 555.126 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3680 | 555.278 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3682 | 555.311 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3686 | 555.393 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3688 | 555.428 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3692 | 555.501 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3694 | 555.535 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3698 | 555.616 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3700 | 555.650 | 8160 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3704 | 555.740 | 8160 | date | openat | `/etc/localtime` |
| 3716 | 555.970 | 8160 | date | exit_group | `code=0` |
| 3736 | 556.544 | 8159 | downloaded.sh | vfork | `` |
| 3738 | 556.624 | 8161 | downloaded.sh | execve | `/usr/bin/sleep` |
| 3777 | 557.606 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3779 | 557.639 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3788 | 557.802 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3790 | 557.836 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3794 | 557.912 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3796 | 557.946 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3800 | 558.019 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3802 | 558.052 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3806 | 558.132 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3808 | 558.165 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3812 | 558.238 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3814 | 558.273 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3818 | 558.356 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3820 | 558.390 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3823 | 558.440 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3827 | 558.518 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3829 | 558.552 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3833 | 558.632 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3835 | 558.666 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3839 | 558.772 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3841 | 558.815 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3845 | 558.907 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3847 | 558.949 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3851 | 559.040 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3853 | 559.082 | 8161 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3875 | 760.092 | 8161 | sleep | exit_group | `code=0` |
| 3879 | 760.808 | 8159 | downloaded.sh | exit_group | `code=0` |
| 3927 | 765.518 | 8146 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 69.806 ms |
| Workload CPU (user+sys) | 80.357 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 13.461 ms |
| Evidence size | 1330062 bytes |

