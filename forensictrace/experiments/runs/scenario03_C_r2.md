# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | C |
| Events recorded | 1154 |
| Failed exec attempts removed | 12 |
| Duration | 587.179 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_C_r2.json` (428187 bytes) |
| SHA-256 | `981a8108e31d558939394c4bde7d3a31daf2608747754aaa4bdc689be82dc576` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_C_r2.json.sha256`

## 1. Process tree

- `7420` /usr/bin/bash
  - `7421` /usr/bin/rm
  - `7422` /usr/bin/mkdir
  - `7423` /usr/bin/python3
  - `7424` /usr/bin/sleep
  - `7426` /usr/bin/curl
  - `7427` /usr/bin/python3
  - `7428` /usr/bin/cat
  - `7429` /usr/bin/chmod
  - `7430` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7420 (?) executed `/usr/bin/bash`
- +16.610 ms pid 7421 (bash) executed `/usr/bin/rm`
- +21.566 ms pid 7422 (bash) executed `/usr/bin/mkdir`
- +28.018 ms pid 7424 (bash) executed `/usr/bin/sleep`
- +28.802 ms pid 7423 (bash) executed `/usr/bin/python3`
- +543.378 ms pid 7426 (bash) executed `/usr/bin/curl`
- +568.974 ms pid 7428 (bash) executed `/usr/bin/cat`
- +575.422 ms pid 7429 (bash) executed `/usr/bin/chmod`
- +580.725 ms pid 7430 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +107.411 ms pid 7423 (python3) connected to `unix:/var/run/nscd/socket`
- +107.507 ms pid 7423 (python3) connected to `ipv6:[...]`
- +107.552 ms pid 7423 (python3) connected to `sockfd=3`
- +107.569 ms pid 7423 (python3) connected to `0.0.0.0:8766`
- +109.237 ms pid 7423 (python3) connected to `unix:/var/run/nscd/socket`
- +557.211 ms pid 7426 (curl) connected to `unix:/var/run/nscd/socket`
- +557.292 ms pid 7426 (curl) connected to `unix:/var/run/nscd/socket`
- +558.236 ms pid 7426 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +25.663 ms by pid 7420 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +543.145 ms by pid 7426 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +568.650 ms by pid 7428 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +579.606 ms pid 7429 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +20.068 ms pid 7421 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +20.117 ms pid 7421 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +20.145 ms pid 7421 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +20.187 ms pid 7421 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +557.525 ms pid 7426 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +580.725 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7430 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +20.117 ms #138 `unlinkat` by pid 7421 (rm)
    - +568.650 ms #988 `openat` by pid 7428 (bash)
    - +568.774 ms #989 `close` by pid 7428 (bash)
    - +573.735 ms #1056 `write` by pid 7428 (cat)
    - +573.881 ms #1059 `close` by pid 7428 (cat)
    - +579.606 ms #1127 `fchmodat` by pid 7429 (chmod)
    - +580.725 ms #1134 `execve` by pid 7430 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7420 | ? | execve | `/usr/bin/bash` |
| 15 | 5.923 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 5.998 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 6.299 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 6.368 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 6.540 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 6.606 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 6.769 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 6.839 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 6.993 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 7.055 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 7.199 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 7.277 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 7.435 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 7.513 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 7.593 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 7.721 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 7.783 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 7.935 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 7.983 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 8.102 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 8.158 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 8.273 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 8.343 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 8.461 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 8.529 | 7420 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 11.709 | 7420 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 14.430 | 7420 | bash | clone | `` |
| 73 | 16.610 | 7421 | bash | execve | `/usr/bin/rm` |
| 83 | 18.038 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 18.087 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 18.310 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 18.355 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 18.463 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 18.509 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 18.610 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 18.657 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 18.754 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 18.801 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 18.897 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 18.951 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 19.085 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 19.121 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 19.175 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 19.257 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 19.295 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 19.376 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 19.413 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 19.508 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 19.543 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 19.621 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 19.657 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 19.734 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 19.770 | 7421 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 19.903 | 7421 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 20.068 | 7421 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 20.117 | 7421 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 20.145 | 7421 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 20.187 | 7421 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 20.317 | 7421 | rm | exit_group | `code=0` |
| 146 | 21.165 | 7420 | bash | clone | `` |
| 148 | 21.566 | 7422 | bash | execve | `/usr/bin/mkdir` |
| 168 | 23.203 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 23.244 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 23.409 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 23.449 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 23.527 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 23.563 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 23.640 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 23.674 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 23.749 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 23.783 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 23.860 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 23.895 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 23.979 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 24.015 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 24.066 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 24.176 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 24.226 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 24.325 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 24.373 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 24.491 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 24.538 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 24.638 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 24.696 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 24.897 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 24.935 | 7422 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 25.270 | 7422 | mkdir | exit_group | `code=0` |
| 224 | 25.663 | 7420 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 25.857 | 7420 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 26.034 | 7420 | bash | clone | `` |
| 231 | 27.568 | 7420 | bash | clone | `` |
| 233 | 28.018 | 7424 | bash | execve | `/usr/bin/sleep` |
| 238 | 28.802 | 7423 | bash | execve | `/usr/bin/python3` |
| 262 | 31.684 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 265 | 31.790 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 271 | 32.002 | 7423 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 273 | 32.093 | 7423 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 275 | 32.196 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 278 | 32.264 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 282 | 32.445 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 284 | 32.518 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 286 | 33.184 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 288 | 33.523 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 290 | 33.662 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 292 | 33.757 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 294 | 33.877 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 295 | 36.068 | 7423 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 296 | 36.139 | 7423 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 298 | 36.276 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 299 | 36.320 | 7423 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 300 | 36.362 | 7423 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 301 | 36.404 | 7423 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 303 | 36.522 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 305 | 36.588 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 307 | 36.675 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 309 | 36.801 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 311 | 36.858 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 313 | 37.007 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 315 | 37.070 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 317 | 37.224 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 319 | 37.285 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 321 | 37.427 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 323 | 37.508 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 325 | 37.636 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 327 | 37.696 | 7424 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 334 | 37.994 | 7423 | python3 | openat | `/etc/localtime` |
| 362 | 45.021 | 7423 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 45.200 | 7423 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 45.462 | 7423 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 46.680 | 7423 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 46.893 | 7423 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 47.103 | 7423 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 57.218 | 7423 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 107.130 | 7423 | python3 | openat | `/etc/gai.conf` |
| 726 | 107.320 | 7423 | python3 | sendto | `socket:[44925]` |
| 727 | 107.411 | 7423 | python3 | connect | `unix:/var/run/nscd/socket` |
| 730 | 107.507 | 7423 | python3 | connect | `ipv6:[...]` |
| 731 | 107.552 | 7423 | python3 | connect | `sockfd=3` |
| 732 | 107.569 | 7423 | python3 | connect | `0.0.0.0:8766` |
| 742 | 109.237 | 7423 | python3 | connect | `unix:/var/run/nscd/socket` |
| 744 | 109.319 | 7423 | python3 | openat | `/etc/nsswitch.conf` |
| 748 | 109.458 | 7423 | python3 | openat | `/etc/host.conf` |
| 752 | 109.562 | 7423 | python3 | openat | `/etc/resolv.conf` |
| 756 | 109.673 | 7423 | python3 | openat | `/etc/hosts` |
| 760 | 109.814 | 7423 | python3 | openat | `/etc/hosts` |
| 765 | 539.003 | 7424 | sleep | exit_group | `code=0` |
| 767 | 541.981 | 7420 | bash | clone | `` |
| 769 | 543.145 | 7426 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 771 | 543.378 | 7426 | bash | execve | `/usr/bin/curl` |
| 867 | 553.717 | 7426 | curl | openat | `/etc/gnutls/config` |
| 885 | 555.274 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 887 | 555.320 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 891 | 555.530 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 893 | 555.571 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 895 | 555.671 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 897 | 555.714 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 899 | 555.806 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 901 | 555.849 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 903 | 555.937 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 905 | 555.980 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 907 | 556.072 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 909 | 556.114 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 911 | 556.218 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 913 | 556.259 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 915 | 556.321 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 556.415 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 556.461 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 921 | 556.556 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 923 | 556.598 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 925 | 556.697 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 927 | 556.740 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 929 | 556.831 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 931 | 556.874 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 933 | 556.970 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 935 | 557.013 | 7426 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 937 | 557.110 | 7426 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 938 | 557.134 | 7426 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 939 | 557.211 | 7426 | curl | connect | `unix:/var/run/nscd/socket` |
| 941 | 557.292 | 7426 | curl | connect | `unix:/var/run/nscd/socket` |
| 943 | 557.381 | 7426 | curl | openat | `/etc/nsswitch.conf` |
| 947 | 557.525 | 7426 | curl | openat | `/etc/passwd` |
| 950 | 557.636 | 7426 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 951 | 558.236 | 7426 | curl | connect | `127.0.0.1:8766` |
| 952 | 558.398 | 7423 | python3 | accept4 | `sockfd=3` |
| 953 | 558.602 | 7426 | curl | sendto | `socket:[46675]` |
| 954 | 558.719 | 7423 | python3 | clone3 | `` |
| 955 | 559.121 | 7427 | python3 | recvfrom | `socket:[44930]` |
| 956 | 559.489 | 7427 | python3 | openat | `/etc/mime.types` |
| 969 | 561.875 | 7427 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 971 | 562.105 | 7427 | python3 | sendto | `socket:[44930]` |
| 974 | 562.233 | 7427 | python3 | sendto | `socket:[44930]` |
| 975 | 562.242 | 7426 | curl | recvfrom | `socket:[46675]` |
| 980 | 562.388 | 7426 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 981 | 562.502 | 7427 | python3 | exit | `code=0` |
| 984 | 562.972 | 7426 | curl | exit_group | `code=0` |
| 986 | 567.963 | 7420 | bash | clone | `` |
| 988 | 568.650 | 7428 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 993 | 568.974 | 7428 | bash | execve | `/usr/bin/cat` |
| 1003 | 570.919 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1005 | 570.984 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1009 | 571.286 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1011 | 571.358 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1013 | 571.509 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1015 | 571.565 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1017 | 571.696 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1019 | 571.752 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1021 | 571.884 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1023 | 571.941 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1025 | 572.073 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1027 | 572.141 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1029 | 572.282 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1031 | 572.342 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1033 | 572.433 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1035 | 572.579 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1037 | 572.636 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1039 | 572.767 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1041 | 572.827 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1043 | 572.975 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1045 | 573.034 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1047 | 573.172 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1049 | 573.231 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1051 | 573.364 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1053 | 573.426 | 7428 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1056 | 573.735 | 7428 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1061 | 573.946 | 7428 | cat | exit_group | `code=0` |
| 1063 | 574.978 | 7420 | bash | clone | `` |
| 1065 | 575.422 | 7429 | bash | execve | `/usr/bin/chmod` |
| 1075 | 576.853 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1077 | 576.904 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1081 | 577.132 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1083 | 577.183 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1085 | 577.290 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1087 | 577.343 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1089 | 577.552 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1091 | 577.611 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1093 | 577.740 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1095 | 577.799 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1097 | 577.928 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1099 | 577.987 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1101 | 578.134 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1103 | 578.193 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1105 | 578.279 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1107 | 578.411 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1109 | 578.482 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1111 | 578.735 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1113 | 578.804 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1115 | 578.950 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1117 | 579.014 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1119 | 579.147 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1121 | 579.209 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1123 | 579.342 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1125 | 579.401 | 7429 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1127 | 579.606 | 7429 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 579.743 | 7429 | chmod | exit_group | `code=0` |
| 1132 | 580.269 | 7420 | bash | clone | `` |
| 1134 | 580.725 | 7430 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1140 | 582.059 | 7430 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1145 | 582.374 | 7430 | runme.sh | exit_group | `code=0` |
| 1154 | 584.735 | 7420 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 62.441 ms |
| Workload CPU (user+sys) | 81.857 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.895 ms |
| Evidence size | 428187 bytes |

