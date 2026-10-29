# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario01 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| Evidence configuration | B |
| Events recorded | 1291 |
| Failed exec attempts removed | 12 |
| Duration | 785.483 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_B_r4.json` (481012 bytes) |
| SHA-256 | `500e737520f7e347f1c6361e2d4b7655bfb55611c29119dc53ce9d692f7d744d` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario01_B_r4.json.sha256`

## 1. Process tree

- `7725` /usr/bin/bash
  - `7726` /usr/bin/rm
  - `7727` /usr/bin/mkdir
  - `7728` /usr/bin/cat
  - `7729` /usr/bin/python3
  - `7730` /usr/bin/sleep
  - `7731` /usr/bin/curl
  - `7732` /usr/bin/python3
  - `7733` /usr/bin/chmod
  - `7734` /tmp/ft_scenario01/downloaded.sh
    - `7735` /usr/bin/date
    - `7736` /usr/bin/sleep

12 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7725 (?) executed `/usr/bin/bash`
- +6.133 ms pid 7726 (bash) executed `/usr/bin/rm`
- +10.654 ms pid 7727 (bash) executed `/usr/bin/mkdir`
- +15.817 ms pid 7728 (bash) executed `/usr/bin/cat`
- +22.787 ms pid 7729 (bash) executed `/usr/bin/python3`
- +22.808 ms pid 7730 (bash) executed `/usr/bin/sleep`
- +532.295 ms pid 7731 (bash) executed `/usr/bin/curl`
- +564.897 ms pid 7733 (bash) executed `/usr/bin/chmod`
- +568.203 ms pid 7734 (bash) executed `/tmp/ft_scenario01/downloaded.sh` **(from a temporary directory)**
- +570.335 ms pid 7735 (downloaded.sh) executed `/usr/bin/date`
- +574.952 ms pid 7736 (downloaded.sh) executed `/usr/bin/sleep`

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario01/payload.sh` first touched +15.535 ms by pid 7728 (bash), created/truncated; 1 write call(s), 55 byte(s)
- `/tmp/ft_scenario01/downloaded.sh` first touched +562.549 ms by pid 7731 (curl), created/truncated; 1 write call(s), 55 byte(s)

## 5. Permission changes

- +567.488 ms pid 7733 (chmod) changed permissions of `/tmp/ft_scenario01/downloaded.sh` (dirfd=-100 mode=0775 raw=downloaded.sh)

## 6. Deletions

- +9.270 ms pid 7726 (rm) deleted `/tmp/ft_scenario01/payload.sh`
- +9.319 ms pid 7726 (rm) deleted `/tmp/ft_scenario01/downloaded.sh`
- +9.365 ms pid 7726 (rm) deleted `/tmp/ft_scenario01`

## 7. Access to sensitive resources

- +557.477 ms pid 7731 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +568.203 ms `/tmp/ft_scenario01/downloaded.sh` executed by pid 7734 (bash)
  - history of `/tmp/ft_scenario01/downloaded.sh`:
    - +9.319 ms #138 `unlinkat` by pid 7726 (rm)
    - +562.549 ms #1033 `openat` by pid 7731 (curl)
    - +562.773 ms #1037 `write` by pid 7731 (curl)
    - +562.812 ms #1038 `close` by pid 7731 (curl)
    - +567.488 ms #1107 `fchmodat` by pid 7733 (chmod)
    - +568.203 ms #1114 `execve` by pid 7734 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7725 | ? | execve | `/usr/bin/bash` |
| 15 | 1.293 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.331 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.494 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.529 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.618 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.673 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.295 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.334 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.411 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.444 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.521 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 2.556 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.643 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 2.677 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 2.728 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 2.803 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 2.838 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.911 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.945 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 3.028 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.063 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 3.137 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 3.170 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 3.246 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 3.279 | 7725 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 4.860 | 7725 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario01_download_execute.sh` |
| 71 | 5.781 | 7725 | bash | clone | `` |
| 73 | 6.133 | 7726 | bash | execve | `/usr/bin/rm` |
| 83 | 7.335 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 7.383 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 7.613 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 7.658 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 7.775 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 7.854 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 7.994 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 8.032 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 8.105 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 8.140 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 8.212 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 8.248 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 8.332 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 8.366 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 8.417 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 8.491 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 8.526 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 8.603 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 8.647 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 8.731 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 8.764 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 8.838 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 8.872 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 8.946 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 8.984 | 7726 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 9.111 | 7726 | rm | openat | `/tmp/ft_scenario01` |
| 137 | 9.270 | 7726 | rm | unlinkat | `/tmp/ft_scenario01/payload.sh` |
| 138 | 9.319 | 7726 | rm | unlinkat | `/tmp/ft_scenario01/downloaded.sh` |
| 140 | 9.365 | 7726 | rm | unlinkat | `/tmp/ft_scenario01` |
| 144 | 9.494 | 7726 | rm | exit_group | `code=0` |
| 145 | 10.264 | 7725 | bash | clone | `` |
| 147 | 10.654 | 7727 | bash | execve | `/usr/bin/mkdir` |
| 167 | 12.517 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 169 | 12.560 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 173 | 12.769 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 175 | 12.804 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 177 | 12.881 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 179 | 12.915 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 181 | 12.988 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 183 | 13.022 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 185 | 13.093 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 187 | 13.128 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 189 | 13.208 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 191 | 13.242 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 193 | 13.326 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 195 | 13.359 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 197 | 13.409 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 199 | 13.482 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 201 | 13.515 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 203 | 13.589 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 205 | 13.626 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 207 | 13.706 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 209 | 13.740 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 211 | 13.813 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 213 | 13.847 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 215 | 13.920 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 217 | 13.954 | 7727 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 221 | 14.192 | 7727 | mkdir | exit_group | `code=0` |
| 223 | 15.101 | 7725 | bash | clone | `` |
| 225 | 15.535 | 7728 | bash | openat | `/tmp/ft_scenario01/payload.sh` |
| 230 | 15.817 | 7728 | bash | execve | `/usr/bin/cat` |
| 240 | 17.077 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 242 | 17.121 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 246 | 17.314 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 248 | 17.354 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 250 | 17.445 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 252 | 17.487 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 254 | 17.576 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 256 | 17.623 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 258 | 17.712 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 260 | 17.754 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 262 | 17.842 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 264 | 17.882 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 266 | 18.037 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 268 | 18.101 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 270 | 18.171 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 272 | 18.283 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 274 | 18.338 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 276 | 18.562 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 278 | 18.639 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 280 | 19.650 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 282 | 19.739 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 284 | 19.882 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 286 | 19.940 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 288 | 20.041 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 290 | 20.087 | 7728 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 293 | 20.299 | 7728 | cat | write | `/tmp/ft_scenario01/payload.sh` |
| 298 | 20.479 | 7728 | cat | exit_group | `code=0` |
| 300 | 20.897 | 7725 | bash | clone | `` |
| 303 | 22.198 | 7725 | bash | clone | `` |
| 309 | 22.787 | 7729 | bash | execve | `/usr/bin/python3` |
| 310 | 22.808 | 7730 | bash | execve | `/usr/bin/sleep` |
| 333 | 24.408 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 335 | 24.572 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 340 | 24.820 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 24.865 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 24.965 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 25.011 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 25.105 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 25.152 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 352 | 25.250 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 354 | 25.295 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 357 | 25.396 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 359 | 25.444 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 364 | 25.559 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 365 | 25.570 | 7729 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 367 | 25.611 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 369 | 25.653 | 7729 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 371 | 25.682 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 375 | 25.792 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 377 | 25.836 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 380 | 25.946 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 382 | 25.989 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 384 | 26.093 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 386 | 26.141 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 388 | 26.242 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 390 | 26.281 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 392 | 26.372 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 394 | 26.412 | 7730 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 409 | 28.869 | 7729 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 410 | 28.895 | 7729 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 411 | 28.960 | 7729 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 412 | 28.982 | 7729 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 413 | 29.002 | 7729 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 414 | 29.926 | 7729 | python3 | openat | `/etc/localtime` |
| 434 | 35.287 | 7729 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 436 | 35.560 | 7729 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 440 | 35.829 | 7729 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 448 | 36.895 | 7729 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 450 | 37.057 | 7729 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 452 | 37.203 | 7729 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 524 | 46.286 | 7729 | python3 | openat | `/tmp/ft_scenario01` |
| 794 | 92.120 | 7729 | python3 | openat | `/etc/gai.conf` |
| 810 | 94.705 | 7729 | python3 | openat | `/etc/nsswitch.conf` |
| 814 | 94.848 | 7729 | python3 | openat | `/etc/host.conf` |
| 818 | 94.953 | 7729 | python3 | openat | `/etc/resolv.conf` |
| 822 | 95.068 | 7729 | python3 | openat | `/etc/hosts` |
| 826 | 95.214 | 7729 | python3 | openat | `/etc/hosts` |
| 831 | 527.592 | 7730 | sleep | exit_group | `code=0` |
| 833 | 530.876 | 7725 | bash | clone | `` |
| 835 | 532.295 | 7731 | bash | execve | `/usr/bin/curl` |
| 931 | 551.766 | 7731 | curl | openat | `/etc/gnutls/config` |
| 949 | 554.358 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 951 | 554.430 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 955 | 554.753 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 957 | 554.812 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 959 | 554.941 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 961 | 554.999 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 963 | 555.122 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 965 | 555.181 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 967 | 555.315 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 969 | 555.371 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 971 | 555.497 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 973 | 555.553 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 975 | 555.705 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 977 | 555.764 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 979 | 555.849 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 981 | 555.980 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 983 | 556.036 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 985 | 556.163 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 987 | 556.221 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 989 | 556.355 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 991 | 556.414 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 993 | 556.538 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 995 | 556.596 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 997 | 556.742 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 999 | 556.799 | 7731 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1001 | 556.930 | 7731 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1002 | 556.961 | 7731 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1005 | 557.287 | 7731 | curl | openat | `/etc/nsswitch.conf` |
| 1009 | 557.477 | 7731 | curl | openat | `/etc/passwd` |
| 1012 | 557.663 | 7731 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1013 | 559.220 | 7729 | python3 | clone3 | `` |
| 1014 | 559.917 | 7732 | python3 | openat | `/etc/mime.types` |
| 1027 | 562.159 | 7732 | python3 | openat | `/tmp/ft_scenario01/payload.sh` |
| 1033 | 562.549 | 7731 | curl | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1036 | 562.730 | 7732 | python3 | exit | `code=0` |
| 1037 | 562.773 | 7731 | curl | write | `/tmp/ft_scenario01/downloaded.sh` |
| 1041 | 563.312 | 7731 | curl | exit_group | `code=0` |
| 1043 | 564.525 | 7725 | bash | clone | `` |
| 1045 | 564.897 | 7733 | bash | execve | `/usr/bin/chmod` |
| 1055 | 565.955 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1057 | 565.993 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1061 | 566.194 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1063 | 566.229 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1065 | 566.303 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1067 | 566.337 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1069 | 566.410 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1071 | 566.444 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1073 | 566.517 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1075 | 566.550 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1077 | 566.629 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1079 | 566.662 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1081 | 566.746 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1083 | 566.781 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1085 | 566.832 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1087 | 566.907 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1089 | 566.941 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1091 | 567.016 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1093 | 567.051 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1095 | 567.130 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1097 | 567.164 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1099 | 567.237 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1101 | 567.271 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1103 | 567.346 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1105 | 567.379 | 7733 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1107 | 567.488 | 7733 | chmod | fchmodat | `/tmp/ft_scenario01/downloaded.sh` |
| 1110 | 567.558 | 7733 | chmod | exit_group | `code=0` |
| 1112 | 567.850 | 7725 | bash | clone | `` |
| 1114 | 568.203 | 7734 | bash | execve | `/tmp/ft_scenario01/downloaded.sh` |
| 1120 | 569.369 | 7734 | downloaded.sh | openat | `/tmp/ft_scenario01/downloaded.sh` |
| 1123 | 569.717 | 7734 | downloaded.sh | clone | `` |
| 1129 | 570.335 | 7735 | downloaded.sh | execve | `/usr/bin/date` |
| 1139 | 571.753 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1141 | 571.809 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1145 | 572.040 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1147 | 572.089 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1149 | 572.193 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1151 | 572.243 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1153 | 572.350 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1155 | 572.407 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1157 | 572.533 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1159 | 572.580 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1161 | 572.685 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1163 | 572.735 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1165 | 572.847 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1167 | 572.897 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1169 | 572.966 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1171 | 573.073 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1173 | 573.133 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1175 | 573.249 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1177 | 573.306 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1179 | 573.420 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1181 | 573.473 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1183 | 573.583 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1185 | 573.639 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1187 | 573.745 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1189 | 573.794 | 7735 | date | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1191 | 573.914 | 7735 | date | openat | `/etc/localtime` |
| 1200 | 574.285 | 7735 | date | exit_group | `code=0` |
| 1202 | 574.837 | 7734 | downloaded.sh | vfork | `` |
| 1203 | 574.952 | 7736 | downloaded.sh | execve | `/usr/bin/sleep` |
| 1213 | 576.216 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1215 | 576.259 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1219 | 576.460 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1221 | 576.503 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1223 | 576.593 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1225 | 576.640 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1227 | 576.730 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1229 | 576.770 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1231 | 576.860 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1233 | 576.902 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1235 | 576.989 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1237 | 577.031 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1239 | 577.131 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1241 | 577.174 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1243 | 577.236 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1245 | 577.326 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1247 | 577.369 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1249 | 577.475 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1251 | 577.707 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1253 | 577.888 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1255 | 577.936 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1257 | 578.038 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1259 | 578.075 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1261 | 578.178 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1263 | 578.226 | 7736 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1280 | 779.467 | 7736 | sleep | exit_group | `code=0` |
| 1282 | 780.216 | 7734 | downloaded.sh | exit_group | `code=0` |
| 1291 | 784.831 | 7725 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 68.103 ms |
| Workload CPU (user+sys) | 86.160 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 3.138 ms |
| Evidence size | 481012 bytes |

