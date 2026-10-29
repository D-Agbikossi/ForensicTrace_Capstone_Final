# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | D |
| Events recorded | 1118 |
| Failed exec attempts removed | 12 |
| Duration | 42.875 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_D_r4.json` (382031 bytes) |
| SHA-256 | `455d3412d9e77c7dd2ba020bb16110a6a1596a83cd3be63767d186763418be89` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario02_D_r4.json.sha256`

## 1. Process tree

- `8582` /usr/bin/bash
  - `8583` /usr/bin/rm
  - `8584` /usr/bin/mkdir
  - `8585` /usr/bin/cat
  - `8586` /usr/bin/cat
  - `8587` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8582 (?) executed `/usr/bin/bash`
- +9.318 ms pid 8583 (bash) executed `/usr/bin/rm`
- +16.304 ms pid 8584 (bash) executed `/usr/bin/mkdir`
- +26.450 ms pid 8585 (bash) executed `/usr/bin/cat`
- +30.989 ms pid 8586 (bash) executed `/usr/bin/cat`
- +36.699 ms pid 8587 (bash) executed `/usr/bin/rm`

## 3. Network activity

None observed.

## 4. Files created or modified

- `/tmp/ft_scenario02/fake_passwd_entry` first touched +30.145 ms by pid 8582 (bash), created/truncated; 1 write call(s), 43 byte(s)

## 5. Permission changes

None observed.

## 6. Deletions

- +14.827 ms pid 8583 (rm) deleted `/tmp/ft_scenario02`
- +40.680 ms pid 8587 (rm) deleted `/tmp/ft_scenario02/fake_passwd_entry`

## 7. Access to sensitive resources

- +29.315 ms pid 8585 (cat) `openat` on `/etc/shadow` — **attempt failed** (access denied or missing)

## 8. Provenance of files executed from temporary directories

None.

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8582 | ? | execve | `/usr/bin/bash` |
| 49 | 2.346 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 51 | 2.455 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 60 | 2.869 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 62 | 2.939 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 66 | 3.171 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 68 | 3.229 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 72 | 3.401 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 74 | 3.680 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 78 | 3.833 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 80 | 3.885 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 84 | 3.996 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 86 | 4.062 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 90 | 4.273 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 92 | 4.319 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 95 | 4.430 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 99 | 4.544 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 101 | 4.588 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 105 | 4.685 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 107 | 4.732 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 111 | 4.853 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 113 | 4.905 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 117 | 5.008 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 119 | 5.054 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 123 | 5.159 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 125 | 5.205 | 8582 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 195 | 7.185 | 8582 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| 239 | 8.498 | 8582 | bash | clone | `` |
| 256 | 9.318 | 8583 | bash | execve | `/usr/bin/rm` |
| 293 | 12.001 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 295 | 12.058 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 304 | 12.289 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 306 | 12.335 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 310 | 12.437 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 312 | 12.484 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 316 | 12.588 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 318 | 12.632 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 322 | 12.732 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 324 | 12.776 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 328 | 12.877 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 330 | 12.922 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 334 | 13.030 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 336 | 13.076 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 339 | 13.142 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 343 | 13.240 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 345 | 13.287 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 349 | 13.389 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 351 | 13.433 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 355 | 13.542 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 357 | 13.586 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 361 | 13.682 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 363 | 13.728 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 367 | 13.838 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 369 | 13.884 | 8583 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 14.057 | 8583 | rm | openat | `/tmp/ft_scenario02` |
| 386 | 14.827 | 8583 | rm | unlinkat | `/tmp/ft_scenario02` |
| 391 | 15.075 | 8583 | rm | exit_group | `code=0` |
| 425 | 15.881 | 8582 | bash | clone | `` |
| 442 | 16.304 | 8584 | bash | execve | `/usr/bin/mkdir` |
| 506 | 19.500 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 508 | 19.558 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 517 | 19.830 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 519 | 19.883 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 523 | 20.009 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 525 | 20.058 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 529 | 20.159 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 531 | 20.207 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 535 | 20.310 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 537 | 20.359 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 541 | 20.465 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 543 | 20.512 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 547 | 20.637 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 549 | 20.692 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 552 | 20.759 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 556 | 21.053 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 558 | 21.115 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 562 | 21.221 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 564 | 21.274 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 568 | 21.416 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 570 | 21.507 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 574 | 21.671 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 576 | 21.738 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 580 | 21.995 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 582 | 22.140 | 8584 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 593 | 22.897 | 8584 | mkdir | exit_group | `code=0` |
| 632 | 25.678 | 8582 | bash | clone | `` |
| 654 | 26.450 | 8585 | bash | execve | `/usr/bin/cat` |
| 691 | 27.622 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 693 | 27.658 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 702 | 27.845 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 704 | 27.881 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 708 | 27.958 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 710 | 27.991 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 714 | 28.067 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 716 | 28.100 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 720 | 28.175 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 722 | 28.210 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 726 | 28.284 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 728 | 28.318 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 732 | 28.402 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 734 | 28.437 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 737 | 28.487 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 741 | 28.563 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 743 | 28.597 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 747 | 28.672 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 749 | 28.707 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 753 | 28.788 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 755 | 28.841 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 759 | 28.947 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 761 | 28.994 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 765 | 29.093 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 767 | 29.138 | 8585 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 772 | 29.315 | 8585 | cat | openat | `/etc/shadow` (failed) |
| 791 | 29.863 | 8585 | cat | exit_group | `code=1` |
| 798 | 30.145 | 8582 | bash | openat | `/tmp/ft_scenario02/fake_passwd_entry` |
| 806 | 30.332 | 8582 | bash | write | `/tmp/ft_scenario02/fake_passwd_entry` |
| 813 | 30.526 | 8582 | bash | clone | `` |
| 830 | 30.989 | 8586 | bash | execve | `/usr/bin/cat` |
| 867 | 32.250 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 869 | 32.286 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 878 | 32.449 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 880 | 32.482 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 884 | 32.559 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 886 | 32.592 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 890 | 32.668 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 892 | 32.701 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 896 | 32.775 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 898 | 32.820 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 902 | 32.894 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 904 | 32.929 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 908 | 33.012 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 910 | 33.046 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 913 | 33.102 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 33.206 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 33.246 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 923 | 33.348 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 925 | 33.392 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 929 | 33.559 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 931 | 33.604 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 935 | 33.696 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 937 | 33.738 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 941 | 33.840 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 943 | 33.880 | 8586 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 948 | 33.996 | 8586 | cat | openat | `/tmp/ft_scenario02/fake_passwd_entry` |
| 959 | 34.273 | 8586 | cat | exit_group | `code=0` |
| 968 | 35.009 | 8582 | bash | clone | `` |
| 985 | 36.699 | 8587 | bash | execve | `/usr/bin/rm` |
| 1022 | 38.298 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1024 | 38.546 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1033 | 38.913 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1035 | 38.966 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1039 | 39.069 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1041 | 39.117 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1045 | 39.221 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1047 | 39.268 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1051 | 39.371 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1053 | 39.419 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1057 | 39.520 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1059 | 39.567 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1063 | 39.684 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1065 | 39.729 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1068 | 39.796 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1072 | 39.933 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1074 | 39.975 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1078 | 40.071 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1080 | 40.112 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1084 | 40.220 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1086 | 40.259 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1090 | 40.351 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1092 | 40.390 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1096 | 40.484 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1098 | 40.523 | 8587 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1104 | 40.680 | 8587 | rm | unlinkat | `/tmp/ft_scenario02/fake_passwd_entry` |
| 1109 | 40.893 | 8587 | rm | exit_group | `code=0` |
| 1118 | 42.164 | 8582 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 21.471 ms |
| Workload CPU (user+sys) | 15.895 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.014 ms |
| Evidence size | 382031 bytes |

