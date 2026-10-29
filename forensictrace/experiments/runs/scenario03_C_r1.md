# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | C |
| Events recorded | 1154 |
| Failed exec attempts removed | 12 |
| Duration | 558.308 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_C_r1.json` (428187 bytes) |
| SHA-256 | `151f3a00dad10b4a25c68a41b832a1e3287951d1e64143fd2b64391ab6600059` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_C_r1.json.sha256`

## 1. Process tree

- `7253` /usr/bin/bash
  - `7254` /usr/bin/rm
  - `7255` /usr/bin/mkdir
  - `7256` /usr/bin/python3
  - `7257` /usr/bin/sleep
  - `7258` /usr/bin/curl
  - `7259` /usr/bin/python3
  - `7260` /usr/bin/cat
  - `7261` /usr/bin/chmod
  - `7262` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7253 (?) executed `/usr/bin/bash`
- +8.289 ms pid 7254 (bash) executed `/usr/bin/rm`
- +13.161 ms pid 7255 (bash) executed `/usr/bin/mkdir`
- +19.018 ms pid 7256 (bash) executed `/usr/bin/python3`
- +19.077 ms pid 7257 (bash) executed `/usr/bin/sleep`
- +525.031 ms pid 7258 (bash) executed `/usr/bin/curl`
- +545.044 ms pid 7260 (bash) executed `/usr/bin/cat`
- +549.874 ms pid 7261 (bash) executed `/usr/bin/chmod`
- +554.385 ms pid 7262 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

- +96.495 ms pid 7256 (python3) connected to `unix:/var/run/nscd/socket`
- +96.703 ms pid 7256 (python3) connected to `ipv6:[...]`
- +96.748 ms pid 7256 (python3) connected to `sockfd=3`
- +96.767 ms pid 7256 (python3) connected to `0.0.0.0:8766`
- +99.224 ms pid 7256 (python3) connected to `unix:/var/run/nscd/socket`
- +538.051 ms pid 7258 (curl) connected to `unix:/var/run/nscd/socket`
- +538.134 ms pid 7258 (curl) connected to `unix:/var/run/nscd/socket`
- +539.082 ms pid 7258 (curl) connected to `127.0.0.1:8766`

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +17.249 ms by pid 7253 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +524.919 ms by pid 7258 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +544.861 ms by pid 7260 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +553.404 ms pid 7261 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +11.750 ms pid 7254 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +11.801 ms pid 7254 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +11.837 ms pid 7254 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +11.891 ms pid 7254 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +538.368 ms pid 7258 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +554.385 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7262 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +11.801 ms #138 `unlinkat` by pid 7254 (rm)
    - +544.861 ms #988 `openat` by pid 7260 (bash)
    - +544.927 ms #989 `close` by pid 7260 (bash)
    - +548.044 ms #1056 `write` by pid 7260 (cat)
    - +548.193 ms #1059 `close` by pid 7260 (cat)
    - +553.404 ms #1127 `fchmodat` by pid 7261 (chmod)
    - +554.385 ms #1134 `execve` by pid 7262 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7253 | ? | execve | `/usr/bin/bash` |
| 15 | 2.208 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 2.252 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 2.453 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 2.502 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 2.669 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 2.717 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.825 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.865 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.961 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 3.006 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 3.103 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 3.148 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 3.255 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 3.297 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 3.357 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 3.453 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 3.493 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 3.606 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 3.649 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 3.783 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.827 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 4.026 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 4.097 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 4.217 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 4.263 | 7253 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 6.622 | 7253 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 7.899 | 7253 | bash | clone | `` |
| 73 | 8.289 | 7254 | bash | execve | `/usr/bin/rm` |
| 83 | 9.574 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 9.620 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 9.831 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 9.873 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 9.969 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 10.012 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 10.108 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 10.152 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 10.245 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 10.290 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 10.382 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 10.426 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 10.538 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 10.585 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 10.653 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 10.768 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 10.813 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 10.910 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 10.953 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 11.057 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 11.100 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 11.198 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 11.242 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 11.337 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 11.382 | 7254 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 11.546 | 7254 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 11.750 | 7254 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 11.801 | 7254 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 11.837 | 7254 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 11.891 | 7254 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 12.039 | 7254 | rm | exit_group | `code=0` |
| 146 | 12.842 | 7253 | bash | clone | `` |
| 148 | 13.161 | 7255 | bash | execve | `/usr/bin/mkdir` |
| 168 | 15.064 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 15.115 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 15.342 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 15.416 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 15.542 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 15.607 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 15.691 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 15.725 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 15.797 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 15.831 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 15.905 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 15.939 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 16.021 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 16.054 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 16.104 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 16.178 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 16.213 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 16.286 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 16.320 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 16.399 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 16.434 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 16.507 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 16.547 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 16.623 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 16.656 | 7255 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 16.921 | 7255 | mkdir | exit_group | `code=0` |
| 224 | 17.249 | 7253 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 17.398 | 7253 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 17.544 | 7253 | bash | clone | `` |
| 231 | 18.663 | 7253 | bash | clone | `` |
| 237 | 19.018 | 7256 | bash | execve | `/usr/bin/python3` |
| 238 | 19.077 | 7257 | bash | execve | `/usr/bin/sleep` |
| 261 | 20.819 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 263 | 20.861 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 21.056 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 21.098 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 21.191 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 21.230 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 21.323 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 278 | 21.370 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 280 | 21.464 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 282 | 21.502 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 284 | 21.592 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 287 | 21.636 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 292 | 21.739 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 293 | 21.747 | 7256 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 296 | 21.783 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 297 | 21.798 | 7256 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 299 | 21.848 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 21.960 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 22.000 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 22.090 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 22.129 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 22.227 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 22.266 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 22.357 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 22.395 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 22.486 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 22.525 | 7257 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 25.053 | 7256 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 25.081 | 7256 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 25.156 | 7256 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 25.176 | 7256 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 25.198 | 7256 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 26.135 | 7256 | python3 | openat | `/etc/localtime` |
| 362 | 32.082 | 7256 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 32.282 | 7256 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 32.604 | 7256 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 33.993 | 7256 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 34.322 | 7256 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 34.545 | 7256 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 43.334 | 7256 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 96.206 | 7256 | python3 | openat | `/etc/gai.conf` |
| 726 | 96.401 | 7256 | python3 | sendto | `socket:[46272]` |
| 727 | 96.495 | 7256 | python3 | connect | `unix:/var/run/nscd/socket` |
| 730 | 96.703 | 7256 | python3 | connect | `ipv6:[...]` |
| 731 | 96.748 | 7256 | python3 | connect | `sockfd=3` |
| 732 | 96.767 | 7256 | python3 | connect | `0.0.0.0:8766` |
| 742 | 99.224 | 7256 | python3 | connect | `unix:/var/run/nscd/socket` |
| 744 | 99.350 | 7256 | python3 | openat | `/etc/nsswitch.conf` |
| 748 | 99.538 | 7256 | python3 | openat | `/etc/host.conf` |
| 752 | 99.677 | 7256 | python3 | openat | `/etc/resolv.conf` |
| 756 | 99.820 | 7256 | python3 | openat | `/etc/hosts` |
| 760 | 100.000 | 7256 | python3 | openat | `/etc/hosts` |
| 765 | 523.256 | 7257 | sleep | exit_group | `code=0` |
| 767 | 524.514 | 7253 | bash | clone | `` |
| 769 | 524.919 | 7258 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 771 | 525.031 | 7258 | bash | execve | `/usr/bin/curl` |
| 867 | 534.345 | 7258 | curl | openat | `/etc/gnutls/config` |
| 885 | 536.042 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 887 | 536.089 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 891 | 536.308 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 893 | 536.342 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 895 | 536.449 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 897 | 536.483 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 899 | 536.579 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 901 | 536.621 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 903 | 536.711 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 905 | 536.752 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 907 | 536.847 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 909 | 536.888 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 911 | 536.992 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 913 | 537.033 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 915 | 537.105 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 917 | 537.215 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 919 | 537.260 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 921 | 537.361 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 923 | 537.403 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 925 | 537.505 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 927 | 537.561 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 929 | 537.655 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 931 | 537.700 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 933 | 537.799 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 935 | 537.844 | 7258 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 937 | 537.947 | 7258 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 938 | 537.972 | 7258 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 939 | 538.051 | 7258 | curl | connect | `unix:/var/run/nscd/socket` |
| 941 | 538.134 | 7258 | curl | connect | `unix:/var/run/nscd/socket` |
| 943 | 538.224 | 7258 | curl | openat | `/etc/nsswitch.conf` |
| 947 | 538.368 | 7258 | curl | openat | `/etc/passwd` |
| 950 | 538.481 | 7258 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 951 | 539.082 | 7258 | curl | connect | `127.0.0.1:8766` |
| 952 | 539.231 | 7256 | python3 | accept4 | `sockfd=3` |
| 953 | 539.423 | 7258 | curl | sendto | `socket:[46279]` |
| 954 | 539.529 | 7256 | python3 | clone3 | `` |
| 955 | 539.893 | 7259 | python3 | recvfrom | `socket:[45356]` |
| 956 | 540.234 | 7259 | python3 | openat | `/etc/mime.types` |
| 969 | 542.447 | 7259 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 971 | 542.644 | 7259 | python3 | sendto | `socket:[45356]` |
| 974 | 542.779 | 7259 | python3 | sendto | `socket:[45356]` |
| 975 | 542.789 | 7258 | curl | recvfrom | `socket:[46279]` |
| 980 | 542.965 | 7258 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 981 | 543.066 | 7259 | python3 | exit | `code=0` |
| 984 | 543.442 | 7258 | curl | exit_group | `code=0` |
| 986 | 544.473 | 7253 | bash | clone | `` |
| 988 | 544.861 | 7260 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 993 | 545.044 | 7260 | bash | execve | `/usr/bin/cat` |
| 1003 | 546.057 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1005 | 546.093 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1009 | 546.257 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1011 | 546.291 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1013 | 546.365 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1015 | 546.398 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1017 | 546.471 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1019 | 546.504 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1021 | 546.580 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1023 | 546.614 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1025 | 546.685 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1027 | 546.719 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1029 | 546.801 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1031 | 546.835 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1033 | 546.894 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1035 | 547.045 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1037 | 547.103 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1039 | 547.228 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1041 | 547.309 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1043 | 547.452 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1045 | 547.504 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1047 | 547.622 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1049 | 547.672 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1051 | 547.782 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1053 | 547.828 | 7260 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1056 | 548.044 | 7260 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1061 | 548.249 | 7260 | cat | exit_group | `code=0` |
| 1063 | 549.355 | 7253 | bash | clone | `` |
| 1065 | 549.874 | 7261 | bash | execve | `/usr/bin/chmod` |
| 1075 | 551.353 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1077 | 551.403 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1081 | 551.631 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1083 | 551.681 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1085 | 551.783 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1087 | 551.831 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1089 | 551.930 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1091 | 551.972 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1093 | 552.064 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1095 | 552.107 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1097 | 552.200 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1099 | 552.243 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1101 | 552.349 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1103 | 552.400 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1105 | 552.475 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1107 | 552.646 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1109 | 552.699 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1111 | 552.807 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1113 | 552.848 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1115 | 552.951 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1117 | 552.998 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1119 | 553.078 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1121 | 553.114 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1123 | 553.208 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1125 | 553.254 | 7261 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1127 | 553.404 | 7261 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 553.502 | 7261 | chmod | exit_group | `code=0` |
| 1132 | 553.993 | 7253 | bash | clone | `` |
| 1134 | 554.385 | 7262 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1140 | 555.448 | 7262 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1145 | 555.705 | 7262 | runme.sh | exit_group | `code=0` |
| 1154 | 557.343 | 7253 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 54.983 ms |
| Workload CPU (user+sys) | 78.808 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.431 ms |
| Evidence size | 428187 bytes |

