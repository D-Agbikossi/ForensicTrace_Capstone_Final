# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | B |
| Events recorded | 1139 |
| Failed exec attempts removed | 12 |
| Duration | 540.497 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_B_r4.json` (423005 bytes) |
| SHA-256 | `be760a4ec35a80d1ae15403fafe4122f434228845c3b63af89677f3bf71c017a` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_B_r4.json.sha256`

## 1. Process tree

- `8624` /usr/bin/bash
  - `8625` /usr/bin/rm
  - `8626` /usr/bin/mkdir
  - `8627` /usr/bin/python3
  - `8628` /usr/bin/sleep
  - `8633` /usr/bin/curl
  - `8634` /usr/bin/python3
  - `8635` /usr/bin/cat
  - `8636` /usr/bin/chmod
  - `8637` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8624 (?) executed `/usr/bin/bash`
- +2.885 ms pid 8625 (bash) executed `/usr/bin/rm`
- +6.971 ms pid 8626 (bash) executed `/usr/bin/mkdir`
- +11.264 ms pid 8627 (bash) executed `/usr/bin/python3`
- +11.282 ms pid 8628 (bash) executed `/usr/bin/sleep`
- +516.543 ms pid 8633 (bash) executed `/usr/bin/curl`
- +533.771 ms pid 8635 (bash) executed `/usr/bin/cat`
- +535.891 ms pid 8636 (bash) executed `/usr/bin/chmod`
- +537.828 ms pid 8637 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +10.609 ms by pid 8624 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +516.297 ms by pid 8633 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +533.621 ms by pid 8635 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +537.503 ms pid 8636 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +5.984 ms pid 8625 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +6.046 ms pid 8625 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +6.085 ms pid 8625 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +6.144 ms pid 8625 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +529.215 ms pid 8633 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +537.828 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8637 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +6.046 ms #138 `unlinkat` by pid 8625 (rm)
    - +533.621 ms #973 `openat` by pid 8635 (bash)
    - +533.676 ms #974 `close` by pid 8635 (bash)
    - +535.485 ms #1041 `write` by pid 8635 (cat)
    - +535.555 ms #1044 `close` by pid 8635 (cat)
    - +537.503 ms #1112 `fchmodat` by pid 8636 (chmod)
    - +537.828 ms #1119 `execve` by pid 8637 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8624 | ? | execve | `/usr/bin/bash` |
| 15 | 0.875 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 0.923 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.040 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.086 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.144 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.192 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.250 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.295 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.354 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.398 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.459 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.504 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.569 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.614 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.660 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.755 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.804 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 1.862 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 1.907 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 1.972 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 2.017 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 2.075 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.118 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.178 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.222 | 8624 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.501 | 8624 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 2.704 | 8624 | bash | clone | `` |
| 73 | 2.885 | 8625 | bash | execve | `/usr/bin/rm` |
| 83 | 3.464 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.499 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 3.590 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 3.623 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 3.674 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 3.714 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 3.774 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 3.818 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 3.876 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 3.921 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 3.974 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 4.021 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 4.078 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 4.111 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 4.148 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 4.193 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 4.246 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 5.331 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 5.441 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 5.531 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 5.578 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 5.647 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 5.696 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 5.771 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 5.826 | 8625 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 5.904 | 8625 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 5.984 | 8625 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 6.046 | 8625 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 6.085 | 8625 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 6.144 | 8625 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 6.309 | 8625 | rm | exit_group | `code=0` |
| 146 | 6.670 | 8624 | bash | clone | `` |
| 148 | 6.971 | 8626 | bash | execve | `/usr/bin/mkdir` |
| 168 | 8.863 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 8.909 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 9.029 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 9.069 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 9.128 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 9.168 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 9.229 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 9.269 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 9.327 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 9.367 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 9.427 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 9.468 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 9.536 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 9.579 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 9.623 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 9.681 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 9.736 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 9.799 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 9.840 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 9.904 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 9.945 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 10.006 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 10.046 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 10.105 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 10.144 | 8626 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 10.349 | 8626 | mkdir | exit_group | `code=0` |
| 224 | 10.609 | 8624 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 10.693 | 8624 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 10.776 | 8624 | bash | clone | `` |
| 231 | 11.055 | 8624 | bash | clone | `` |
| 237 | 11.264 | 8627 | bash | execve | `/usr/bin/python3` |
| 238 | 11.282 | 8628 | bash | execve | `/usr/bin/sleep` |
| 258 | 12.236 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 262 | 12.292 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 12.410 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 12.457 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 12.524 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 275 | 12.802 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 277 | 12.937 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 280 | 12.988 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 283 | 13.042 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 286 | 13.085 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 287 | 13.098 | 8627 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 13.140 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 291 | 13.157 | 8627 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 13.190 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 298 | 13.266 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 300 | 13.315 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 302 | 13.365 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 13.423 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 13.471 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 13.532 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 13.582 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 13.651 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 13.698 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 13.777 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 13.824 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 13.887 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 13.934 | 8628 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 15.903 | 8627 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 15.954 | 8627 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 16.001 | 8627 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 16.028 | 8627 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 16.054 | 8627 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 16.837 | 8627 | python3 | openat | `/etc/localtime` |
| 362 | 19.878 | 8627 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 19.988 | 8627 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 20.153 | 8627 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 21.227 | 8627 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 21.382 | 8627 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 22.938 | 8627 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 33.291 | 8627 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 71.782 | 8627 | python3 | openat | `/etc/gai.conf` |
| 738 | 74.247 | 8627 | python3 | openat | `/etc/nsswitch.conf` |
| 742 | 74.391 | 8627 | python3 | openat | `/etc/host.conf` |
| 746 | 74.504 | 8627 | python3 | openat | `/etc/resolv.conf` |
| 750 | 74.624 | 8627 | python3 | openat | `/etc/hosts` |
| 754 | 74.758 | 8627 | python3 | openat | `/etc/hosts` |
| 759 | 515.030 | 8628 | sleep | exit_group | `code=0` |
| 761 | 515.638 | 8624 | bash | clone | `` |
| 763 | 516.297 | 8633 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 765 | 516.543 | 8633 | bash | execve | `/usr/bin/curl` |
| 861 | 526.415 | 8633 | curl | openat | `/etc/gnutls/config` |
| 879 | 527.564 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 881 | 527.613 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 885 | 527.791 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 887 | 527.839 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 889 | 527.908 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 891 | 527.982 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 893 | 528.056 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 895 | 528.103 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 897 | 528.192 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 899 | 528.250 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 901 | 528.316 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 903 | 528.350 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 905 | 528.407 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 907 | 528.441 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 909 | 528.477 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 911 | 528.528 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 913 | 528.561 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 915 | 528.609 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 917 | 528.643 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 919 | 528.693 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 921 | 528.733 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 923 | 528.780 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 925 | 528.815 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 927 | 528.862 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 929 | 528.895 | 8633 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 931 | 528.951 | 8633 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 932 | 528.970 | 8633 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 935 | 529.064 | 8633 | curl | openat | `/etc/nsswitch.conf` |
| 939 | 529.215 | 8633 | curl | openat | `/etc/passwd` |
| 942 | 529.280 | 8633 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 943 | 529.654 | 8627 | python3 | clone3 | `` |
| 944 | 530.058 | 8634 | python3 | openat | `/etc/mime.types` |
| 957 | 532.240 | 8634 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 964 | 532.559 | 8633 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 968 | 532.675 | 8634 | python3 | exit | `code=0` |
| 969 | 532.857 | 8633 | curl | exit_group | `code=0` |
| 971 | 533.397 | 8624 | bash | clone | `` |
| 973 | 533.621 | 8635 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 978 | 533.771 | 8635 | bash | execve | `/usr/bin/cat` |
| 988 | 534.390 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 990 | 534.427 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 994 | 534.519 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 996 | 534.552 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 998 | 534.600 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1000 | 534.634 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1002 | 534.679 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1004 | 534.717 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1006 | 534.763 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1008 | 534.797 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1010 | 534.842 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1012 | 534.875 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1014 | 534.930 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1016 | 534.963 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1018 | 534.999 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1020 | 535.046 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1022 | 535.079 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1024 | 535.128 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1026 | 535.164 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1028 | 535.216 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1030 | 535.251 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1032 | 535.295 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1034 | 535.329 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1036 | 535.375 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 535.409 | 8635 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 535.485 | 8635 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1046 | 535.593 | 8635 | cat | exit_group | `code=0` |
| 1048 | 535.742 | 8624 | bash | clone | `` |
| 1050 | 535.891 | 8636 | bash | execve | `/usr/bin/chmod` |
| 1060 | 536.448 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1062 | 536.483 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1066 | 536.571 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1068 | 536.609 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1070 | 536.655 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1072 | 536.688 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1074 | 536.741 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1076 | 536.775 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1078 | 536.821 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1080 | 536.855 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1082 | 536.898 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1084 | 536.932 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1086 | 536.985 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1088 | 537.019 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1090 | 537.056 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1092 | 537.100 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1094 | 537.134 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1096 | 537.179 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1098 | 537.213 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1100 | 537.263 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1102 | 537.296 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1104 | 537.341 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1106 | 537.374 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1108 | 537.420 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1110 | 537.454 | 8636 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1112 | 537.503 | 8636 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1115 | 537.570 | 8636 | chmod | exit_group | `code=0` |
| 1117 | 537.687 | 8624 | bash | clone | `` |
| 1119 | 537.828 | 8637 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1125 | 538.371 | 8637 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 538.512 | 8637 | runme.sh | exit_group | `code=0` |
| 1139 | 539.696 | 8624 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 26.383 ms |
| Workload CPU (user+sys) | 73.686 ms |
| Tracer peak memory | 30128 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.686 ms |
| Evidence size | 423005 bytes |

