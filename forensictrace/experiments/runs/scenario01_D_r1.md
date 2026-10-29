# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | D |
| Events recorded | 3925 |
| Failed exec attempts removed | 12 |
| Duration | 770.345 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_D_r1.json` (1329400 bytes) |
| SHA-256 | `d95426a2ec3e8e75e883f628748227c10551a5aba58b7351946f024dfa10018e` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_D_r1.json.sha256`

## 1. Process tree

- `7160` /usr/bin/bash
  - `7161` /usr/bin/rm
  - `7162` /usr/bin/mkdir
  - `7163` /usr/bin/cat
  - `7164` /usr/bin/python3
  - `7165` /usr/bin/sleep
  - `7166` /usr/bin/curl
  - `7167` /usr/bin/python3
  - `7168` /usr/bin/chmod
  - `7169` /tmp/ft_scenario01/downloaded.sh
    - `7170` /usr/bin/date
    - `7171` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7160 (?) executed `/usr/bin/bash`
- +6.477 ms pid 7161 (bash) executed `/usr/bin/rm`
- +11.626 ms pid 7162 (bash) executed `/usr/bin/mkdir`
- +16.764 ms pid 7163 (bash) executed `/usr/bin/cat`
- +22.300 ms pid 7164 (bash) executed `/usr/bin/python3`
- +22.331 ms pid 7165 (bash) executed `/usr/bin/sleep`
- +528.270 ms pid 7166 (bash) executed `/usr/bin/curl`
- +547.729 ms pid 7168 (bash) executed `/usr/bin/chmod`
- +553.147 ms pid 7169 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +555.243 ms pid 7170 (downloaded.sh) executed `/usr/bin/date`
- +559.373 ms pid 7171 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +103.951 ms pid 7164 (python3) connected to `unix:/var/run/nscd/socket`
- +104.036 ms pid 7164 (python3) connected to `ipv6:[...]`
- +104.080 ms pid 7164 (python3) connected to `sockfd=3`
- +104.096 ms pid 7164 (python3) connected to `0.0.0.0:8765`
- +105.959 ms pid 7164 (python3) connected to `unix:/var/run/nscd/socket`
- +540.774 ms pid 7166 (curl) connected to `unix:/var/run/nscd/socket`
- +540.848 ms pid 7166 (curl) connected to `unix:/var/run/nscd/socket`
- +541.760 ms pid 7166 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +16.548 ms by pid 7163 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +545.668 ms by pid 7166 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +552.345 ms pid 7168 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +10.186 ms pid 7161 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +10.238 ms pid 7161 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +10.294 ms pid 7161 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +541.071 ms pid 7166 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +553.147 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7169 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +10.238 ms #386 `unlinkat` by pid 7161 (rm)
    - +545.668 ms #3280 `openat` by pid 7166 (curl)
    - +545.861 ms #3290 `write` by pid 7166 (curl)
    - +545.900 ms #3292 `close` by pid 7166 (curl)
    - +552.345 ms #3480 `fchmodat` by pid 7168 (chmod)
    - +553.147 ms #3510 `execve` by pid 7169 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7160 | ? | execve | `/usr/bin/bash` |
| 49 | 1.927 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.965 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 2.188 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 2.227 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 2.321 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 2.361 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 2.459 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 2.501 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 2.591 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 2.633 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.726 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.768 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.869 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.909 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.969 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 3.063 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 3.103 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 3.192 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 3.233 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 3.332 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 3.380 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 3.472 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 3.514 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 3.606 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 3.646 | 7160 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 5.173 | 7160 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 239 | 6.087 | 7160 | bash | clone | `` |
| 256 | 6.477 | 7161 | bash | execve | `/usr/bin/rm` |
| 293 | 8.083 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 8.122 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 8.302 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 8.352 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 8.468 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 8.505 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 8.583 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 8.615 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 8.690 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 8.722 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 8.795 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 8.829 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 8.959 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 8.997 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 9.053 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 9.136 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 9.178 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 9.263 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 9.303 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 9.473 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 9.522 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 9.652 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 9.699 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 9.792 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 9.834 | 7161 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 9.991 | 7161 | rm | openat | `/tmp/ft_scenario01` |
| 385 | 10.186 | 7161 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 386 | 10.238 | 7161 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 388 | 10.294 | 7161 | rm | unlinkat | `/tmp/ft_scenario01` |
| 393 | 10.440 | 7161 | rm | exit_group | `code=0` |
| 427 | 11.218 | 7160 | bash | clone | `` |
| 444 | 11.626 | 7162 | bash | execve | `/usr/bin/mkdir` |
| 508 | 13.400 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 510 | 13.442 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 519 | 13.638 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 521 | 13.680 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 525 | 13.769 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 527 | 13.809 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 531 | 13.900 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 533 | 13.941 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 537 | 14.029 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 539 | 14.071 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 543 | 14.160 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 545 | 14.201 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 549 | 14.301 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 551 | 14.342 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 554 | 14.406 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 558 | 14.495 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 560 | 14.535 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 564 | 14.624 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 566 | 14.666 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 570 | 14.760 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 572 | 14.802 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 576 | 14.890 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 578 | 14.932 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 582 | 15.023 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 584 | 15.063 | 7162 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 595 | 15.359 | 7162 | mkdir | exit_group | `code=0` |
| 634 | 16.130 | 7160 | bash | clone | `` |
| 651 | 16.548 | 7163 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 660 | 16.764 | 7163 | bash | execve | `/usr/bin/cat` |
| 697 | 18.375 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 699 | 18.423 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 708 | 18.650 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 710 | 18.694 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 714 | 18.792 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 716 | 18.835 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 720 | 18.931 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 722 | 18.978 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 726 | 19.074 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 728 | 19.118 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 732 | 19.213 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 734 | 19.261 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 738 | 19.376 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 740 | 19.419 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 743 | 19.483 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 747 | 19.581 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 749 | 19.626 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 753 | 19.727 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 755 | 19.771 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 759 | 19.911 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 761 | 19.950 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 765 | 20.030 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 767 | 20.064 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 771 | 20.139 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 773 | 20.172 | 7163 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 782 | 20.339 | 7163 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 788 | 20.518 | 7163 | cat | exit_group | `code=0` |
| 798 | 20.856 | 7160 | bash | clone | `` |
| 872 | 21.925 | 7160 | bash | clone | `` |
| 900 | 22.300 | 7164 | bash | execve | `/usr/bin/python3` |
| 902 | 22.331 | 7165 | bash | execve | `/usr/bin/sleep` |
| 969 | 23.646 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 972 | 23.699 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 990 | 23.970 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 993 | 24.024 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1001 | 24.175 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1005 | 24.235 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1014 | 24.765 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1017 | 24.834 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1023 | 24.937 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1026 | 24.985 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1034 | 25.117 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1037 | 25.169 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1043 | 25.257 | 7164 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1045 | 25.287 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1046 | 25.304 | 7164 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1049 | 25.341 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1054 | 25.417 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1062 | 25.507 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1065 | 25.547 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1070 | 25.642 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1072 | 25.681 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1079 | 25.783 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1082 | 25.822 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1086 | 25.913 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1088 | 25.952 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1092 | 26.044 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1094 | 26.085 | 7165 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1130 | 28.428 | 7164 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 1131 | 28.454 | 7164 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 1134 | 28.628 | 7164 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 1135 | 28.656 | 7164 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 1136 | 28.681 | 7164 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 1147 | 29.715 | 7164 | python3 | openat | `/etc/localtime` |
| 1302 | 35.935 | 7164 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1308 | 36.100 | 7164 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 1317 | 36.322 | 7164 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1348 | 37.924 | 7164 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 1356 | 38.106 | 7164 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 1364 | 38.268 | 7164 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 1612 | 48.089 | 7164 | python3 | openat | `/tmp/ft_scenario01` |
| 2547 | 103.648 | 7164 | python3 | openat | `/etc/gai.conf` |
| 2557 | 103.866 | 7164 | python3 | sendto | `socket:[44547]` |
| 2561 | 103.951 | 7164 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2565 | 104.036 | 7164 | python3 | connect | `ipv6:[...]` |
| 2567 | 104.080 | 7164 | python3 | connect | `sockfd=3` |
| 2568 | 104.096 | 7164 | python3 | connect | `0.0.0.0:8765` |
| 2609 | 105.959 | 7164 | python3 | connect | `unix:/var/run/nscd/socket` |
| 2613 | 106.055 | 7164 | python3 | openat | `/etc/nsswitch.conf` |
| 2620 | 106.211 | 7164 | python3 | openat | `/etc/host.conf` |
| 2626 | 106.331 | 7164 | python3 | openat | `/etc/resolv.conf` |
| 2632 | 106.490 | 7164 | python3 | openat | `/etc/hosts` |
| 2640 | 106.687 | 7164 | python3 | openat | `/etc/hosts` |
| 2650 | 526.794 | 7165 | sleep | exit_group | `code=0` |
| 2686 | 527.882 | 7160 | bash | clone | `` |
| 2703 | 528.270 | 7166 | bash | execve | `/usr/bin/curl` |
| 3019 | 537.246 | 7166 | curl | openat | `/etc/gnutls/config` |
| 3066 | 538.669 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3068 | 538.706 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3077 | 538.873 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3079 | 538.907 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3083 | 538.984 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3085 | 539.018 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3089 | 539.091 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3091 | 539.125 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3095 | 539.198 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3097 | 539.231 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3101 | 539.306 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3103 | 539.338 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3107 | 539.431 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3109 | 539.473 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3112 | 539.538 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3116 | 539.632 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3118 | 539.675 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3122 | 539.772 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3124 | 539.816 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3128 | 539.920 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3130 | 539.968 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3134 | 540.299 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3136 | 540.429 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3140 | 540.533 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3142 | 540.577 | 7166 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3146 | 540.675 | 7166 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3147 | 540.698 | 7166 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 3150 | 540.774 | 7166 | curl | connect | `unix:/var/run/nscd/socket` |
| 3153 | 540.848 | 7166 | curl | connect | `unix:/var/run/nscd/socket` |
| 3157 | 540.935 | 7166 | curl | openat | `/etc/nsswitch.conf` |
| 3163 | 541.071 | 7166 | curl | openat | `/etc/passwd` |
| 3168 | 541.179 | 7166 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 3192 | 541.760 | 7166 | curl | connect | `127.0.0.1:8765` |
| 3196 | 541.897 | 7164 | python3 | accept4 | `sockfd=3` |
| 3211 | 542.114 | 7166 | curl | sendto | `socket:[44555]` |
| 3214 | 542.170 | 7164 | python3 | clone3 | `` |
| 3232 | 542.597 | 7167 | python3 | recvfrom | `socket:[46085]` |
| 3240 | 542.913 | 7167 | python3 | openat | `/etc/mime.types` |
| 3265 | 545.269 | 7167 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 3271 | 545.495 | 7167 | python3 | sendto | `socket:[46085]` |
| 3277 | 545.614 | 7167 | python3 | sendto | `socket:[46085]` |
| 3278 | 545.630 | 7166 | curl | recvfrom | `socket:[44555]` |
| 3280 | 545.668 | 7166 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3290 | 545.861 | 7166 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 3293 | 545.910 | 7167 | python3 | exit | `code=0` |
| 3308 | 546.320 | 7166 | curl | exit_group | `code=0` |
| 3344 | 547.341 | 7160 | bash | clone | `` |
| 3361 | 547.729 | 7168 | bash | execve | `/usr/bin/chmod` |
| 3398 | 549.267 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3400 | 549.305 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3409 | 549.847 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3411 | 550.001 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3415 | 550.240 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3417 | 550.289 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3421 | 550.442 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3423 | 550.488 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3427 | 550.586 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3429 | 550.628 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3433 | 550.744 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3435 | 550.801 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3439 | 550.910 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3441 | 550.949 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3444 | 551.009 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3448 | 551.183 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3450 | 551.242 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3454 | 551.543 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3456 | 551.586 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3460 | 551.900 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3462 | 551.942 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3466 | 552.032 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3468 | 552.073 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3472 | 552.165 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3474 | 552.207 | 7168 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3480 | 552.345 | 7168 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 3483 | 552.452 | 7168 | chmod | exit_group | `code=0` |
| 3493 | 552.772 | 7160 | bash | clone | `` |
| 3510 | 553.147 | 7169 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 3550 | 554.409 | 7169 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 3564 | 554.735 | 7169 | downloaded.sh | clone | `` |
| 3585 | 555.243 | 7170 | downloaded.sh | execve | `/usr/bin/date` |
| 3622 | 556.310 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3624 | 556.358 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3633 | 556.589 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3635 | 556.665 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3639 | 556.763 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3641 | 556.805 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3645 | 556.893 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3647 | 556.934 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3651 | 557.024 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3653 | 557.065 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3657 | 557.152 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3659 | 557.191 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3663 | 557.296 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3665 | 557.335 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3668 | 557.397 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3672 | 557.486 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3674 | 557.529 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3678 | 557.620 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3680 | 557.661 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3684 | 557.758 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3686 | 557.797 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3690 | 557.887 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3692 | 557.926 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3696 | 558.017 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3698 | 558.058 | 7170 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3702 | 558.162 | 7170 | date | openat | `/etc/localtime` |
| 3715 | 558.452 | 7170 | date | exit_group | `code=0` |
| 3734 | 559.292 | 7169 | downloaded.sh | vfork | `` |
| 3736 | 559.373 | 7171 | downloaded.sh | execve | `/usr/bin/sleep` |
| 3775 | 560.310 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 3777 | 560.346 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 3786 | 560.525 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 3788 | 560.557 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 3792 | 560.631 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 3794 | 560.667 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 3798 | 560.745 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 3800 | 560.788 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 3804 | 560.958 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 3806 | 561.013 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 3810 | 561.171 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 3812 | 561.228 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 3816 | 561.338 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 3818 | 561.388 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 3821 | 561.463 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 3825 | 561.588 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 3827 | 561.643 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 3831 | 562.005 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 3833 | 562.076 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 3837 | 562.248 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 3839 | 562.318 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 3843 | 562.457 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 3845 | 562.507 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 3849 | 562.614 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 3851 | 562.665 | 7171 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 3873 | 763.929 | 7171 | sleep | exit_group | `code=0` |
| 3877 | 764.702 | 7169 | downloaded.sh | exit_group | `code=0` |
| 3925 | 769.642 | 7160 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 72.691 ms |
| Workload CPU (user+sys) | 83.846 ms |
| Tracer peak memory | 23160 KiB |
| Processing time (normalise+correlate+reconstruct) | 12.907 ms |
| Evidence size | 1329400 bytes |

