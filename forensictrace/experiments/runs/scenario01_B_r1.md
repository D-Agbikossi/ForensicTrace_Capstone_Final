# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | B |
| Events recorded | 1291 |
| Failed exec attempts removed | 12 |
| Duration | 802.346 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_B_r1.json` (481010 bytes) |
| SHA-256 | `a4940201f15b35b55c9919ed835fbc5ea95fa170412a81fd3ae1816cf03486c7` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_B_r1.json.sha256`

## 1. Process tree

- `7147` /usr/bin/bash
  - `7148` /usr/bin/rm
  - `7149` /usr/bin/mkdir
  - `7150` /usr/bin/cat
  - `7151` /usr/bin/python3
  - `7152` /usr/bin/sleep
  - `7153` /usr/bin/curl
  - `7154` /usr/bin/python3
  - `7155` /usr/bin/chmod
  - `7156` /tmp/ft_scenario01/downloaded.sh
    - `7157` /usr/bin/date
    - `7158` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7147 (?) executed `/usr/bin/bash`
- +12.709 ms pid 7148 (bash) executed `/usr/bin/rm`
- +23.218 ms pid 7149 (bash) executed `/usr/bin/mkdir`
- +31.790 ms pid 7150 (bash) executed `/usr/bin/cat`
- +40.492 ms pid 7152 (bash) executed `/usr/bin/sleep`
- +43.848 ms pid 7151 (bash) executed `/usr/bin/python3`
- +551.547 ms pid 7153 (bash) executed `/usr/bin/curl`
- +581.358 ms pid 7155 (bash) executed `/usr/bin/chmod`
- +586.047 ms pid 7156 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +588.359 ms pid 7157 (downloaded.sh) executed `/usr/bin/date`
- +594.244 ms pid 7158 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +31.493 ms by pid 7150 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +577.156 ms by pid 7153 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +585.222 ms pid 7155 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +18.520 ms pid 7148 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +18.583 ms pid 7148 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +18.714 ms pid 7148 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +570.988 ms pid 7153 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +586.047 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7156 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +18.583 ms #138 `unlinkat` by pid 7148 (rm)
    - +577.156 ms #1032 `openat` by pid 7153 (curl)
    - +577.404 ms #1036 `write` by pid 7153 (curl)
    - +577.451 ms #1037 `close` by pid 7153 (curl)
    - +585.222 ms #1107 `fchmodat` by pid 7155 (chmod)
    - +586.047 ms #1114 `execve` by pid 7156 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7147 | ? | execve | `/usr/bin/bash` |
| 15 | 3.891 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 3.950 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 4.314 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 4.362 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 4.481 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 4.536 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 4.658 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 4.708 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 4.815 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 4.862 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 4.987 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 5.042 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 5.173 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 5.232 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 5.308 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 5.416 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 5.463 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 5.576 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 5.627 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 5.759 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 5.814 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 5.925 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 5.969 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 6.092 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 6.144 | 7147 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 8.197 | 7147 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 9.368 | 7147 | bash | clone | `` |
| 73 | 12.709 | 7148 | bash | execve | `/usr/bin/rm` |
| 83 | 14.469 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 14.517 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 14.823 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 14.868 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 14.968 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 15.011 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 16.196 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 16.317 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 16.428 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 16.476 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 16.635 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 16.703 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 16.819 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 16.862 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 16.928 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 17.023 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 17.068 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 17.172 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 17.252 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 17.361 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 17.404 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 17.501 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 17.545 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 17.648 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 17.985 | 7148 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 18.158 | 7148 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 18.520 | 7148 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 18.583 | 7148 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 18.714 | 7148 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 18.891 | 7148 | rm | exit_group | `code=0` |
| 145 | 20.866 | 7147 | bash | clone | `` |
| 147 | 23.218 | 7149 | bash | execve | `/usr/bin/mkdir` |
| 167 | 25.790 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 25.840 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 26.086 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 26.138 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 26.270 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 26.326 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 26.452 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 26.504 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 26.606 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 26.670 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 26.777 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 26.821 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 26.936 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 26.980 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 27.053 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 27.168 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 27.216 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 27.344 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 27.389 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 27.499 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 27.544 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 27.662 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 27.716 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 27.862 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 27.907 | 7149 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 28.285 | 7149 | mkdir | exit_group | `code=0` |
| 223 | 29.479 | 7147 | bash | clone | `` |
| 225 | 31.493 | 7150 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 31.790 | 7150 | bash | execve | `/usr/bin/cat` |
| 240 | 33.972 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 34.028 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 34.265 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 34.754 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 34.935 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 35.010 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 35.163 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 35.234 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 35.387 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 35.455 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 35.609 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 35.679 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 35.834 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 35.894 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 35.986 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 36.118 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 36.180 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 36.332 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 36.393 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 36.626 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 36.688 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 36.783 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 36.830 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 37.516 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 37.626 | 7150 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 37.895 | 7150 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 38.138 | 7150 | cat | exit_group | `code=0` |
| 300 | 38.641 | 7147 | bash | clone | `` |
| 302 | 39.551 | 7147 | bash | clone | `` |
| 305 | 40.492 | 7152 | bash | execve | `/usr/bin/sleep` |
| 318 | 43.713 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 321 | 43.779 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 322 | 43.848 | 7151 | bash | execve | `/usr/bin/python3` |
| 326 | 44.790 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 328 | 44.837 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 330 | 44.953 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 332 | 44.998 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 334 | 45.098 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 336 | 45.151 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 338 | 45.265 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 340 | 45.314 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 342 | 45.418 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 344 | 45.504 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 346 | 45.647 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 348 | 45.699 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 350 | 45.777 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 352 | 45.901 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 354 | 45.951 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 356 | 46.081 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 358 | 46.135 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 360 | 46.269 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 362 | 46.338 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 364 | 46.438 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 366 | 46.483 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 368 | 46.579 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 370 | 46.626 | 7152 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 403 | 64.967 | 7151 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 405 | 65.004 | 7151 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 70.260 | 7151 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 70.316 | 7151 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 70.415 | 7151 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 70.447 | 7151 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 70.475 | 7151 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 73.125 | 7151 | python3 | openat | `/etc/localtime` |
| 434 | 83.603 | 7151 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 84.744 | 7151 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 86.355 | 7151 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 88.036 | 7151 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 88.739 | 7151 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 88.979 | 7151 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 103.398 | 7151 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 160.206 | 7151 | python3 | openat | `/etc/gai.conf` |
| 810 | 162.534 | 7151 | python3 | openat | `/etc/nsswitch.conf` |
| 814 | 162.703 | 7151 | python3 | openat | `/etc/host.conf` |
| 818 | 162.824 | 7151 | python3 | openat | `/etc/resolv.conf` |
| 822 | 162.966 | 7151 | python3 | openat | `/etc/hosts` |
| 826 | 163.161 | 7151 | python3 | openat | `/etc/hosts` |
| 831 | 547.538 | 7152 | sleep | exit_group | `code=0` |
| 833 | 550.314 | 7147 | bash | clone | `` |
| 835 | 551.547 | 7153 | bash | execve | `/usr/bin/curl` |
| 931 | 566.813 | 7153 | curl | openat | `/etc/gnutls/config` |
| 949 | 568.422 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 951 | 568.466 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 955 | 568.670 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 957 | 568.712 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 959 | 568.802 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 961 | 568.844 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 963 | 568.934 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 965 | 568.975 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 967 | 569.073 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 969 | 569.113 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 971 | 569.203 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 973 | 569.242 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 975 | 569.344 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 977 | 569.386 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 979 | 569.446 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 981 | 569.536 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 983 | 569.576 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 985 | 569.672 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 987 | 569.714 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 989 | 569.811 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 991 | 569.853 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 993 | 570.083 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 995 | 570.253 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 997 | 570.474 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 999 | 570.522 | 7153 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1001 | 570.609 | 7153 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1002 | 570.635 | 7153 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1005 | 570.837 | 7153 | curl | openat | `/etc/nsswitch.conf` |
| 1009 | 570.988 | 7153 | curl | openat | `/etc/passwd` |
| 1012 | 571.097 | 7153 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1013 | 572.245 | 7151 | python3 | clone3 | `` |
| 1014 | 573.204 | 7154 | python3 | openat | `/etc/mime.types` |
| 1027 | 576.305 | 7154 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1032 | 577.156 | 7153 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1036 | 577.404 | 7153 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1038 | 577.465 | 7154 | python3 | exit | `code=0` |
| 1041 | 578.361 | 7153 | curl | exit_group | `code=0` |
| 1043 | 580.889 | 7147 | bash | clone | `` |
| 1045 | 581.358 | 7155 | bash | execve | `/usr/bin/chmod` |
| 1055 | 583.170 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1057 | 583.234 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1061 | 583.424 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1063 | 583.462 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1065 | 583.644 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1067 | 583.690 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1069 | 583.771 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1071 | 583.811 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1073 | 583.895 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1075 | 583.934 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1077 | 584.016 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1079 | 584.055 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1081 | 584.195 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1083 | 584.257 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1085 | 584.375 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1087 | 584.487 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1089 | 584.532 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1091 | 584.627 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1093 | 584.683 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1095 | 584.782 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1097 | 584.824 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1099 | 584.912 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1101 | 584.954 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1103 | 585.045 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1105 | 585.085 | 7155 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1107 | 585.222 | 7155 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1110 | 585.314 | 7155 | chmod | exit_group | `code=0` |
| 1112 | 585.646 | 7147 | bash | clone | `` |
| 1114 | 586.047 | 7156 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1120 | 587.097 | 7156 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1123 | 587.324 | 7156 | downloaded.sh | clone | `` |
| 1129 | 588.359 | 7157 | downloaded.sh | execve | `/usr/bin/date` |
| 1139 | 590.418 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1141 | 590.645 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1145 | 591.071 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1147 | 591.133 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1149 | 591.303 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1151 | 591.361 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1153 | 591.592 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1155 | 591.906 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1157 | 592.018 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1159 | 592.064 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1161 | 592.161 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1163 | 592.205 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1165 | 592.311 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1167 | 592.357 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1169 | 592.423 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1171 | 592.525 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1173 | 592.575 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1175 | 592.704 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1177 | 592.752 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1179 | 592.858 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1181 | 592.906 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1183 | 593.006 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1185 | 593.051 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1187 | 593.151 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1189 | 593.194 | 7157 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1191 | 593.318 | 7157 | date | openat | `/etc/localtime` |
| 1199 | 593.624 | 7157 | date | exit_group | `code=0` |
| 1202 | 594.134 | 7156 | downloaded.sh | vfork | `` |
| 1203 | 594.244 | 7158 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1213 | 596.819 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1215 | 596.883 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1219 | 597.104 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1221 | 597.140 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1223 | 597.232 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1225 | 597.279 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1227 | 597.367 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1229 | 597.401 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1231 | 597.493 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1233 | 597.527 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1235 | 597.606 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1237 | 597.658 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1239 | 597.767 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1241 | 597.801 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1243 | 597.866 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1245 | 597.949 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1247 | 597.985 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1249 | 598.073 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1251 | 598.121 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1253 | 598.247 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1255 | 598.294 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1257 | 598.402 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1259 | 598.446 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1261 | 598.550 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1263 | 598.619 | 7158 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1280 | 799.287 | 7158 | sleep | exit_group | `code=0` |
| 1282 | 799.719 | 7156 | downloaded.sh | exit_group | `code=0` |
| 1291 | 801.561 | 7147 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 74.785 ms |
| Workload CPU (user+sys) | 105.160 ms |
| Tracer peak memory | 21904 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.646 ms |
| Evidence size | 481010 bytes |

