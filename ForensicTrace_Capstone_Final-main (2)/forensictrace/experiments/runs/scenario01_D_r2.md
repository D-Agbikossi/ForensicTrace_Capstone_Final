# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | D |
| Events recorded | 3919 |
| Failed exec attempts removed | 12 |
| Duration | 808.310 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_D_r2.json` (1327532 bytes) |
| SHA-256 | `c64d43523e9699d5210208999d52c75179d058c451d6b0796dfc14d05eb5d1fc` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_D_r2.json.sha256`

## 1. Process tree

- `7348` /usr/bin/bash
  - `7349` /usr/bin/rm
  - `7350` /usr/bin/mkdir
  - `7351` /usr/bin/cat
  - `7352` /usr/bin/python3
  - `7354` /usr/bin/sleep
  - `7355` /usr/bin/curl
  - `7356` /usr/bin/python3
  - `7357` /usr/bin/chmod
  - `7358` /tmp/ft_scenario01/downloaded.sh
    - `7359` /usr/bin/date
    - `7360` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7348 (?) executed `/usr/bin/bash`
- +9.876 ms pid 7349 (bash) executed `/usr/bin/rm`
- +16.157 ms pid 7350 (bash) executed `/usr/bin/mkdir`
- +24.018 ms pid 7351 (bash) executed `/usr/bin/cat`
- +32.159 ms pid 7352 (bash) executed `/usr/bin/python3`
- +48.268 ms pid 7354 (bash) executed `/usr/bin/sleep`
- +570.538 ms pid 7355 (bash) executed `/usr/bin/curl`
- +593.414 ms pid 7357 (bash) executed `/usr/bin/chmod`
- +596.930 ms pid 7358 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +599.092 ms pid 7359 (downloaded.sh) executed `/usr/bin/date`
- +602.187 ms pid 7360 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +158.105 ms pid 7352 (python3) connected to `unix:/var/run/nscd/socket`
- +158.253 ms pid 7352 (python3) connected to `ipv6:[...]`
- +158.321 ms pid 7352 (python3) connected to `sockfd=3`
- +158.346 ms pid 7352 (python3) connected to `0.0.0.0:8765`
- +161.512 ms pid 7352 (python3) connected to `unix:/var/run/nscd/socket`
- +585.743 ms pid 7355 (curl) connected to `unix:/var/run/nscd/socket`
- +585.807 ms pid 7355 (curl) connected to `unix:/var/run/nscd/socket`
- +586.548 ms pid 7355 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +23.540 ms by pid 7351 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +591.062 ms by pid 7355 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +596.158 ms pid 7357 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +14.642 ms pid 7349 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +14.701 ms pid 7349 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +14.765 ms pid 7349 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +585.989 ms pid 7355 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +596.930 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7358 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +14.701 ms #386 `unlinkat` by pid 7349 (rm)
    - +591.062 ms #3281 `openat` by pid 7355 (curl)
    - +591.291 ms #3292 `write` by pid 7355 (curl)
    - +591.330 ms #3293 `close` by pid 7355 (curl)
    - +596.158 ms #3480 `fchmodat` by pid 7357 (chmod)
    - +596.930 ms #3510 `execve` by pid 7358 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7348 | ? | execve | `/usr/bin/bash` |
| 49 | 1.658 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.706 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.935 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.981 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 2.085 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 2.130 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 2.241 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 2.289 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 2.392 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 2.439 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.540 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.587 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.698 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.744 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.817 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.917 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.965 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 3.083 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 3.149 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 3.286 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 3.348 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 3.507 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 3.564 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 4.112 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 4.169 | 7348 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 7.684 | 7348 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 239 | 9.399 | 7348 | bash | clone | `` |
| 256 | 9.876 | 7349 | bash | execve | `/usr/bin/rm` |
| 293 | 11.210 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 11.265 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 11.484 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 11.531 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 11.629 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 11.677 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 11.783 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 11.830 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 11.939 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 11.986 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 12.099 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 12.147 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 12.321 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 12.371 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 12.444 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 12.544 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 12.593 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 12.693 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 12.740 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 12.851 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 12.899 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 13.002 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 13.048 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 13.150 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 14.207 | 7349 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 14.416 | 7349 | rm | openat | `/tmp/ft_scenario01` |
| 385 | 14.642 | 7349 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 386 | 14.701 | 7349 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 388 | 14.765 | 7349 | rm | unlinkat | `/tmp/ft_scenario01` |
| 393 | 14.928 | 7349 | rm | exit_group | `code=0` |
| 427 | 15.724 | 7348 | bash | clone | `` |
| 444 | 16.157 | 7350 | bash | execve | `/usr/bin/mkdir` |
| 508 | 18.182 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 510 | 18.237 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 519 | 18.471 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 521 | 18.520 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 525 | 18.623 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 527 | 18.672 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 531 | 18.779 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 533 | 18.829 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 537 | 18.934 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 539 | 18.984 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 543 | 19.088 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 545 | 19.144 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 549 | 19.291 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 551 | 19.350 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 554 | 19.434 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 558 | 19.559 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 560 | 19.607 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 564 | 19.714 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 566 | 19.765 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 570 | 19.875 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 572 | 19.925 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 576 | 20.033 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 578 | 20.087 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 582 | 20.200 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 584 | 20.250 | 7350 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 595 | 20.697 | 7350 | mkdir | exit_group | `code=0` |
| 634 | 21.649 | 7348 | bash | clone | `` |
| 651 | 23.540 | 7351 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 660 | 24.018 | 7351 | bash | execve | `/usr/bin/cat` |
| 697 | 26.063 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 699 | 26.123 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 708 | 26.413 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 710 | 26.468 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 714 | 26.646 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 716 | 26.696 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 720 | 26.837 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 722 | 26.892 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 726 | 27.301 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 728 | 27.353 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 732 | 27.477 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 734 | 27.534 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 738 | 27.670 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 740 | 27.725 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 743 | 27.807 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 747 | 27.934 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 749 | 27.992 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 753 | 28.128 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 755 | 28.188 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 759 | 28.359 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 761 | 28.421 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 765 | 28.559 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 767 | 28.619 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 771 | 28.747 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 773 | 28.848 | 7351 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 782 | 29.158 | 7351 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 788 | 29.448 | 7351 | cat | exit_group | `code=0` |
| 798 | 30.244 | 7348 | bash | clone | `` |
| 863 | 32.159 | 7352 | bash | execve | `/usr/bin/python3` |
| 895 | 33.458 | 7348 | bash | clone | `` |
| 919 | 48.268 | 7354 | bash | execve | `/usr/bin/sleep` |
| 983 | 53.663 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 987 | 53.753 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1011 | 55.079 | 7352 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1013 | 55.137 | 7352 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1030 | 59.984 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1034 | 61.227 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1048 | 61.646 | 7352 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 1049 | 61.700 | 7352 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 1055 | 62.058 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1057 | 62.113 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1061 | 62.222 | 7352 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 1062 | 62.260 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1063 | 62.275 | 7352 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 1065 | 62.312 | 7352 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 1066 | 62.590 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1073 | 62.820 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1077 | 62.888 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1084 | 63.598 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1087 | 63.842 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1091 | 64.246 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1093 | 64.600 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1096 | 64.693 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1100 | 64.940 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1102 | 64.996 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1107 | 65.328 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1109 | 65.379 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1111 | 65.426 | 7352 | python3 | openat | `/etc/localtime` |
| 1116 | 65.519 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1119 | 65.585 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1126 | 65.728 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1128 | 65.787 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1134 | 65.920 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1137 | 65.975 | 7354 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1302 | 80.172 | 7352 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1308 | 80.429 | 7352 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1317 | 80.697 | 7352 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1348 | 82.037 | 7352 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1356 | 82.257 | 7352 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1364 | 83.103 | 7352 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1612 | 95.830 | 7352 | python3 | openat | `/tmp/ft_scenario01` |
| 2547 | 157.650 | 7352 | python3 | openat | `/etc/gai.conf` |
| 2557 | 157.962 | 7352 | python3 | sendto | `socket:[46493]` |
| 2561 | 158.105 | 7352 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2565 | 158.253 | 7352 | python3 | connect | `ipv6:[...]` |
| 2567 | 158.321 | 7352 | python3 | connect | `sockfd=3` |
| 2568 | 158.346 | 7352 | python3 | connect | `0.0.0.0:8765` |
| 2608 | 161.512 | 7352 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2612 | 161.607 | 7352 | python3 | openat | `/etc/nsswitch.conf` |
| 2619 | 161.759 | 7352 | python3 | openat | `/etc/host.conf` |
| 2625 | 161.870 | 7352 | python3 | openat | `/etc/resolv.conf` |
| 2631 | 162.032 | 7352 | python3 | openat | `/etc/hosts` |
| 2639 | 162.198 | 7352 | python3 | openat | `/etc/hosts` |
| 2649 | 567.479 | 7354 | sleep | exit_group | `code=0` |
| 2685 | 569.905 | 7348 | bash | clone | `` |
| 2702 | 570.538 | 7355 | bash | execve | `/usr/bin/curl` |
| 3018 | 582.281 | 7355 | curl | openat | `/etc/gnutls/config` |
| 3065 | 584.006 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3067 | 584.049 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3076 | 584.267 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3078 | 584.309 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3082 | 584.400 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3084 | 584.440 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3088 | 584.583 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3090 | 584.621 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3094 | 584.698 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3096 | 584.733 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3100 | 584.808 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3102 | 584.843 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3106 | 584.928 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3108 | 584.963 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3111 | 585.014 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3115 | 585.094 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3117 | 585.128 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3121 | 585.214 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3123 | 585.250 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3127 | 585.330 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3129 | 585.365 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3133 | 585.438 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3135 | 585.472 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3139 | 585.545 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3141 | 585.579 | 7355 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3145 | 585.658 | 7355 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3146 | 585.677 | 7355 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 3149 | 585.743 | 7355 | curl | connect | `unix:/var/run/nscd/socket` |
| 3152 | 585.807 | 7355 | curl | connect | `unix:/var/run/nscd/socket` |
| 3156 | 585.876 | 7355 | curl | openat | `/etc/nsswitch.conf` |
| 3162 | 585.989 | 7355 | curl | openat | `/etc/passwd` |
| 3167 | 586.076 | 7355 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3191 | 586.548 | 7355 | curl | connect | `127.0.0.1:8765` |
| 3195 | 586.680 | 7352 | python3 | accept4 | `sockfd=3` |
| 3207 | 586.877 | 7355 | curl | sendto | `socket:[44839]` |
| 3215 | 586.991 | 7352 | python3 | clone3 | `` |
| 3231 | 587.364 | 7356 | python3 | recvfrom | `socket:[46499]` |
| 3239 | 587.777 | 7356 | python3 | openat | `/etc/mime.types` |
| 3265 | 590.607 | 7356 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 3271 | 590.835 | 7356 | python3 | sendto | `socket:[46499]` |
| 3276 | 590.975 | 7356 | python3 | sendto | `socket:[46499]` |
| 3279 | 591.024 | 7355 | curl | recvfrom | `socket:[44839]` |
| 3281 | 591.062 | 7355 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3291 | 591.274 | 7356 | python3 | exit | `code=0` |
| 3292 | 591.291 | 7355 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 3308 | 591.734 | 7355 | curl | exit_group | `code=0` |
| 3344 | 592.929 | 7348 | bash | clone | `` |
| 3361 | 593.414 | 7357 | bash | execve | `/usr/bin/chmod` |
| 3398 | 594.660 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3400 | 594.696 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3409 | 594.861 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3411 | 594.895 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3415 | 594.970 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3417 | 595.004 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3421 | 595.078 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3423 | 595.111 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3427 | 595.185 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3429 | 595.224 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3433 | 595.296 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3435 | 595.330 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3439 | 595.413 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3441 | 595.447 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3444 | 595.499 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3448 | 595.574 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3450 | 595.608 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3454 | 595.682 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3456 | 595.715 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3460 | 595.797 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3462 | 595.830 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3466 | 595.906 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3468 | 595.939 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3472 | 596.013 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3474 | 596.047 | 7357 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3480 | 596.158 | 7357 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 3483 | 596.344 | 7357 | chmod | exit_group | `code=0` |
| 3493 | 596.593 | 7348 | bash | clone | `` |
| 3510 | 596.930 | 7358 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 3550 | 598.388 | 7358 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3564 | 598.667 | 7358 | downloaded.sh | clone | `` |
| 3585 | 599.092 | 7359 | downloaded.sh | execve | `/usr/bin/date` |
| 3622 | 600.003 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3624 | 600.038 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3633 | 600.204 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3635 | 600.237 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3639 | 600.311 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3641 | 600.345 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3645 | 600.418 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3647 | 600.452 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3651 | 600.525 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3653 | 600.558 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3657 | 600.629 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3659 | 600.661 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3663 | 600.744 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3665 | 600.776 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3668 | 600.826 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3672 | 600.901 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3674 | 600.936 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3678 | 601.009 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3680 | 601.042 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3684 | 601.120 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3686 | 601.153 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3690 | 601.231 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3692 | 601.264 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3696 | 601.337 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3698 | 601.371 | 7359 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3702 | 601.454 | 7359 | date | openat | `/etc/localtime` |
| 3715 | 601.669 | 7359 | date | exit_group | `code=0` |
| 3734 | 602.087 | 7358 | downloaded.sh | vfork | `` |
| 3736 | 602.187 | 7360 | downloaded.sh | execve | `/usr/bin/sleep` |
| 3775 | 603.042 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3777 | 603.077 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3786 | 603.239 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3788 | 603.272 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3792 | 603.345 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3794 | 603.379 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3798 | 603.451 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3800 | 603.485 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3804 | 603.557 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3806 | 603.591 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3810 | 603.662 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3812 | 603.695 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3816 | 603.876 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3818 | 603.915 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3821 | 603.977 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3825 | 604.085 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3827 | 604.129 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3831 | 604.238 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3833 | 604.281 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3837 | 604.377 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3839 | 604.422 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3843 | 604.511 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3845 | 604.550 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3849 | 604.641 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3851 | 604.681 | 7360 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3873 | 805.350 | 7360 | sleep | exit_group | `code=0` |
| 3877 | 805.614 | 7358 | downloaded.sh | exit_group | `code=0` |
| 3919 | 807.638 | 7348 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 73.406 ms |
| Workload CPU (user+sys) | 99.017 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 7.471 ms |
| Evidence size | 1327532 bytes |

