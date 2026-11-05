# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | C |
| Events recorded | 1154 |
| Failed exec attempts removed | 12 |
| Duration | 574.262 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_C_r1.json` (428189 bytes) |
| SHA-256 | `d2c3f87176408860f851d80fef7acb6c3db15e3eb9b7cacec8a92b55edafd610` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_C_r1.json.sha256`

## 1. Process tree

- `8034` /usr/bin/bash
  - `8035` /usr/bin/rm
  - `8036` /usr/bin/mkdir
  - `8037` /usr/bin/python3
  - `8038` /usr/bin/sleep
  - `8042` /usr/bin/curl
  - `8044` /usr/bin/python3
  - `8045` /usr/bin/cat
  - `8047` /usr/bin/chmod
  - `8049` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8034 (?) executed `/usr/bin/bash`
- +2.910 ms pid 8035 (bash) executed `/usr/bin/rm`
- +5.339 ms pid 8036 (bash) executed `/usr/bin/mkdir`
- +8.865 ms pid 8038 (bash) executed `/usr/bin/sleep`
- +8.907 ms pid 8037 (bash) executed `/usr/bin/python3`
- +513.406 ms pid 8042 (bash) executed `/usr/bin/curl`
- +542.024 ms pid 8045 (bash) executed `/usr/bin/cat`
- +553.069 ms pid 8047 (bash) executed `/usr/bin/chmod`
- +562.273 ms pid 8049 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +81.670 ms pid 8037 (python3) connected to `unix:/var/run/nscd/socket`
- +81.748 ms pid 8037 (python3) connected to `ipv6:[...]`
- +81.777 ms pid 8037 (python3) connected to `sockfd=3`
- +81.795 ms pid 8037 (python3) connected to `0.0.0.0:8766`
- +82.987 ms pid 8037 (python3) connected to `unix:/var/run/nscd/socket`
- +532.360 ms pid 8042 (curl) connected to `unix:/var/run/nscd/socket`
- +532.439 ms pid 8042 (curl) connected to `unix:/var/run/nscd/socket`
- +533.115 ms pid 8042 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +8.072 ms by pid 8034 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +513.067 ms by pid 8042 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +541.749 ms by pid 8045 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +558.036 ms pid 8047 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +4.829 ms pid 8035 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +4.876 ms pid 8035 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +4.902 ms pid 8035 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +4.944 ms pid 8035 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +532.876 ms pid 8042 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +562.273 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8049 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +4.876 ms #138 `unlinkat` by pid 8035 (rm)
    - +541.749 ms #988 `openat` by pid 8045 (bash)
    - +541.850 ms #989 `close` by pid 8045 (bash)
    - +549.095 ms #1056 `write` by pid 8045 (cat)
    - +549.233 ms #1059 `close` by pid 8045 (cat)
    - +558.036 ms #1127 `fchmodat` by pid 8047 (chmod)
    - +562.273 ms #1134 `execve` by pid 8049 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8034 | ? | execve | `/usr/bin/bash` |
| 15 | 0.807 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 0.855 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 0.976 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.040 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.104 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.151 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.211 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.255 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.312 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.355 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.419 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.465 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.532 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.577 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.622 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.681 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.727 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 1.783 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 1.827 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 1.890 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 1.936 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 1.994 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.037 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.097 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.141 | 8034 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.490 | 8034 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 2.723 | 8034 | bash | clone | `` |
| 73 | 2.910 | 8035 | bash | execve | `/usr/bin/rm` |
| 83 | 3.597 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.643 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 3.761 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 3.808 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 3.905 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 3.940 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 3.990 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 4.024 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 4.068 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 4.103 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 4.146 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 4.180 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 4.235 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 4.268 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 4.305 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 4.349 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 4.384 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 4.436 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 4.469 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 4.522 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 4.557 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 4.602 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 4.636 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 4.681 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 4.716 | 8035 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 4.769 | 8035 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 4.829 | 8035 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 4.876 | 8035 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 4.902 | 8035 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 4.944 | 8035 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 5.063 | 8035 | rm | exit_group | `code=0` |
| 146 | 5.199 | 8034 | bash | clone | `` |
| 148 | 5.339 | 8036 | bash | execve | `/usr/bin/mkdir` |
| 168 | 6.322 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 6.368 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 6.486 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 6.535 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 6.593 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 6.639 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 6.696 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 6.740 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 6.797 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 6.841 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 6.899 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 6.945 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 7.010 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 7.054 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 7.100 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 7.157 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 7.202 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 7.257 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 7.303 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 7.366 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 7.416 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 7.474 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 7.518 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 7.576 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 7.620 | 8036 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 7.836 | 8036 | mkdir | exit_group | `code=0` |
| 224 | 8.072 | 8034 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 8.238 | 8034 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 8.332 | 8034 | bash | clone | `` |
| 231 | 8.681 | 8034 | bash | clone | `` |
| 236 | 8.865 | 8038 | bash | execve | `/usr/bin/sleep` |
| 238 | 8.907 | 8037 | bash | execve | `/usr/bin/python3` |
| 261 | 9.671 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 264 | 9.723 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 9.837 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 9.882 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 274 | 9.960 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 277 | 10.008 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 280 | 10.065 | 8037 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 281 | 10.076 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 284 | 10.118 | 8037 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 285 | 10.129 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 289 | 10.194 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 292 | 10.243 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 294 | 10.298 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 296 | 10.344 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 298 | 10.426 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 300 | 10.473 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 302 | 10.520 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 10.579 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 10.625 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 10.682 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 10.727 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 10.792 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 10.835 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 10.892 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 10.935 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 10.993 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 11.038 | 8038 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 12.548 | 8037 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 12.585 | 8037 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 12.621 | 8037 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 12.642 | 8037 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 12.661 | 8037 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 13.428 | 8037 | python3 | openat | `/etc/localtime` |
| 362 | 19.566 | 8037 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 20.193 | 8037 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 20.636 | 8037 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 21.764 | 8037 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 21.869 | 8037 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 21.946 | 8037 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 43.018 | 8037 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 81.507 | 8037 | python3 | openat | `/etc/gai.conf` |
| 726 | 81.624 | 8037 | python3 | sendto | `socket:[50585]` |
| 727 | 81.670 | 8037 | python3 | connect | `unix:/var/run/nscd/socket` |
| 730 | 81.748 | 8037 | python3 | connect | `ipv6:[...]` |
| 731 | 81.777 | 8037 | python3 | connect | `sockfd=3` |
| 732 | 81.795 | 8037 | python3 | connect | `0.0.0.0:8766` |
| 742 | 82.987 | 8037 | python3 | connect | `unix:/var/run/nscd/socket` |
| 744 | 83.042 | 8037 | python3 | openat | `/etc/nsswitch.conf` |
| 748 | 83.128 | 8037 | python3 | openat | `/etc/host.conf` |
| 752 | 83.200 | 8037 | python3 | openat | `/etc/resolv.conf` |
| 756 | 83.279 | 8037 | python3 | openat | `/etc/hosts` |
| 760 | 83.358 | 8037 | python3 | openat | `/etc/hosts` |
| 765 | 511.782 | 8038 | sleep | exit_group | `code=0` |
| 767 | 512.374 | 8034 | bash | clone | `` |
| 769 | 513.067 | 8042 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 771 | 513.406 | 8042 | bash | execve | `/usr/bin/curl` |
| 867 | 529.683 | 8042 | curl | openat | `/etc/gnutls/config` |
| 885 | 530.844 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 887 | 530.896 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 891 | 531.027 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 893 | 531.073 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 895 | 531.136 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 897 | 531.183 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 899 | 531.241 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 901 | 531.289 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 903 | 531.344 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 905 | 531.400 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 907 | 531.463 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 909 | 531.509 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 911 | 531.581 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 913 | 531.627 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 915 | 531.677 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 531.745 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 531.791 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 921 | 531.852 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 923 | 531.897 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 925 | 531.965 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 927 | 532.012 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 929 | 532.070 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 931 | 532.117 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 933 | 532.174 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 935 | 532.220 | 8042 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 937 | 532.288 | 8042 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 938 | 532.314 | 8042 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 939 | 532.360 | 8042 | curl | connect | `unix:/var/run/nscd/socket` |
| 941 | 532.439 | 8042 | curl | connect | `unix:/var/run/nscd/socket` |
| 943 | 532.495 | 8042 | curl | openat | `/etc/nsswitch.conf` |
| 947 | 532.876 | 8042 | curl | openat | `/etc/passwd` |
| 950 | 532.959 | 8042 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 951 | 533.115 | 8042 | curl | connect | `127.0.0.1:8766` |
| 952 | 533.263 | 8037 | python3 | accept4 | `sockfd=3` |
| 953 | 533.296 | 8042 | curl | sendto | `socket:[50593]` |
| 954 | 533.460 | 8037 | python3 | clone3 | `` |
| 955 | 533.636 | 8044 | python3 | recvfrom | `socket:[49646]` |
| 956 | 533.933 | 8044 | python3 | openat | `/etc/mime.types` |
| 969 | 538.251 | 8044 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 971 | 538.533 | 8044 | python3 | sendto | `socket:[49646]` |
| 974 | 538.735 | 8044 | python3 | sendto | `socket:[49646]` |
| 975 | 538.792 | 8042 | curl | recvfrom | `socket:[50593]` |
| 980 | 539.149 | 8044 | python3 | exit | `code=0` |
| 981 | 539.193 | 8042 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 984 | 539.662 | 8042 | curl | exit_group | `code=0` |
| 986 | 540.365 | 8034 | bash | clone | `` |
| 988 | 541.749 | 8045 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 993 | 542.024 | 8045 | bash | execve | `/usr/bin/cat` |
| 1003 | 544.113 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1005 | 544.274 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1009 | 544.767 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1011 | 544.821 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1013 | 544.893 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1015 | 544.937 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1017 | 545.149 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1019 | 545.213 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1021 | 545.288 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1023 | 545.343 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1025 | 545.417 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1027 | 545.479 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1029 | 545.568 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1031 | 545.630 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1033 | 545.685 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1035 | 545.760 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1037 | 545.817 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1039 | 545.891 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1041 | 545.947 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1043 | 546.037 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1045 | 548.573 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1047 | 548.757 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1049 | 548.813 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1051 | 548.897 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1053 | 548.956 | 8045 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1056 | 549.095 | 8045 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1061 | 549.309 | 8045 | cat | exit_group | `code=0` |
| 1063 | 549.722 | 8034 | bash | clone | `` |
| 1065 | 553.069 | 8047 | bash | execve | `/usr/bin/chmod` |
| 1075 | 554.269 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1077 | 554.335 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1081 | 555.674 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1083 | 555.726 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1085 | 555.800 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1087 | 555.847 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1089 | 555.917 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1091 | 555.969 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1093 | 556.042 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1095 | 556.093 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1097 | 557.007 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1099 | 557.091 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1101 | 557.191 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1103 | 557.246 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1105 | 557.304 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1107 | 557.382 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1109 | 557.456 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1111 | 557.536 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1113 | 557.589 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1115 | 557.672 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1117 | 557.720 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1119 | 557.784 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1121 | 557.832 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1123 | 557.901 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1125 | 557.952 | 8047 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1127 | 558.036 | 8047 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 561.574 | 8047 | chmod | exit_group | `code=0` |
| 1132 | 561.977 | 8034 | bash | clone | `` |
| 1134 | 562.273 | 8049 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1140 | 563.198 | 8049 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1145 | 563.775 | 8049 | runme.sh | exit_group | `code=0` |
| 1154 | 573.113 | 8034 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 31.405 ms |
| Workload CPU (user+sys) | 80.720 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 2.639 ms |
| Evidence size | 428189 bytes |

