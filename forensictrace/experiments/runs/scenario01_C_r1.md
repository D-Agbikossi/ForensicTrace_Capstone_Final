# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | C |
| Events recorded | 1306 |
| Failed exec attempts removed | 12 |
| Duration | 795.820 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_C_r1.json` (486192 bytes) |
| SHA-256 | `acb89c7f86cf513f19110a66db84adb99c1e7a38d3fdd4fbe6082ec8b9cd6cdd` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_C_r1.json.sha256`

## 1. Process tree

- `7129` /usr/bin/bash
  - `7130` /usr/bin/rm
  - `7131` /usr/bin/mkdir
  - `7132` /usr/bin/cat
  - `7133` /usr/bin/python3
  - `7134` /usr/bin/sleep
  - `7139` /usr/bin/curl
  - `7140` /usr/bin/python3
  - `7141` /usr/bin/chmod
  - `7142` /tmp/ft_scenario01/downloaded.sh
    - `7143` /usr/bin/date
    - `7144` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7129 (?) executed `/usr/bin/bash`
- +6.145 ms pid 7130 (bash) executed `/usr/bin/rm`
- +10.252 ms pid 7131 (bash) executed `/usr/bin/mkdir`
- +15.175 ms pid 7132 (bash) executed `/usr/bin/cat`
- +20.214 ms pid 7134 (bash) executed `/usr/bin/sleep`
- +20.268 ms pid 7133 (bash) executed `/usr/bin/python3`
- +527.743 ms pid 7139 (bash) executed `/usr/bin/curl`
- +563.876 ms pid 7141 (bash) executed `/usr/bin/chmod`
- +567.134 ms pid 7142 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +568.957 ms pid 7143 (downloaded.sh) executed `/usr/bin/date`
- +573.505 ms pid 7144 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +88.432 ms pid 7133 (python3) connected to `unix:/var/run/nscd/socket`
- +88.517 ms pid 7133 (python3) connected to `ipv6:[...]`
- +88.558 ms pid 7133 (python3) connected to `sockfd=3`
- +88.577 ms pid 7133 (python3) connected to `0.0.0.0:8765`
- +90.270 ms pid 7133 (python3) connected to `unix:/var/run/nscd/socket`
- +556.935 ms pid 7139 (curl) connected to `unix:/var/run/nscd/socket`
- +557.133 ms pid 7139 (curl) connected to `unix:/var/run/nscd/socket`
- +557.904 ms pid 7139 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +14.922 ms by pid 7132 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +561.671 ms by pid 7139 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +566.501 ms pid 7141 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +9.109 ms pid 7130 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +9.157 ms pid 7130 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +9.202 ms pid 7130 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +557.351 ms pid 7139 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +567.134 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7142 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +9.157 ms #138 `unlinkat` by pid 7130 (rm)
    - +561.671 ms #1048 `openat` by pid 7139 (curl)
    - +561.876 ms #1052 `write` by pid 7139 (curl)
    - +561.922 ms #1053 `close` by pid 7139 (curl)
    - +566.501 ms #1122 `fchmodat` by pid 7141 (chmod)
    - +567.134 ms #1129 `execve` by pid 7142 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7129 | ? | execve | `/usr/bin/bash` |
| 15 | 1.574 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.619 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.818 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.853 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.928 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.968 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.042 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.075 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.149 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.182 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.288 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 2.335 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.443 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 2.489 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 2.552 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 2.650 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 2.695 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.789 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.834 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 2.936 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 2.981 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 3.077 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 3.119 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 3.220 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 3.265 | 7129 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 4.838 | 7129 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 5.777 | 7129 | bash | clone | `` |
| 73 | 6.145 | 7130 | bash | execve | `/usr/bin/rm` |
| 83 | 7.188 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 7.232 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 7.397 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 7.433 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 7.509 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 7.544 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 7.626 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 7.664 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 7.738 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 7.772 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 7.847 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 7.881 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 7.966 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 8.001 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 8.054 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 8.130 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 8.165 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 8.260 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 8.302 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 8.458 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 8.505 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 8.654 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 8.714 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 8.793 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 8.828 | 7130 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 8.954 | 7130 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 9.109 | 7130 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 9.157 | 7130 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 9.202 | 7130 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 9.334 | 7130 | rm | exit_group | `code=0` |
| 145 | 9.938 | 7129 | bash | clone | `` |
| 147 | 10.252 | 7131 | bash | execve | `/usr/bin/mkdir` |
| 167 | 11.781 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 11.817 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 11.975 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 12.008 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 12.085 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 12.120 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 12.192 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 12.233 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 12.305 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 12.340 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 12.414 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 12.447 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 12.529 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 12.562 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 12.612 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 12.684 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 12.717 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 12.790 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 12.823 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 12.901 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 12.935 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 13.006 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 13.040 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 13.112 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 13.147 | 7131 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 13.486 | 7131 | mkdir | exit_group | `code=0` |
| 223 | 14.395 | 7129 | bash | clone | `` |
| 225 | 14.922 | 7132 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 15.175 | 7132 | bash | execve | `/usr/bin/cat` |
| 240 | 16.771 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 16.809 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 16.979 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 17.013 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 17.092 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 17.127 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 17.200 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 17.238 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 17.311 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 17.346 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 17.419 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 17.452 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 17.535 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 17.568 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 17.620 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 17.693 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 17.727 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 17.807 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 17.840 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 17.919 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 17.953 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 18.025 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 18.059 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 18.133 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 18.167 | 7132 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 18.343 | 7132 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 18.474 | 7132 | cat | exit_group | `code=0` |
| 300 | 18.789 | 7129 | bash | clone | `` |
| 303 | 19.838 | 7129 | bash | clone | `` |
| 309 | 20.214 | 7134 | bash | execve | `/usr/bin/sleep` |
| 310 | 20.268 | 7133 | bash | execve | `/usr/bin/python3` |
| 333 | 21.496 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 335 | 21.536 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 339 | 21.728 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 21.769 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 21.851 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 21.892 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 21.982 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 22.036 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 352 | 22.124 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 354 | 22.162 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 356 | 22.257 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 358 | 22.296 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 360 | 22.396 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 362 | 22.436 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 366 | 22.539 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 370 | 22.629 | 7133 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 371 | 22.637 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 374 | 22.673 | 7133 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 375 | 22.683 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 379 | 22.775 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 381 | 22.816 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 22.913 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 22.954 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 23.040 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 23.078 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 23.167 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 23.205 | 7134 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 25.831 | 7133 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 25.859 | 7133 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 25.922 | 7133 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 25.945 | 7133 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 25.965 | 7133 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 26.905 | 7133 | python3 | openat | `/etc/localtime` |
| 434 | 32.517 | 7133 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 32.695 | 7133 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 32.912 | 7133 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 33.988 | 7133 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 34.192 | 7133 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 34.369 | 7133 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 43.424 | 7133 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 88.139 | 7133 | python3 | openat | `/etc/gai.conf` |
| 798 | 88.347 | 7133 | python3 | sendto | `socket:[43763]` |
| 799 | 88.432 | 7133 | python3 | connect | `unix:/var/run/nscd/socket` |
| 802 | 88.517 | 7133 | python3 | connect | `ipv6:[...]` |
| 803 | 88.558 | 7133 | python3 | connect | `sockfd=3` |
| 804 | 88.577 | 7133 | python3 | connect | `0.0.0.0:8765` |
| 814 | 90.270 | 7133 | python3 | connect | `unix:/var/run/nscd/socket` |
| 816 | 90.347 | 7133 | python3 | openat | `/etc/nsswitch.conf` |
| 820 | 90.474 | 7133 | python3 | openat | `/etc/host.conf` |
| 824 | 90.571 | 7133 | python3 | openat | `/etc/resolv.conf` |
| 828 | 90.678 | 7133 | python3 | openat | `/etc/hosts` |
| 832 | 90.813 | 7133 | python3 | openat | `/etc/hosts` |
| 837 | 524.112 | 7134 | sleep | exit_group | `code=0` |
| 839 | 526.544 | 7129 | bash | clone | `` |
| 841 | 527.743 | 7139 | bash | execve | `/usr/bin/curl` |
| 937 | 551.152 | 7139 | curl | openat | `/etc/gnutls/config` |
| 955 | 553.995 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 957 | 554.075 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 961 | 554.559 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 963 | 554.632 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 965 | 554.794 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 967 | 554.865 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 969 | 555.011 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 971 | 555.081 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 973 | 555.241 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 975 | 555.316 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 977 | 555.512 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 555.589 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 981 | 555.758 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 983 | 555.829 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 985 | 555.929 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 987 | 556.059 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 989 | 556.093 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 991 | 556.169 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 993 | 556.235 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 995 | 556.355 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 997 | 556.400 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 999 | 556.486 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1001 | 556.524 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1003 | 556.621 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1005 | 556.663 | 7139 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1007 | 556.780 | 7139 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1008 | 556.804 | 7139 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1009 | 556.935 | 7139 | curl | connect | `unix:/var/run/nscd/socket` |
| 1011 | 557.133 | 7139 | curl | connect | `unix:/var/run/nscd/socket` |
| 1013 | 557.235 | 7139 | curl | openat | `/etc/nsswitch.conf` |
| 1017 | 557.351 | 7139 | curl | openat | `/etc/passwd` |
| 1020 | 557.442 | 7139 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1021 | 557.904 | 7139 | curl | connect | `127.0.0.1:8765` |
| 1022 | 558.030 | 7133 | python3 | accept4 | `sockfd=3` |
| 1023 | 558.287 | 7139 | curl | sendto | `socket:[37835]` |
| 1024 | 558.325 | 7133 | python3 | clone3 | `` |
| 1025 | 558.660 | 7140 | python3 | recvfrom | `socket:[43773]` |
| 1026 | 559.004 | 7140 | python3 | openat | `/etc/mime.types` |
| 1039 | 561.302 | 7140 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1041 | 561.488 | 7140 | python3 | sendto | `socket:[43773]` |
| 1044 | 561.602 | 7140 | python3 | sendto | `socket:[43773]` |
| 1045 | 561.620 | 7139 | curl | recvfrom | `socket:[37835]` |
| 1048 | 561.671 | 7139 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1051 | 561.857 | 7140 | python3 | exit | `code=0` |
| 1052 | 561.876 | 7139 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1056 | 562.451 | 7139 | curl | exit_group | `code=0` |
| 1058 | 563.517 | 7129 | bash | clone | `` |
| 1060 | 563.876 | 7141 | bash | execve | `/usr/bin/chmod` |
| 1070 | 564.992 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1072 | 565.028 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1076 | 565.194 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1078 | 565.235 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1080 | 565.312 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1082 | 565.345 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1084 | 565.418 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1086 | 565.451 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1088 | 565.524 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1090 | 565.558 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1092 | 565.628 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1094 | 565.663 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1096 | 565.749 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1098 | 565.783 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1100 | 565.833 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1102 | 565.906 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1104 | 565.941 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1106 | 566.017 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1108 | 566.051 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1110 | 566.132 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1112 | 566.166 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1114 | 566.246 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1116 | 566.282 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1118 | 566.360 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1120 | 566.394 | 7141 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1122 | 566.501 | 7141 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1125 | 566.574 | 7141 | chmod | exit_group | `code=0` |
| 1127 | 566.828 | 7129 | bash | clone | `` |
| 1129 | 567.134 | 7142 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1135 | 568.121 | 7142 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1138 | 568.349 | 7142 | downloaded.sh | clone | `` |
| 1144 | 568.957 | 7143 | downloaded.sh | execve | `/usr/bin/date` |
| 1154 | 570.273 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1156 | 570.388 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1160 | 570.655 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1162 | 570.707 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1164 | 570.906 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1166 | 570.963 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1168 | 571.325 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1170 | 571.390 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1172 | 571.493 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1174 | 571.533 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1176 | 571.624 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1178 | 571.662 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1180 | 571.769 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1182 | 571.807 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1184 | 571.868 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1186 | 571.960 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1188 | 572.000 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1190 | 572.095 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1192 | 572.133 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1194 | 572.264 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1196 | 572.314 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1198 | 572.415 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1200 | 572.460 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1202 | 572.556 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1204 | 572.600 | 7143 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1206 | 572.713 | 7143 | date | openat | `/etc/localtime` |
| 1214 | 572.993 | 7143 | date | exit_group | `code=0` |
| 1217 | 573.419 | 7142 | downloaded.sh | vfork | `` |
| 1218 | 573.505 | 7144 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1228 | 574.601 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1230 | 574.638 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1234 | 574.807 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1236 | 574.842 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1238 | 574.916 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1240 | 574.950 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1242 | 575.022 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1244 | 575.056 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1246 | 575.129 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1248 | 575.161 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1250 | 575.241 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1252 | 575.275 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1254 | 575.358 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1256 | 575.392 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1258 | 575.442 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1260 | 575.515 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1262 | 575.554 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1264 | 575.663 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1266 | 575.713 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1268 | 575.824 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1270 | 575.883 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1272 | 575.978 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1274 | 576.025 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1276 | 576.122 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1278 | 576.196 | 7144 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1295 | 778.609 | 7144 | sleep | exit_group | `code=0` |
| 1297 | 783.007 | 7142 | downloaded.sh | exit_group | `code=0` |
| 1306 | 794.606 | 7129 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 64.567 ms |
| Workload CPU (user+sys) | 85.315 ms |
| Tracer peak memory | 18464 KiB |
| Processing time (normalise+correlate+reconstruct) | 3.017 ms |
| Evidence size | 486192 bytes |

