# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario05 |
| Command | `bash scenarios/scenario05_multistage_intrusion.sh` |
| Evidence configuration | C |
| Events recorded | 1970 |
| Failed exec attempts removed | 12 |
| Duration | 700.702 ms |
| Evidence file | `docs/examples/custody_demo/demo_scenario05.json` (1313571 bytes) |
| SHA-256 | `a774c0bf0f80127009ad2ccc11ebd50063bb651fc72cb9d216a89a5fc13a30ad` |
| Case | DEMO-001 |
| Investigator | Demo Analyst |
| Session | `ac8f1ebe-3683-49ae-a760-953b618c9e11` |
| Started (UTC) | 2026-11-04T08:06:02.038803073Z |
| Hash-chain head | `abd8c13da47f0b2e811bc320a1abf024e76b18c117755002e6047f79ad0448c2` |

Verify integrity and custody: `forensictrace verify docs/examples/custody_demo/demo_scenario05.json`

## 1. Process tree

- `15076` /usr/bin/bash
  - `15077` /usr/bin/rm
  - `15078` /usr/bin/mkdir
  - `15079` /usr/bin/cat
  - `15080` /usr/bin/cat
  - `15081` /usr/bin/python3
  - `15082` /usr/bin/python3
  - `15083` /usr/bin/sleep
  - `15084` /usr/bin/bash
    - `15085` /usr/bin/curl
    - `15087` /usr/bin/chmod
    - `15088` /tmp/ft_scenario05/update.sh
      - `15089` /usr/bin/curl
  - `15086` /usr/bin/python3
  - `15090` /usr/bin/python3

15 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 15076 (?) executed `/usr/bin/bash`
- +17.204 ms pid 15077 (bash) executed `/usr/bin/rm`
- +27.012 ms pid 15078 (bash) executed `/usr/bin/mkdir`
- +37.170 ms pid 15079 (bash) executed `/usr/bin/cat`
- +43.460 ms pid 15080 (bash) executed `/usr/bin/cat`
- +50.466 ms pid 15082 (bash) executed `/usr/bin/python3`
- +50.492 ms pid 15081 (bash) executed `/usr/bin/python3`
- +50.559 ms pid 15083 (bash) executed `/usr/bin/sleep`
- +560.784 ms pid 15084 (bash) executed `/usr/bin/bash`
- +579.140 ms pid 15085 (bash) executed `/usr/bin/curl`
- +632.763 ms pid 15087 (bash) executed `/usr/bin/chmod`
- +648.119 ms pid 15088 (bash) executed `/tmp/ft_scenario05/update.sh` **(from a temporary directory)**
- +656.235 ms pid 15089 (update.sh) executed `/usr/bin/curl`

## 3. Network activity

- +184.260 ms pid 15082 (python3) connected to `unix:/var/run/nscd/socket`
- +184.285 ms pid 15081 (python3) connected to `unix:/var/run/nscd/socket`
- +185.484 ms pid 15082 (python3) connected to `unix:/var/run/nscd/socket`
- +186.030 ms pid 15081 (python3) connected to `unix:/var/run/nscd/socket`
- +610.686 ms pid 15085 (curl) connected to `unix:/var/run/nscd/socket`
- +612.024 ms pid 15085 (curl) connected to `unix:/var/run/nscd/socket`
- +615.554 ms pid 15085 (curl) connected to `127.0.0.1:8767`
- +685.438 ms pid 15089 (curl) connected to `unix:/var/run/nscd/socket`
- +686.036 ms pid 15089 (curl) connected to `unix:/var/run/nscd/socket`
- +687.635 ms pid 15089 (curl) connected to `127.0.0.1:8768`

## 4. Files created or modified

- `/tmp/ft_scenario05/victim/settings.conf` first touched +33.567 ms by pid 15076 (bash), created/truncated; 2 write call(s), 33 byte(s)
- `/tmp/ft_scenario05/www/update.sh` first touched +36.789 ms by pid 15079 (bash), created/truncated; 1 write call(s), 302 byte(s)
- `/tmp/ft_scenario05/stage1.sh` first touched +43.191 ms by pid 15080 (bash), created/truncated; 1 write call(s), 226 byte(s)
- `/tmp/ft_scenario05/update.sh` first touched +626.028 ms by pid 15085 (curl), created/truncated; 1 write call(s), 302 byte(s)
- `/tmp/ft_scenario05/victim/persistence.cron` first touched +653.476 ms by pid 15088 (update.sh), created/truncated; 1 write call(s), 37 byte(s)

## 5. Permission changes

- +645.544 ms pid 15087 (chmod) changed permissions of `/tmp/ft_scenario05/update.sh` (dirfd=-100 mode=0775)

## 6. Deletions

- +24.192 ms pid 15077 (rm) deleted `/tmp/ft_scenario05/victim/settings.conf`
- +24.280 ms pid 15077 (rm) deleted `/tmp/ft_scenario05/victim/persistence.cron`
- +24.366 ms pid 15077 (rm) deleted `/tmp/ft_scenario05/victim`
- +24.772 ms pid 15077 (rm) deleted `/tmp/ft_scenario05/www/update.sh`
- +24.852 ms pid 15077 (rm) deleted `/tmp/ft_scenario05/www`
- +24.897 ms pid 15077 (rm) deleted `/tmp/ft_scenario05/update.sh`
- +24.946 ms pid 15077 (rm) deleted `/tmp/ft_scenario05/stage1.sh`
- +25.024 ms pid 15077 (rm) deleted `/tmp/ft_scenario05`

## 7. Access to sensitive resources

- +613.547 ms pid 15085 (curl) `openat` on `/etc/passwd`
- +686.747 ms pid 15089 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +648.119 ms `/tmp/ft_scenario05/update.sh` executed by pid 15088 (bash)
  - history of `/tmp/ft_scenario05/update.sh`:
    - +24.897 ms #148 `unlinkat` by pid 15077 (rm)
    - +626.028 ms #1644 `openat` by pid 15085 (curl)
    - +626.635 ms #1648 `write` by pid 15085 (curl)
    - +626.739 ms #1649 `close` by pid 15085 (curl)
    - +645.544 ms #1718 `fchmodat` by pid 15087 (chmod)
    - +648.119 ms #1725 `execve` by pid 15088 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 15076 | ? | execve | `/usr/bin/bash` |
| 15 | 4.391 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 4.528 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 5.125 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 5.259 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 5.519 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 5.652 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 5.908 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 6.025 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 6.327 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 6.431 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 6.673 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 6.773 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 7.013 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 7.111 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 7.288 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 7.524 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 7.632 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 7.859 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 7.965 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 8.207 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 8.338 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 8.574 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 8.678 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 8.923 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 9.029 | 15076 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 13.503 | 15076 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario05_multistage_intrusion.sh` |
| 71 | 16.077 | 15076 | bash | clone | `` |
| 73 | 17.204 | 15077 | bash | execve | `/usr/bin/rm` |
| 83 | 20.401 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 20.461 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 20.744 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 20.801 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 20.931 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 20.989 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 21.119 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 21.179 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 21.313 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 21.374 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 21.498 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 21.559 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 21.703 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 21.762 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 21.849 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 21.976 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 22.039 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 22.168 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 22.237 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 22.383 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 22.442 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 22.574 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 22.634 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 22.762 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 22.826 | 15077 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 23.046 | 15077 | rm | openat | `/tmp/ft_scenario05` |
| 137 | 23.822 | 15077 | rm | openat | `/tmp/ft_scenario05/victim` |
| 139 | 24.192 | 15077 | rm | unlinkat | `/tmp/ft_scenario05/victim/settings.conf` |
| 140 | 24.280 | 15077 | rm | unlinkat | `/tmp/ft_scenario05/victim/persistence.cron` |
| 142 | 24.366 | 15077 | rm | unlinkat | `/tmp/ft_scenario05/victim` |
| 143 | 24.449 | 15077 | rm | openat | `/tmp/ft_scenario05/www` |
| 145 | 24.772 | 15077 | rm | unlinkat | `/tmp/ft_scenario05/www/update.sh` |
| 147 | 24.852 | 15077 | rm | unlinkat | `/tmp/ft_scenario05/www` |
| 148 | 24.897 | 15077 | rm | unlinkat | `/tmp/ft_scenario05/update.sh` |
| 149 | 24.946 | 15077 | rm | unlinkat | `/tmp/ft_scenario05/stage1.sh` |
| 151 | 25.024 | 15077 | rm | unlinkat | `/tmp/ft_scenario05` |
| 155 | 25.523 | 15077 | rm | exit_group | `code=0` |
| 156 | 26.532 | 15076 | bash | clone | `` |
| 158 | 27.012 | 15078 | bash | execve | `/usr/bin/mkdir` |
| 178 | 29.483 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 180 | 29.547 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 184 | 29.826 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 186 | 29.887 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 188 | 30.013 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 190 | 30.073 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 192 | 30.203 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 194 | 30.287 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 196 | 30.416 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 198 | 30.474 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 200 | 30.603 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 202 | 30.664 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 204 | 30.802 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 206 | 30.863 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 208 | 30.952 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 210 | 31.079 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 212 | 31.139 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 214 | 31.273 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 216 | 31.334 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 218 | 31.469 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 220 | 31.530 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 222 | 31.658 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 224 | 31.716 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 226 | 31.841 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 228 | 31.898 | 15078 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 230 | 32.219 | 15078 | mkdir | openat | `/tmp/ft_scenario05` |
| 234 | 32.757 | 15078 | mkdir | exit_group | `code=0` |
| 236 | 33.567 | 15076 | bash | openat | `/tmp/ft_scenario05/victim/settings.conf` |
| 238 | 34.058 | 15076 | bash | write | `/tmp/ft_scenario05/victim/settings.conf` |
| 240 | 35.585 | 15076 | bash | clone | `` |
| 242 | 36.789 | 15079 | bash | openat | `/tmp/ft_scenario05/www/update.sh` |
| 247 | 37.170 | 15079 | bash | execve | `/usr/bin/cat` |
| 257 | 39.844 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 259 | 39.901 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 263 | 40.148 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 265 | 40.201 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 267 | 40.328 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 269 | 40.378 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 271 | 40.482 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 273 | 40.531 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 275 | 40.636 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 277 | 40.684 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 279 | 40.787 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 281 | 40.839 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 283 | 40.960 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 285 | 41.010 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 287 | 41.081 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 289 | 41.188 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 291 | 41.250 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 293 | 41.367 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 295 | 41.421 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 297 | 41.535 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 299 | 41.584 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 301 | 41.683 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 303 | 41.729 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 305 | 41.831 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 307 | 41.876 | 15079 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 310 | 42.099 | 15079 | cat | write | `/tmp/ft_scenario05/www/update.sh` |
| 315 | 42.291 | 15079 | cat | exit_group | `code=0` |
| 317 | 42.684 | 15076 | bash | clone | `` |
| 319 | 43.191 | 15080 | bash | openat | `/tmp/ft_scenario05/stage1.sh` |
| 324 | 43.460 | 15080 | bash | execve | `/usr/bin/cat` |
| 334 | 44.907 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 336 | 44.964 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 340 | 45.204 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 342 | 45.261 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 344 | 45.371 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 346 | 45.426 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 348 | 45.525 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 350 | 45.571 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 352 | 45.671 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 354 | 45.716 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 356 | 45.820 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 358 | 45.864 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 360 | 45.977 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 362 | 46.023 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 364 | 46.090 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 366 | 46.192 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 368 | 46.244 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 370 | 46.357 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 372 | 46.404 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 374 | 46.512 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 376 | 46.560 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 378 | 46.665 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 380 | 46.710 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 382 | 46.812 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 384 | 46.857 | 15080 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 387 | 47.071 | 15080 | cat | write | `/tmp/ft_scenario05/stage1.sh` |
| 392 | 47.247 | 15080 | cat | exit_group | `code=0` |
| 394 | 47.651 | 15076 | bash | clone | `` |
| 397 | 48.273 | 15076 | bash | clone | `` |
| 402 | 49.966 | 15076 | bash | clone | `` |
| 410 | 50.466 | 15082 | bash | execve | `/usr/bin/python3` |
| 411 | 50.492 | 15081 | bash | execve | `/usr/bin/python3` |
| 412 | 50.559 | 15083 | bash | execve | `/usr/bin/sleep` |
| 445 | 52.606 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 448 | 52.671 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 455 | 53.003 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 457 | 53.068 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 459 | 53.232 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 461 | 53.297 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 464 | 53.431 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 466 | 53.497 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 468 | 53.682 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 471 | 53.783 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 476 | 53.985 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 478 | 54.036 | 15082 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 479 | 54.057 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 481 | 54.118 | 15082 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 484 | 54.248 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 487 | 54.320 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 490 | 54.423 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 492 | 54.586 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 494 | 54.652 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 498 | 54.825 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 501 | 54.899 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 503 | 54.991 | 15081 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 506 | 55.077 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 507 | 55.094 | 15081 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 509 | 55.165 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 513 | 55.355 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 516 | 55.445 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 518 | 55.623 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 520 | 55.695 | 15083 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 535 | 58.979 | 15082 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 536 | 59.025 | 15082 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 537 | 59.144 | 15082 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 538 | 59.188 | 15082 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 539 | 59.237 | 15082 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 540 | 59.594 | 15081 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 541 | 59.640 | 15081 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 542 | 59.757 | 15081 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 543 | 59.795 | 15081 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 544 | 59.832 | 15081 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 545 | 60.812 | 15082 | python3 | openat | `/etc/localtime` |
| 549 | 61.211 | 15081 | python3 | openat | `/etc/localtime` |
| 585 | 69.744 | 15082 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 586 | 69.822 | 15081 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 588 | 70.026 | 15082 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 590 | 70.159 | 15081 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 595 | 70.388 | 15082 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 600 | 70.652 | 15081 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 612 | 72.093 | 15082 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 615 | 72.401 | 15082 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 617 | 72.645 | 15081 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 618 | 72.661 | 15082 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 622 | 73.014 | 15081 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 624 | 73.283 | 15081 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 755 | 87.143 | 15082 | python3 | openat | `/tmp/ft_scenario05` |
| 775 | 89.684 | 15081 | python3 | openat | `/tmp/ft_scenario05` |
| 1321 | 183.700 | 15082 | python3 | openat | `/etc/host.conf` |
| 1322 | 183.715 | 15081 | python3 | openat | `/etc/host.conf` |
| 1329 | 184.000 | 15082 | python3 | openat | `/etc/resolv.conf` |
| 1330 | 184.025 | 15081 | python3 | openat | `/etc/resolv.conf` |
| 1337 | 184.260 | 15082 | python3 | connect | `unix:/var/run/nscd/socket` |
| 1338 | 184.285 | 15081 | python3 | connect | `unix:/var/run/nscd/socket` |
| 1341 | 185.484 | 15082 | python3 | connect | `unix:/var/run/nscd/socket` |
| 1342 | 186.030 | 15081 | python3 | connect | `unix:/var/run/nscd/socket` |
| 1345 | 186.677 | 15082 | python3 | openat | `/etc/nsswitch.conf` |
| 1346 | 186.708 | 15081 | python3 | openat | `/etc/nsswitch.conf` |
| 1352 | 186.882 | 15082 | python3 | openat | `/etc/hosts` |
| 1356 | 187.087 | 15081 | python3 | openat | `/etc/hosts` |
| 1361 | 557.031 | 15083 | sleep | exit_group | `code=0` |
| 1363 | 559.618 | 15076 | bash | clone | `` |
| 1365 | 560.784 | 15084 | bash | execve | `/usr/bin/bash` |
| 1379 | 566.214 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1381 | 566.367 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1385 | 566.932 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1387 | 567.052 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1389 | 567.334 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1391 | 567.475 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1393 | 567.757 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1395 | 567.875 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1397 | 568.141 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1399 | 568.284 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1401 | 568.568 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1403 | 568.704 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1405 | 569.017 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1407 | 569.149 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1409 | 569.370 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1411 | 569.668 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1413 | 569.803 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1415 | 570.082 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1417 | 570.219 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1419 | 570.540 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1421 | 570.670 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1423 | 570.955 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1425 | 571.092 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1427 | 571.422 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1429 | 571.556 | 15084 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1431 | 575.573 | 15084 | bash | openat | `/tmp/ft_scenario05/stage1.sh` |
| 1435 | 578.096 | 15084 | bash | clone | `` |
| 1437 | 579.140 | 15085 | bash | execve | `/usr/bin/curl` |
| 1533 | 597.651 | 15085 | curl | openat | `/etc/gnutls/config` |
| 1551 | 604.673 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1553 | 604.813 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1557 | 605.443 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1559 | 605.573 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1561 | 605.853 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1563 | 605.983 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1565 | 606.261 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1567 | 606.380 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1569 | 606.633 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1571 | 606.749 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1573 | 607.003 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1575 | 607.122 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1577 | 607.413 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1579 | 607.533 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1581 | 607.706 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1583 | 607.975 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1585 | 608.096 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1587 | 608.362 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1589 | 608.483 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1591 | 608.748 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1593 | 608.869 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1595 | 609.122 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1597 | 609.249 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1599 | 609.509 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1601 | 609.625 | 15085 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1603 | 609.937 | 15085 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1604 | 610.320 | 15085 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1605 | 610.686 | 15085 | curl | connect | `unix:/var/run/nscd/socket` |
| 1607 | 612.024 | 15085 | curl | connect | `unix:/var/run/nscd/socket` |
| 1609 | 613.169 | 15085 | curl | openat | `/etc/nsswitch.conf` |
| 1613 | 613.547 | 15085 | curl | openat | `/etc/passwd` |
| 1616 | 613.839 | 15085 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1617 | 615.554 | 15085 | curl | connect | `127.0.0.1:8767` |
| 1618 | 616.083 | 15081 | python3 | accept4 | `sockfd=3` |
| 1619 | 616.974 | 15085 | curl | sendto | `socket:[137673]` |
| 1620 | 617.185 | 15081 | python3 | clone3 | `` |
| 1621 | 618.051 | 15086 | python3 | recvfrom | `socket:[136771]` |
| 1622 | 618.809 | 15086 | python3 | openat | `/etc/mime.types` |
| 1635 | 625.023 | 15086 | python3 | openat | `/tmp/ft_scenario05/www/update.sh` |
| 1637 | 625.499 | 15086 | python3 | sendto | `socket:[136771]` |
| 1640 | 625.816 | 15086 | python3 | sendto | `socket:[136771]` |
| 1641 | 625.883 | 15085 | curl | recvfrom | `socket:[137673]` |
| 1644 | 626.028 | 15085 | curl | openat | `/tmp/ft_scenario05/update.sh` |
| 1647 | 626.553 | 15086 | python3 | exit | `code=0` |
| 1648 | 626.635 | 15085 | curl | write | `/tmp/ft_scenario05/update.sh` |
| 1652 | 628.335 | 15085 | curl | exit_group | `code=0` |
| 1654 | 631.707 | 15084 | bash | clone | `` |
| 1656 | 632.763 | 15087 | bash | execve | `/usr/bin/chmod` |
| 1666 | 637.109 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1668 | 637.258 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1672 | 637.877 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1674 | 638.004 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1676 | 638.302 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1678 | 638.429 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1680 | 638.686 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1682 | 638.812 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1684 | 639.085 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1686 | 639.412 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1688 | 639.756 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1690 | 639.879 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1692 | 640.209 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1694 | 640.360 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1696 | 640.552 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1698 | 640.835 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1700 | 640.963 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1702 | 641.263 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1704 | 641.392 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1706 | 641.688 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1708 | 641.821 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1710 | 642.288 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1712 | 642.601 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1714 | 642.938 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1716 | 644.469 | 15087 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1718 | 645.544 | 15087 | chmod | fchmodat | `/tmp/ft_scenario05/update.sh` |
| 1721 | 645.823 | 15087 | chmod | exit_group | `code=0` |
| 1723 | 646.897 | 15084 | bash | clone | `` |
| 1725 | 648.119 | 15088 | bash | execve | `/tmp/ft_scenario05/update.sh` |
| 1731 | 652.625 | 15088 | update.sh | openat | `/tmp/ft_scenario05/update.sh` |
| 1734 | 653.476 | 15088 | update.sh | openat | `/tmp/ft_scenario05/victim/persistence.cron` |
| 1737 | 654.170 | 15088 | update.sh | write | `/tmp/ft_scenario05/victim/persistence.cron` |
| 1739 | 654.440 | 15088 | update.sh | openat | `/tmp/ft_scenario05/victim/settings.conf` |
| 1742 | 654.828 | 15088 | update.sh | write | `/tmp/ft_scenario05/victim/settings.conf` |
| 1744 | 655.923 | 15088 | update.sh | vfork | `` |
| 1745 | 656.235 | 15089 | update.sh | execve | `/usr/bin/curl` |
| 1841 | 680.149 | 15089 | curl | openat | `/etc/gnutls/config` |
| 1859 | 683.193 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1861 | 683.269 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1865 | 683.561 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1867 | 683.613 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1869 | 683.723 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1871 | 683.776 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1873 | 683.876 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1875 | 683.921 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1877 | 684.025 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1879 | 684.076 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1881 | 684.177 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1883 | 684.229 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1885 | 684.345 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1887 | 684.390 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1889 | 684.459 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1891 | 684.565 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1893 | 684.610 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1895 | 684.713 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1897 | 684.758 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1899 | 684.865 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1901 | 684.910 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1903 | 685.008 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1905 | 685.054 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1907 | 685.155 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1909 | 685.202 | 15089 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1911 | 685.320 | 15089 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1912 | 685.346 | 15089 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 1913 | 685.438 | 15089 | curl | connect | `unix:/var/run/nscd/socket` |
| 1915 | 686.036 | 15089 | curl | connect | `unix:/var/run/nscd/socket` |
| 1917 | 686.586 | 15089 | curl | openat | `/etc/nsswitch.conf` |
| 1921 | 686.747 | 15089 | curl | openat | `/etc/passwd` |
| 1924 | 686.868 | 15089 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 1925 | 687.635 | 15089 | curl | connect | `127.0.0.1:8768` |
| 1926 | 687.972 | 15082 | python3 | accept4 | `sockfd=3` |
| 1927 | 688.426 | 15089 | curl | sendto | `socket:[138588]` |
| 1928 | 688.547 | 15082 | python3 | clone3 | `` |
| 1929 | 689.098 | 15090 | python3 | recvfrom | `socket:[136175]` |
| 1930 | 689.588 | 15090 | python3 | openat | `/etc/mime.types` |
| 1943 | 692.861 | 15090 | python3 | openat | `/tmp/ft_scenario05/www/beacon` (failed) |
| 1946 | 693.085 | 15090 | python3 | sendto | `socket:[136175]` |
| 1947 | 693.152 | 15090 | python3 | sendto | `socket:[136175]` |
| 1949 | 693.298 | 15089 | curl | recvfrom | `socket:[138588]` |
| 1951 | 693.454 | 15090 | python3 | exit | `code=0` |
| 1957 | 694.195 | 15089 | curl | exit_group | `code=0` |
| 1959 | 695.049 | 15088 | update.sh | exit_group | `code=0` |
| 1961 | 695.554 | 15084 | bash | exit_group | `code=0` |
| 1970 | 699.208 | 15076 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 168.438 ms |
| Workload CPU (user+sys) | 246.512 ms |
| Tracer peak memory | 8100 KiB |
| Processing time (normalise+correlate+reconstruct) | 3.916 ms |
| Evidence size | 1313571 bytes |

