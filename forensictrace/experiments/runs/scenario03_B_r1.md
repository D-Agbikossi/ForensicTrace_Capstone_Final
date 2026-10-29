# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | B |
| Events recorded | 1139 |
| Failed exec attempts removed | 12 |
| Duration | 553.123 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_B_r1.json` (423005 bytes) |
| SHA-256 | `a689b2e0f4a02180a6c357bf9ebb00de096c5706a46539e55541087a076b78ec` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_B_r1.json.sha256`

## 1. Process tree

- `7231` /usr/bin/bash
  - `7232` /usr/bin/rm
  - `7233` /usr/bin/mkdir
  - `7234` /usr/bin/python3
  - `7235` /usr/bin/sleep
  - `7236` /usr/bin/curl
  - `7237` /usr/bin/python3
  - `7238` /usr/bin/cat
  - `7239` /usr/bin/chmod
  - `7240` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7231 (?) executed `/usr/bin/bash`
- +6.010 ms pid 7232 (bash) executed `/usr/bin/rm`
- +10.066 ms pid 7233 (bash) executed `/usr/bin/mkdir`
- +16.336 ms pid 7234 (bash) executed `/usr/bin/python3`
- +16.363 ms pid 7235 (bash) executed `/usr/bin/sleep`
- +522.982 ms pid 7236 (bash) executed `/usr/bin/curl`
- +542.146 ms pid 7238 (bash) executed `/usr/bin/cat`
- +546.105 ms pid 7239 (bash) executed `/usr/bin/chmod`
- +549.167 ms pid 7240 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +14.635 ms by pid 7231 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +522.819 ms by pid 7236 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +541.951 ms by pid 7238 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +548.505 ms pid 7239 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +8.855 ms pid 7232 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +8.901 ms pid 7232 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +8.933 ms pid 7232 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +8.976 ms pid 7232 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +535.415 ms pid 7236 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +549.167 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7240 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +8.901 ms #138 `unlinkat` by pid 7232 (rm)
    - +541.951 ms #973 `openat` by pid 7238 (bash)
    - +542.027 ms #974 `close` by pid 7238 (bash)
    - +544.862 ms #1041 `write` by pid 7238 (cat)
    - +544.963 ms #1044 `close` by pid 7238 (cat)
    - +548.505 ms #1112 `fchmodat` by pid 7239 (chmod)
    - +549.167 ms #1119 `execve` by pid 7240 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7231 | ? | execve | `/usr/bin/bash` |
| 15 | 1.393 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.431 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.593 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.627 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.701 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.735 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.809 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.842 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.915 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.973 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.068 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 2.110 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.210 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 2.252 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 2.311 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 2.401 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 2.443 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.531 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.573 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 2.668 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 2.711 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 2.800 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.840 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.939 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.979 | 7231 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 4.648 | 7231 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 5.571 | 7231 | bash | clone | `` |
| 73 | 6.010 | 7232 | bash | execve | `/usr/bin/rm` |
| 83 | 7.119 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 7.155 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 7.321 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 7.353 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 7.428 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 7.461 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 7.534 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 7.568 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 7.640 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 7.674 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 7.745 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 7.781 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 7.863 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 7.896 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 8.006 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 8.100 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 8.137 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 8.213 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 8.246 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 8.326 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 8.360 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 8.434 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 8.469 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 8.542 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 8.577 | 7232 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 8.700 | 7232 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 8.855 | 7232 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 8.901 | 7232 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 8.933 | 7232 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 8.976 | 7232 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 9.100 | 7232 | rm | exit_group | `code=0` |
| 146 | 9.702 | 7231 | bash | clone | `` |
| 148 | 10.066 | 7233 | bash | execve | `/usr/bin/mkdir` |
| 168 | 11.799 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 11.845 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 12.044 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 12.086 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 12.193 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 12.244 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 12.360 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 12.428 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 12.560 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 12.633 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 12.771 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 12.829 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 12.966 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 13.026 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 13.103 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 13.215 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 13.271 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 13.382 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 13.438 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 13.550 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 13.599 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 13.710 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 13.760 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 13.905 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 13.956 | 7233 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 14.280 | 7233 | mkdir | exit_group | `code=0` |
| 224 | 14.635 | 7231 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 14.833 | 7231 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 14.996 | 7231 | bash | clone | `` |
| 231 | 16.000 | 7231 | bash | clone | `` |
| 237 | 16.336 | 7234 | bash | execve | `/usr/bin/python3` |
| 238 | 16.363 | 7235 | bash | execve | `/usr/bin/sleep` |
| 261 | 17.717 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 263 | 17.779 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 18.249 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 18.308 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 18.424 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 18.473 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 18.610 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 278 | 18.657 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 280 | 18.772 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 282 | 18.830 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 286 | 19.003 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 289 | 19.056 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 291 | 19.132 | 7234 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 294 | 19.192 | 7234 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 295 | 19.207 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 297 | 19.263 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 300 | 19.354 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 303 | 19.489 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 19.550 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 19.677 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 19.730 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 19.881 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 19.947 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 20.075 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 20.134 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 20.262 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 20.320 | 7235 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 23.341 | 7234 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 23.404 | 7234 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 23.505 | 7234 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 23.532 | 7234 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 23.560 | 7234 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 24.762 | 7234 | python3 | openat | `/etc/localtime` |
| 362 | 30.235 | 7234 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 30.376 | 7234 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 30.582 | 7234 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 31.658 | 7234 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 31.823 | 7234 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 31.988 | 7234 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 41.630 | 7234 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 94.496 | 7234 | python3 | openat | `/etc/gai.conf` |
| 738 | 96.624 | 7234 | python3 | openat | `/etc/nsswitch.conf` |
| 742 | 96.751 | 7234 | python3 | openat | `/etc/host.conf` |
| 746 | 96.848 | 7234 | python3 | openat | `/etc/resolv.conf` |
| 750 | 97.000 | 7234 | python3 | openat | `/etc/hosts` |
| 754 | 97.146 | 7234 | python3 | openat | `/etc/hosts` |
| 759 | 521.295 | 7235 | sleep | exit_group | `code=0` |
| 761 | 522.328 | 7231 | bash | clone | `` |
| 763 | 522.819 | 7236 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 765 | 522.982 | 7236 | bash | execve | `/usr/bin/curl` |
| 861 | 532.010 | 7236 | curl | openat | `/etc/gnutls/config` |
| 879 | 533.490 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 881 | 533.537 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 885 | 533.790 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 887 | 533.838 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 889 | 533.916 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 891 | 533.961 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 893 | 534.034 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 895 | 534.068 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 897 | 534.140 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 899 | 534.174 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 901 | 534.247 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 903 | 534.280 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 905 | 534.363 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 907 | 534.396 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 909 | 534.446 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 911 | 534.525 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 913 | 534.558 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 915 | 534.633 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 917 | 534.667 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 919 | 534.745 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 921 | 534.779 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 923 | 534.852 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 925 | 534.886 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 927 | 534.970 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 929 | 535.004 | 7236 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 931 | 535.088 | 7236 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 932 | 535.107 | 7236 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 935 | 535.303 | 7236 | curl | openat | `/etc/nsswitch.conf` |
| 939 | 535.415 | 7236 | curl | openat | `/etc/passwd` |
| 942 | 535.504 | 7236 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 943 | 536.418 | 7234 | python3 | clone3 | `` |
| 944 | 537.185 | 7237 | python3 | openat | `/etc/mime.types` |
| 957 | 539.598 | 7237 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 965 | 540.025 | 7236 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 966 | 540.115 | 7237 | python3 | exit | `code=0` |
| 969 | 540.463 | 7236 | curl | exit_group | `code=0` |
| 971 | 541.558 | 7231 | bash | clone | `` |
| 973 | 541.951 | 7238 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 978 | 542.146 | 7238 | bash | execve | `/usr/bin/cat` |
| 988 | 543.166 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 990 | 543.202 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 994 | 543.361 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 996 | 543.394 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 998 | 543.469 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1000 | 543.544 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1002 | 543.619 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1004 | 543.661 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1006 | 543.741 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1008 | 543.779 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1010 | 543.856 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1012 | 543.891 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1014 | 543.986 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1016 | 544.019 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1018 | 544.084 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1020 | 544.162 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1022 | 544.206 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1024 | 544.289 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1026 | 544.327 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1028 | 544.415 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1030 | 544.451 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1032 | 544.530 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1034 | 544.569 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1036 | 544.647 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 544.686 | 7238 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 544.862 | 7238 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1046 | 545.005 | 7238 | cat | exit_group | `code=0` |
| 1048 | 545.780 | 7231 | bash | clone | `` |
| 1050 | 546.105 | 7239 | bash | execve | `/usr/bin/chmod` |
| 1060 | 547.040 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1062 | 547.075 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1066 | 547.230 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1068 | 547.264 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1070 | 547.339 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1072 | 547.372 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1074 | 547.448 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1076 | 547.481 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1078 | 547.554 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1080 | 547.587 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1082 | 547.658 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1084 | 547.692 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1086 | 547.772 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1088 | 547.806 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1090 | 547.860 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1092 | 547.934 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1094 | 547.970 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1096 | 548.043 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1098 | 548.077 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1100 | 548.154 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1102 | 548.187 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1104 | 548.259 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1106 | 548.291 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1108 | 548.365 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1110 | 548.399 | 7239 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1112 | 548.505 | 7239 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1115 | 548.573 | 7239 | chmod | exit_group | `code=0` |
| 1117 | 548.836 | 7231 | bash | clone | `` |
| 1119 | 549.167 | 7240 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1125 | 550.114 | 7240 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 550.376 | 7240 | runme.sh | exit_group | `code=0` |
| 1139 | 552.547 | 7231 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 51.247 ms |
| Workload CPU (user+sys) | 76.946 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.540 ms |
| Evidence size | 423005 bytes |

