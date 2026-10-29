# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | B |
| Events recorded | 1291 |
| Failed exec attempts removed | 12 |
| Duration | 832.467 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_B_r2.json` (481012 bytes) |
| SHA-256 | `4a1a17c175a88edabf692fb1b475685d66441bd6733c93e70d049f1c798b6af7` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_B_r2.json.sha256`

## 1. Process tree

- `7321` /usr/bin/bash
  - `7322` /usr/bin/rm
  - `7323` /usr/bin/mkdir
  - `7324` /usr/bin/cat
  - `7325` /usr/bin/python3
  - `7326` /usr/bin/sleep
  - `7328` /usr/bin/curl
  - `7329` /usr/bin/python3
  - `7330` /usr/bin/chmod
  - `7331` /tmp/ft_scenario01/downloaded.sh
    - `7332` /usr/bin/date
    - `7333` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7321 (?) executed `/usr/bin/bash`
- +13.570 ms pid 7322 (bash) executed `/usr/bin/rm`
- +19.030 ms pid 7323 (bash) executed `/usr/bin/mkdir`
- +23.823 ms pid 7324 (bash) executed `/usr/bin/cat`
- +28.529 ms pid 7325 (bash) executed `/usr/bin/python3`
- +28.900 ms pid 7326 (bash) executed `/usr/bin/sleep`
- +534.858 ms pid 7328 (bash) executed `/usr/bin/curl`
- +613.192 ms pid 7330 (bash) executed `/usr/bin/chmod`
- +618.338 ms pid 7331 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +620.733 ms pid 7332 (downloaded.sh) executed `/usr/bin/date`
- +625.286 ms pid 7333 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +23.644 ms by pid 7324 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +588.442 ms by pid 7328 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +617.225 ms pid 7330 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +17.534 ms pid 7322 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +17.607 ms pid 7322 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +17.682 ms pid 7322 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +550.209 ms pid 7328 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +618.338 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7331 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +17.607 ms #138 `unlinkat` by pid 7322 (rm)
    - +588.442 ms #1032 `openat` by pid 7328 (curl)
    - +588.797 ms #1036 `write` by pid 7328 (curl)
    - +589.225 ms #1037 `close` by pid 7328 (curl)
    - +617.225 ms #1107 `fchmodat` by pid 7330 (chmod)
    - +618.338 ms #1114 `execve` by pid 7331 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7321 | ? | execve | `/usr/bin/bash` |
| 15 | 5.582 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 5.727 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 6.449 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 6.584 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 6.895 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 7.089 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 7.431 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 7.538 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 7.757 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 7.848 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 8.073 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 8.160 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 8.381 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 8.483 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 8.677 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 8.902 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 8.998 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 9.159 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 9.231 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 9.399 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 9.473 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 9.632 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 9.704 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 9.867 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 9.953 | 7321 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 11.672 | 7321 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 13.053 | 7321 | bash | clone | `` |
| 73 | 13.570 | 7322 | bash | execve | `/usr/bin/rm` |
| 83 | 15.243 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 15.288 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 15.509 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 15.549 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 15.648 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 15.688 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 15.808 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 15.856 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 15.957 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 16.003 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 16.096 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 16.141 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 16.248 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 16.291 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 16.355 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 16.450 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 16.495 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 16.593 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 16.637 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 16.743 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 16.787 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 16.884 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 16.930 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 17.036 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 17.092 | 7322 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 17.316 | 7322 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 17.534 | 7322 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 17.607 | 7322 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 17.682 | 7322 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 17.858 | 7322 | rm | exit_group | `code=0` |
| 145 | 18.667 | 7321 | bash | clone | `` |
| 147 | 19.030 | 7323 | bash | execve | `/usr/bin/mkdir` |
| 167 | 20.592 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 20.628 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 20.789 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 20.821 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 20.896 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 20.930 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 21.038 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 21.083 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 21.176 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 21.223 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 21.318 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 21.361 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 21.466 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 21.508 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 21.573 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 21.667 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 21.710 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 21.804 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 21.847 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 21.954 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 21.999 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 22.092 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 22.136 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 22.231 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 22.276 | 7323 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 22.606 | 7323 | mkdir | exit_group | `code=0` |
| 223 | 23.320 | 7321 | bash | clone | `` |
| 225 | 23.644 | 7324 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 23.823 | 7324 | bash | execve | `/usr/bin/cat` |
| 240 | 24.773 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 24.807 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 24.968 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 25.001 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 25.076 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 25.110 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 25.182 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 25.216 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 25.286 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 25.320 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 25.391 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 25.423 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 25.505 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 25.538 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 25.588 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 25.660 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 25.694 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 25.772 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 25.806 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 25.885 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 25.919 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 26.114 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 26.148 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 26.234 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 26.282 | 7324 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 26.501 | 7324 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 26.707 | 7324 | cat | exit_group | `code=0` |
| 300 | 27.144 | 7321 | bash | clone | `` |
| 303 | 28.183 | 7321 | bash | clone | `` |
| 309 | 28.529 | 7325 | bash | execve | `/usr/bin/python3` |
| 310 | 28.900 | 7326 | bash | execve | `/usr/bin/sleep` |
| 334 | 30.176 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 336 | 30.223 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 340 | 30.446 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 30.522 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 30.644 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 30.690 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 30.786 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 30.831 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 353 | 30.925 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 356 | 30.981 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 360 | 31.060 | 7325 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 361 | 31.080 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 364 | 31.120 | 7325 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 365 | 31.130 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 369 | 31.243 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 371 | 31.292 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 374 | 31.364 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 31.461 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 31.509 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 31.610 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 31.658 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 31.760 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 31.809 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 31.911 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 31.964 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 32.066 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 32.113 | 7326 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 34.489 | 7325 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 34.522 | 7325 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 34.604 | 7325 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 34.631 | 7325 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 34.657 | 7325 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 35.650 | 7325 | python3 | openat | `/etc/localtime` |
| 434 | 40.757 | 7325 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 40.897 | 7325 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 41.122 | 7325 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 42.174 | 7325 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 42.335 | 7325 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 42.481 | 7325 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 51.654 | 7325 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 97.427 | 7325 | python3 | openat | `/etc/gai.conf` |
| 810 | 99.967 | 7325 | python3 | openat | `/etc/nsswitch.conf` |
| 814 | 100.133 | 7325 | python3 | openat | `/etc/host.conf` |
| 818 | 100.258 | 7325 | python3 | openat | `/etc/resolv.conf` |
| 822 | 100.392 | 7325 | python3 | openat | `/etc/hosts` |
| 826 | 100.566 | 7325 | python3 | openat | `/etc/hosts` |
| 831 | 532.872 | 7326 | sleep | exit_group | `code=0` |
| 833 | 534.133 | 7321 | bash | clone | `` |
| 835 | 534.858 | 7328 | bash | execve | `/usr/bin/curl` |
| 931 | 546.051 | 7328 | curl | openat | `/etc/gnutls/config` |
| 949 | 547.475 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 951 | 547.509 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 955 | 547.926 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 957 | 547.972 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 959 | 548.053 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 961 | 548.085 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 963 | 548.168 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 965 | 548.210 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 967 | 548.302 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 969 | 548.344 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 971 | 548.445 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 973 | 548.486 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 975 | 548.600 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 977 | 548.649 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 979 | 548.713 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 981 | 548.835 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 983 | 548.883 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 985 | 549.019 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 987 | 549.064 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 989 | 549.186 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 991 | 549.240 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 993 | 549.342 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 995 | 549.392 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 997 | 549.511 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 999 | 549.562 | 7328 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1001 | 549.696 | 7328 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1002 | 549.729 | 7328 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1005 | 550.055 | 7328 | curl | openat | `/etc/nsswitch.conf` |
| 1009 | 550.209 | 7328 | curl | openat | `/etc/passwd` |
| 1012 | 550.332 | 7328 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1013 | 552.470 | 7325 | python3 | clone3 | `` |
| 1014 | 574.761 | 7329 | python3 | openat | `/etc/mime.types` |
| 1027 | 587.486 | 7329 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1032 | 588.442 | 7328 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1036 | 588.797 | 7328 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1038 | 589.257 | 7329 | python3 | exit | `code=0` |
| 1041 | 591.362 | 7328 | curl | exit_group | `code=0` |
| 1043 | 612.512 | 7321 | bash | clone | `` |
| 1045 | 613.192 | 7330 | bash | execve | `/usr/bin/chmod` |
| 1055 | 614.553 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1057 | 614.611 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1061 | 614.929 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1063 | 614.999 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1065 | 615.096 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1067 | 615.140 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1069 | 615.237 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1071 | 615.298 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1073 | 615.453 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1075 | 615.532 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1077 | 615.874 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1079 | 615.922 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1081 | 616.050 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1083 | 616.091 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1085 | 616.149 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1087 | 616.248 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1089 | 616.288 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1091 | 616.392 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1093 | 616.431 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1095 | 616.553 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1097 | 616.613 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1099 | 616.776 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1101 | 616.819 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1103 | 616.912 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1105 | 617.072 | 7330 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1107 | 617.225 | 7330 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1110 | 617.326 | 7330 | chmod | exit_group | `code=0` |
| 1112 | 617.739 | 7321 | bash | clone | `` |
| 1114 | 618.338 | 7331 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1120 | 619.789 | 7331 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1123 | 620.145 | 7331 | downloaded.sh | clone | `` |
| 1129 | 620.733 | 7332 | downloaded.sh | execve | `/usr/bin/date` |
| 1139 | 622.085 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1141 | 622.140 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1145 | 622.347 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1147 | 622.392 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1149 | 622.486 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1151 | 622.531 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1153 | 622.626 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1155 | 622.668 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1157 | 622.761 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1159 | 622.832 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1161 | 622.985 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1163 | 623.035 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1165 | 623.140 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1167 | 623.198 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1169 | 623.275 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1171 | 623.368 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1173 | 623.407 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1175 | 623.485 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1177 | 623.522 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1179 | 623.623 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1181 | 623.703 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1183 | 623.797 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1185 | 623.834 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1187 | 623.911 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1189 | 623.955 | 7332 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1191 | 624.399 | 7332 | date | openat | `/etc/localtime` |
| 1200 | 624.777 | 7332 | date | exit_group | `code=0` |
| 1202 | 625.214 | 7331 | downloaded.sh | vfork | `` |
| 1203 | 625.286 | 7333 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1213 | 626.314 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1215 | 626.350 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1219 | 626.509 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1221 | 626.548 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1223 | 626.621 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1225 | 626.655 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1227 | 626.728 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1229 | 626.760 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1231 | 626.833 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1233 | 626.868 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1235 | 626.942 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1237 | 626.986 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1239 | 627.091 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1241 | 627.137 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1243 | 627.209 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1245 | 627.304 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1247 | 627.352 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1249 | 627.450 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1251 | 627.496 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1253 | 627.584 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1255 | 627.618 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1257 | 627.690 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1259 | 627.723 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1261 | 627.796 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1263 | 627.830 | 7333 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1280 | 828.401 | 7333 | sleep | exit_group | `code=0` |
| 1282 | 828.647 | 7331 | downloaded.sh | exit_group | `code=0` |
| 1291 | 830.654 | 7321 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 65.556 ms |
| Workload CPU (user+sys) | 85.098 ms |
| Tracer peak memory | 29476 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.919 ms |
| Evidence size | 481012 bytes |

