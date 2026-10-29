# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | D |
| Events recorded | 3929 |
| Failed exec attempts removed | 12 |
| Duration | 794.504 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_D_r3.json` (1330715 bytes) |
| SHA-256 | `d64d270665c971d7f8c21d0de0e3f1af090ead8f518df3f91ce930afd1ec233e` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_D_r3.json.sha256`

## 1. Process tree

- `7558` /usr/bin/bash
  - `7559` /usr/bin/rm
  - `7560` /usr/bin/mkdir
  - `7561` /usr/bin/cat
  - `7562` /usr/bin/python3
  - `7563` /usr/bin/sleep
  - `7564` /usr/bin/curl
  - `7565` /usr/bin/python3
  - `7566` /usr/bin/chmod
  - `7567` /tmp/ft_scenario01/downloaded.sh
    - `7568` /usr/bin/date
    - `7569` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7558 (?) executed `/usr/bin/bash`
- +7.156 ms pid 7559 (bash) executed `/usr/bin/rm`
- +12.210 ms pid 7560 (bash) executed `/usr/bin/mkdir`
- +17.209 ms pid 7561 (bash) executed `/usr/bin/cat`
- +22.109 ms pid 7562 (bash) executed `/usr/bin/python3`
- +22.135 ms pid 7563 (bash) executed `/usr/bin/sleep`
- +535.493 ms pid 7564 (bash) executed `/usr/bin/curl`
- +566.331 ms pid 7566 (bash) executed `/usr/bin/chmod`
- +570.543 ms pid 7567 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +573.632 ms pid 7568 (downloaded.sh) executed `/usr/bin/date`
- +577.836 ms pid 7569 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +97.507 ms pid 7562 (python3) connected to `unix:/var/run/nscd/socket`
- +97.615 ms pid 7562 (python3) connected to `ipv6:[...]`
- +97.672 ms pid 7562 (python3) connected to `sockfd=3`
- +97.702 ms pid 7562 (python3) connected to `0.0.0.0:8765`
- +100.490 ms pid 7562 (python3) connected to `unix:/var/run/nscd/socket`
- +557.921 ms pid 7564 (curl) connected to `unix:/var/run/nscd/socket`
- +558.006 ms pid 7564 (curl) connected to `unix:/var/run/nscd/socket`
- +559.022 ms pid 7564 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +17.020 ms by pid 7561 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +563.769 ms by pid 7564 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +569.741 ms pid 7566 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +10.659 ms pid 7559 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +10.733 ms pid 7559 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +10.792 ms pid 7559 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +558.255 ms pid 7564 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +570.543 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7567 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +10.733 ms #386 `unlinkat` by pid 7559 (rm)
    - +563.769 ms #3285 `openat` by pid 7564 (curl)
    - +564.000 ms #3295 `write` by pid 7564 (curl)
    - +564.041 ms #3297 `close` by pid 7564 (curl)
    - +569.741 ms #3484 `fchmodat` by pid 7566 (chmod)
    - +570.543 ms #3514 `execve` by pid 7567 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7558 | ? | execve | `/usr/bin/bash` |
| 49 | 1.469 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.513 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.725 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.766 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.862 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.902 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 1.994 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 2.037 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 2.128 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 2.170 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.262 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.304 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.408 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.448 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.510 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.615 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.656 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.755 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.798 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.899 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.940 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 3.032 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 3.074 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 3.171 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 3.212 | 7558 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 5.910 | 7558 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 239 | 6.748 | 7558 | bash | clone | `` |
| 256 | 7.156 | 7559 | bash | execve | `/usr/bin/rm` |
| 293 | 8.490 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 8.536 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 8.747 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 8.790 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 8.883 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 8.926 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 9.018 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 9.059 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 9.151 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 9.192 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 9.282 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 9.324 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 9.428 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 9.471 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 9.533 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 9.629 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 9.672 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 9.770 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 9.814 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 9.931 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 9.988 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 10.118 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 10.165 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 10.260 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 10.303 | 7559 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 10.459 | 7559 | rm | openat | `/tmp/ft_scenario01` |
| 385 | 10.659 | 7559 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 386 | 10.733 | 7559 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 388 | 10.792 | 7559 | rm | unlinkat | `/tmp/ft_scenario01` |
| 393 | 10.954 | 7559 | rm | exit_group | `code=0` |
| 427 | 11.806 | 7558 | bash | clone | `` |
| 444 | 12.210 | 7560 | bash | execve | `/usr/bin/mkdir` |
| 508 | 14.039 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 510 | 14.074 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 519 | 14.239 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 521 | 14.273 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 525 | 14.350 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 527 | 14.383 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 531 | 14.463 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 533 | 14.496 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 537 | 14.570 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 539 | 14.605 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 543 | 14.680 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 545 | 14.730 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 549 | 14.815 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 551 | 14.850 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 554 | 14.900 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 558 | 14.976 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 560 | 15.009 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 564 | 15.083 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 566 | 15.118 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 570 | 15.198 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 572 | 15.233 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 576 | 15.307 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 578 | 15.342 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 582 | 15.422 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 584 | 15.455 | 7560 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 595 | 15.739 | 7560 | mkdir | exit_group | `code=0` |
| 634 | 16.634 | 7558 | bash | clone | `` |
| 651 | 17.020 | 7561 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 660 | 17.209 | 7561 | bash | execve | `/usr/bin/cat` |
| 697 | 18.347 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 699 | 18.384 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 708 | 18.550 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 710 | 18.585 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 714 | 18.663 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 716 | 18.700 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 720 | 18.775 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 722 | 18.811 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 726 | 18.886 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 728 | 18.921 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 732 | 18.995 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 734 | 19.031 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 738 | 19.115 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 740 | 19.149 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 743 | 19.201 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 747 | 19.281 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 749 | 19.321 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 753 | 19.427 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 755 | 19.472 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 759 | 19.577 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 761 | 19.625 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 765 | 19.720 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 767 | 19.765 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 771 | 19.863 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 773 | 19.987 | 7561 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 782 | 20.245 | 7561 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 788 | 20.404 | 7561 | cat | exit_group | `code=0` |
| 798 | 20.721 | 7558 | bash | clone | `` |
| 873 | 21.749 | 7558 | bash | clone | `` |
| 900 | 22.109 | 7562 | bash | execve | `/usr/bin/python3` |
| 902 | 22.135 | 7563 | bash | execve | `/usr/bin/sleep` |
| 978 | 23.387 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 982 | 23.432 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 997 | 23.630 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1000 | 23.671 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1007 | 23.792 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1010 | 23.835 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1017 | 23.931 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1019 | 23.969 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1026 | 24.060 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1030 | 24.106 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1037 | 24.192 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1039 | 24.219 | 7562 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1040 | 24.233 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1043 | 24.270 | 7562 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1049 | 24.340 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1052 | 24.380 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1058 | 24.449 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1063 | 24.539 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1066 | 24.652 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1073 | 24.771 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1076 | 24.810 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1080 | 24.909 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1082 | 24.949 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1086 | 25.041 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1088 | 25.082 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1092 | 25.173 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1094 | 25.213 | 7563 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1130 | 27.815 | 7562 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 1131 | 27.856 | 7562 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 1134 | 27.942 | 7562 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 1135 | 27.967 | 7562 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 1136 | 27.993 | 7562 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 1147 | 29.384 | 7562 | python3 | openat | `/etc/localtime` |
| 1302 | 36.020 | 7562 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1308 | 36.247 | 7562 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1317 | 36.775 | 7562 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1348 | 38.137 | 7562 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1356 | 38.309 | 7562 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1364 | 38.584 | 7562 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1612 | 50.378 | 7562 | python3 | openat | `/tmp/ft_scenario01` |
| 2547 | 97.126 | 7562 | python3 | openat | `/etc/gai.conf` |
| 2557 | 97.396 | 7562 | python3 | sendto | `socket:[45762]` |
| 2561 | 97.507 | 7562 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2565 | 97.615 | 7562 | python3 | connect | `ipv6:[...]` |
| 2567 | 97.672 | 7562 | python3 | connect | `sockfd=3` |
| 2568 | 97.702 | 7562 | python3 | connect | `0.0.0.0:8765` |
| 2608 | 100.490 | 7562 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2612 | 100.601 | 7562 | python3 | openat | `/etc/nsswitch.conf` |
| 2619 | 100.783 | 7562 | python3 | openat | `/etc/host.conf` |
| 2625 | 100.912 | 7562 | python3 | openat | `/etc/resolv.conf` |
| 2631 | 101.053 | 7562 | python3 | openat | `/etc/hosts` |
| 2639 | 101.236 | 7562 | python3 | openat | `/etc/hosts` |
| 2649 | 526.458 | 7563 | sleep | exit_group | `code=0` |
| 2685 | 533.884 | 7558 | bash | clone | `` |
| 2702 | 535.493 | 7564 | bash | execve | `/usr/bin/curl` |
| 3018 | 553.523 | 7564 | curl | openat | `/etc/gnutls/config` |
| 3065 | 555.701 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3067 | 555.777 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3076 | 556.022 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3078 | 556.070 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3082 | 556.177 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3084 | 556.223 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3088 | 556.330 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3090 | 556.376 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3094 | 556.478 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3096 | 556.524 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3100 | 556.622 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3102 | 556.672 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3106 | 556.820 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3108 | 556.869 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3111 | 556.942 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3115 | 557.042 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3117 | 557.088 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3121 | 557.190 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3123 | 557.236 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3127 | 557.343 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3129 | 557.392 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3133 | 557.496 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3135 | 557.545 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3139 | 557.647 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3141 | 557.701 | 7564 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3145 | 557.809 | 7564 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3146 | 557.835 | 7564 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 3149 | 557.921 | 7564 | curl | connect | `unix:/var/run/nscd/socket` |
| 3152 | 558.006 | 7564 | curl | connect | `unix:/var/run/nscd/socket` |
| 3156 | 558.100 | 7564 | curl | openat | `/etc/nsswitch.conf` |
| 3162 | 558.255 | 7564 | curl | openat | `/etc/passwd` |
| 3167 | 558.378 | 7564 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3191 | 559.022 | 7564 | curl | connect | `127.0.0.1:8765` |
| 3194 | 559.158 | 7562 | python3 | accept4 | `sockfd=3` |
| 3211 | 559.637 | 7562 | python3 | clone3 | `` |
| 3212 | 559.646 | 7564 | curl | sendto | `socket:[48269]` |
| 3231 | 560.115 | 7565 | python3 | recvfrom | `socket:[46962]` |
| 3241 | 560.501 | 7565 | python3 | openat | `/etc/mime.types` |
| 3267 | 563.024 | 7565 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 3273 | 563.394 | 7565 | python3 | sendto | `socket:[46962]` |
| 3278 | 563.628 | 7564 | curl | recvfrom | `socket:[48269]` |
| 3280 | 563.673 | 7565 | python3 | sendto | `socket:[46962]` |
| 3283 | 563.730 | 7564 | curl | recvfrom | `socket:[48269]` |
| 3285 | 563.769 | 7564 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3295 | 564.000 | 7564 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 3296 | 564.022 | 7565 | python3 | exit | `code=0` |
| 3312 | 564.569 | 7564 | curl | exit_group | `code=0` |
| 3348 | 565.884 | 7558 | bash | clone | `` |
| 3365 | 566.331 | 7566 | bash | execve | `/usr/bin/chmod` |
| 3402 | 567.676 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3404 | 567.736 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3413 | 567.960 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3415 | 568.008 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3419 | 568.111 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3421 | 568.158 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3425 | 568.262 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3427 | 568.310 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3431 | 568.412 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3433 | 568.458 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3437 | 568.558 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3439 | 568.604 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3443 | 568.718 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3445 | 568.765 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3448 | 568.837 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3452 | 568.936 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3454 | 568.985 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3458 | 569.089 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3460 | 569.136 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3464 | 569.243 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3466 | 569.289 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3470 | 569.392 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3472 | 569.437 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3476 | 569.539 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3478 | 569.587 | 7566 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3484 | 569.741 | 7566 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 3487 | 569.835 | 7566 | chmod | exit_group | `code=0` |
| 3497 | 570.156 | 7558 | bash | clone | `` |
| 3514 | 570.543 | 7567 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 3554 | 571.832 | 7567 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3568 | 572.150 | 7567 | downloaded.sh | clone | `` |
| 3589 | 573.632 | 7568 | downloaded.sh | execve | `/usr/bin/date` |
| 3626 | 574.954 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3628 | 575.008 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3637 | 575.233 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3639 | 575.271 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3643 | 575.350 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3645 | 575.383 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3649 | 575.458 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3651 | 575.509 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3655 | 575.607 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3657 | 575.653 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3661 | 575.761 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3663 | 575.796 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3667 | 575.881 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3669 | 575.918 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3672 | 575.990 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3676 | 576.088 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3678 | 576.133 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3682 | 576.229 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3684 | 576.276 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3688 | 576.384 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3690 | 576.433 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3694 | 576.536 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3696 | 576.573 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3700 | 576.682 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3702 | 576.736 | 7568 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3706 | 576.857 | 7568 | date | openat | `/etc/localtime` |
| 3719 | 577.196 | 7568 | date | exit_group | `code=0` |
| 3738 | 577.746 | 7567 | downloaded.sh | vfork | `` |
| 3740 | 577.836 | 7569 | downloaded.sh | execve | `/usr/bin/sleep` |
| 3779 | 581.958 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3781 | 582.019 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3790 | 582.286 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3792 | 582.333 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3796 | 582.488 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3798 | 582.557 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3802 | 583.051 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3804 | 583.114 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3808 | 583.241 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3810 | 583.299 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3814 | 583.430 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3816 | 583.486 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3820 | 583.621 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3822 | 583.716 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3825 | 583.858 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3829 | 584.004 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3831 | 584.063 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3835 | 584.205 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3837 | 584.267 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3841 | 584.922 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3843 | 584.987 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3847 | 585.105 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3849 | 585.158 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3853 | 585.278 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3855 | 585.329 | 7569 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3877 | 786.348 | 7569 | sleep | exit_group | `code=0` |
| 3881 | 787.029 | 7567 | downloaded.sh | exit_group | `code=0` |
| 3929 | 793.555 | 7558 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 77.492 ms |
| Workload CPU (user+sys) | 89.794 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 13.975 ms |
| Evidence size | 1330715 bytes |

