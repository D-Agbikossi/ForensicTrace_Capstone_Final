# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | C |
| Events recorded | 1154 |
| Failed exec attempts removed | 12 |
| Duration | 562.757 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_C_r4.json` (428188 bytes) |
| SHA-256 | `36376b968c99534ea2f36f062b5dcba5db8b753d897c6a5ab559e19e234e6e22` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_C_r4.json.sha256`

## 1. Process tree

- `7845` /usr/bin/bash
  - `7846` /usr/bin/rm
  - `7847` /usr/bin/mkdir
  - `7848` /usr/bin/python3
  - `7849` /usr/bin/sleep
  - `7850` /usr/bin/curl
  - `7851` /usr/bin/python3
  - `7852` /usr/bin/cat
  - `7853` /usr/bin/chmod
  - `7854` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7845 (?) executed `/usr/bin/bash`
- +5.020 ms pid 7846 (bash) executed `/usr/bin/rm`
- +9.774 ms pid 7847 (bash) executed `/usr/bin/mkdir`
- +14.983 ms pid 7848 (bash) executed `/usr/bin/python3`
- +15.704 ms pid 7849 (bash) executed `/usr/bin/sleep`
- +524.941 ms pid 7850 (bash) executed `/usr/bin/curl`
- +551.796 ms pid 7852 (bash) executed `/usr/bin/cat`
- +555.519 ms pid 7853 (bash) executed `/usr/bin/chmod`
- +558.559 ms pid 7854 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +83.752 ms pid 7848 (python3) connected to `unix:/var/run/nscd/socket`
- +83.838 ms pid 7848 (python3) connected to `ipv6:[...]`
- +83.881 ms pid 7848 (python3) connected to `sockfd=3`
- +83.898 ms pid 7848 (python3) connected to `0.0.0.0:8766`
- +85.795 ms pid 7848 (python3) connected to `unix:/var/run/nscd/socket`
- +544.735 ms pid 7850 (curl) connected to `unix:/var/run/nscd/socket`
- +544.800 ms pid 7850 (curl) connected to `unix:/var/run/nscd/socket`
- +545.542 ms pid 7850 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +13.138 ms by pid 7845 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +524.503 ms by pid 7850 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +551.608 ms by pid 7852 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +557.911 ms pid 7853 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +8.343 ms pid 7846 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +8.394 ms pid 7846 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +8.430 ms pid 7846 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +8.484 ms pid 7846 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +544.980 ms pid 7850 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +558.559 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7854 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +8.394 ms #138 `unlinkat` by pid 7846 (rm)
    - +551.608 ms #988 `openat` by pid 7852 (bash)
    - +551.678 ms #989 `close` by pid 7852 (bash)
    - +554.336 ms #1056 `write` by pid 7852 (cat)
    - +554.418 ms #1059 `close` by pid 7852 (cat)
    - +557.911 ms #1127 `fchmodat` by pid 7853 (chmod)
    - +558.559 ms #1134 `execve` by pid 7854 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7845 | ? | execve | `/usr/bin/bash` |
| 15 | 1.291 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.328 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.489 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.523 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.597 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.632 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.706 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.739 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.815 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.847 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.921 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.955 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.037 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 2.071 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 2.121 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 2.203 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 2.238 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.311 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.345 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 2.423 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 2.458 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 2.532 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.565 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.641 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.674 | 7845 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 3.904 | 7845 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 4.642 | 7845 | bash | clone | `` |
| 73 | 5.020 | 7846 | bash | execve | `/usr/bin/rm` |
| 83 | 6.188 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 6.235 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 6.444 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 6.487 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 6.584 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 6.627 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 6.723 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 6.767 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 6.860 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 6.905 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 6.996 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 7.041 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 7.147 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 7.197 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 7.262 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 7.359 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 7.405 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 7.505 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 7.547 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 7.650 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 7.693 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 7.791 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 7.835 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 7.930 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 7.976 | 7846 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 8.137 | 7846 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 8.343 | 7846 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 8.394 | 7846 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 8.430 | 7846 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 8.484 | 7846 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 8.664 | 7846 | rm | exit_group | `code=0` |
| 146 | 9.446 | 7845 | bash | clone | `` |
| 148 | 9.774 | 7847 | bash | execve | `/usr/bin/mkdir` |
| 168 | 11.209 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 11.244 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 11.402 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 11.436 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 11.508 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 11.542 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 11.616 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 11.649 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 11.722 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 11.756 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 11.829 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 11.863 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 11.944 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 11.978 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 12.027 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 12.100 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 12.135 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 12.211 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 12.247 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 12.334 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 12.369 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 12.442 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 12.475 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 12.548 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 12.582 | 7847 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 12.826 | 7847 | mkdir | exit_group | `code=0` |
| 224 | 13.138 | 7845 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 13.348 | 7845 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 13.513 | 7845 | bash | clone | `` |
| 235 | 14.983 | 7848 | bash | execve | `/usr/bin/python3` |
| 236 | 15.236 | 7845 | bash | clone | `` |
| 241 | 15.704 | 7849 | bash | execve | `/usr/bin/sleep` |
| 262 | 17.137 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 264 | 17.200 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 269 | 17.437 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 272 | 17.491 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 276 | 17.581 | 7848 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 278 | 17.618 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 279 | 17.638 | 7848 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 281 | 17.675 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 285 | 17.792 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 287 | 17.841 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 290 | 17.946 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 292 | 17.992 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 294 | 18.088 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 296 | 18.135 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 298 | 18.258 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 300 | 18.303 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 302 | 18.368 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 18.464 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 18.510 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 18.605 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 18.650 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 18.756 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 18.799 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 18.895 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 18.938 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 19.035 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 19.084 | 7849 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 21.803 | 7848 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 21.847 | 7848 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 21.921 | 7848 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 21.941 | 7848 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 21.960 | 7848 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 22.931 | 7848 | python3 | openat | `/etc/localtime` |
| 362 | 27.804 | 7848 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 27.943 | 7848 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 28.150 | 7848 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 29.237 | 7848 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 29.403 | 7848 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 29.547 | 7848 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 38.049 | 7848 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 83.405 | 7848 | python3 | openat | `/etc/gai.conf` |
| 726 | 83.666 | 7848 | python3 | sendto | `socket:[48756]` |
| 727 | 83.752 | 7848 | python3 | connect | `unix:/var/run/nscd/socket` |
| 730 | 83.838 | 7848 | python3 | connect | `ipv6:[...]` |
| 731 | 83.881 | 7848 | python3 | connect | `sockfd=3` |
| 732 | 83.898 | 7848 | python3 | connect | `0.0.0.0:8766` |
| 742 | 85.795 | 7848 | python3 | connect | `unix:/var/run/nscd/socket` |
| 744 | 85.894 | 7848 | python3 | openat | `/etc/nsswitch.conf` |
| 748 | 86.057 | 7848 | python3 | openat | `/etc/host.conf` |
| 752 | 86.191 | 7848 | python3 | openat | `/etc/resolv.conf` |
| 756 | 86.328 | 7848 | python3 | openat | `/etc/hosts` |
| 760 | 86.502 | 7848 | python3 | openat | `/etc/hosts` |
| 765 | 520.089 | 7849 | sleep | exit_group | `code=0` |
| 767 | 522.867 | 7845 | bash | clone | `` |
| 769 | 524.503 | 7850 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 771 | 524.941 | 7850 | bash | execve | `/usr/bin/curl` |
| 867 | 541.877 | 7850 | curl | openat | `/etc/gnutls/config` |
| 885 | 543.191 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 887 | 543.229 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 891 | 543.392 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 893 | 543.425 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 895 | 543.506 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 897 | 543.541 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 899 | 543.613 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 901 | 543.647 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 903 | 543.718 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 905 | 543.752 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 907 | 543.825 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 909 | 543.857 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 911 | 543.940 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 913 | 543.972 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 915 | 544.022 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 544.100 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 544.133 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 921 | 544.214 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 923 | 544.247 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 925 | 544.325 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 927 | 544.361 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 929 | 544.433 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 931 | 544.467 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 933 | 544.540 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 935 | 544.575 | 7850 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 937 | 544.652 | 7850 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 938 | 544.671 | 7850 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 939 | 544.735 | 7850 | curl | connect | `unix:/var/run/nscd/socket` |
| 941 | 544.800 | 7850 | curl | connect | `unix:/var/run/nscd/socket` |
| 943 | 544.869 | 7850 | curl | openat | `/etc/nsswitch.conf` |
| 947 | 544.980 | 7850 | curl | openat | `/etc/passwd` |
| 950 | 545.067 | 7850 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 951 | 545.542 | 7850 | curl | connect | `127.0.0.1:8766` |
| 952 | 545.673 | 7848 | python3 | accept4 | `sockfd=3` |
| 953 | 545.872 | 7850 | curl | sendto | `socket:[49364]` |
| 954 | 545.981 | 7848 | python3 | clone3 | `` |
| 955 | 546.334 | 7851 | python3 | recvfrom | `socket:[48763]` |
| 956 | 546.682 | 7851 | python3 | openat | `/etc/mime.types` |
| 969 | 549.041 | 7851 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 971 | 549.276 | 7851 | python3 | sendto | `socket:[48763]` |
| 974 | 549.428 | 7851 | python3 | sendto | `socket:[48763]` |
| 975 | 549.439 | 7850 | curl | recvfrom | `socket:[49364]` |
| 979 | 549.593 | 7850 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 981 | 549.729 | 7851 | python3 | exit | `code=0` |
| 984 | 550.057 | 7850 | curl | exit_group | `code=0` |
| 986 | 551.205 | 7845 | bash | clone | `` |
| 988 | 551.608 | 7852 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 993 | 551.796 | 7852 | bash | execve | `/usr/bin/cat` |
| 1003 | 552.805 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1005 | 552.843 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1009 | 553.008 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1011 | 553.043 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1013 | 553.118 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1015 | 553.150 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1017 | 553.229 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1019 | 553.261 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1021 | 553.334 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1023 | 553.368 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1025 | 553.439 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1027 | 553.473 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1029 | 553.554 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1031 | 553.588 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1033 | 553.639 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1035 | 553.711 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1037 | 553.746 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1039 | 553.818 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1041 | 553.853 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1043 | 553.933 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1045 | 553.966 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1047 | 554.038 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1049 | 554.071 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1051 | 554.144 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1053 | 554.181 | 7852 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1056 | 554.336 | 7852 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1061 | 554.458 | 7852 | cat | exit_group | `code=0` |
| 1063 | 555.196 | 7845 | bash | clone | `` |
| 1065 | 555.519 | 7853 | bash | execve | `/usr/bin/chmod` |
| 1075 | 556.442 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1077 | 556.477 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1081 | 556.636 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1083 | 556.670 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1085 | 556.741 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1087 | 556.775 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1089 | 556.847 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1091 | 556.881 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1093 | 556.953 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1095 | 556.987 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1097 | 557.058 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1099 | 557.091 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1101 | 557.177 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1103 | 557.211 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1105 | 557.260 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1107 | 557.332 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1109 | 557.365 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1111 | 557.439 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1113 | 557.473 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1115 | 557.550 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1117 | 557.584 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1119 | 557.661 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1121 | 557.696 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1123 | 557.770 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1125 | 557.803 | 7853 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1127 | 557.911 | 7853 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 557.979 | 7853 | chmod | exit_group | `code=0` |
| 1132 | 558.245 | 7845 | bash | clone | `` |
| 1134 | 558.559 | 7854 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1140 | 559.650 | 7854 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1145 | 560.011 | 7854 | runme.sh | exit_group | `code=0` |
| 1154 | 562.229 | 7845 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 53.411 ms |
| Workload CPU (user+sys) | 77.173 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.443 ms |
| Evidence size | 428188 bytes |

