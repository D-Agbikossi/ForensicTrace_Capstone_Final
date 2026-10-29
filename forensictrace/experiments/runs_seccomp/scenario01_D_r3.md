# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | D |
| Events recorded | 3927 |
| Failed exec attempts removed | 12 |
| Duration | 775.926 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_D_r3.json` (1330073 bytes) |
| SHA-256 | `db94572b4df546fd632d26f0fd0ab823a1d1e0cbb40b9c36ddbfbfbd5fae6c2d` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_D_r3.json.sha256`

## 1. Process tree

- `8359` /usr/bin/bash
  - `8360` /usr/bin/rm
  - `8361` /usr/bin/mkdir
  - `8362` /usr/bin/cat
  - `8363` /usr/bin/python3
  - `8364` /usr/bin/sleep
  - `8365` /usr/bin/curl
  - `8366` /usr/bin/python3
  - `8367` /usr/bin/chmod
  - `8368` /tmp/ft_scenario01/downloaded.sh
    - `8369` /usr/bin/date
    - `8370` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8359 (?) executed `/usr/bin/bash`
- +5.340 ms pid 8360 (bash) executed `/usr/bin/rm`
- +9.386 ms pid 8361 (bash) executed `/usr/bin/mkdir`
- +14.519 ms pid 8362 (bash) executed `/usr/bin/cat`
- +19.217 ms pid 8363 (bash) executed `/usr/bin/python3`
- +19.271 ms pid 8364 (bash) executed `/usr/bin/sleep`
- +527.800 ms pid 8365 (bash) executed `/usr/bin/curl`
- +556.412 ms pid 8367 (bash) executed `/usr/bin/chmod`
- +561.049 ms pid 8368 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +563.465 ms pid 8369 (downloaded.sh) executed `/usr/bin/date`
- +566.759 ms pid 8370 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +93.934 ms pid 8363 (python3) connected to `unix:/var/run/nscd/socket`
- +94.020 ms pid 8363 (python3) connected to `ipv6:[...]`
- +94.064 ms pid 8363 (python3) connected to `sockfd=3`
- +94.080 ms pid 8363 (python3) connected to `0.0.0.0:8765`
- +95.787 ms pid 8363 (python3) connected to `unix:/var/run/nscd/socket`
- +549.172 ms pid 8365 (curl) connected to `unix:/var/run/nscd/socket`
- +549.236 ms pid 8365 (curl) connected to `unix:/var/run/nscd/socket`
- +550.002 ms pid 8365 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +14.339 ms by pid 8362 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +553.830 ms by pid 8365 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +560.012 ms pid 8367 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +8.045 ms pid 8360 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +8.090 ms pid 8360 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +8.134 ms pid 8360 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +549.427 ms pid 8365 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +561.049 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8368 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +8.090 ms #386 `unlinkat` by pid 8360 (rm)
    - +553.830 ms #3283 `openat` by pid 8365 (curl)
    - +554.042 ms #3294 `write` by pid 8365 (curl)
    - +554.082 ms #3295 `close` by pid 8365 (curl)
    - +560.012 ms #3482 `fchmodat` by pid 8367 (chmod)
    - +561.049 ms #3512 `execve` by pid 8368 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8359 | ? | execve | `/usr/bin/bash` |
| 49 | 1.320 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.357 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.526 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.559 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.636 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.673 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 1.748 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 1.782 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 1.856 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 1.890 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 1.964 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 1.998 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.083 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.116 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.167 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.242 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.276 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.349 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.383 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.466 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.501 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 2.575 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 2.609 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 2.691 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 2.725 | 8359 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 4.007 | 8359 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 239 | 4.987 | 8359 | bash | clone | `` |
| 256 | 5.340 | 8360 | bash | execve | `/usr/bin/rm` |
| 293 | 6.315 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 6.352 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 6.512 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 6.546 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 6.626 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 6.660 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 6.764 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 6.798 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 6.874 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 6.907 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 6.980 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 7.014 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 7.110 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 7.145 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 7.196 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 7.271 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 7.306 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 7.381 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 7.414 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 7.495 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 7.528 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 7.604 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 7.638 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 7.723 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 7.757 | 8360 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 7.885 | 8360 | rm | openat | `/tmp/ft_scenario01` |
| 385 | 8.045 | 8360 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 386 | 8.090 | 8360 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 388 | 8.134 | 8360 | rm | unlinkat | `/tmp/ft_scenario01` |
| 393 | 8.261 | 8360 | rm | exit_group | `code=0` |
| 427 | 9.050 | 8359 | bash | clone | `` |
| 444 | 9.386 | 8361 | bash | execve | `/usr/bin/mkdir` |
| 508 | 10.911 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 510 | 10.954 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 519 | 11.162 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 521 | 11.208 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 525 | 11.313 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 527 | 11.373 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 531 | 11.570 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 533 | 11.645 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 537 | 11.784 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 539 | 11.833 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 543 | 11.914 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 545 | 11.957 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 549 | 12.067 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 551 | 12.113 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 554 | 12.176 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 558 | 12.272 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 560 | 12.315 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 564 | 12.410 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 566 | 12.455 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 570 | 12.557 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 572 | 12.602 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 576 | 12.703 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 578 | 12.748 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 582 | 12.844 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 584 | 12.888 | 8361 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 595 | 13.200 | 8361 | mkdir | exit_group | `code=0` |
| 634 | 13.963 | 8359 | bash | clone | `` |
| 651 | 14.339 | 8362 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 660 | 14.519 | 8362 | bash | execve | `/usr/bin/cat` |
| 697 | 15.489 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 699 | 15.524 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 708 | 15.828 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 710 | 15.862 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 714 | 15.938 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 716 | 15.971 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 720 | 16.048 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 722 | 16.082 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 726 | 16.156 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 728 | 16.189 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 732 | 16.260 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 734 | 16.294 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 738 | 16.377 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 740 | 16.409 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 743 | 16.460 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 747 | 16.533 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 749 | 16.568 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 753 | 16.642 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 755 | 16.686 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 759 | 16.800 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 761 | 16.845 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 765 | 16.941 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 767 | 16.985 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 771 | 17.083 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 773 | 17.126 | 8362 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 782 | 17.336 | 8362 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 788 | 17.497 | 8362 | cat | exit_group | `code=0` |
| 798 | 17.805 | 8359 | bash | clone | `` |
| 873 | 18.864 | 8359 | bash | clone | `` |
| 899 | 19.217 | 8363 | bash | execve | `/usr/bin/python3` |
| 902 | 19.271 | 8364 | bash | execve | `/usr/bin/sleep` |
| 978 | 20.571 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 982 | 20.616 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 997 | 20.830 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1000 | 20.869 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1007 | 20.965 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1010 | 21.007 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1017 | 21.092 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1019 | 21.129 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1026 | 21.222 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1029 | 21.264 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1037 | 21.365 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1039 | 21.392 | 8363 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1040 | 21.406 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1043 | 21.444 | 8363 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1049 | 21.514 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1052 | 21.554 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1058 | 21.621 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1063 | 22.063 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1066 | 22.138 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1071 | 22.262 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1074 | 22.317 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1080 | 22.463 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1082 | 22.512 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1086 | 22.632 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1088 | 22.692 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1092 | 22.822 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1094 | 22.875 | 8364 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1130 | 25.381 | 8363 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 1131 | 25.422 | 8363 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 1134 | 25.508 | 8363 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 1135 | 25.535 | 8363 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 1136 | 25.562 | 8363 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 1147 | 27.029 | 8363 | python3 | openat | `/etc/localtime` |
| 1302 | 33.298 | 8363 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1308 | 33.476 | 8363 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1317 | 33.749 | 8363 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1348 | 35.012 | 8363 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1356 | 35.227 | 8363 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1364 | 35.424 | 8363 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1612 | 45.242 | 8363 | python3 | openat | `/tmp/ft_scenario01` |
| 2547 | 93.647 | 8363 | python3 | openat | `/etc/gai.conf` |
| 2557 | 93.845 | 8363 | python3 | sendto | `socket:[51043]` |
| 2561 | 93.934 | 8363 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2565 | 94.020 | 8363 | python3 | connect | `ipv6:[...]` |
| 2567 | 94.064 | 8363 | python3 | connect | `sockfd=3` |
| 2568 | 94.080 | 8363 | python3 | connect | `0.0.0.0:8765` |
| 2608 | 95.787 | 8363 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2612 | 95.866 | 8363 | python3 | openat | `/etc/nsswitch.conf` |
| 2619 | 95.998 | 8363 | python3 | openat | `/etc/host.conf` |
| 2625 | 96.097 | 8363 | python3 | openat | `/etc/resolv.conf` |
| 2631 | 96.207 | 8363 | python3 | openat | `/etc/hosts` |
| 2639 | 96.347 | 8363 | python3 | openat | `/etc/hosts` |
| 2649 | 524.185 | 8364 | sleep | exit_group | `code=0` |
| 2685 | 526.620 | 8359 | bash | clone | `` |
| 2702 | 527.800 | 8365 | bash | execve | `/usr/bin/curl` |
| 3018 | 545.811 | 8365 | curl | openat | `/etc/gnutls/config` |
| 3065 | 547.320 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3067 | 547.363 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3076 | 547.573 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3078 | 547.614 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3082 | 547.710 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3084 | 547.750 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3088 | 547.841 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3090 | 547.883 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3094 | 547.971 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3096 | 548.014 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3100 | 548.103 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3102 | 548.145 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3106 | 548.246 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3108 | 548.290 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3111 | 548.350 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3115 | 548.442 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3117 | 548.482 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3121 | 548.574 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3123 | 548.614 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3127 | 548.736 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3129 | 548.776 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3133 | 548.860 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3135 | 548.894 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3139 | 548.970 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3141 | 549.005 | 8365 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3145 | 549.087 | 8365 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3146 | 549.107 | 8365 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 3149 | 549.172 | 8365 | curl | connect | `unix:/var/run/nscd/socket` |
| 3152 | 549.236 | 8365 | curl | connect | `unix:/var/run/nscd/socket` |
| 3156 | 549.308 | 8365 | curl | openat | `/etc/nsswitch.conf` |
| 3162 | 549.427 | 8365 | curl | openat | `/etc/passwd` |
| 3167 | 549.516 | 8365 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3191 | 550.002 | 8365 | curl | connect | `127.0.0.1:8765` |
| 3195 | 550.136 | 8363 | python3 | accept4 | `sockfd=3` |
| 3208 | 550.347 | 8365 | curl | sendto | `socket:[51755]` |
| 3215 | 550.459 | 8363 | python3 | clone3 | `` |
| 3231 | 550.827 | 8366 | python3 | recvfrom | `socket:[51053]` |
| 3242 | 551.205 | 8366 | python3 | openat | `/etc/mime.types` |
| 3267 | 553.381 | 8366 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 3273 | 553.565 | 8366 | python3 | sendto | `socket:[51053]` |
| 3279 | 553.761 | 8366 | python3 | sendto | `socket:[51053]` |
| 3280 | 553.779 | 8365 | curl | recvfrom | `socket:[51755]` |
| 3283 | 553.830 | 8365 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3293 | 554.022 | 8366 | python3 | exit | `code=0` |
| 3294 | 554.042 | 8365 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 3310 | 554.568 | 8365 | curl | exit_group | `code=0` |
| 3346 | 555.918 | 8359 | bash | clone | `` |
| 3363 | 556.412 | 8367 | bash | execve | `/usr/bin/chmod` |
| 3400 | 557.812 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3402 | 557.865 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3411 | 558.094 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3413 | 558.146 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3417 | 558.276 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3419 | 558.325 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3423 | 558.429 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3425 | 558.483 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3429 | 558.590 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3431 | 558.642 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3435 | 558.748 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3437 | 558.797 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3441 | 558.908 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3443 | 558.956 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3446 | 559.029 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3450 | 559.130 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3452 | 559.176 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3456 | 559.281 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3458 | 559.329 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3462 | 559.437 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3464 | 559.488 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3468 | 559.603 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3470 | 559.658 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3474 | 559.802 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3476 | 559.848 | 8367 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3482 | 560.012 | 8367 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 3485 | 560.132 | 8367 | chmod | exit_group | `code=0` |
| 3495 | 560.574 | 8359 | bash | clone | `` |
| 3512 | 561.049 | 8368 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 3552 | 562.712 | 8368 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3566 | 563.013 | 8368 | downloaded.sh | clone | `` |
| 3587 | 563.465 | 8369 | downloaded.sh | execve | `/usr/bin/date` |
| 3624 | 564.484 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3626 | 564.519 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3635 | 564.688 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3637 | 564.723 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3641 | 564.800 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3643 | 564.835 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3647 | 564.908 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3649 | 564.941 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3653 | 565.017 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3655 | 565.050 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3659 | 565.122 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3661 | 565.156 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3665 | 565.241 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3667 | 565.275 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3670 | 565.326 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3674 | 565.400 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3676 | 565.434 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3680 | 565.511 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3682 | 565.543 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3686 | 565.623 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3688 | 565.658 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3692 | 565.787 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3694 | 565.824 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3698 | 565.900 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3700 | 565.934 | 8369 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3704 | 566.021 | 8369 | date | openat | `/etc/localtime` |
| 3717 | 566.244 | 8369 | date | exit_group | `code=0` |
| 3736 | 566.691 | 8368 | downloaded.sh | vfork | `` |
| 3738 | 566.759 | 8370 | downloaded.sh | execve | `/usr/bin/sleep` |
| 3777 | 567.654 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3779 | 567.698 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3788 | 567.859 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3790 | 567.894 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3794 | 567.968 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3796 | 568.002 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3800 | 568.076 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3802 | 568.112 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3806 | 568.187 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3808 | 568.219 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3812 | 568.292 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3814 | 568.326 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3818 | 568.408 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3820 | 568.442 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3823 | 568.493 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3827 | 568.567 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3829 | 568.602 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3833 | 568.681 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3835 | 568.714 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3839 | 568.793 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3841 | 568.827 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3845 | 568.900 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3847 | 568.935 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3851 | 569.009 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3853 | 569.043 | 8370 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3875 | 769.897 | 8370 | sleep | exit_group | `code=0` |
| 3879 | 770.456 | 8368 | downloaded.sh | exit_group | `code=0` |
| 3927 | 775.176 | 8359 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 69.723 ms |
| Workload CPU (user+sys) | 84.238 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 8.137 ms |
| Evidence size | 1330073 bytes |

