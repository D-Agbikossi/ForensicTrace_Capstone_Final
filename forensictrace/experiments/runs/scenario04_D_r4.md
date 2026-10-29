# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario04 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| Evidence configuration | D |
| Events recorded | 1118 |
| Failed exec attempts removed | 12 |
| Duration | 24.958 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_D_r4.json` (381012 bytes) |
| SHA-256 | `4801b658d405c516e48ada727f5b555377bec7f80334a4e75ce03a4bafb345fa` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario04_D_r4.json.sha256`

## 1. Process tree

- `7862` /usr/bin/bash
  - `7863` /usr/bin/rm
  - `7864` /usr/bin/mkdir
  - `7865` /usr/bin/cat
  - `7866` /usr/bin/cat
  - `7867` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7862 (?) executed `/usr/bin/bash`
- +4.899 ms pid 7863 (bash) executed `/usr/bin/rm`
- +9.194 ms pid 7864 (bash) executed `/usr/bin/mkdir`
- +14.886 ms pid 7865 (bash) executed `/usr/bin/cat`
- +18.439 ms pid 7866 (bash) executed `/usr/bin/cat`
- +21.655 ms pid 7867 (bash) executed `/usr/bin/rm`

## 3. Network activity

None observed.

## 4. Files created or modified

- `/tmp/ft_scenario04/important.txt` first touched +13.624 ms by pid 7862 (bash), created/truncated; 2 write call(s), 56 byte(s)

## 5. Permission changes

None observed.

## 6. Deletions

- +8.027 ms pid 7863 (rm) deleted `/tmp/ft_scenario04`
- +24.040 ms pid 7867 (rm) deleted `/tmp/ft_scenario04/important.txt`

## 7. Access to sensitive resources

None observed.

## 8. Provenance of files executed from temporary directories

None.

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7862 | ? | execve | `/usr/bin/bash` |
| 49 | 1.162 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 1.196 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 1.360 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 1.393 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 1.468 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 1.500 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 1.579 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 1.622 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 1.695 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 1.731 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 1.807 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 1.841 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 1.921 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 1.953 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 2.004 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 2.076 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 2.109 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 2.180 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 2.214 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 2.288 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 2.322 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 2.429 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 2.464 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 2.538 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 2.570 | 7862 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 3.810 | 7862 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario04_file_corruption.sh` |
| 239 | 4.544 | 7862 | bash | clone | `` |
| 256 | 4.899 | 7863 | bash | execve | `/usr/bin/rm` |
| 293 | 5.964 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 6.006 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 6.199 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 6.241 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 6.331 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 6.381 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 6.471 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 6.511 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 6.602 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 6.642 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 6.729 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 6.771 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 6.871 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 6.913 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 6.973 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 7.064 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 7.106 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 7.196 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 7.236 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 7.339 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 7.395 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 7.486 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 7.528 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 7.618 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 7.659 | 7863 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 7.812 | 7863 | rm | openat | `/tmp/ft_scenario04` |
| 386 | 8.027 | 7863 | rm | unlinkat | `/tmp/ft_scenario04` |
| 391 | 8.178 | 7863 | rm | exit_group | `code=0` |
| 425 | 8.841 | 7862 | bash | clone | `` |
| 442 | 9.194 | 7864 | bash | execve | `/usr/bin/mkdir` |
| 506 | 10.938 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 508 | 10.980 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 517 | 11.169 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 519 | 11.211 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 523 | 11.300 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 525 | 11.341 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 529 | 11.435 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 531 | 11.477 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 535 | 11.565 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 537 | 11.604 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 541 | 11.694 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 543 | 11.733 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 547 | 11.831 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 549 | 11.873 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 552 | 11.933 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 556 | 12.022 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 558 | 12.067 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 562 | 12.160 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 564 | 12.201 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 568 | 12.296 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 570 | 12.335 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 574 | 12.475 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 576 | 12.523 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 580 | 12.953 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 582 | 13.009 | 7864 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 593 | 13.312 | 7864 | mkdir | exit_group | `code=0` |
| 603 | 13.624 | 7862 | bash | openat | `/tmp/ft_scenario04/important.txt` |
| 611 | 13.777 | 7862 | bash | write | `/tmp/ft_scenario04/important.txt` |
| 645 | 14.547 | 7862 | bash | clone | `` |
| 662 | 14.886 | 7865 | bash | execve | `/usr/bin/cat` |
| 699 | 15.838 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 701 | 15.874 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 710 | 16.031 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 712 | 16.065 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 716 | 16.144 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 718 | 16.178 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 722 | 16.252 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 724 | 16.286 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 728 | 16.363 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 730 | 16.397 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 734 | 16.470 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 736 | 16.502 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 740 | 16.585 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 742 | 16.619 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 745 | 16.669 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 749 | 16.748 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 751 | 16.782 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 755 | 16.860 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 757 | 16.894 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 761 | 16.970 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 763 | 17.003 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 767 | 17.077 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 769 | 17.110 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 773 | 17.183 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 775 | 17.217 | 7865 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 780 | 17.303 | 7865 | cat | openat | `/tmp/ft_scenario04/important.txt` |
| 791 | 17.505 | 7865 | cat | exit_group | `code=0` |
| 798 | 17.721 | 7862 | bash | openat | `/tmp/ft_scenario04/important.txt` |
| 805 | 17.880 | 7862 | bash | write | `/tmp/ft_scenario04/important.txt` |
| 813 | 18.113 | 7862 | bash | clone | `` |
| 830 | 18.439 | 7866 | bash | execve | `/usr/bin/cat` |
| 867 | 19.367 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 869 | 19.403 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 878 | 19.562 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 880 | 19.595 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 884 | 19.670 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 886 | 19.702 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 890 | 19.776 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 892 | 19.808 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 896 | 19.881 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 898 | 19.915 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 902 | 19.985 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 904 | 20.019 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 908 | 20.104 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 910 | 20.138 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 913 | 20.202 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 20.286 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 20.320 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 923 | 20.400 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 925 | 20.435 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 929 | 20.510 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 931 | 20.544 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 935 | 20.616 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 937 | 20.650 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 941 | 20.724 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 943 | 20.756 | 7866 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 948 | 20.844 | 7866 | cat | openat | `/tmp/ft_scenario04/important.txt` |
| 959 | 21.041 | 7866 | cat | exit_group | `code=0` |
| 968 | 21.308 | 7862 | bash | clone | `` |
| 985 | 21.655 | 7867 | bash | execve | `/usr/bin/rm` |
| 1022 | 22.562 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1024 | 22.597 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1033 | 22.758 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1035 | 22.791 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1039 | 22.864 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1041 | 22.899 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1045 | 22.971 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1047 | 23.005 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1051 | 23.077 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1053 | 23.111 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1057 | 23.181 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1059 | 23.214 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1063 | 23.295 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1065 | 23.328 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1068 | 23.383 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1072 | 23.455 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1074 | 23.490 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1078 | 23.564 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1080 | 23.598 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1084 | 23.674 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1086 | 23.707 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1090 | 23.779 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1092 | 23.812 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1096 | 23.885 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1098 | 23.918 | 7867 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1104 | 24.040 | 7867 | rm | unlinkat | `/tmp/ft_scenario04/important.txt` |
| 1109 | 24.190 | 7867 | rm | exit_group | `code=0` |
| 1118 | 24.500 | 7862 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 15.495 ms |
| Workload CPU (user+sys) | 9.713 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.831 ms |
| Evidence size | 381012 bytes |

