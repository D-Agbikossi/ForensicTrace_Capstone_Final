# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | B |
| Events recorded | 1139 |
| Failed exec attempts removed | 12 |
| Duration | 601.919 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_B_r4.json` (423006 bytes) |
| SHA-256 | `55235c7a6e96569a64d9a5d89220419646ee4555ad1ce10e8ce8409d3dea0e20` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_B_r4.json.sha256`

## 1. Process tree

- `7823` /usr/bin/bash
  - `7824` /usr/bin/rm
  - `7825` /usr/bin/mkdir
  - `7826` /usr/bin/python3
  - `7827` /usr/bin/sleep
  - `7828` /usr/bin/curl
  - `7829` /usr/bin/python3
  - `7830` /usr/bin/cat
  - `7831` /usr/bin/chmod
  - `7832` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7823 (?) executed `/usr/bin/bash`
- +6.961 ms pid 7824 (bash) executed `/usr/bin/rm`
- +12.322 ms pid 7825 (bash) executed `/usr/bin/mkdir`
- +18.257 ms pid 7827 (bash) executed `/usr/bin/sleep`
- +18.406 ms pid 7826 (bash) executed `/usr/bin/python3`
- +528.278 ms pid 7828 (bash) executed `/usr/bin/curl`
- +571.491 ms pid 7830 (bash) executed `/usr/bin/cat`
- +580.005 ms pid 7831 (bash) executed `/usr/bin/chmod`
- +589.380 ms pid 7832 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +16.457 ms by pid 7823 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +528.013 ms by pid 7828 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +571.221 ms by pid 7830 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +587.560 ms pid 7831 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +10.715 ms pid 7824 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +10.766 ms pid 7824 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +10.798 ms pid 7824 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +10.842 ms pid 7824 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +555.580 ms pid 7828 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +589.380 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7832 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +10.766 ms #138 `unlinkat` by pid 7824 (rm)
    - +571.221 ms #973 `openat` by pid 7830 (bash)
    - +571.327 ms #974 `close` by pid 7830 (bash)
    - +577.252 ms #1041 `write` by pid 7830 (cat)
    - +577.394 ms #1044 `close` by pid 7830 (cat)
    - +587.560 ms #1112 `fchmodat` by pid 7831 (chmod)
    - +589.380 ms #1119 `execve` by pid 7832 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7823 | ? | execve | `/usr/bin/bash` |
| 15 | 1.769 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.817 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 2.042 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 2.088 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 2.190 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 2.236 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.340 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.383 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.480 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.522 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.618 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 2.661 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.763 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 2.805 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 2.866 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 2.957 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 3.023 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 3.113 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 3.155 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 3.255 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.298 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 3.390 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 3.431 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 3.526 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 3.567 | 7823 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 5.155 | 7823 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 6.482 | 7823 | bash | clone | `` |
| 73 | 6.961 | 7824 | bash | execve | `/usr/bin/rm` |
| 83 | 8.703 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 8.741 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 8.915 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 8.949 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 9.040 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 9.074 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 9.153 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 9.188 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 9.264 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 9.299 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 9.374 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 9.409 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 9.494 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 9.527 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 9.578 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 9.652 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 9.686 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 9.761 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 9.794 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 9.874 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 9.906 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 10.037 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 10.085 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 10.344 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 10.382 | 7824 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 10.528 | 7824 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 10.715 | 7824 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 10.766 | 7824 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 10.798 | 7824 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 10.842 | 7824 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 11.057 | 7824 | rm | exit_group | `code=0` |
| 146 | 11.948 | 7823 | bash | clone | `` |
| 148 | 12.322 | 7825 | bash | execve | `/usr/bin/mkdir` |
| 168 | 14.271 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 14.309 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 14.470 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 14.505 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 14.583 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 14.618 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 14.691 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 14.724 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 14.796 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 14.831 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 14.905 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 14.939 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 15.054 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 15.100 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 15.160 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 15.250 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 15.292 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 15.380 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 15.423 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 15.519 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 15.561 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 15.650 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 15.691 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 15.783 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 15.824 | 7825 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 16.132 | 7825 | mkdir | exit_group | `code=0` |
| 224 | 16.457 | 7823 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 16.662 | 7823 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 16.845 | 7823 | bash | clone | `` |
| 231 | 17.846 | 7823 | bash | clone | `` |
| 235 | 18.257 | 7827 | bash | execve | `/usr/bin/sleep` |
| 238 | 18.406 | 7826 | bash | execve | `/usr/bin/python3` |
| 262 | 19.735 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 264 | 19.776 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 19.973 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 20.025 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 20.127 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 20.172 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 20.266 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 278 | 20.308 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 281 | 20.406 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 284 | 20.459 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 288 | 20.556 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 289 | 20.566 | 7826 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 292 | 20.605 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 293 | 20.623 | 7826 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 296 | 20.719 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 299 | 20.768 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 302 | 20.843 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 20.934 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 21.092 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 21.190 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 21.241 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 21.351 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 21.398 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 21.508 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 21.560 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 21.674 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 21.727 | 7827 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 24.372 | 7826 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 24.405 | 7826 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 24.486 | 7826 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 24.510 | 7826 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 24.534 | 7826 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 25.566 | 7826 | python3 | openat | `/etc/localtime` |
| 362 | 30.947 | 7826 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 31.175 | 7826 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 31.521 | 7826 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 33.233 | 7826 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 33.616 | 7826 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 33.836 | 7826 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 44.062 | 7826 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 90.407 | 7826 | python3 | openat | `/etc/gai.conf` |
| 738 | 93.828 | 7826 | python3 | openat | `/etc/nsswitch.conf` |
| 742 | 93.993 | 7826 | python3 | openat | `/etc/host.conf` |
| 746 | 94.112 | 7826 | python3 | openat | `/etc/resolv.conf` |
| 750 | 94.245 | 7826 | python3 | openat | `/etc/hosts` |
| 754 | 94.418 | 7826 | python3 | openat | `/etc/hosts` |
| 759 | 523.368 | 7827 | sleep | exit_group | `code=0` |
| 761 | 526.713 | 7823 | bash | clone | `` |
| 763 | 528.013 | 7828 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 765 | 528.278 | 7828 | bash | execve | `/usr/bin/curl` |
| 861 | 550.165 | 7828 | curl | openat | `/etc/gnutls/config` |
| 879 | 551.933 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 881 | 552.010 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 885 | 552.318 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 887 | 552.381 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 889 | 552.521 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 891 | 552.583 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 893 | 552.707 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 895 | 552.769 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 897 | 552.926 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 899 | 553.121 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 901 | 553.343 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 903 | 553.720 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 905 | 553.936 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 907 | 554.057 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 909 | 554.156 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 911 | 554.328 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 913 | 554.416 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 915 | 554.517 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 917 | 554.568 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 919 | 554.673 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 921 | 554.719 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 923 | 554.814 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 925 | 554.859 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 927 | 554.967 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 929 | 555.012 | 7828 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 931 | 555.119 | 7828 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 932 | 555.145 | 7828 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 935 | 555.425 | 7828 | curl | openat | `/etc/nsswitch.conf` |
| 939 | 555.580 | 7828 | curl | openat | `/etc/passwd` |
| 942 | 555.699 | 7828 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 943 | 557.132 | 7826 | python3 | clone3 | `` |
| 944 | 558.327 | 7829 | python3 | openat | `/etc/mime.types` |
| 957 | 565.693 | 7829 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 965 | 567.050 | 7828 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 966 | 567.176 | 7829 | python3 | exit | `code=0` |
| 969 | 568.390 | 7828 | curl | exit_group | `code=0` |
| 971 | 570.125 | 7823 | bash | clone | `` |
| 973 | 571.221 | 7830 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 978 | 571.491 | 7830 | bash | execve | `/usr/bin/cat` |
| 988 | 573.810 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 990 | 573.865 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 994 | 574.558 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 996 | 574.911 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 998 | 575.455 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1000 | 575.515 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1002 | 575.694 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1004 | 575.743 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1006 | 575.846 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1008 | 575.893 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1010 | 576.011 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1012 | 576.056 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1014 | 576.168 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1016 | 576.213 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1018 | 576.281 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1020 | 576.384 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1022 | 576.428 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1024 | 576.536 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1026 | 576.579 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1028 | 576.687 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1030 | 576.732 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1032 | 576.827 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1034 | 576.872 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1036 | 576.981 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 577.025 | 7830 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 577.252 | 7830 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1046 | 577.448 | 7830 | cat | exit_group | `code=0` |
| 1048 | 579.223 | 7823 | bash | clone | `` |
| 1050 | 580.005 | 7831 | bash | execve | `/usr/bin/chmod` |
| 1060 | 582.658 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1062 | 582.717 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1066 | 583.021 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1068 | 583.078 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1070 | 583.687 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1072 | 583.738 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1074 | 583.843 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1076 | 583.891 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1078 | 584.727 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1080 | 584.970 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1082 | 585.107 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1084 | 585.162 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1086 | 585.293 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1088 | 585.347 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1090 | 585.423 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1092 | 585.550 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1094 | 586.427 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1096 | 586.602 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1098 | 586.664 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1100 | 586.807 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1102 | 586.857 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1104 | 587.019 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1106 | 587.090 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1108 | 587.250 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1110 | 587.325 | 7831 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1112 | 587.560 | 7831 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1115 | 587.738 | 7831 | chmod | exit_group | `code=0` |
| 1117 | 588.475 | 7823 | bash | clone | `` |
| 1119 | 589.380 | 7832 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1125 | 593.076 | 7832 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 595.234 | 7832 | runme.sh | exit_group | `code=0` |
| 1139 | 601.072 | 7823 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 66.738 ms |
| Workload CPU (user+sys) | 90.675 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 2.371 ms |
| Evidence size | 423006 bytes |

