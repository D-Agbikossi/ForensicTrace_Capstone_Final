# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | B |
| Events recorded | 1291 |
| Failed exec attempts removed | 12 |
| Duration | 741.687 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_B_r3.json` (481012 bytes) |
| SHA-256 | `0e3d1e0b896b6dc1036ecca554715caf561a3f4bf66093f6d7ca1f3dbc6e25d9` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario01_B_r3.json.sha256`

## 1. Process tree

- `8342` /usr/bin/bash
  - `8343` /usr/bin/rm
  - `8344` /usr/bin/mkdir
  - `8345` /usr/bin/cat
  - `8346` /usr/bin/python3
  - `8347` /usr/bin/sleep
  - `8352` /usr/bin/curl
  - `8353` /usr/bin/python3
  - `8354` /usr/bin/chmod
  - `8355` /tmp/ft_scenario01/downloaded.sh
    - `8356` /usr/bin/date
    - `8357` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8342 (?) executed `/usr/bin/bash`
- +2.654 ms pid 8343 (bash) executed `/usr/bin/rm`
- +4.810 ms pid 8344 (bash) executed `/usr/bin/mkdir`
- +7.703 ms pid 8345 (bash) executed `/usr/bin/cat`
- +9.964 ms pid 8347 (bash) executed `/usr/bin/sleep`
- +10.029 ms pid 8346 (bash) executed `/usr/bin/python3`
- +513.822 ms pid 8352 (bash) executed `/usr/bin/curl`
- +529.347 ms pid 8354 (bash) executed `/usr/bin/chmod`
- +531.580 ms pid 8355 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +532.549 ms pid 8356 (downloaded.sh) executed `/usr/bin/date`
- +535.514 ms pid 8357 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +7.582 ms by pid 8345 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +528.222 ms by pid 8352 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +531.149 ms pid 8354 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +4.332 ms pid 8343 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +4.376 ms pid 8343 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +4.421 ms pid 8343 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +525.084 ms pid 8352 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +531.580 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 8355 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +4.376 ms #138 `unlinkat` by pid 8343 (rm)
    - +528.222 ms #1032 `openat` by pid 8352 (curl)
    - +528.349 ms #1036 `write` by pid 8352 (curl)
    - +528.403 ms #1038 `close` by pid 8352 (curl)
    - +531.149 ms #1107 `fchmodat` by pid 8354 (chmod)
    - +531.580 ms #1114 `execve` by pid 8355 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8342 | ? | execve | `/usr/bin/bash` |
| 15 | 0.820 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 0.886 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.006 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.051 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.110 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.164 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.223 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.267 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.324 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.368 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.427 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.476 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.543 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.585 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.622 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.670 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.705 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 1.751 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 1.786 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 1.839 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 1.877 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 1.933 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 1.967 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.016 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.051 | 8342 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.316 | 8342 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 2.485 | 8342 | bash | clone | `` |
| 73 | 2.654 | 8343 | bash | execve | `/usr/bin/rm` |
| 83 | 3.211 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.245 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 3.337 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 3.370 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 3.417 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 3.450 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 3.497 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 3.531 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 3.575 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 3.610 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 3.653 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 3.687 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 3.743 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 3.775 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 3.811 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 3.857 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 3.892 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 3.938 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 3.971 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 4.022 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 4.055 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 4.100 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 4.134 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 4.185 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 4.220 | 8343 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 4.275 | 8343 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 4.332 | 8343 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 4.376 | 8343 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 4.421 | 8343 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 4.540 | 8343 | rm | exit_group | `code=0` |
| 145 | 4.666 | 8342 | bash | clone | `` |
| 147 | 4.810 | 8344 | bash | execve | `/usr/bin/mkdir` |
| 167 | 5.767 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 5.813 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 5.927 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 5.970 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 6.045 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 6.093 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 6.166 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 6.212 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 6.269 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 6.314 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 6.373 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 6.417 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 6.484 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 6.527 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 6.574 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 6.631 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 6.674 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 6.731 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 6.775 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 6.837 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 6.882 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 6.938 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 6.983 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 7.039 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 7.085 | 8344 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 7.263 | 8344 | mkdir | exit_group | `code=0` |
| 223 | 7.429 | 8342 | bash | clone | `` |
| 225 | 7.582 | 8345 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 7.703 | 8345 | bash | execve | `/usr/bin/cat` |
| 240 | 8.210 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 8.245 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 8.332 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 8.364 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 8.410 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 8.445 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 8.488 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 8.522 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 8.565 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 8.600 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 8.646 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 8.679 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 8.734 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 8.766 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 8.803 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 8.847 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 8.880 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 8.925 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 8.958 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 9.006 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 9.040 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 9.084 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 9.118 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 9.183 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 9.245 | 8345 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 9.346 | 8345 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 9.490 | 8345 | cat | exit_group | `code=0` |
| 300 | 9.627 | 8342 | bash | clone | `` |
| 303 | 9.797 | 8342 | bash | clone | `` |
| 307 | 9.964 | 8347 | bash | execve | `/usr/bin/sleep` |
| 310 | 10.029 | 8346 | bash | execve | `/usr/bin/python3` |
| 327 | 10.554 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 331 | 10.610 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 338 | 10.728 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 341 | 10.781 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 10.844 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 10.893 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 10.950 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 10.999 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 352 | 11.058 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 355 | 11.111 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 359 | 11.189 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 362 | 11.238 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 363 | 11.250 | 8346 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 366 | 11.304 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 367 | 11.313 | 8346 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 369 | 11.348 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 372 | 11.392 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 376 | 11.450 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 378 | 11.494 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 11.550 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 11.598 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 11.661 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 11.712 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 11.773 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 11.821 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 11.884 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 11.931 | 8347 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 14.085 | 8346 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 14.142 | 8346 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 14.186 | 8346 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 14.216 | 8346 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 14.243 | 8346 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 15.142 | 8346 | python3 | openat | `/etc/localtime` |
| 434 | 18.246 | 8346 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 18.354 | 8346 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 18.520 | 8346 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 19.310 | 8346 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 19.406 | 8346 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 19.482 | 8346 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 25.800 | 8346 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 58.773 | 8346 | python3 | openat | `/etc/gai.conf` |
| 810 | 60.509 | 8346 | python3 | openat | `/etc/nsswitch.conf` |
| 814 | 60.623 | 8346 | python3 | openat | `/etc/host.conf` |
| 818 | 60.716 | 8346 | python3 | openat | `/etc/resolv.conf` |
| 822 | 60.817 | 8346 | python3 | openat | `/etc/hosts` |
| 826 | 60.919 | 8346 | python3 | openat | `/etc/hosts` |
| 831 | 512.669 | 8347 | sleep | exit_group | `code=0` |
| 833 | 513.302 | 8342 | bash | clone | `` |
| 835 | 513.822 | 8352 | bash | execve | `/usr/bin/curl` |
| 931 | 522.894 | 8352 | curl | openat | `/etc/gnutls/config` |
| 949 | 523.781 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 951 | 523.818 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 955 | 523.912 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 957 | 523.946 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 959 | 523.993 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 961 | 524.027 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 963 | 524.072 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 965 | 524.106 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 967 | 524.158 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 969 | 524.192 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 971 | 524.239 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 973 | 524.271 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 975 | 524.326 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 977 | 524.360 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 979 | 524.396 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 981 | 524.448 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 983 | 524.482 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 985 | 524.529 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 987 | 524.564 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 989 | 524.628 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 991 | 524.675 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 993 | 524.724 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 995 | 524.759 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 997 | 524.805 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 999 | 524.838 | 8352 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1001 | 524.890 | 8352 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1002 | 524.908 | 8352 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1005 | 525.002 | 8352 | curl | openat | `/etc/nsswitch.conf` |
| 1009 | 525.084 | 8352 | curl | openat | `/etc/passwd` |
| 1012 | 525.150 | 8352 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1013 | 525.480 | 8346 | python3 | clone3 | `` |
| 1014 | 525.859 | 8353 | python3 | openat | `/etc/mime.types` |
| 1027 | 527.944 | 8353 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1032 | 528.222 | 8352 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1036 | 528.349 | 8352 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1037 | 528.368 | 8353 | python3 | exit | `code=0` |
| 1041 | 528.634 | 8352 | curl | exit_group | `code=0` |
| 1043 | 529.160 | 8342 | bash | clone | `` |
| 1045 | 529.347 | 8354 | bash | execve | `/usr/bin/chmod` |
| 1055 | 529.974 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1057 | 530.012 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1061 | 530.104 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1063 | 530.156 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1065 | 530.205 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1067 | 530.239 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1069 | 530.284 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1071 | 530.318 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1073 | 530.363 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1075 | 530.396 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1077 | 530.441 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1079 | 530.474 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1081 | 530.529 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1083 | 530.562 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1085 | 530.598 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1087 | 530.644 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1089 | 530.677 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1091 | 530.724 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1093 | 530.767 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1095 | 530.842 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1097 | 530.887 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1099 | 530.941 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1101 | 530.985 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1103 | 531.040 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1105 | 531.080 | 8354 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1107 | 531.149 | 8354 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1110 | 531.235 | 8354 | chmod | exit_group | `code=0` |
| 1112 | 531.395 | 8342 | bash | clone | `` |
| 1114 | 531.580 | 8355 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1120 | 532.187 | 8355 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1123 | 532.293 | 8355 | downloaded.sh | clone | `` |
| 1129 | 532.549 | 8356 | downloaded.sh | execve | `/usr/bin/date` |
| 1139 | 533.277 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1141 | 533.330 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1145 | 533.454 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1147 | 533.505 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1149 | 533.567 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1151 | 533.616 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1153 | 533.683 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1155 | 533.730 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1157 | 533.789 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1159 | 533.837 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1161 | 533.896 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1163 | 533.944 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1165 | 534.011 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1167 | 534.066 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1169 | 534.114 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1171 | 534.187 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1173 | 534.244 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1175 | 534.313 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1177 | 534.380 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1179 | 534.455 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1181 | 534.506 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1183 | 534.571 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1185 | 534.623 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1187 | 534.689 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1189 | 534.739 | 8356 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1191 | 534.835 | 8356 | date | openat | `/etc/localtime` |
| 1200 | 535.239 | 8356 | date | exit_group | `code=0` |
| 1202 | 535.443 | 8355 | downloaded.sh | vfork | `` |
| 1203 | 535.514 | 8357 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1213 | 536.346 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1215 | 536.386 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1219 | 536.866 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1221 | 536.916 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1223 | 536.981 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1225 | 537.025 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1227 | 537.084 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1229 | 537.127 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1231 | 537.193 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1233 | 537.241 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1235 | 537.300 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1237 | 537.353 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1239 | 537.438 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1241 | 537.514 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1243 | 537.594 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1245 | 537.689 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1247 | 537.728 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1249 | 537.778 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1251 | 537.813 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1253 | 537.867 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1255 | 537.901 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1257 | 537.952 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1259 | 537.985 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1261 | 538.034 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1263 | 538.068 | 8357 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1280 | 738.806 | 8357 | sleep | exit_group | `code=0` |
| 1282 | 739.074 | 8355 | downloaded.sh | exit_group | `code=0` |
| 1291 | 740.971 | 8342 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 26.374 ms |
| Workload CPU (user+sys) | 66.537 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 2.015 ms |
| Evidence size | 481012 bytes |

