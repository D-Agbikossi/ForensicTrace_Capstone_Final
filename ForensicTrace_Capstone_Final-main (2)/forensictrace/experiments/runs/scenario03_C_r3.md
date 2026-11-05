# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | C |
| Events recorded | 1154 |
| Failed exec attempts removed | 12 |
| Duration | 573.119 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_C_r3.json` (428188 bytes) |
| SHA-256 | `4d54c96fcb7239fb01c540a7038e22c1a7a599515341ec7770dcd13116c3f104` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_C_r3.json.sha256`

## 1. Process tree

- `7617` /usr/bin/bash
  - `7618` /usr/bin/rm
  - `7619` /usr/bin/mkdir
  - `7620` /usr/bin/python3
  - `7621` /usr/bin/sleep
  - `7622` /usr/bin/curl
  - `7623` /usr/bin/python3
  - `7624` /usr/bin/cat
  - `7625` /usr/bin/chmod
  - `7626` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7617 (?) executed `/usr/bin/bash`
- +10.759 ms pid 7618 (bash) executed `/usr/bin/rm`
- +18.326 ms pid 7619 (bash) executed `/usr/bin/mkdir`
- +27.229 ms pid 7620 (bash) executed `/usr/bin/python3`
- +27.282 ms pid 7621 (bash) executed `/usr/bin/sleep`
- +534.002 ms pid 7622 (bash) executed `/usr/bin/curl`
- +557.676 ms pid 7624 (bash) executed `/usr/bin/cat`
- +562.062 ms pid 7625 (bash) executed `/usr/bin/chmod`
- +565.789 ms pid 7626 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +104.854 ms pid 7620 (python3) connected to `unix:/var/run/nscd/socket`
- +104.957 ms pid 7620 (python3) connected to `ipv6:[...]`
- +105.003 ms pid 7620 (python3) connected to `sockfd=3`
- +105.028 ms pid 7620 (python3) connected to `0.0.0.0:8766`
- +106.959 ms pid 7620 (python3) connected to `unix:/var/run/nscd/socket`
- +548.459 ms pid 7622 (curl) connected to `unix:/var/run/nscd/socket`
- +548.594 ms pid 7622 (curl) connected to `unix:/var/run/nscd/socket`
- +549.676 ms pid 7622 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +25.431 ms by pid 7617 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +533.901 ms by pid 7622 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +557.450 ms by pid 7624 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +564.986 ms pid 7625 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +15.662 ms pid 7618 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +15.750 ms pid 7618 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +15.795 ms pid 7618 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +15.864 ms pid 7618 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +548.872 ms pid 7622 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +565.789 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7626 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +15.750 ms #138 `unlinkat` by pid 7618 (rm)
    - +557.450 ms #988 `openat` by pid 7624 (bash)
    - +557.532 ms #989 `close` by pid 7624 (bash)
    - +560.852 ms #1056 `write` by pid 7624 (cat)
    - +560.949 ms #1059 `close` by pid 7624 (cat)
    - +564.986 ms #1127 `fchmodat` by pid 7625 (chmod)
    - +565.789 ms #1134 `execve` by pid 7626 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7617 | ? | execve | `/usr/bin/bash` |
| 15 | 4.687 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 4.738 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 4.990 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 5.045 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 5.163 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 5.213 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 5.328 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 5.386 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 5.522 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 5.574 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 5.688 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 5.733 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 5.844 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 5.890 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 5.956 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 6.067 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 6.118 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 6.231 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 6.285 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 6.438 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 6.499 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 6.630 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 6.687 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 6.810 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 6.858 | 7617 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 8.735 | 7617 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 9.793 | 7617 | bash | clone | `` |
| 73 | 10.759 | 7618 | bash | execve | `/usr/bin/rm` |
| 83 | 12.540 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 12.588 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 12.834 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 12.883 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 12.996 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 13.045 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 13.151 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 13.204 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 13.308 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 13.359 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 13.472 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 13.522 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 13.643 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 13.690 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 13.767 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 13.877 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 13.946 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 14.147 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 14.211 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 14.823 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 14.873 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 14.978 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 15.021 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 15.123 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 15.173 | 7618 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 15.422 | 7618 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 15.662 | 7618 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 15.750 | 7618 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 15.795 | 7618 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 15.864 | 7618 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 16.093 | 7618 | rm | exit_group | `code=0` |
| 146 | 17.221 | 7617 | bash | clone | `` |
| 148 | 18.326 | 7619 | bash | execve | `/usr/bin/mkdir` |
| 168 | 22.441 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 22.493 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 22.722 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 22.768 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 22.869 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 22.910 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 23.000 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 23.038 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 23.133 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 23.172 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 23.264 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 23.304 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 23.409 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 23.455 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 23.513 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 23.607 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 23.647 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 23.735 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 23.778 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 24.001 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 24.067 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 24.182 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 24.228 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 24.337 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 24.379 | 7619 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 24.804 | 7619 | mkdir | exit_group | `code=0` |
| 224 | 25.431 | 7617 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 25.623 | 7617 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 25.785 | 7617 | bash | clone | `` |
| 231 | 26.806 | 7617 | bash | clone | `` |
| 237 | 27.229 | 7620 | bash | execve | `/usr/bin/python3` |
| 238 | 27.282 | 7621 | bash | execve | `/usr/bin/sleep` |
| 261 | 28.576 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 263 | 28.699 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 28.907 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 28.948 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 29.038 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 29.077 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 29.164 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 278 | 29.203 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 280 | 29.295 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 282 | 29.336 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 284 | 29.436 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 286 | 29.485 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 291 | 29.607 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 294 | 29.647 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 295 | 29.657 | 7620 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 298 | 29.706 | 7620 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 299 | 29.715 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 303 | 29.812 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 305 | 29.930 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 30.030 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 30.072 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 30.170 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 30.210 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 31.306 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 31.350 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 31.456 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 31.497 | 7621 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 33.450 | 7620 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 33.478 | 7620 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 33.546 | 7620 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 33.567 | 7620 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 33.587 | 7620 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 34.620 | 7620 | python3 | openat | `/etc/localtime` |
| 362 | 39.710 | 7620 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 39.859 | 7620 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 40.084 | 7620 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 41.212 | 7620 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 41.393 | 7620 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 41.592 | 7620 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 53.541 | 7620 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 104.524 | 7620 | python3 | openat | `/etc/gai.conf` |
| 726 | 104.757 | 7620 | python3 | sendto | `socket:[45875]` |
| 727 | 104.854 | 7620 | python3 | connect | `unix:/var/run/nscd/socket` |
| 730 | 104.957 | 7620 | python3 | connect | `ipv6:[...]` |
| 731 | 105.003 | 7620 | python3 | connect | `sockfd=3` |
| 732 | 105.028 | 7620 | python3 | connect | `0.0.0.0:8766` |
| 742 | 106.959 | 7620 | python3 | connect | `unix:/var/run/nscd/socket` |
| 744 | 107.040 | 7620 | python3 | openat | `/etc/nsswitch.conf` |
| 748 | 107.176 | 7620 | python3 | openat | `/etc/host.conf` |
| 752 | 107.276 | 7620 | python3 | openat | `/etc/resolv.conf` |
| 756 | 107.384 | 7620 | python3 | openat | `/etc/hosts` |
| 760 | 107.535 | 7620 | python3 | openat | `/etc/hosts` |
| 765 | 532.659 | 7621 | sleep | exit_group | `code=0` |
| 767 | 533.504 | 7617 | bash | clone | `` |
| 769 | 533.901 | 7622 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 771 | 534.002 | 7622 | bash | execve | `/usr/bin/curl` |
| 867 | 543.403 | 7622 | curl | openat | `/etc/gnutls/config` |
| 885 | 545.022 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 887 | 545.068 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 891 | 545.265 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 893 | 545.312 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 895 | 545.410 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 897 | 545.466 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 899 | 545.573 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 901 | 545.640 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 903 | 546.013 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 905 | 546.072 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 907 | 546.171 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 909 | 546.211 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 911 | 546.316 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 913 | 546.356 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 915 | 546.417 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 546.524 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 546.564 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 921 | 546.701 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 923 | 546.750 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 925 | 546.853 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 927 | 546.892 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 929 | 547.001 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 931 | 547.058 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 933 | 547.169 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 935 | 547.217 | 7622 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 937 | 547.327 | 7622 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 938 | 547.353 | 7622 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 939 | 548.459 | 7622 | curl | connect | `unix:/var/run/nscd/socket` |
| 941 | 548.594 | 7622 | curl | connect | `unix:/var/run/nscd/socket` |
| 943 | 548.703 | 7622 | curl | openat | `/etc/nsswitch.conf` |
| 947 | 548.872 | 7622 | curl | openat | `/etc/passwd` |
| 950 | 548.991 | 7622 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 951 | 549.676 | 7622 | curl | connect | `127.0.0.1:8766` |
| 952 | 549.835 | 7620 | python3 | accept4 | `sockfd=3` |
| 953 | 550.094 | 7622 | curl | sendto | `socket:[47027]` |
| 954 | 550.233 | 7620 | python3 | clone3 | `` |
| 955 | 550.751 | 7623 | python3 | recvfrom | `socket:[45880]` |
| 956 | 551.192 | 7623 | python3 | openat | `/etc/mime.types` |
| 969 | 554.944 | 7623 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 971 | 555.159 | 7623 | python3 | sendto | `socket:[45880]` |
| 974 | 555.285 | 7623 | python3 | sendto | `socket:[45880]` |
| 976 | 555.322 | 7622 | curl | recvfrom | `socket:[47027]` |
| 980 | 555.487 | 7622 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 981 | 555.543 | 7623 | python3 | exit | `code=0` |
| 984 | 555.953 | 7622 | curl | exit_group | `code=0` |
| 986 | 557.027 | 7617 | bash | clone | `` |
| 988 | 557.450 | 7624 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 993 | 557.676 | 7624 | bash | execve | `/usr/bin/cat` |
| 1003 | 559.023 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1005 | 559.067 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1009 | 559.249 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1011 | 559.286 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1013 | 559.367 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1015 | 559.406 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1017 | 559.503 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1019 | 559.539 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1021 | 559.616 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1023 | 559.656 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1025 | 559.733 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1027 | 559.782 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1029 | 559.913 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1031 | 559.972 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1033 | 560.087 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1035 | 560.189 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1037 | 560.233 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1039 | 560.310 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1041 | 560.344 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1043 | 560.434 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1045 | 560.468 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1047 | 560.543 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1049 | 560.577 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1051 | 560.653 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1053 | 560.687 | 7624 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1056 | 560.852 | 7624 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1061 | 560.991 | 7624 | cat | exit_group | `code=0` |
| 1063 | 561.661 | 7617 | bash | clone | `` |
| 1065 | 562.062 | 7625 | bash | execve | `/usr/bin/chmod` |
| 1075 | 563.454 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1077 | 563.493 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1081 | 563.669 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1083 | 563.705 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1085 | 563.783 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1087 | 563.818 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1089 | 563.893 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1091 | 563.927 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1093 | 564.000 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1095 | 564.033 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1097 | 564.106 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1099 | 564.139 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1101 | 564.222 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1103 | 564.257 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1105 | 564.306 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1107 | 564.382 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1109 | 564.415 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1111 | 564.497 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1113 | 564.531 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1115 | 564.611 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1117 | 564.647 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1119 | 564.721 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1121 | 564.755 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1123 | 564.830 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1125 | 564.863 | 7625 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1127 | 564.986 | 7625 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 565.080 | 7625 | chmod | exit_group | `code=0` |
| 1132 | 565.423 | 7617 | bash | clone | `` |
| 1134 | 565.789 | 7626 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1140 | 566.979 | 7626 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1145 | 567.429 | 7626 | runme.sh | exit_group | `code=0` |
| 1154 | 569.366 | 7617 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 54.263 ms |
| Workload CPU (user+sys) | 82.299 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.480 ms |
| Evidence size | 428188 bytes |

