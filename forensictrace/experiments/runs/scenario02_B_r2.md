# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario02 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| Evidence configuration | B |
| Events recorded | 455 |
| Failed exec attempts removed | 12 |
| Duration | 58.182 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_B_r2.json` (171208 bytes) |
| SHA-256 | `3b314ed6e01a376347f44d202219136d3ae0b08469a1ad6c5c02a3fb18de848b` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario02_B_r2.json.sha256`

## 1. Process tree

- `7382` /usr/bin/bash
  - `7383` /usr/bin/rm
  - `7384` /usr/bin/mkdir
  - `7385` /usr/bin/cat
  - `7386` /usr/bin/cat
  - `7387` /usr/bin/rm

6 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7382 (?) executed `/usr/bin/bash`
- +8.645 ms pid 7383 (bash) executed `/usr/bin/rm`
- +19.311 ms pid 7384 (bash) executed `/usr/bin/mkdir`
- +29.958 ms pid 7385 (bash) executed `/usr/bin/cat`
- +38.043 ms pid 7386 (bash) executed `/usr/bin/cat`
- +50.592 ms pid 7387 (bash) executed `/usr/bin/rm`

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario02/fake_passwd_entry` first touched +36.975 ms by pid 7382 (bash), created/truncated; 1 write call(s), 43 byte(s)

## 5. Permission changes

None observed.

## 6. Deletions

- +15.401 ms pid 7383 (rm) deleted `/tmp/ft_scenario02`
- +56.758 ms pid 7387 (rm) deleted `/tmp/ft_scenario02/fake_passwd_entry`

## 7. Access to sensitive resources

- +34.710 ms pid 7385 (cat) `openat` on `/etc/shadow` — **attempt failed** (access denied or missing)

## 8. Provenance of files executed from temporary directories

None.

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7382 | ? | execve | `/usr/bin/bash` |
| 15 | 1.474 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.515 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.693 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.730 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.805 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.846 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.923 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.956 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.030 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.063 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.141 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 2.198 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.397 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 2.461 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 2.513 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 2.595 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 2.631 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.834 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.887 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 2.970 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.005 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 3.078 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 3.111 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 3.187 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 3.220 | 7382 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 5.025 | 7382 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario02_privilege_escalation.sh` |
| 71 | 8.186 | 7382 | bash | clone | `` |
| 73 | 8.645 | 7383 | bash | execve | `/usr/bin/rm` |
| 83 | 10.748 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 10.814 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 11.246 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 11.295 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 11.415 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 11.468 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 11.617 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 11.672 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 11.796 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 12.209 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 12.338 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 12.391 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 12.539 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 12.581 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 12.643 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 12.733 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 12.775 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 13.014 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 14.082 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 14.272 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 14.315 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 14.435 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 14.484 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 14.589 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 14.636 | 7383 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 15.150 | 7383 | rm | openat | `/tmp/ft_scenario02` |
| 138 | 15.401 | 7383 | rm | unlinkat | `/tmp/ft_scenario02` |
| 142 | 15.596 | 7383 | rm | exit_group | `code=0` |
| 143 | 17.656 | 7382 | bash | clone | `` |
| 145 | 19.311 | 7384 | bash | execve | `/usr/bin/mkdir` |
| 165 | 21.739 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 167 | 21.788 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 171 | 22.061 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 173 | 22.107 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 175 | 22.212 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 177 | 22.305 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 179 | 22.408 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 181 | 22.451 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 183 | 22.548 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 185 | 22.591 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 187 | 22.689 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 189 | 22.734 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 191 | 22.848 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 193 | 22.894 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 195 | 22.958 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 197 | 23.055 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 199 | 23.100 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 201 | 23.194 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 203 | 23.239 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 205 | 23.343 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 207 | 23.387 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 209 | 23.485 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 211 | 23.528 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 213 | 23.626 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 215 | 23.668 | 7384 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 219 | 24.037 | 7384 | mkdir | exit_group | `code=0` |
| 221 | 29.126 | 7382 | bash | clone | `` |
| 225 | 29.958 | 7385 | bash | execve | `/usr/bin/cat` |
| 235 | 32.123 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 237 | 32.184 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 241 | 32.477 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 243 | 32.539 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 245 | 32.666 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 247 | 32.720 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 249 | 32.878 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 251 | 32.935 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 253 | 33.068 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 255 | 33.126 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 257 | 33.255 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 259 | 33.314 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 261 | 33.455 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 263 | 33.515 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 265 | 33.602 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 267 | 33.775 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 269 | 33.851 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 271 | 33.978 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 273 | 34.035 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 275 | 34.161 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 277 | 34.210 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 279 | 34.327 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 281 | 34.379 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 283 | 34.498 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 285 | 34.554 | 7385 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 287 | 34.710 | 7385 | cat | openat | `/etc/shadow` (failed) |
| 306 | 35.354 | 7385 | cat | exit_group | `code=1` |
| 308 | 36.975 | 7382 | bash | openat | `/tmp/ft_scenario02/fake_passwd_entry` |
| 310 | 37.242 | 7382 | bash | write | `/tmp/ft_scenario02/fake_passwd_entry` |
| 312 | 37.461 | 7382 | bash | clone | `` |
| 314 | 38.043 | 7386 | bash | execve | `/usr/bin/cat` |
| 324 | 40.084 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 326 | 40.151 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 330 | 40.430 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 332 | 40.488 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 334 | 40.861 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 336 | 44.941 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 338 | 45.386 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 340 | 45.447 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 342 | 45.570 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 344 | 45.624 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 346 | 45.748 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 348 | 45.802 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 350 | 45.959 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 352 | 46.054 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 354 | 46.141 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 356 | 46.298 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 358 | 46.375 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 360 | 46.539 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 362 | 46.635 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 364 | 46.821 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 366 | 46.914 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 368 | 47.046 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 370 | 47.124 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 372 | 47.283 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 374 | 47.366 | 7386 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 376 | 47.594 | 7386 | cat | openat | `/tmp/ft_scenario02/fake_passwd_entry` |
| 383 | 48.454 | 7386 | cat | exit_group | `code=0` |
| 385 | 50.037 | 7382 | bash | clone | `` |
| 387 | 50.592 | 7387 | bash | execve | `/usr/bin/rm` |
| 397 | 53.637 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 399 | 53.719 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 403 | 54.695 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 405 | 54.775 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 407 | 54.947 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 409 | 55.014 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 411 | 55.167 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 413 | 55.221 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 415 | 55.344 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 417 | 55.396 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 419 | 55.513 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 421 | 55.562 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 423 | 55.693 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 425 | 55.744 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 427 | 55.816 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 429 | 55.940 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 431 | 55.990 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 433 | 56.120 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 435 | 56.173 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 437 | 56.299 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 439 | 56.342 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 441 | 56.438 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 443 | 56.480 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 445 | 56.574 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 447 | 56.618 | 7387 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 449 | 56.758 | 7387 | rm | unlinkat | `/tmp/ft_scenario02/fake_passwd_entry` |
| 453 | 56.954 | 7387 | rm | exit_group | `code=0` |
| 455 | 57.320 | 7382 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 22.417 ms |
| Workload CPU (user+sys) | 17.827 ms |
| Tracer peak memory | 29588 KiB |
| Processing time (normalise+correlate+reconstruct) | 0.454 ms |
| Evidence size | 171208 bytes |

