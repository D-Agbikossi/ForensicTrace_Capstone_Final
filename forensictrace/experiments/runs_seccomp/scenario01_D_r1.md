# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | D |
| Events recorded | 3927 |
| Failed exec attempts removed | 12 |
| Duration | 762.828 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_D_r1.json` (1330056 bytes) |
| SHA-256 | `9f83d65c63f80c86ec82d8a6946dfdcf604081ae5ee83f8c38183793611ad957` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_D_r1.json.sha256`

## 1. Process tree

- `7937` /usr/bin/bash
  - `7938` /usr/bin/rm
  - `7939` /usr/bin/mkdir
  - `7940` /usr/bin/cat
  - `7941` /usr/bin/python3
  - `7942` /usr/bin/sleep
  - `7943` /usr/bin/curl
  - `7944` /usr/bin/python3
  - `7945` /usr/bin/chmod
  - `7946` /tmp/ft_scenario01/downloaded.sh
    - `7947` /usr/bin/date
    - `7948` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7937 (?) executed `/usr/bin/bash`
- +5.654 ms pid 7938 (bash) executed `/usr/bin/rm`
- +10.301 ms pid 7939 (bash) executed `/usr/bin/mkdir`
- +15.201 ms pid 7940 (bash) executed `/usr/bin/cat`
- +21.109 ms pid 7942 (bash) executed `/usr/bin/sleep`
- +24.175 ms pid 7941 (bash) executed `/usr/bin/python3`
- +528.578 ms pid 7943 (bash) executed `/usr/bin/curl`
- +548.295 ms pid 7945 (bash) executed `/usr/bin/chmod`
- +551.721 ms pid 7946 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +553.635 ms pid 7947 (downloaded.sh) executed `/usr/bin/date`
- +556.785 ms pid 7948 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +97.976 ms pid 7941 (python3) connected to `unix:/var/run/nscd/socket`
- +98.061 ms pid 7941 (python3) connected to `ipv6:[...]`
- +98.105 ms pid 7941 (python3) connected to `sockfd=3`
- +98.121 ms pid 7941 (python3) connected to `0.0.0.0:8765`
- +99.786 ms pid 7941 (python3) connected to `unix:/var/run/nscd/socket`
- +540.891 ms pid 7943 (curl) connected to `unix:/var/run/nscd/socket`
- +540.955 ms pid 7943 (curl) connected to `unix:/var/run/nscd/socket`
- +541.704 ms pid 7943 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +14.973 ms by pid 7940 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +545.872 ms by pid 7943 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +550.871 ms pid 7945 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +9.024 ms pid 7938 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +9.074 ms pid 7938 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +9.118 ms pid 7938 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +541.140 ms pid 7943 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +551.721 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7946 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +9.074 ms #386 `unlinkat` by pid 7938 (rm)
    - +545.872 ms #3283 `openat` by pid 7943 (curl)
    - +546.168 ms #3294 `write` by pid 7943 (curl)
    - +546.205 ms #3295 `close` by pid 7943 (curl)
    - +550.871 ms #3482 `fchmodat` by pid 7945 (chmod)
    - +551.721 ms #3512 `execve` by pid 7946 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7937 | ? | execve | `/usr/bin/bash` |
| 49 | 1.290 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.326 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.492 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.524 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.601 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.634 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 1.714 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 1.748 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 1.822 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 1.857 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 1.931 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 1.965 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.050 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.082 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.133 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.210 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.244 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.318 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.352 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.436 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.470 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 2.544 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 2.578 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 2.654 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 2.692 | 7937 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 4.201 | 7937 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 239 | 5.183 | 7937 | bash | clone | `` |
| 256 | 5.654 | 7938 | bash | execve | `/usr/bin/rm` |
| 293 | 7.049 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 7.094 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 7.306 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 7.376 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 7.486 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 7.534 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 7.643 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 7.687 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 7.776 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 7.815 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 7.935 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 7.981 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 8.070 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 8.106 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 8.156 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 8.233 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 8.268 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 8.345 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 8.379 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 8.463 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 8.497 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 8.571 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 8.606 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 8.690 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 8.729 | 7938 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 8.862 | 7938 | rm | openat | `/tmp/ft_scenario01` |
| 385 | 9.024 | 7938 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 386 | 9.074 | 7938 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 388 | 9.118 | 7938 | rm | unlinkat | `/tmp/ft_scenario01` |
| 393 | 9.245 | 7938 | rm | exit_group | `code=0` |
| 427 | 9.917 | 7937 | bash | clone | `` |
| 444 | 10.301 | 7939 | bash | execve | `/usr/bin/mkdir` |
| 508 | 12.128 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 510 | 12.166 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 519 | 12.343 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 521 | 12.405 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 525 | 12.495 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 527 | 12.529 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 531 | 12.606 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 533 | 12.639 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 537 | 12.717 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 539 | 12.752 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 543 | 12.827 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 545 | 12.861 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 549 | 12.944 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 551 | 12.978 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 554 | 13.028 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 558 | 13.103 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 560 | 13.137 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 564 | 13.211 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 566 | 13.245 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 570 | 13.325 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 572 | 13.359 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 576 | 13.433 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 578 | 13.468 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 582 | 13.544 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 584 | 13.577 | 7939 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 595 | 13.833 | 7939 | mkdir | exit_group | `code=0` |
| 634 | 14.562 | 7937 | bash | clone | `` |
| 651 | 14.973 | 7940 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 660 | 15.201 | 7940 | bash | execve | `/usr/bin/cat` |
| 697 | 16.489 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 699 | 16.535 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 708 | 16.751 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 710 | 16.794 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 714 | 16.892 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 716 | 16.936 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 720 | 17.032 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 722 | 17.077 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 726 | 17.173 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 728 | 17.218 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 732 | 17.312 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 734 | 17.357 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 738 | 17.464 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 740 | 17.508 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 743 | 17.670 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 747 | 17.782 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 749 | 17.827 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 753 | 17.927 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 755 | 17.973 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 759 | 18.068 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 761 | 18.109 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 765 | 18.205 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 767 | 18.239 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 771 | 18.324 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 773 | 18.363 | 7940 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 782 | 18.549 | 7940 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 788 | 18.710 | 7940 | cat | exit_group | `code=0` |
| 798 | 19.014 | 7937 | bash | clone | `` |
| 851 | 20.641 | 7937 | bash | clone | `` |
| 868 | 21.109 | 7942 | bash | execve | `/usr/bin/sleep` |
| 914 | 23.034 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 918 | 23.102 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 936 | 23.523 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 938 | 23.579 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 945 | 23.718 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 947 | 23.771 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 955 | 23.913 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 958 | 23.970 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 965 | 24.089 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 969 | 24.152 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 970 | 24.175 | 7941 | bash | execve | `/usr/bin/python3` |
| 976 | 24.755 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 24.827 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 987 | 25.047 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 989 | 25.095 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 995 | 25.196 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1003 | 25.330 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1006 | 25.387 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1014 | 25.550 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1018 | 25.643 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1032 | 25.988 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1036 | 26.041 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1044 | 26.156 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1048 | 26.209 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1054 | 26.378 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1057 | 26.439 | 7942 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1098 | 27.266 | 7941 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1100 | 27.315 | 7941 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1130 | 30.391 | 7941 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 1131 | 30.425 | 7941 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 1134 | 30.509 | 7941 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 1135 | 30.535 | 7941 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 1136 | 30.561 | 7941 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 1147 | 31.562 | 7941 | python3 | openat | `/etc/localtime` |
| 1302 | 37.532 | 7941 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1308 | 37.724 | 7941 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1317 | 38.041 | 7941 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1348 | 39.543 | 7941 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1356 | 39.773 | 7941 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1364 | 39.962 | 7941 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1612 | 49.066 | 7941 | python3 | openat | `/tmp/ft_scenario01` |
| 2547 | 97.663 | 7941 | python3 | openat | `/etc/gai.conf` |
| 2557 | 97.887 | 7941 | python3 | sendto | `socket:[48908]` |
| 2561 | 97.976 | 7941 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2565 | 98.061 | 7941 | python3 | connect | `ipv6:[...]` |
| 2567 | 98.105 | 7941 | python3 | connect | `sockfd=3` |
| 2568 | 98.121 | 7941 | python3 | connect | `0.0.0.0:8765` |
| 2608 | 99.786 | 7941 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2612 | 99.865 | 7941 | python3 | openat | `/etc/nsswitch.conf` |
| 2619 | 99.996 | 7941 | python3 | openat | `/etc/host.conf` |
| 2625 | 100.094 | 7941 | python3 | openat | `/etc/resolv.conf` |
| 2631 | 100.202 | 7941 | python3 | openat | `/etc/hosts` |
| 2639 | 100.342 | 7941 | python3 | openat | `/etc/hosts` |
| 2649 | 527.178 | 7942 | sleep | exit_group | `code=0` |
| 2685 | 528.165 | 7937 | bash | clone | `` |
| 2702 | 528.578 | 7943 | bash | execve | `/usr/bin/curl` |
| 3018 | 537.937 | 7943 | curl | openat | `/etc/gnutls/config` |
| 3065 | 539.324 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3067 | 539.360 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3076 | 539.531 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3078 | 539.566 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3082 | 539.642 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3084 | 539.675 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3088 | 539.755 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3090 | 539.788 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3094 | 539.861 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3096 | 539.895 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3100 | 539.969 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3102 | 540.004 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3106 | 540.087 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3108 | 540.122 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3111 | 540.173 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3115 | 540.252 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3117 | 540.286 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3121 | 540.361 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3123 | 540.394 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3127 | 540.474 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3129 | 540.508 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3133 | 540.582 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3135 | 540.617 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3139 | 540.694 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3141 | 540.728 | 7943 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3145 | 540.807 | 7943 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3146 | 540.826 | 7943 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 3149 | 540.891 | 7943 | curl | connect | `unix:/var/run/nscd/socket` |
| 3152 | 540.955 | 7943 | curl | connect | `unix:/var/run/nscd/socket` |
| 3156 | 541.024 | 7943 | curl | openat | `/etc/nsswitch.conf` |
| 3162 | 541.140 | 7943 | curl | openat | `/etc/passwd` |
| 3167 | 541.228 | 7943 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3191 | 541.704 | 7943 | curl | connect | `127.0.0.1:8765` |
| 3194 | 541.829 | 7941 | python3 | accept4 | `sockfd=3` |
| 3209 | 542.062 | 7943 | curl | sendto | `socket:[49515]` |
| 3215 | 542.159 | 7941 | python3 | clone3 | `` |
| 3231 | 542.522 | 7944 | python3 | recvfrom | `socket:[48913]` |
| 3241 | 542.905 | 7944 | python3 | openat | `/etc/mime.types` |
| 3267 | 545.426 | 7944 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 3273 | 545.677 | 7944 | python3 | sendto | `socket:[48913]` |
| 3279 | 545.800 | 7944 | python3 | sendto | `socket:[48913]` |
| 3280 | 545.818 | 7943 | curl | recvfrom | `socket:[49515]` |
| 3283 | 545.872 | 7943 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3291 | 546.078 | 7944 | python3 | exit | `code=0` |
| 3294 | 546.168 | 7943 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 3310 | 546.700 | 7943 | curl | exit_group | `code=0` |
| 3346 | 547.900 | 7937 | bash | clone | `` |
| 3363 | 548.295 | 7945 | bash | execve | `/usr/bin/chmod` |
| 3400 | 549.338 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3402 | 549.376 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3411 | 549.540 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3413 | 549.573 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3417 | 549.652 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3419 | 549.689 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3423 | 549.765 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3425 | 549.800 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3429 | 549.873 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3431 | 549.908 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3435 | 549.981 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3437 | 550.015 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3441 | 550.098 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3443 | 550.132 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3446 | 550.183 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3450 | 550.259 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3452 | 550.292 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3456 | 550.368 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3458 | 550.402 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3462 | 550.483 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3464 | 550.517 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3468 | 550.591 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3470 | 550.625 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3474 | 550.704 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3476 | 550.738 | 7945 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3482 | 550.871 | 7945 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 3485 | 550.964 | 7945 | chmod | exit_group | `code=0` |
| 3495 | 551.295 | 7937 | bash | clone | `` |
| 3512 | 551.721 | 7946 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 3552 | 552.946 | 7946 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3566 | 553.217 | 7946 | downloaded.sh | clone | `` |
| 3587 | 553.635 | 7947 | downloaded.sh | execve | `/usr/bin/date` |
| 3624 | 554.557 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3626 | 554.592 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3635 | 554.761 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3637 | 554.795 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3641 | 554.875 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3643 | 554.910 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3647 | 554.983 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3649 | 555.016 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3653 | 555.091 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3655 | 555.124 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3659 | 555.196 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3661 | 555.231 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3665 | 555.313 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3667 | 555.347 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3670 | 555.398 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3674 | 555.473 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3676 | 555.507 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3680 | 555.582 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3682 | 555.615 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3686 | 555.699 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3688 | 555.733 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3692 | 555.806 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3694 | 555.840 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3698 | 555.915 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3700 | 555.949 | 7947 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3704 | 556.032 | 7947 | date | openat | `/etc/localtime` |
| 3717 | 556.282 | 7947 | date | exit_group | `code=0` |
| 3736 | 556.722 | 7946 | downloaded.sh | vfork | `` |
| 3738 | 556.785 | 7948 | downloaded.sh | execve | `/usr/bin/sleep` |
| 3777 | 557.639 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3779 | 557.673 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3788 | 557.847 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3790 | 557.881 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3794 | 557.966 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3796 | 558.034 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3800 | 558.114 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3802 | 558.162 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3806 | 558.245 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3808 | 558.300 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3812 | 558.387 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3814 | 558.431 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3818 | 558.533 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3820 | 558.576 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3823 | 558.648 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3827 | 558.736 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3829 | 558.787 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3833 | 558.877 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3835 | 558.923 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3839 | 559.019 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3841 | 559.063 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3845 | 559.146 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3847 | 559.203 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3851 | 559.286 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3853 | 559.334 | 7948 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3875 | 759.993 | 7948 | sleep | exit_group | `code=0` |
| 3879 | 760.220 | 7946 | downloaded.sh | exit_group | `code=0` |
| 3927 | 762.214 | 7937 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 60.250 ms |
| Workload CPU (user+sys) | 78.081 ms |
| Tracer peak memory | 22848 KiB |
| Processing time (normalise+correlate+reconstruct) | 5.035 ms |
| Evidence size | 1330056 bytes |

