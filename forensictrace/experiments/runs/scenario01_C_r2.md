# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | C |
| Events recorded | 1306 |
| Failed exec attempts removed | 12 |
| Duration | 770.786 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_C_r2.json` (486193 bytes) |
| SHA-256 | `7f9879ee574fd8879277e1101d0b9d3a6393af60ee57ae78cb23e2df67f2ff43` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_C_r2.json.sha256`

## 1. Process tree

- `7335` /usr/bin/bash
  - `7336` /usr/bin/rm
  - `7337` /usr/bin/mkdir
  - `7338` /usr/bin/cat
  - `7339` /usr/bin/python3
  - `7340` /usr/bin/sleep
  - `7341` /usr/bin/curl
  - `7342` /usr/bin/python3
  - `7343` /usr/bin/chmod
  - `7344` /tmp/ft_scenario01/downloaded.sh
    - `7345` /usr/bin/date
    - `7346` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7335 (?) executed `/usr/bin/bash`
- +7.066 ms pid 7336 (bash) executed `/usr/bin/rm`
- +10.910 ms pid 7337 (bash) executed `/usr/bin/mkdir`
- +15.263 ms pid 7338 (bash) executed `/usr/bin/cat`
- +23.805 ms pid 7340 (bash) executed `/usr/bin/sleep`
- +23.846 ms pid 7339 (bash) executed `/usr/bin/python3`
- +531.772 ms pid 7341 (bash) executed `/usr/bin/curl`
- +551.492 ms pid 7343 (bash) executed `/usr/bin/chmod`
- +555.185 ms pid 7344 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +557.059 ms pid 7345 (downloaded.sh) executed `/usr/bin/date`
- +560.184 ms pid 7346 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

- +93.490 ms pid 7339 (python3) connected to `unix:/var/run/nscd/socket`
- +93.596 ms pid 7339 (python3) connected to `ipv6:[...]`
- +93.647 ms pid 7339 (python3) connected to `sockfd=3`
- +93.675 ms pid 7339 (python3) connected to `0.0.0.0:8765`
- +95.540 ms pid 7339 (python3) connected to `unix:/var/run/nscd/socket`
- +544.781 ms pid 7341 (curl) connected to `unix:/var/run/nscd/socket`
- +544.844 ms pid 7341 (curl) connected to `unix:/var/run/nscd/socket`
- +545.566 ms pid 7341 (curl) connected to `127.0.0.1:8765`

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +15.052 ms by pid 7338 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +549.464 ms by pid 7341 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +554.499 ms pid 7343 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +9.788 ms pid 7336 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +9.824 ms pid 7336 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +9.869 ms pid 7336 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +545.025 ms pid 7341 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +555.185 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7344 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +9.824 ms #138 `unlinkat` by pid 7336 (rm)
    - +549.464 ms #1049 `openat` by pid 7341 (curl)
    - +549.654 ms #1052 `write` by pid 7341 (curl)
    - +549.693 ms #1053 `close` by pid 7341 (curl)
    - +554.499 ms #1122 `fchmodat` by pid 7343 (chmod)
    - +555.185 ms #1129 `execve` by pid 7344 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7335 | ? | execve | `/usr/bin/bash` |
| 15 | 1.579 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.634 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.869 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.918 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 2.043 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 2.097 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.370 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.433 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.557 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.933 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 3.411 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 3.471 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 3.593 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 3.646 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 3.719 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 3.819 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 3.865 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 3.963 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 4.011 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 4.112 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 4.156 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 4.260 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 4.305 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 4.420 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 4.467 | 7335 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 5.870 | 7335 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 6.657 | 7335 | bash | clone | `` |
| 73 | 7.066 | 7336 | bash | execve | `/usr/bin/rm` |
| 83 | 8.146 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 8.181 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 8.340 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 8.373 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 8.447 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 8.480 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 8.553 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 8.587 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 8.665 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 8.700 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 8.770 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 8.804 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 8.886 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 8.919 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 8.969 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 9.041 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 9.075 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 9.149 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 9.181 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 9.261 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 9.294 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 9.365 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 9.399 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 9.472 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 9.506 | 7336 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 9.630 | 7336 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 9.788 | 7336 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 9.824 | 7336 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 9.869 | 7336 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 9.996 | 7336 | rm | exit_group | `code=0` |
| 145 | 10.596 | 7335 | bash | clone | `` |
| 147 | 10.910 | 7337 | bash | execve | `/usr/bin/mkdir` |
| 167 | 12.381 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 12.417 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 12.571 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 12.604 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 12.685 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 12.720 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 12.792 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 12.826 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 12.896 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 12.930 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 13.004 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 13.036 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 13.120 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 13.153 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 13.203 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 13.275 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 13.308 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 13.381 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 13.414 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 13.493 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 13.527 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 13.599 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 13.632 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 13.710 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 13.745 | 7337 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 13.978 | 7337 | mkdir | exit_group | `code=0` |
| 223 | 14.674 | 7335 | bash | clone | `` |
| 225 | 15.052 | 7338 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 15.263 | 7338 | bash | execve | `/usr/bin/cat` |
| 240 | 19.266 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 19.314 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 19.531 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 19.574 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 19.680 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 19.725 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 19.819 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 19.864 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 19.957 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 20.003 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 20.098 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 20.141 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 20.247 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 20.293 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 20.364 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 20.480 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 20.525 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 20.627 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 20.679 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 20.791 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 20.839 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 20.940 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 20.985 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 21.086 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 21.152 | 7338 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 21.409 | 7338 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 21.591 | 7338 | cat | exit_group | `code=0` |
| 300 | 22.295 | 7335 | bash | clone | `` |
| 303 | 23.408 | 7335 | bash | clone | `` |
| 309 | 23.805 | 7340 | bash | execve | `/usr/bin/sleep` |
| 310 | 23.846 | 7339 | bash | execve | `/usr/bin/python3` |
| 333 | 25.230 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 336 | 25.282 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 340 | 25.509 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 25.555 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 25.660 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 25.709 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 25.806 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 25.857 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 354 | 25.965 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 357 | 26.013 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 359 | 26.072 | 7339 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 362 | 26.120 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 363 | 26.136 | 7339 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 365 | 26.171 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 369 | 26.291 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 372 | 26.343 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 374 | 26.407 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 26.508 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 26.555 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 26.664 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 26.709 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 26.810 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 26.855 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 26.949 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 26.992 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 27.087 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 27.129 | 7340 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 29.623 | 7339 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 29.792 | 7339 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 29.865 | 7339 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 29.891 | 7339 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 29.914 | 7339 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 31.548 | 7339 | python3 | openat | `/etc/localtime` |
| 434 | 37.194 | 7339 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 37.355 | 7339 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 37.564 | 7339 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 38.615 | 7339 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 38.783 | 7339 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 38.928 | 7339 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 48.023 | 7339 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 93.136 | 7339 | python3 | openat | `/etc/gai.conf` |
| 798 | 93.382 | 7339 | python3 | sendto | `socket:[47171]` |
| 799 | 93.490 | 7339 | python3 | connect | `unix:/var/run/nscd/socket` |
| 802 | 93.596 | 7339 | python3 | connect | `ipv6:[...]` |
| 803 | 93.647 | 7339 | python3 | connect | `sockfd=3` |
| 804 | 93.675 | 7339 | python3 | connect | `0.0.0.0:8765` |
| 814 | 95.540 | 7339 | python3 | connect | `unix:/var/run/nscd/socket` |
| 816 | 95.640 | 7339 | python3 | openat | `/etc/nsswitch.conf` |
| 820 | 95.807 | 7339 | python3 | openat | `/etc/host.conf` |
| 824 | 95.937 | 7339 | python3 | openat | `/etc/resolv.conf` |
| 828 | 96.072 | 7339 | python3 | openat | `/etc/hosts` |
| 832 | 96.249 | 7339 | python3 | openat | `/etc/hosts` |
| 837 | 528.155 | 7340 | sleep | exit_group | `code=0` |
| 839 | 530.800 | 7335 | bash | clone | `` |
| 841 | 531.772 | 7341 | bash | execve | `/usr/bin/curl` |
| 937 | 541.872 | 7341 | curl | openat | `/etc/gnutls/config` |
| 955 | 543.218 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 957 | 543.255 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 961 | 543.422 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 963 | 543.455 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 965 | 543.530 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 967 | 543.565 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 969 | 543.637 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 971 | 543.685 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 973 | 543.756 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 975 | 543.791 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 977 | 543.864 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 979 | 543.897 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 981 | 543.979 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 983 | 544.012 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 985 | 544.063 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 987 | 544.145 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 989 | 544.179 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 991 | 544.253 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 993 | 544.286 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 995 | 544.366 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 997 | 544.400 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 999 | 544.473 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1001 | 544.508 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1003 | 544.579 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1005 | 544.615 | 7341 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1007 | 544.699 | 7341 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1008 | 544.718 | 7341 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1009 | 544.781 | 7341 | curl | connect | `unix:/var/run/nscd/socket` |
| 1011 | 544.844 | 7341 | curl | connect | `unix:/var/run/nscd/socket` |
| 1013 | 544.914 | 7341 | curl | openat | `/etc/nsswitch.conf` |
| 1017 | 545.025 | 7341 | curl | openat | `/etc/passwd` |
| 1020 | 545.112 | 7341 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1021 | 545.566 | 7341 | curl | connect | `127.0.0.1:8765` |
| 1022 | 545.701 | 7339 | python3 | accept4 | `sockfd=3` |
| 1023 | 545.890 | 7341 | curl | sendto | `socket:[45422]` |
| 1024 | 545.996 | 7339 | python3 | clone3 | `` |
| 1025 | 546.342 | 7342 | python3 | recvfrom | `socket:[47176]` |
| 1026 | 546.719 | 7342 | python3 | openat | `/etc/mime.types` |
| 1039 | 548.957 | 7342 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1041 | 549.143 | 7342 | python3 | sendto | `socket:[47176]` |
| 1044 | 549.269 | 7342 | python3 | sendto | `socket:[47176]` |
| 1047 | 549.425 | 7341 | curl | recvfrom | `socket:[45422]` |
| 1049 | 549.464 | 7341 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1050 | 549.568 | 7342 | python3 | exit | `code=0` |
| 1052 | 549.654 | 7341 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1056 | 550.089 | 7341 | curl | exit_group | `code=0` |
| 1058 | 551.098 | 7335 | bash | clone | `` |
| 1060 | 551.492 | 7343 | bash | execve | `/usr/bin/chmod` |
| 1070 | 552.707 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1072 | 552.749 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1076 | 552.943 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1078 | 552.984 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1080 | 553.075 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1082 | 553.115 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1084 | 553.204 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1086 | 553.244 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1088 | 553.334 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1090 | 553.375 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1092 | 553.461 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1094 | 553.502 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1096 | 553.602 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1098 | 553.643 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1100 | 553.710 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1102 | 553.798 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1104 | 553.839 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1106 | 553.930 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1108 | 553.972 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1110 | 554.070 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1112 | 554.109 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1114 | 554.198 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1116 | 554.238 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1118 | 554.327 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1120 | 554.368 | 7343 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1122 | 554.499 | 7343 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1125 | 554.581 | 7343 | chmod | exit_group | `code=0` |
| 1127 | 554.851 | 7335 | bash | clone | `` |
| 1129 | 555.185 | 7344 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1135 | 556.349 | 7344 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1138 | 556.630 | 7344 | downloaded.sh | clone | `` |
| 1144 | 557.059 | 7345 | downloaded.sh | execve | `/usr/bin/date` |
| 1154 | 558.001 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1156 | 558.039 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1160 | 558.198 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1162 | 558.231 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1164 | 558.307 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1166 | 558.342 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1168 | 558.415 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1170 | 558.449 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1172 | 558.521 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1174 | 558.555 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1176 | 558.627 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1178 | 558.663 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1180 | 558.747 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1182 | 558.780 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1184 | 558.831 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1186 | 558.905 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1188 | 558.938 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1190 | 559.017 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1192 | 559.050 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1194 | 559.130 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1196 | 559.164 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1198 | 559.236 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1200 | 559.270 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1202 | 559.342 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1204 | 559.376 | 7345 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1206 | 559.460 | 7345 | date | openat | `/etc/localtime` |
| 1215 | 559.683 | 7345 | date | exit_group | `code=0` |
| 1217 | 560.091 | 7344 | downloaded.sh | vfork | `` |
| 1218 | 560.184 | 7346 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1228 | 561.055 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1230 | 561.092 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1234 | 561.249 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1236 | 561.283 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1238 | 561.354 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1240 | 561.388 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1242 | 561.459 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1244 | 561.494 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1246 | 561.567 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1248 | 561.599 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1250 | 561.696 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1252 | 561.741 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1254 | 561.835 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1256 | 561.875 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1258 | 561.933 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1260 | 562.014 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1262 | 562.047 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1264 | 562.120 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1266 | 562.154 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1268 | 562.229 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1270 | 562.263 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1272 | 562.334 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1274 | 562.369 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1276 | 562.442 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1278 | 562.474 | 7346 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1295 | 763.287 | 7346 | sleep | exit_group | `code=0` |
| 1297 | 764.022 | 7344 | downloaded.sh | exit_group | `code=0` |
| 1306 | 769.803 | 7335 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 60.046 ms |
| Workload CPU (user+sys) | 80.332 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 5.475 ms |
| Evidence size | 486193 bytes |

