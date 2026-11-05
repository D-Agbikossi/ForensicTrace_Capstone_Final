# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | C |
| Events recorded | 1155 |
| Failed exec attempts removed | 12 |
| Duration | 553.527 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_C_r2.json` (428526 bytes) |
| SHA-256 | `a3a70adc9f0b3704f7b36f91eac45d19f45e82cb08e9c83e6580195e5807484d` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_C_r2.json.sha256`

## 1. Process tree

- `8224` /usr/bin/bash
  - `8225` /usr/bin/rm
  - `8226` /usr/bin/mkdir
  - `8227` /usr/bin/python3
  - `8228` /usr/bin/sleep
  - `8229` /usr/bin/curl
  - `8230` /usr/bin/python3
  - `8231` /usr/bin/cat
  - `8232` /usr/bin/chmod
  - `8233` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8224 (?) executed `/usr/bin/bash`
- +3.220 ms pid 8225 (bash) executed `/usr/bin/rm`
- +10.257 ms pid 8226 (bash) executed `/usr/bin/mkdir`
- +16.461 ms pid 8228 (bash) executed `/usr/bin/sleep`
- +16.510 ms pid 8227 (bash) executed `/usr/bin/python3`
- +523.931 ms pid 8229 (bash) executed `/usr/bin/curl`
- +546.104 ms pid 8231 (bash) executed `/usr/bin/cat`
- +548.629 ms pid 8232 (bash) executed `/usr/bin/chmod`
- +550.972 ms pid 8233 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +64.221 ms pid 8227 (python3) connected to `unix:/var/run/nscd/socket`
- +64.292 ms pid 8227 (python3) connected to `ipv6:[...]`
- +64.320 ms pid 8227 (python3) connected to `sockfd=3`
- +64.337 ms pid 8227 (python3) connected to `0.0.0.0:8766`
- +65.526 ms pid 8227 (python3) connected to `unix:/var/run/nscd/socket`
- +540.836 ms pid 8229 (curl) connected to `unix:/var/run/nscd/socket`
- +540.914 ms pid 8229 (curl) connected to `unix:/var/run/nscd/socket`
- +541.397 ms pid 8229 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +15.780 ms by pid 8224 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +523.621 ms by pid 8229 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +545.951 ms by pid 8231 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +550.526 ms pid 8232 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +9.513 ms pid 8225 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +9.578 ms pid 8225 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +9.615 ms pid 8225 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +9.675 ms pid 8225 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +541.115 ms pid 8229 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +550.972 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8233 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +9.578 ms #138 `unlinkat` by pid 8225 (rm)
    - +545.951 ms #989 `openat` by pid 8231 (bash)
    - +546.009 ms #990 `close` by pid 8231 (bash)
    - +548.180 ms #1057 `write` by pid 8231 (cat)
    - +548.265 ms #1060 `close` by pid 8231 (cat)
    - +550.526 ms #1128 `fchmodat` by pid 8232 (chmod)
    - +550.972 ms #1135 `execve` by pid 8233 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8224 | ? | execve | `/usr/bin/bash` |
| 15 | 1.039 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.094 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.225 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.272 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.332 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.377 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.436 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.481 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.539 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.582 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.642 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.687 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.754 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.807 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.853 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.913 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.959 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.016 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.062 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 2.128 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 2.173 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 2.231 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.275 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.344 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.389 | 8224 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.680 | 8224 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 2.928 | 8224 | bash | clone | `` |
| 73 | 3.220 | 8225 | bash | execve | `/usr/bin/rm` |
| 83 | 7.624 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 7.694 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 7.863 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 7.914 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 7.989 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 8.044 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 8.118 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 8.180 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 8.263 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 8.322 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 8.400 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 8.464 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 8.561 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 8.624 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 8.692 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 8.770 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 8.836 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 8.917 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 8.973 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 9.058 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 9.113 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 9.186 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 9.237 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 9.302 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 9.354 | 8225 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 9.431 | 8225 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 9.513 | 8225 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 9.578 | 8225 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 9.615 | 8225 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 9.675 | 8225 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 9.834 | 8225 | rm | exit_group | `code=0` |
| 146 | 10.043 | 8224 | bash | clone | `` |
| 148 | 10.257 | 8226 | bash | execve | `/usr/bin/mkdir` |
| 168 | 11.601 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 11.660 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 11.815 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 11.874 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 11.955 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 12.016 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 12.113 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 12.167 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 12.248 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 12.302 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 12.384 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 12.442 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 12.532 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 12.589 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 12.651 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 12.719 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 12.769 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 14.517 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 14.614 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 15.015 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 15.077 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 15.152 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 15.203 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 15.267 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 15.317 | 8226 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 15.524 | 8226 | mkdir | exit_group | `code=0` |
| 224 | 15.780 | 8224 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 15.871 | 8224 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 15.950 | 8224 | bash | clone | `` |
| 231 | 16.225 | 8224 | bash | clone | `` |
| 236 | 16.461 | 8228 | bash | execve | `/usr/bin/sleep` |
| 238 | 16.510 | 8227 | bash | execve | `/usr/bin/python3` |
| 262 | 17.545 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 266 | 18.959 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 272 | 19.088 | 8227 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 274 | 19.125 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 275 | 19.146 | 8227 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 277 | 19.183 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 282 | 19.279 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 284 | 19.410 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 286 | 19.489 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 288 | 19.543 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 290 | 19.617 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 292 | 19.671 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 294 | 19.742 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 296 | 19.806 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 298 | 19.891 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 300 | 19.946 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 302 | 20.004 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 20.087 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 20.155 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 20.244 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 20.309 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 20.400 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 20.459 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 20.576 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 20.633 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 20.710 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 20.768 | 8228 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 22.389 | 8227 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 22.464 | 8227 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 22.526 | 8227 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 22.551 | 8227 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 22.571 | 8227 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 23.840 | 8227 | python3 | openat | `/etc/localtime` |
| 362 | 26.810 | 8227 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 26.895 | 8227 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 27.052 | 8227 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 27.752 | 8227 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 27.839 | 8227 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 27.898 | 8227 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 33.702 | 8227 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 64.014 | 8227 | python3 | openat | `/etc/gai.conf` |
| 726 | 64.177 | 8227 | python3 | sendto | `socket:[51567]` |
| 727 | 64.221 | 8227 | python3 | connect | `unix:/var/run/nscd/socket` |
| 730 | 64.292 | 8227 | python3 | connect | `ipv6:[...]` |
| 731 | 64.320 | 8227 | python3 | connect | `sockfd=3` |
| 732 | 64.337 | 8227 | python3 | connect | `0.0.0.0:8766` |
| 742 | 65.526 | 8227 | python3 | connect | `unix:/var/run/nscd/socket` |
| 744 | 65.585 | 8227 | python3 | openat | `/etc/nsswitch.conf` |
| 748 | 65.669 | 8227 | python3 | openat | `/etc/host.conf` |
| 752 | 65.741 | 8227 | python3 | openat | `/etc/resolv.conf` |
| 756 | 65.827 | 8227 | python3 | openat | `/etc/hosts` |
| 760 | 65.906 | 8227 | python3 | openat | `/etc/hosts` |
| 765 | 521.889 | 8228 | sleep | exit_group | `code=0` |
| 767 | 522.758 | 8224 | bash | clone | `` |
| 769 | 523.621 | 8229 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 771 | 523.931 | 8229 | bash | execve | `/usr/bin/curl` |
| 867 | 537.172 | 8229 | curl | openat | `/etc/gnutls/config` |
| 885 | 539.011 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 887 | 539.071 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 891 | 539.220 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 893 | 539.274 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 895 | 539.354 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 897 | 539.409 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 899 | 539.481 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 901 | 539.537 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 903 | 539.607 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 905 | 539.663 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 907 | 539.736 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 909 | 539.796 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 911 | 539.885 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 913 | 539.939 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 915 | 540.004 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 540.080 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 540.134 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 921 | 540.210 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 923 | 540.264 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 925 | 540.347 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 927 | 540.404 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 929 | 540.476 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 931 | 540.532 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 933 | 540.606 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 935 | 540.663 | 8229 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 937 | 540.745 | 8229 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 938 | 540.779 | 8229 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 939 | 540.836 | 8229 | curl | connect | `unix:/var/run/nscd/socket` |
| 941 | 540.914 | 8229 | curl | connect | `unix:/var/run/nscd/socket` |
| 943 | 540.979 | 8229 | curl | openat | `/etc/nsswitch.conf` |
| 947 | 541.115 | 8229 | curl | openat | `/etc/passwd` |
| 950 | 541.213 | 8229 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 951 | 541.397 | 8229 | curl | connect | `127.0.0.1:8766` |
| 952 | 541.547 | 8229 | curl | sendto | `socket:[52291]` |
| 953 | 541.575 | 8227 | python3 | accept4 | `sockfd=3` |
| 954 | 541.769 | 8227 | python3 | clone3 | `` |
| 955 | 542.047 | 8230 | python3 | recvfrom | `socket:[51572]` |
| 956 | 542.339 | 8230 | python3 | openat | `/etc/mime.types` |
| 969 | 544.436 | 8230 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 971 | 544.576 | 8230 | python3 | sendto | `socket:[51572]` |
| 973 | 544.660 | 8229 | curl | recvfrom | `socket:[52291]` |
| 975 | 544.706 | 8230 | python3 | sendto | `socket:[51572]` |
| 976 | 544.730 | 8229 | curl | recvfrom | `socket:[52291]` |
| 980 | 544.823 | 8229 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 984 | 544.913 | 8230 | python3 | exit | `code=0` |
| 985 | 545.086 | 8229 | curl | exit_group | `code=0` |
| 987 | 545.736 | 8224 | bash | clone | `` |
| 989 | 545.951 | 8231 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 994 | 546.104 | 8231 | bash | execve | `/usr/bin/cat` |
| 1004 | 546.880 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1006 | 546.923 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1010 | 547.033 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1012 | 547.074 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1014 | 547.131 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1016 | 547.171 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1018 | 547.225 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1020 | 547.268 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1022 | 547.320 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1024 | 547.362 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1026 | 547.413 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1028 | 547.454 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1030 | 547.517 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1032 | 547.557 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1034 | 547.601 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1036 | 547.656 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1038 | 547.698 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1040 | 547.753 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1042 | 547.798 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1044 | 547.859 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1046 | 547.899 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1048 | 547.953 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1050 | 547.995 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1052 | 548.049 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1054 | 548.090 | 8231 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1057 | 548.180 | 8231 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1062 | 548.313 | 8231 | cat | exit_group | `code=0` |
| 1064 | 548.481 | 8224 | bash | clone | `` |
| 1066 | 548.629 | 8232 | bash | execve | `/usr/bin/chmod` |
| 1076 | 549.269 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1078 | 549.313 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1082 | 549.419 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1084 | 549.461 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1086 | 549.515 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1088 | 549.556 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1090 | 549.613 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1092 | 549.653 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1094 | 549.707 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1096 | 549.747 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1098 | 549.807 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1100 | 549.849 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1102 | 549.911 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1104 | 549.953 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1106 | 549.994 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1108 | 550.050 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1110 | 550.092 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1112 | 550.150 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1114 | 550.216 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1116 | 550.280 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1118 | 550.316 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1120 | 550.362 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1122 | 550.395 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1124 | 550.441 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1126 | 550.473 | 8232 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1128 | 550.526 | 8232 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1131 | 550.620 | 8232 | chmod | exit_group | `code=0` |
| 1133 | 550.808 | 8224 | bash | clone | `` |
| 1135 | 550.972 | 8233 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1141 | 551.431 | 8233 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1146 | 551.537 | 8233 | runme.sh | exit_group | `code=0` |
| 1155 | 552.832 | 8224 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 26.360 ms |
| Workload CPU (user+sys) | 69.389 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.429 ms |
| Evidence size | 428526 bytes |

