# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | B |
| Events recorded | 1139 |
| Failed exec attempts removed | 12 |
| Duration | 540.188 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_B_r3.json` (423005 bytes) |
| SHA-256 | `7c6a94c143c9113a963b1f633c9f0d0b88d69361196b5e4d5dc560f154395e83` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_B_r3.json.sha256`

## 1. Process tree

- `8429` /usr/bin/bash
  - `8430` /usr/bin/rm
  - `8431` /usr/bin/mkdir
  - `8432` /usr/bin/python3
  - `8433` /usr/bin/sleep
  - `8434` /usr/bin/curl
  - `8435` /usr/bin/python3
  - `8436` /usr/bin/cat
  - `8437` /usr/bin/chmod
  - `8438` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8429 (?) executed `/usr/bin/bash`
- +2.846 ms pid 8430 (bash) executed `/usr/bin/rm`
- +6.055 ms pid 8431 (bash) executed `/usr/bin/mkdir`
- +9.983 ms pid 8433 (bash) executed `/usr/bin/sleep`
- +10.089 ms pid 8432 (bash) executed `/usr/bin/python3`
- +515.441 ms pid 8434 (bash) executed `/usr/bin/curl`
- +533.469 ms pid 8436 (bash) executed `/usr/bin/cat`
- +535.704 ms pid 8437 (bash) executed `/usr/bin/chmod`
- +537.753 ms pid 8438 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +9.274 ms by pid 8429 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +515.245 ms by pid 8434 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +533.327 ms by pid 8436 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +537.392 ms pid 8437 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +5.232 ms pid 8430 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +5.300 ms pid 8430 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +5.354 ms pid 8430 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +5.414 ms pid 8430 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +527.508 ms pid 8434 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +537.753 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8438 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +5.300 ms #138 `unlinkat` by pid 8430 (rm)
    - +533.327 ms #973 `openat` by pid 8436 (bash)
    - +533.387 ms #974 `close` by pid 8436 (bash)
    - +535.241 ms #1041 `write` by pid 8436 (cat)
    - +535.312 ms #1044 `close` by pid 8436 (cat)
    - +537.392 ms #1112 `fchmodat` by pid 8437 (chmod)
    - +537.753 ms #1119 `execve` by pid 8438 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8429 | ? | execve | `/usr/bin/bash` |
| 15 | 0.896 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 0.934 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.028 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.062 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.110 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.144 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.191 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.223 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.270 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.303 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.349 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.384 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.438 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.472 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.513 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.562 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.596 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 1.645 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 1.684 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 1.760 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 1.815 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 1.878 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 1.915 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 1.975 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.015 | 8429 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.403 | 8429 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 2.644 | 8429 | bash | clone | `` |
| 73 | 2.846 | 8430 | bash | execve | `/usr/bin/rm` |
| 83 | 3.587 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.635 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 3.759 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 3.811 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 3.873 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 3.918 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 3.978 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 4.028 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 4.132 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 4.191 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 4.253 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 4.300 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 4.369 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 4.420 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 4.500 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 4.575 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 4.623 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 4.689 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 4.737 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 4.811 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 4.855 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 4.918 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 4.961 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 5.020 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 5.063 | 8430 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 5.138 | 8430 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 5.232 | 8430 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 5.300 | 8430 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 5.354 | 8430 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 5.414 | 8430 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 5.582 | 8430 | rm | exit_group | `code=0` |
| 146 | 5.805 | 8429 | bash | clone | `` |
| 148 | 6.055 | 8431 | bash | execve | `/usr/bin/mkdir` |
| 168 | 7.335 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 7.385 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 7.520 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 7.571 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 7.634 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 7.680 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 7.742 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 7.791 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 7.852 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 7.901 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 7.965 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 8.016 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 8.086 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 8.136 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 8.187 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 8.255 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 8.305 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 8.365 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 8.413 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 8.482 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 8.550 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 8.612 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 8.659 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 8.728 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 8.780 | 8431 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 9.013 | 8431 | mkdir | exit_group | `code=0` |
| 224 | 9.274 | 8429 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 9.364 | 8429 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 9.442 | 8429 | bash | clone | `` |
| 231 | 9.715 | 8429 | bash | clone | `` |
| 235 | 9.983 | 8433 | bash | execve | `/usr/bin/sleep` |
| 238 | 10.089 | 8432 | bash | execve | `/usr/bin/python3` |
| 258 | 10.907 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 262 | 10.967 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 11.089 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 11.135 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 11.198 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 11.242 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 11.301 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 279 | 11.351 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 283 | 11.421 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 286 | 11.472 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 287 | 11.482 | 8432 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 11.548 | 8432 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 291 | 11.560 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 294 | 11.609 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 298 | 11.690 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 300 | 11.734 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 302 | 11.781 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 12.657 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 12.716 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 12.786 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 12.837 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 12.915 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 12.959 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 13.021 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 13.067 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 13.138 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 13.190 | 8433 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 15.206 | 8432 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 15.248 | 8432 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 15.287 | 8432 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 15.308 | 8432 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 15.327 | 8432 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 16.163 | 8432 | python3 | openat | `/etc/localtime` |
| 362 | 19.247 | 8432 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 19.422 | 8432 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 19.636 | 8432 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 20.800 | 8432 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 20.920 | 8432 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 21.001 | 8432 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 29.078 | 8432 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 61.985 | 8432 | python3 | openat | `/etc/gai.conf` |
| 738 | 63.658 | 8432 | python3 | openat | `/etc/nsswitch.conf` |
| 742 | 63.932 | 8432 | python3 | openat | `/etc/host.conf` |
| 746 | 64.222 | 8432 | python3 | openat | `/etc/resolv.conf` |
| 750 | 64.362 | 8432 | python3 | openat | `/etc/hosts` |
| 754 | 64.480 | 8432 | python3 | openat | `/etc/hosts` |
| 759 | 514.152 | 8433 | sleep | exit_group | `code=0` |
| 761 | 514.770 | 8429 | bash | clone | `` |
| 763 | 515.245 | 8434 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 765 | 515.441 | 8434 | bash | execve | `/usr/bin/curl` |
| 861 | 524.446 | 8434 | curl | openat | `/etc/gnutls/config` |
| 879 | 525.654 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 881 | 525.708 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 885 | 525.871 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 887 | 525.926 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 889 | 525.986 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 891 | 526.032 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 893 | 526.095 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 895 | 526.144 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 897 | 526.204 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 899 | 526.250 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 901 | 526.309 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 903 | 526.359 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 905 | 526.431 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 907 | 526.480 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 909 | 526.552 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 911 | 526.619 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 913 | 526.665 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 915 | 526.732 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 917 | 526.786 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 919 | 526.860 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 921 | 526.916 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 923 | 526.974 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 925 | 527.027 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 927 | 527.091 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 929 | 527.143 | 8434 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 931 | 527.216 | 8434 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 932 | 527.245 | 8434 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 935 | 527.383 | 8434 | curl | openat | `/etc/nsswitch.conf` |
| 939 | 527.508 | 8434 | curl | openat | `/etc/passwd` |
| 942 | 527.770 | 8434 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 943 | 528.287 | 8432 | python3 | clone3 | `` |
| 944 | 528.781 | 8435 | python3 | openat | `/etc/mime.types` |
| 957 | 531.411 | 8435 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 964 | 531.893 | 8434 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 968 | 532.046 | 8435 | python3 | exit | `code=0` |
| 969 | 532.446 | 8434 | curl | exit_group | `code=0` |
| 971 | 533.087 | 8429 | bash | clone | `` |
| 973 | 533.327 | 8436 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 978 | 533.469 | 8436 | bash | execve | `/usr/bin/cat` |
| 988 | 534.130 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 990 | 534.168 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 994 | 534.260 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 996 | 534.294 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 998 | 534.342 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1000 | 534.376 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1002 | 534.421 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1004 | 534.456 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1006 | 534.501 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1008 | 534.551 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1010 | 534.597 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1012 | 534.631 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1014 | 534.691 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1016 | 534.724 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1018 | 534.761 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1020 | 534.807 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1022 | 534.841 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1024 | 534.888 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1026 | 534.921 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1028 | 534.974 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1030 | 535.008 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1032 | 535.052 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1034 | 535.087 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1036 | 535.133 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 535.168 | 8436 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 535.241 | 8436 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1046 | 535.351 | 8436 | cat | exit_group | `code=0` |
| 1048 | 535.500 | 8429 | bash | clone | `` |
| 1050 | 535.704 | 8437 | bash | execve | `/usr/bin/chmod` |
| 1060 | 536.319 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1062 | 536.355 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1066 | 536.445 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1068 | 536.480 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1070 | 536.535 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1072 | 536.570 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1074 | 536.617 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1076 | 536.650 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1078 | 536.695 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1080 | 536.734 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1082 | 536.778 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1084 | 536.812 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1086 | 536.866 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1088 | 536.901 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1090 | 536.938 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1092 | 536.983 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1094 | 537.017 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1096 | 537.063 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1098 | 537.098 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1100 | 537.149 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1102 | 537.183 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1104 | 537.228 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1106 | 537.261 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1108 | 537.308 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1110 | 537.342 | 8437 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1112 | 537.392 | 8437 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1115 | 537.461 | 8437 | chmod | exit_group | `code=0` |
| 1117 | 537.588 | 8429 | bash | clone | `` |
| 1119 | 537.753 | 8438 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1125 | 538.241 | 8438 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 538.351 | 8438 | runme.sh | exit_group | `code=0` |
| 1139 | 539.581 | 8429 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 25.431 ms |
| Workload CPU (user+sys) | 68.985 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.496 ms |
| Evidence size | 423005 bytes |

