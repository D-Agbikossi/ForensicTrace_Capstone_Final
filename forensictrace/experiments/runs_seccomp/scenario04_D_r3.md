# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | D |
| Events recorded | 1118 |
| Failed exec attempts removed | 12 |
| Duration | 30.493 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_D_r3.json` (381014 bytes) |
| SHA-256 | `6aef94589368995d6137ae3781a25ee5b32872364a51c1d06542e86229f60cd9` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario04_D_r3.json.sha256`

## 1. Process tree

- `8468` /usr/bin/bash
  - `8469` /usr/bin/rm
  - `8470` /usr/bin/mkdir
  - `8471` /usr/bin/cat
  - `8472` /usr/bin/cat
  - `8473` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8468 (?) executed `/usr/bin/bash`
- +5.192 ms pid 8469 (bash) executed `/usr/bin/rm`
- +10.011 ms pid 8470 (bash) executed `/usr/bin/mkdir`
- +15.171 ms pid 8471 (bash) executed `/usr/bin/cat`
- +18.951 ms pid 8472 (bash) executed `/usr/bin/cat`
- +25.539 ms pid 8473 (bash) executed `/usr/bin/rm`

## 3. Network activity

None observed.

## 4. Files created or modified

- `/tmp/ft_scenario04/important.txt` first touched +13.982 ms by pid 8468 (bash), created/truncated; 2 write call(s), 56 byte(s)

## 5. Permission changes

None observed.

## 6. Deletions

- +8.702 ms pid 8469 (rm) deleted `/tmp/ft_scenario04`
- +29.373 ms pid 8473 (rm) deleted `/tmp/ft_scenario04/important.txt`

## 7. Access to sensitive resources

None observed.

## 8. Provenance of files executed from temporary directories

None.

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8468 | ? | execve | `/usr/bin/bash` |
| 49 | 1.267 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.302 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.463 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.498 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.590 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.633 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 1.785 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 1.828 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 1.903 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 1.937 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 2.015 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 2.049 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 2.132 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 2.165 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.215 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.293 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.327 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.400 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.434 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.513 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.547 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 2.620 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 2.654 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 2.737 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 2.771 | 8468 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 4.056 | 8468 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| 239 | 4.815 | 8468 | bash | clone | `` |
| 256 | 5.192 | 8469 | bash | execve | `/usr/bin/rm` |
| 293 | 6.337 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 6.382 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 6.591 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 6.636 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 6.747 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 6.793 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 6.888 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 6.932 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 7.036 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 7.079 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 7.172 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 7.217 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 7.323 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 7.457 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 7.767 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 7.889 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 7.927 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 8.010 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 8.045 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 8.135 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 8.170 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 8.245 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 8.282 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 8.361 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 8.395 | 8469 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 8.523 | 8469 | rm | openat | `/tmp/ft_scenario04` |
| 386 | 8.702 | 8469 | rm | unlinkat | `/tmp/ft_scenario04` |
| 391 | 8.842 | 8469 | rm | exit_group | `code=0` |
| 425 | 9.626 | 8468 | bash | clone | `` |
| 442 | 10.011 | 8470 | bash | execve | `/usr/bin/mkdir` |
| 506 | 11.464 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 508 | 11.499 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 517 | 11.658 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 519 | 11.692 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 523 | 11.774 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 525 | 11.808 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 529 | 11.883 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 531 | 11.917 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 535 | 11.990 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 537 | 12.023 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 541 | 12.098 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 543 | 12.131 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 547 | 12.214 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 549 | 12.248 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 552 | 12.298 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 556 | 12.370 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 558 | 12.404 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 562 | 12.477 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 564 | 12.510 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 568 | 12.589 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 570 | 12.622 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 574 | 12.694 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 576 | 12.848 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 580 | 12.935 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 582 | 12.973 | 8470 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 593 | 13.295 | 8470 | mkdir | exit_group | `code=0` |
| 603 | 13.982 | 8468 | bash | openat | `/tmp/ft_scenario04/important.txt` |
| 611 | 14.166 | 8468 | bash | write | `/tmp/ft_scenario04/important.txt` |
| 645 | 14.818 | 8468 | bash | clone | `` |
| 662 | 15.171 | 8471 | bash | execve | `/usr/bin/cat` |
| 699 | 16.196 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 701 | 16.232 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 710 | 16.410 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 712 | 16.445 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 716 | 16.519 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 718 | 16.553 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 722 | 16.628 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 724 | 16.662 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 728 | 16.742 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 730 | 16.777 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 734 | 16.852 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 736 | 16.885 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 740 | 16.968 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 742 | 17.002 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 745 | 17.053 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 749 | 17.127 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 751 | 17.162 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 755 | 17.237 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 757 | 17.271 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 761 | 17.350 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 763 | 17.383 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 767 | 17.458 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 769 | 17.491 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 773 | 17.605 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 775 | 17.646 | 8471 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 780 | 17.761 | 8471 | cat | openat | `/tmp/ft_scenario04/important.txt` |
| 791 | 17.965 | 8471 | cat | exit_group | `code=0` |
| 798 | 18.214 | 8468 | bash | openat | `/tmp/ft_scenario04/important.txt` |
| 805 | 18.383 | 8468 | bash | write | `/tmp/ft_scenario04/important.txt` |
| 813 | 18.600 | 8468 | bash | clone | `` |
| 830 | 18.951 | 8472 | bash | execve | `/usr/bin/cat` |
| 867 | 20.006 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 869 | 20.050 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 878 | 20.273 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 880 | 20.320 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 884 | 20.415 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 886 | 20.453 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 890 | 20.552 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 892 | 20.746 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 896 | 20.918 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 898 | 20.971 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 902 | 21.084 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 904 | 21.135 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 908 | 21.247 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 910 | 21.296 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 913 | 21.473 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 21.581 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 21.622 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 923 | 21.728 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 925 | 21.778 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 929 | 21.888 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 931 | 21.939 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 935 | 22.041 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 937 | 22.106 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 941 | 22.261 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 943 | 22.394 | 8472 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 948 | 22.542 | 8472 | cat | openat | `/tmp/ft_scenario04/important.txt` |
| 959 | 23.122 | 8472 | cat | exit_group | `code=0` |
| 968 | 23.992 | 8468 | bash | clone | `` |
| 985 | 25.539 | 8473 | bash | execve | `/usr/bin/rm` |
| 1022 | 27.070 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1024 | 27.120 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1033 | 27.343 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1035 | 27.387 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1039 | 27.487 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1041 | 27.537 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1045 | 27.635 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1047 | 27.681 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1051 | 27.784 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1053 | 27.830 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1057 | 27.928 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1059 | 27.974 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1063 | 28.089 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1065 | 28.137 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1068 | 28.207 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1072 | 28.306 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1074 | 28.352 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1078 | 28.452 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1080 | 28.497 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1084 | 28.604 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1086 | 28.649 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1090 | 28.756 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1092 | 28.833 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1096 | 29.134 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1098 | 29.184 | 8473 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1104 | 29.373 | 8473 | rm | unlinkat | `/tmp/ft_scenario04/important.txt` |
| 1109 | 29.554 | 8473 | rm | exit_group | `code=0` |
| 1118 | 29.924 | 8468 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 17.171 ms |
| Workload CPU (user+sys) | 11.585 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.093 ms |
| Evidence size | 381014 bytes |

