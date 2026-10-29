# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | D |
| Events recorded | 3927 |
| Failed exec attempts removed | 12 |
| Duration | 770.455 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_D_r4.json` (1330060 bytes) |
| SHA-256 | `f00d63c09ddce1ae744b067189b9f0ec10ffeb4f5943b6f4e2cd500e515c7d57` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_D_r4.json.sha256`

## 1. Process tree

- `7712` /usr/bin/bash
  - `7713` /usr/bin/rm
  - `7714` /usr/bin/mkdir
  - `7715` /usr/bin/cat
  - `7716` /usr/bin/python3
  - `7717` /usr/bin/sleep
  - `7718` /usr/bin/curl
  - `7719` /usr/bin/python3
  - `7720` /usr/bin/chmod
  - `7721` /tmp/ft_scenario01/downloaded.sh
    - `7722` /usr/bin/date
    - `7723` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7712 (?) executed `/usr/bin/bash`
- +6.652 ms pid 7713 (bash) executed `/usr/bin/rm`
- +10.629 ms pid 7714 (bash) executed `/usr/bin/mkdir`
- +15.825 ms pid 7715 (bash) executed `/usr/bin/cat`
- +21.279 ms pid 7716 (bash) executed `/usr/bin/python3`
- +21.362 ms pid 7717 (bash) executed `/usr/bin/sleep`
- +526.857 ms pid 7718 (bash) executed `/usr/bin/curl`
- +550.480 ms pid 7720 (bash) executed `/usr/bin/chmod`
- +555.220 ms pid 7721 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +557.492 ms pid 7722 (downloaded.sh) executed `/usr/bin/date`
- +561.174 ms pid 7723 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +102.255 ms pid 7716 (python3) connected to `unix:/var/run/nscd/socket`
- +102.406 ms pid 7716 (python3) connected to `ipv6:[...]`
- +102.475 ms pid 7716 (python3) connected to `sockfd=3`
- +102.496 ms pid 7716 (python3) connected to `0.0.0.0:8765`
- +104.818 ms pid 7716 (python3) connected to `unix:/var/run/nscd/socket`
- +542.563 ms pid 7718 (curl) connected to `unix:/var/run/nscd/socket`
- +542.678 ms pid 7718 (curl) connected to `unix:/var/run/nscd/socket`
- +543.662 ms pid 7718 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +15.641 ms by pid 7715 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +547.971 ms by pid 7718 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +554.411 ms pid 7720 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +9.436 ms pid 7713 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +9.482 ms pid 7713 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +9.527 ms pid 7713 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +542.932 ms pid 7718 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +555.220 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7721 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +9.482 ms #386 `unlinkat` by pid 7713 (rm)
    - +547.971 ms #3284 `openat` by pid 7718 (curl)
    - +548.222 ms #3294 `write` by pid 7718 (curl)
    - +548.266 ms #3295 `close` by pid 7718 (curl)
    - +554.411 ms #3482 `fchmodat` by pid 7720 (chmod)
    - +555.220 ms #3512 `execve` by pid 7721 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7712 | ? | execve | `/usr/bin/bash` |
| 49 | 1.731 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.785 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 2.042 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 2.093 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 2.215 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 2.266 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 2.394 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 2.491 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 2.636 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 2.686 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.782 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.817 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.904 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.937 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.989 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 3.068 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 3.103 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 3.179 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 3.305 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 3.406 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 3.442 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 3.517 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 3.551 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 3.637 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 3.670 | 7712 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 5.132 | 7712 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 239 | 6.097 | 7712 | bash | clone | `` |
| 256 | 6.652 | 7713 | bash | execve | `/usr/bin/rm` |
| 293 | 7.748 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 7.784 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 7.945 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 7.980 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 8.055 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 8.090 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 8.168 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 8.201 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 8.276 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 8.309 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 8.381 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 8.416 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 8.499 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 8.533 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 8.584 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 8.665 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 8.700 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 8.774 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 8.806 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 8.893 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 8.927 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 9.001 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 9.036 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 9.111 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 9.145 | 7713 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 9.275 | 7713 | rm | openat | `/tmp/ft_scenario01` |
| 385 | 9.436 | 7713 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 386 | 9.482 | 7713 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 388 | 9.527 | 7713 | rm | unlinkat | `/tmp/ft_scenario01` |
| 393 | 9.665 | 7713 | rm | exit_group | `code=0` |
| 427 | 10.290 | 7712 | bash | clone | `` |
| 444 | 10.629 | 7714 | bash | execve | `/usr/bin/mkdir` |
| 508 | 12.255 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 510 | 12.293 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 519 | 12.474 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 521 | 12.515 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 525 | 12.592 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 527 | 12.636 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 531 | 12.725 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 533 | 12.762 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 537 | 12.840 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 539 | 12.878 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 543 | 12.962 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 545 | 13.002 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 549 | 13.093 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 551 | 13.132 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 554 | 13.184 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 558 | 13.265 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 560 | 13.302 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 564 | 13.389 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 566 | 13.456 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 570 | 13.570 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 572 | 13.631 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 576 | 13.777 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 578 | 13.833 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 582 | 13.918 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 584 | 13.951 | 7714 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 595 | 14.207 | 7714 | mkdir | exit_group | `code=0` |
| 634 | 15.229 | 7712 | bash | clone | `` |
| 651 | 15.641 | 7715 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 660 | 15.825 | 7715 | bash | execve | `/usr/bin/cat` |
| 697 | 16.790 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 699 | 16.825 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 708 | 16.986 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 710 | 17.018 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 714 | 17.094 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 716 | 17.127 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 720 | 17.199 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 722 | 17.235 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 726 | 17.309 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 728 | 17.342 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 732 | 17.414 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 734 | 17.447 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 738 | 17.529 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 740 | 17.562 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 743 | 17.636 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 747 | 17.737 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 749 | 17.783 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 753 | 17.889 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 755 | 17.935 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 759 | 18.098 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 761 | 18.145 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 765 | 18.249 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 767 | 18.325 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 771 | 18.428 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 773 | 18.471 | 7715 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 782 | 18.735 | 7715 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 788 | 18.921 | 7715 | cat | exit_group | `code=0` |
| 798 | 19.394 | 7712 | bash | clone | `` |
| 875 | 20.856 | 7712 | bash | clone | `` |
| 898 | 21.279 | 7716 | bash | execve | `/usr/bin/python3` |
| 902 | 21.362 | 7717 | bash | execve | `/usr/bin/sleep` |
| 980 | 22.767 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 983 | 22.816 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 998 | 23.037 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1001 | 23.081 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1007 | 23.181 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1011 | 23.233 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1017 | 23.327 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1019 | 23.367 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1026 | 23.465 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1028 | 23.507 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1036 | 23.619 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1039 | 23.667 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1040 | 23.681 | 7716 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1044 | 23.734 | 7716 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1047 | 23.781 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1051 | 23.829 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1056 | 23.896 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1063 | 23.997 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1065 | 24.035 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1070 | 24.136 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1073 | 24.175 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1080 | 24.277 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1082 | 24.315 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1086 | 24.405 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1088 | 24.445 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1092 | 24.536 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1094 | 24.576 | 7717 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1130 | 27.052 | 7716 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 1131 | 27.080 | 7716 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 1134 | 27.153 | 7716 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 1135 | 27.173 | 7716 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 1136 | 27.192 | 7716 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 1147 | 28.324 | 7716 | python3 | openat | `/etc/localtime` |
| 1302 | 34.498 | 7716 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1308 | 34.762 | 7716 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1317 | 35.559 | 7716 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1348 | 37.247 | 7716 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1356 | 37.490 | 7716 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1364 | 37.696 | 7716 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1612 | 49.737 | 7716 | python3 | openat | `/tmp/ft_scenario01` |
| 2547 | 101.881 | 7716 | python3 | openat | `/etc/gai.conf` |
| 2557 | 102.133 | 7716 | python3 | sendto | `socket:[46051]` |
| 2561 | 102.255 | 7716 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2565 | 102.406 | 7716 | python3 | connect | `ipv6:[...]` |
| 2567 | 102.475 | 7716 | python3 | connect | `sockfd=3` |
| 2568 | 102.496 | 7716 | python3 | connect | `0.0.0.0:8765` |
| 2608 | 104.818 | 7716 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2612 | 104.935 | 7716 | python3 | openat | `/etc/nsswitch.conf` |
| 2619 | 105.098 | 7716 | python3 | openat | `/etc/host.conf` |
| 2625 | 105.238 | 7716 | python3 | openat | `/etc/resolv.conf` |
| 2631 | 105.385 | 7716 | python3 | openat | `/etc/hosts` |
| 2639 | 105.551 | 7716 | python3 | openat | `/etc/hosts` |
| 2649 | 525.237 | 7717 | sleep | exit_group | `code=0` |
| 2685 | 526.289 | 7712 | bash | clone | `` |
| 2702 | 526.857 | 7718 | bash | execve | `/usr/bin/curl` |
| 3018 | 538.167 | 7718 | curl | openat | `/etc/gnutls/config` |
| 3065 | 539.817 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3067 | 539.862 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3076 | 540.070 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3078 | 540.112 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3082 | 540.205 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3084 | 540.246 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3088 | 540.340 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3090 | 540.382 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3094 | 540.473 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3096 | 540.516 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3100 | 540.615 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3102 | 540.660 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3106 | 540.884 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3108 | 540.938 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3111 | 541.023 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3115 | 541.212 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3117 | 541.277 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3121 | 541.429 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3123 | 541.474 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3127 | 541.635 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3129 | 541.708 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3133 | 541.900 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3135 | 541.958 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3139 | 542.085 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3141 | 542.183 | 7718 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3145 | 542.417 | 7718 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3146 | 542.463 | 7718 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 3149 | 542.563 | 7718 | curl | connect | `unix:/var/run/nscd/socket` |
| 3152 | 542.678 | 7718 | curl | connect | `unix:/var/run/nscd/socket` |
| 3156 | 542.778 | 7718 | curl | openat | `/etc/nsswitch.conf` |
| 3162 | 542.932 | 7718 | curl | openat | `/etc/passwd` |
| 3167 | 543.046 | 7718 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3191 | 543.662 | 7718 | curl | connect | `127.0.0.1:8765` |
| 3195 | 543.819 | 7716 | python3 | accept4 | `sockfd=3` |
| 3208 | 544.017 | 7718 | curl | sendto | `socket:[46060]` |
| 3215 | 544.130 | 7716 | python3 | clone3 | `` |
| 3231 | 544.493 | 7719 | python3 | recvfrom | `socket:[49199]` |
| 3241 | 544.895 | 7719 | python3 | openat | `/etc/mime.types` |
| 3267 | 547.499 | 7719 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 3273 | 547.723 | 7719 | python3 | sendto | `socket:[49199]` |
| 3278 | 547.852 | 7719 | python3 | sendto | `socket:[49199]` |
| 3282 | 547.920 | 7718 | curl | recvfrom | `socket:[46060]` |
| 3284 | 547.971 | 7718 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3291 | 548.133 | 7719 | python3 | exit | `code=0` |
| 3294 | 548.222 | 7718 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 3310 | 548.900 | 7718 | curl | exit_group | `code=0` |
| 3346 | 550.100 | 7712 | bash | clone | `` |
| 3363 | 550.480 | 7720 | bash | execve | `/usr/bin/chmod` |
| 3400 | 552.158 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3402 | 552.237 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3411 | 552.535 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3413 | 552.581 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3417 | 552.694 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3419 | 552.734 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3423 | 552.819 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3425 | 552.859 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3429 | 552.937 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3431 | 552.977 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3435 | 553.056 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3437 | 553.092 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3441 | 553.193 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3443 | 553.250 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3446 | 553.319 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3450 | 553.419 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3452 | 553.460 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3456 | 553.557 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3458 | 553.611 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3462 | 553.718 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3464 | 553.766 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3468 | 554.103 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3470 | 554.144 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3474 | 554.241 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3476 | 554.275 | 7720 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3482 | 554.411 | 7720 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 3485 | 554.497 | 7720 | chmod | exit_group | `code=0` |
| 3495 | 554.839 | 7712 | bash | clone | `` |
| 3512 | 555.220 | 7721 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 3552 | 556.485 | 7721 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3566 | 556.838 | 7721 | downloaded.sh | clone | `` |
| 3587 | 557.492 | 7722 | downloaded.sh | execve | `/usr/bin/date` |
| 3624 | 558.840 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3626 | 558.875 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3635 | 559.051 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3637 | 559.086 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3641 | 559.170 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3643 | 559.211 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3647 | 559.287 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3649 | 559.325 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3653 | 559.406 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3655 | 559.439 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3659 | 559.515 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3661 | 559.550 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3665 | 559.642 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3667 | 559.677 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3670 | 559.729 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3674 | 559.814 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3676 | 559.848 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3680 | 559.928 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3682 | 559.961 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3686 | 560.047 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3688 | 560.086 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3692 | 560.165 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3694 | 560.201 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3698 | 560.279 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3700 | 560.316 | 7722 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3704 | 560.403 | 7722 | date | openat | `/etc/localtime` |
| 3717 | 560.650 | 7722 | date | exit_group | `code=0` |
| 3736 | 561.099 | 7721 | downloaded.sh | vfork | `` |
| 3738 | 561.174 | 7723 | downloaded.sh | execve | `/usr/bin/sleep` |
| 3777 | 562.314 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3779 | 562.356 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3788 | 562.537 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3790 | 562.571 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3794 | 562.666 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3796 | 562.701 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3800 | 562.786 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3802 | 562.819 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3806 | 562.898 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3808 | 562.935 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3812 | 563.010 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3814 | 563.046 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3818 | 563.135 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3820 | 563.171 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3823 | 563.223 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3827 | 563.304 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3829 | 563.339 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3833 | 563.418 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3835 | 563.455 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3839 | 563.542 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3841 | 563.575 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3845 | 563.662 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3847 | 563.697 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3851 | 563.776 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3853 | 563.813 | 7723 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3875 | 764.647 | 7723 | sleep | exit_group | `code=0` |
| 3879 | 765.111 | 7721 | downloaded.sh | exit_group | `code=0` |
| 3927 | 769.711 | 7712 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 65.430 ms |
| Workload CPU (user+sys) | 84.940 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 6.732 ms |
| Evidence size | 1330060 bytes |

