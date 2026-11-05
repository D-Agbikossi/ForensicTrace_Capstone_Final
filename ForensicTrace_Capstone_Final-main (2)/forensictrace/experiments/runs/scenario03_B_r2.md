# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | B |
| Events recorded | 1139 |
| Failed exec attempts removed | 12 |
| Duration | 649.205 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_B_r2.json` (423005 bytes) |
| SHA-256 | `63fe491c435d00c3b9a3a3ff760110f7a9bfec4ed87727d31c68f6f0bcd40fdd` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_B_r2.json.sha256`

## 1. Process tree

- `7432` /usr/bin/bash
  - `7434` /usr/bin/rm
  - `7435` /usr/bin/mkdir
  - `7436` /usr/bin/python3
  - `7437` /usr/bin/sleep
  - `7440` /usr/bin/curl
  - `7441` /usr/bin/python3
  - `7442` /usr/bin/cat
  - `7443` /usr/bin/chmod
  - `7444` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7432 (?) executed `/usr/bin/bash`
- +18.049 ms pid 7434 (bash) executed `/usr/bin/rm`
- +26.423 ms pid 7435 (bash) executed `/usr/bin/mkdir`
- +37.990 ms pid 7437 (bash) executed `/usr/bin/sleep`
- +39.775 ms pid 7436 (bash) executed `/usr/bin/python3`
- +558.835 ms pid 7440 (bash) executed `/usr/bin/curl`
- +605.762 ms pid 7442 (bash) executed `/usr/bin/cat`
- +625.994 ms pid 7443 (bash) executed `/usr/bin/chmod`
- +639.644 ms pid 7444 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +33.328 ms by pid 7432 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +558.401 ms by pid 7440 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +602.604 ms by pid 7442 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +638.427 ms pid 7443 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +24.167 ms pid 7434 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +24.261 ms pid 7434 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +24.316 ms pid 7434 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +24.395 ms pid 7434 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +591.467 ms pid 7440 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +639.644 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7444 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +24.261 ms #138 `unlinkat` by pid 7434 (rm)
    - +602.604 ms #973 `openat` by pid 7442 (bash)
    - +604.995 ms #974 `close` by pid 7442 (bash)
    - +620.042 ms #1041 `write` by pid 7442 (cat)
    - +620.277 ms #1044 `close` by pid 7442 (cat)
    - +638.427 ms #1112 `fchmodat` by pid 7443 (chmod)
    - +639.644 ms #1119 `execve` by pid 7444 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7432 | ? | execve | `/usr/bin/bash` |
| 15 | 9.368 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 9.428 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 9.688 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 9.739 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 9.855 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 9.906 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 10.020 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 10.069 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 10.323 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 10.376 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 10.499 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 10.549 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 10.687 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 10.744 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 10.819 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 10.943 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 11.004 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 11.124 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 11.173 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 11.295 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 11.351 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 11.479 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 11.540 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 11.692 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 11.751 | 7432 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 15.991 | 7432 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 17.273 | 7432 | bash | clone | `` |
| 73 | 18.049 | 7434 | bash | execve | `/usr/bin/rm` |
| 83 | 20.061 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 20.119 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 20.419 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 20.487 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 20.650 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 20.713 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 20.857 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 20.923 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 21.065 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 21.132 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 21.267 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 21.345 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 21.511 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 22.002 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 22.094 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 22.226 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 22.281 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 22.405 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 22.773 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 22.988 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 23.040 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 23.157 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 23.224 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 23.364 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 23.425 | 7434 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 23.679 | 7434 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 24.167 | 7434 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 24.261 | 7434 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 24.316 | 7434 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 24.395 | 7434 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 24.671 | 7434 | rm | exit_group | `code=0` |
| 146 | 25.874 | 7432 | bash | clone | `` |
| 148 | 26.423 | 7435 | bash | execve | `/usr/bin/mkdir` |
| 168 | 29.684 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 29.747 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 30.011 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 30.063 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 30.218 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 30.275 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 30.400 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 30.452 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 30.581 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 30.638 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 30.781 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 30.839 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 30.978 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 31.063 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 31.165 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 31.318 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 31.369 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 31.485 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 31.539 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 31.683 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 31.739 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 31.856 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 31.923 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 32.069 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 32.123 | 7435 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 32.644 | 7435 | mkdir | exit_group | `code=0` |
| 224 | 33.328 | 7432 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 33.792 | 7432 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 34.026 | 7432 | bash | clone | `` |
| 231 | 36.430 | 7432 | bash | clone | `` |
| 233 | 37.990 | 7437 | bash | execve | `/usr/bin/sleep` |
| 242 | 39.775 | 7436 | bash | execve | `/usr/bin/python3` |
| 255 | 41.125 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 258 | 41.181 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 264 | 41.443 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 267 | 41.497 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 271 | 41.636 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 273 | 41.695 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 275 | 41.810 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 277 | 41.858 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 280 | 41.972 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 282 | 42.027 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 284 | 42.137 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 286 | 42.190 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 288 | 42.308 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 291 | 42.727 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 295 | 42.880 | 7436 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 297 | 42.941 | 7436 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 299 | 43.028 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 43.355 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 43.447 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 44.464 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 44.516 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 44.867 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 45.317 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 48.156 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 48.287 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 48.621 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 48.699 | 7437 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 329 | 49.188 | 7436 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 330 | 49.227 | 7436 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 332 | 49.360 | 7436 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 333 | 49.395 | 7436 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 335 | 49.447 | 7436 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 51.389 | 7436 | python3 | openat | `/etc/localtime` |
| 362 | 57.837 | 7436 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 58.050 | 7436 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 58.467 | 7436 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 59.993 | 7436 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 60.176 | 7436 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 60.352 | 7436 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 75.333 | 7436 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 126.231 | 7436 | python3 | openat | `/etc/gai.conf` |
| 738 | 128.495 | 7436 | python3 | openat | `/etc/nsswitch.conf` |
| 742 | 128.724 | 7436 | python3 | openat | `/etc/host.conf` |
| 746 | 128.875 | 7436 | python3 | openat | `/etc/resolv.conf` |
| 750 | 129.012 | 7436 | python3 | openat | `/etc/hosts` |
| 754 | 129.189 | 7436 | python3 | openat | `/etc/hosts` |
| 759 | 550.296 | 7437 | sleep | exit_group | `code=0` |
| 761 | 554.925 | 7432 | bash | clone | `` |
| 763 | 558.401 | 7440 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 765 | 558.835 | 7440 | bash | execve | `/usr/bin/curl` |
| 861 | 586.369 | 7440 | curl | openat | `/etc/gnutls/config` |
| 879 | 588.438 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 881 | 588.503 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 885 | 588.799 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 887 | 588.862 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 889 | 588.991 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 891 | 589.063 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 893 | 589.191 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 895 | 589.254 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 897 | 589.380 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 899 | 589.441 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 901 | 589.570 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 903 | 589.632 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 905 | 589.771 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 907 | 589.833 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 909 | 589.922 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 911 | 590.055 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 913 | 590.114 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 915 | 590.243 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 917 | 590.305 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 919 | 590.438 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 921 | 590.500 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 923 | 590.631 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 925 | 590.694 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 927 | 590.823 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 929 | 590.885 | 7440 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 931 | 590.996 | 7440 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 932 | 591.023 | 7440 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 935 | 591.306 | 7440 | curl | openat | `/etc/nsswitch.conf` |
| 939 | 591.467 | 7440 | curl | openat | `/etc/passwd` |
| 942 | 591.710 | 7440 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 943 | 593.044 | 7436 | python3 | clone3 | `` |
| 944 | 593.905 | 7441 | python3 | openat | `/etc/mime.types` |
| 957 | 596.605 | 7441 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 965 | 598.056 | 7440 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 966 | 598.128 | 7441 | python3 | exit | `code=0` |
| 969 | 598.680 | 7440 | curl | exit_group | `code=0` |
| 971 | 601.779 | 7432 | bash | clone | `` |
| 973 | 602.604 | 7442 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 978 | 605.762 | 7442 | bash | execve | `/usr/bin/cat` |
| 988 | 614.810 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 990 | 614.934 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 994 | 616.971 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 996 | 617.080 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 998 | 617.224 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1000 | 617.291 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1002 | 617.499 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1004 | 617.700 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1006 | 617.948 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1008 | 618.044 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1010 | 618.155 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1012 | 618.199 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1014 | 618.327 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1016 | 618.389 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1018 | 618.515 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1020 | 618.758 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1022 | 618.829 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1024 | 618.969 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1026 | 619.034 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1028 | 619.209 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1030 | 619.287 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1032 | 619.436 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1034 | 619.510 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1036 | 619.648 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 619.698 | 7442 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 620.042 | 7442 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1046 | 620.355 | 7442 | cat | exit_group | `code=0` |
| 1048 | 623.729 | 7432 | bash | clone | `` |
| 1050 | 625.994 | 7443 | bash | execve | `/usr/bin/chmod` |
| 1060 | 636.126 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1062 | 636.180 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1066 | 636.401 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1068 | 636.448 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1070 | 636.574 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1072 | 636.667 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1074 | 636.771 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1076 | 636.815 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1078 | 636.914 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1080 | 636.962 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1082 | 637.061 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1084 | 637.109 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1086 | 637.222 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1088 | 637.286 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1090 | 637.359 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1092 | 637.465 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1094 | 637.516 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1096 | 637.651 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1098 | 637.711 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1100 | 637.859 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1102 | 637.910 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1104 | 638.032 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1106 | 638.094 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1108 | 638.217 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1110 | 638.262 | 7443 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1112 | 638.427 | 7443 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1115 | 638.572 | 7443 | chmod | exit_group | `code=0` |
| 1117 | 639.153 | 7432 | bash | clone | `` |
| 1119 | 639.644 | 7444 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1125 | 642.312 | 7444 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 642.693 | 7444 | runme.sh | exit_group | `code=0` |
| 1139 | 646.915 | 7432 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 76.813 ms |
| Workload CPU (user+sys) | 100.155 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.526 ms |
| Evidence size | 423005 bytes |

