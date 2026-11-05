# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | D |
| Events recorded | 3927 |
| Failed exec attempts removed | 12 |
| Duration | 768.601 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_D_r4.json` (1330074 bytes) |
| SHA-256 | `449c5bd4c3ae8780d0ee031a0fb7d57545bd212d28b07d9785a7d9e0c5916b40` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_D_r4.json.sha256`

## 1. Process tree

- `8514` /usr/bin/bash
  - `8515` /usr/bin/rm
  - `8516` /usr/bin/mkdir
  - `8517` /usr/bin/cat
  - `8518` /usr/bin/python3
  - `8519` /usr/bin/sleep
  - `8520` /usr/bin/curl
  - `8521` /usr/bin/python3
  - `8522` /usr/bin/chmod
  - `8523` /tmp/ft_scenario01/downloaded.sh
    - `8524` /usr/bin/date
    - `8525` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8514 (?) executed `/usr/bin/bash`
- +7.514 ms pid 8515 (bash) executed `/usr/bin/rm`
- +11.953 ms pid 8516 (bash) executed `/usr/bin/mkdir`
- +17.382 ms pid 8517 (bash) executed `/usr/bin/cat`
- +21.812 ms pid 8519 (bash) executed `/usr/bin/sleep`
- +21.826 ms pid 8518 (bash) executed `/usr/bin/python3`
- +531.837 ms pid 8520 (bash) executed `/usr/bin/curl`
- +553.130 ms pid 8522 (bash) executed `/usr/bin/chmod`
- +556.418 ms pid 8523 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +558.068 ms pid 8524 (downloaded.sh) executed `/usr/bin/date`
- +561.882 ms pid 8525 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +98.991 ms pid 8518 (python3) connected to `unix:/var/run/nscd/socket`
- +99.079 ms pid 8518 (python3) connected to `ipv6:[...]`
- +99.121 ms pid 8518 (python3) connected to `sockfd=3`
- +99.138 ms pid 8518 (python3) connected to `0.0.0.0:8765`
- +100.915 ms pid 8518 (python3) connected to `unix:/var/run/nscd/socket`
- +545.253 ms pid 8520 (curl) connected to `unix:/var/run/nscd/socket`
- +545.316 ms pid 8520 (curl) connected to `unix:/var/run/nscd/socket`
- +546.292 ms pid 8520 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +17.198 ms by pid 8517 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +550.819 ms by pid 8520 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +555.679 ms pid 8522 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +10.666 ms pid 8515 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +10.713 ms pid 8515 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +10.758 ms pid 8515 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +545.498 ms pid 8520 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +556.418 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8523 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +10.713 ms #386 `unlinkat` by pid 8515 (rm)
    - +550.819 ms #3283 `openat` by pid 8520 (curl)
    - +551.033 ms #3294 `write` by pid 8520 (curl)
    - +551.073 ms #3295 `close` by pid 8520 (curl)
    - +555.679 ms #3482 `fchmodat` by pid 8522 (chmod)
    - +556.418 ms #3512 `execve` by pid 8523 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8514 | ? | execve | `/usr/bin/bash` |
| 49 | 1.769 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.875 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 2.218 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 2.322 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 2.479 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 2.527 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 2.675 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 2.774 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 2.935 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 2.975 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 3.109 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 3.199 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 3.346 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 3.383 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 3.442 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 3.583 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 3.671 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 3.805 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 3.845 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 3.990 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 4.029 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 4.167 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 4.207 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 4.348 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 4.438 | 8514 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 6.123 | 8514 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 239 | 7.138 | 8514 | bash | clone | `` |
| 256 | 7.514 | 8515 | bash | execve | `/usr/bin/rm` |
| 293 | 8.635 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 8.688 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 8.897 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 8.942 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 9.023 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 9.069 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 9.146 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 9.192 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 9.280 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 9.316 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 9.397 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 9.434 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 9.525 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 9.563 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 9.647 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 9.774 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 9.821 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 9.923 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 9.967 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 10.081 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 10.119 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 10.224 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 10.266 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 10.342 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 10.376 | 8515 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 10.505 | 8515 | rm | openat | `/tmp/ft_scenario01` |
| 385 | 10.666 | 8515 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 386 | 10.713 | 8515 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 388 | 10.758 | 8515 | rm | unlinkat | `/tmp/ft_scenario01` |
| 393 | 10.914 | 8515 | rm | exit_group | `code=0` |
| 427 | 11.565 | 8514 | bash | clone | `` |
| 444 | 11.953 | 8516 | bash | execve | `/usr/bin/mkdir` |
| 508 | 13.872 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 510 | 13.917 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 519 | 14.127 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 521 | 14.246 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 525 | 14.422 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 527 | 14.461 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 531 | 14.540 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 533 | 14.573 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 537 | 14.647 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 539 | 14.682 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 543 | 14.757 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 545 | 14.795 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 549 | 14.880 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 551 | 14.915 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 554 | 14.964 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 558 | 15.039 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 560 | 15.072 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 564 | 15.146 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 566 | 15.216 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 570 | 15.313 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 572 | 15.363 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 576 | 15.453 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 578 | 15.503 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 582 | 15.596 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 584 | 15.643 | 8516 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 595 | 15.945 | 8516 | mkdir | exit_group | `code=0` |
| 634 | 16.736 | 8514 | bash | clone | `` |
| 651 | 17.198 | 8517 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 660 | 17.382 | 8517 | bash | execve | `/usr/bin/cat` |
| 697 | 18.447 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 699 | 18.482 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 708 | 18.648 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 710 | 18.681 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 714 | 18.758 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 716 | 18.791 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 720 | 18.864 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 722 | 18.898 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 726 | 18.971 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 728 | 19.005 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 732 | 19.077 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 734 | 19.111 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 738 | 19.199 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 740 | 19.232 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 743 | 19.283 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 747 | 19.358 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 749 | 19.396 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 753 | 19.473 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 755 | 19.508 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 759 | 19.585 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 761 | 19.620 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 765 | 19.693 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 767 | 19.727 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 771 | 19.801 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 773 | 19.834 | 8517 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 782 | 19.994 | 8517 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 788 | 20.120 | 8517 | cat | exit_group | `code=0` |
| 798 | 20.370 | 8514 | bash | clone | `` |
| 873 | 21.412 | 8514 | bash | clone | `` |
| 901 | 21.812 | 8519 | bash | execve | `/usr/bin/sleep` |
| 902 | 21.826 | 8518 | bash | execve | `/usr/bin/python3` |
| 982 | 23.329 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 986 | 23.379 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1000 | 23.606 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1003 | 23.648 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1010 | 23.763 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1013 | 23.809 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1019 | 23.908 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1022 | 23.954 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1030 | 24.075 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1033 | 24.123 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1034 | 24.135 | 8518 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 24.198 | 8518 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 24.250 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1044 | 24.302 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1052 | 24.419 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1056 | 24.473 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1059 | 24.537 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1064 | 24.634 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1067 | 24.685 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1073 | 24.785 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1076 | 24.834 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1080 | 25.361 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1082 | 25.421 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1086 | 25.549 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1088 | 25.765 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1093 | 25.912 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1095 | 25.967 | 8519 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1130 | 28.067 | 8518 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 1131 | 28.106 | 8518 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 1134 | 28.206 | 8518 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 1135 | 28.232 | 8518 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 1136 | 28.257 | 8518 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 1147 | 29.546 | 8518 | python3 | openat | `/etc/localtime` |
| 1302 | 35.417 | 8518 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1308 | 35.559 | 8518 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1317 | 35.773 | 8518 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1348 | 36.939 | 8518 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1356 | 37.143 | 8518 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1364 | 37.351 | 8518 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1612 | 48.686 | 8518 | python3 | openat | `/tmp/ft_scenario01` |
| 2547 | 98.710 | 8518 | python3 | openat | `/etc/gai.conf` |
| 2557 | 98.902 | 8518 | python3 | sendto | `socket:[54357]` |
| 2561 | 98.991 | 8518 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2565 | 99.079 | 8518 | python3 | connect | `ipv6:[...]` |
| 2567 | 99.121 | 8518 | python3 | connect | `sockfd=3` |
| 2568 | 99.138 | 8518 | python3 | connect | `0.0.0.0:8765` |
| 2608 | 100.915 | 8518 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2612 | 101.012 | 8518 | python3 | openat | `/etc/nsswitch.conf` |
| 2619 | 101.175 | 8518 | python3 | openat | `/etc/host.conf` |
| 2625 | 101.298 | 8518 | python3 | openat | `/etc/resolv.conf` |
| 2631 | 101.423 | 8518 | python3 | openat | `/etc/hosts` |
| 2639 | 101.581 | 8518 | python3 | openat | `/etc/hosts` |
| 2649 | 527.260 | 8519 | sleep | exit_group | `code=0` |
| 2685 | 530.532 | 8514 | bash | clone | `` |
| 2702 | 531.837 | 8520 | bash | execve | `/usr/bin/curl` |
| 3018 | 542.101 | 8520 | curl | openat | `/etc/gnutls/config` |
| 3065 | 543.674 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3067 | 543.710 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3076 | 543.881 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3078 | 543.915 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3082 | 543.992 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3084 | 544.025 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3088 | 544.101 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3090 | 544.135 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3094 | 544.219 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3096 | 544.254 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3100 | 544.328 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3102 | 544.363 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3106 | 544.446 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3108 | 544.481 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3111 | 544.533 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3115 | 544.607 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3117 | 544.640 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3121 | 544.717 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3123 | 544.749 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3127 | 544.831 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3129 | 544.865 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3133 | 544.939 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3135 | 544.976 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3139 | 545.050 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3141 | 545.085 | 8520 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3145 | 545.169 | 8520 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3146 | 545.188 | 8520 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 3149 | 545.253 | 8520 | curl | connect | `unix:/var/run/nscd/socket` |
| 3152 | 545.316 | 8520 | curl | connect | `unix:/var/run/nscd/socket` |
| 3156 | 545.386 | 8520 | curl | openat | `/etc/nsswitch.conf` |
| 3162 | 545.498 | 8520 | curl | openat | `/etc/passwd` |
| 3167 | 545.586 | 8520 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3191 | 546.292 | 8520 | curl | connect | `127.0.0.1:8765` |
| 3195 | 546.427 | 8518 | python3 | accept4 | `sockfd=3` |
| 3207 | 546.628 | 8520 | curl | sendto | `socket:[51945]` |
| 3215 | 546.743 | 8518 | python3 | clone3 | `` |
| 3231 | 547.135 | 8521 | python3 | recvfrom | `socket:[54362]` |
| 3241 | 547.564 | 8521 | python3 | openat | `/etc/mime.types` |
| 3267 | 550.354 | 8521 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 3273 | 550.588 | 8521 | python3 | sendto | `socket:[54362]` |
| 3278 | 550.729 | 8521 | python3 | sendto | `socket:[54362]` |
| 3281 | 550.780 | 8520 | curl | recvfrom | `socket:[51945]` |
| 3283 | 550.819 | 8520 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3293 | 551.018 | 8521 | python3 | exit | `code=0` |
| 3294 | 551.033 | 8520 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 3310 | 551.542 | 8520 | curl | exit_group | `code=0` |
| 3346 | 552.725 | 8514 | bash | clone | `` |
| 3363 | 553.130 | 8522 | bash | execve | `/usr/bin/chmod` |
| 3400 | 554.175 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3402 | 554.213 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3411 | 554.378 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3413 | 554.411 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3417 | 554.488 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3419 | 554.520 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3423 | 554.594 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3425 | 554.629 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3429 | 554.702 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3431 | 554.735 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3435 | 554.808 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3437 | 554.841 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3441 | 554.925 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3443 | 554.959 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3446 | 555.009 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3450 | 555.084 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3452 | 555.118 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3456 | 555.197 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3458 | 555.231 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3462 | 555.312 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3464 | 555.346 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3468 | 555.428 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3470 | 555.462 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3474 | 555.536 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3476 | 555.570 | 8522 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3482 | 555.679 | 8522 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 3485 | 555.749 | 8522 | chmod | exit_group | `code=0` |
| 3495 | 556.047 | 8514 | bash | clone | `` |
| 3512 | 556.418 | 8523 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 3552 | 557.409 | 8523 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3566 | 557.640 | 8523 | downloaded.sh | clone | `` |
| 3587 | 558.068 | 8524 | downloaded.sh | execve | `/usr/bin/date` |
| 3624 | 559.281 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3626 | 559.324 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3635 | 559.530 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3637 | 559.571 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3641 | 559.667 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3643 | 559.705 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3647 | 559.802 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3649 | 559.848 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3653 | 559.942 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3655 | 559.975 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3659 | 560.058 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3661 | 560.108 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3665 | 560.227 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3667 | 560.270 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3670 | 560.331 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3674 | 560.425 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3676 | 560.466 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3680 | 560.565 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3682 | 560.606 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3686 | 560.706 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3688 | 560.749 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3692 | 560.838 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3694 | 560.880 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3698 | 560.971 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3700 | 561.013 | 8524 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3704 | 561.118 | 8524 | date | openat | `/etc/localtime` |
| 3717 | 561.410 | 8524 | date | exit_group | `code=0` |
| 3736 | 561.810 | 8523 | downloaded.sh | vfork | `` |
| 3738 | 561.882 | 8525 | downloaded.sh | execve | `/usr/bin/sleep` |
| 3777 | 562.829 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3779 | 562.862 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3788 | 563.023 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3790 | 563.057 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3794 | 563.132 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3796 | 563.173 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3800 | 563.248 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3802 | 563.281 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3806 | 563.355 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3808 | 563.388 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3812 | 563.459 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3814 | 563.494 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3818 | 563.577 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3820 | 563.611 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3823 | 563.661 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3827 | 563.759 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3829 | 563.804 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3833 | 563.905 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3835 | 563.947 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3839 | 564.054 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3841 | 564.095 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3845 | 564.481 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3847 | 564.706 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3851 | 564.799 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3853 | 564.834 | 8525 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3875 | 765.492 | 8525 | sleep | exit_group | `code=0` |
| 3879 | 765.842 | 8523 | downloaded.sh | exit_group | `code=0` |
| 3927 | 767.976 | 8514 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 63.048 ms |
| Workload CPU (user+sys) | 82.880 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 4.488 ms |
| Evidence size | 1330074 bytes |

