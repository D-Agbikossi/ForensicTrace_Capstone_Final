# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | B |
| Events recorded | 1139 |
| Failed exec attempts removed | 12 |
| Duration | 542.317 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_B_r1.json` (423005 bytes) |
| SHA-256 | `4eadfc1ef86c36d2ea31ec29cb62bdc7868a40cab4e387086cb5ce5aa2ead266` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_B_r1.json.sha256`

## 1. Process tree

- `8007` /usr/bin/bash
  - `8008` /usr/bin/rm
  - `8009` /usr/bin/mkdir
  - `8010` /usr/bin/python3
  - `8011` /usr/bin/sleep
  - `8014` /usr/bin/curl
  - `8015` /usr/bin/python3
  - `8016` /usr/bin/cat
  - `8017` /usr/bin/chmod
  - `8018` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8007 (?) executed `/usr/bin/bash`
- +2.874 ms pid 8008 (bash) executed `/usr/bin/rm`
- +5.593 ms pid 8009 (bash) executed `/usr/bin/mkdir`
- +9.002 ms pid 8011 (bash) executed `/usr/bin/sleep`
- +9.031 ms pid 8010 (bash) executed `/usr/bin/python3`
- +513.627 ms pid 8014 (bash) executed `/usr/bin/curl`
- +535.493 ms pid 8016 (bash) executed `/usr/bin/cat`
- +537.716 ms pid 8017 (bash) executed `/usr/bin/chmod`
- +539.831 ms pid 8018 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +8.519 ms by pid 8007 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +513.440 ms by pid 8014 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +535.355 ms by pid 8016 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +539.440 ms pid 8017 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +4.990 ms pid 8008 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +5.051 ms pid 8008 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +5.088 ms pid 8008 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +5.144 ms pid 8008 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +530.891 ms pid 8014 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +539.831 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8018 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +5.051 ms #138 `unlinkat` by pid 8008 (rm)
    - +535.355 ms #973 `openat` by pid 8016 (bash)
    - +535.415 ms #974 `close` by pid 8016 (bash)
    - +537.289 ms #1041 `write` by pid 8016 (cat)
    - +537.362 ms #1044 `close` by pid 8016 (cat)
    - +539.440 ms #1112 `fchmodat` by pid 8017 (chmod)
    - +539.831 ms #1119 `execve` by pid 8018 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8007 | ? | execve | `/usr/bin/bash` |
| 15 | 0.945 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 0.993 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.114 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.159 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.217 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.262 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.321 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.364 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.422 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.465 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.523 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.568 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 1.690 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 1.744 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 1.790 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 1.875 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 1.912 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 1.960 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 1.994 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 2.066 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 2.103 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 2.151 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.184 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.238 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.271 | 8007 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 2.531 | 8007 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 2.699 | 8007 | bash | clone | `` |
| 73 | 2.874 | 8008 | bash | execve | `/usr/bin/rm` |
| 83 | 3.518 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 3.564 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 3.682 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 3.726 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 3.789 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 3.832 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 3.891 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 3.937 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 3.993 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 4.063 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 4.121 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 4.166 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 4.234 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 4.278 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 4.330 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 4.387 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 4.433 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 4.492 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 4.535 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 4.600 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 4.643 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 4.701 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 4.746 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 4.803 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 4.848 | 8008 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 4.916 | 8008 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 4.990 | 8008 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 5.051 | 8008 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 5.088 | 8008 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 5.144 | 8008 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 5.283 | 8008 | rm | exit_group | `code=0` |
| 146 | 5.424 | 8007 | bash | clone | `` |
| 148 | 5.593 | 8009 | bash | execve | `/usr/bin/mkdir` |
| 168 | 6.639 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 6.687 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 6.833 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 7.009 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 7.096 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 7.146 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 7.209 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 7.254 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 7.313 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 7.358 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 7.418 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 7.464 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 7.532 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 7.578 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 7.625 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 7.686 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 7.732 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 7.787 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 7.833 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 7.894 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 7.939 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 7.996 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 8.052 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 8.112 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 8.156 | 8009 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 8.333 | 8009 | mkdir | exit_group | `code=0` |
| 224 | 8.519 | 8007 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 8.581 | 8007 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 8.639 | 8007 | bash | clone | `` |
| 231 | 8.834 | 8007 | bash | clone | `` |
| 236 | 9.002 | 8011 | bash | execve | `/usr/bin/sleep` |
| 238 | 9.031 | 8010 | bash | execve | `/usr/bin/python3` |
| 261 | 9.767 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 264 | 9.817 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 9.929 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 9.975 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 273 | 10.056 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 276 | 10.108 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 280 | 10.179 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 281 | 10.188 | 8010 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 284 | 10.235 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 285 | 10.252 | 8010 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 288 | 10.297 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 292 | 10.354 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 294 | 10.408 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 296 | 10.543 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 298 | 10.616 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 300 | 10.663 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 302 | 10.710 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 10.768 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 10.814 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 10.872 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 10.918 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 10.981 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 11.025 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 11.092 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 11.135 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 11.198 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 11.243 | 8011 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 12.749 | 8010 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 12.785 | 8010 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 12.822 | 8010 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 12.845 | 8010 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 12.869 | 8010 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 13.687 | 8010 | python3 | openat | `/etc/localtime` |
| 362 | 16.609 | 8010 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 16.696 | 8010 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 16.829 | 8010 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 17.535 | 8010 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 17.611 | 8010 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 17.669 | 8010 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 26.074 | 8010 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 60.526 | 8010 | python3 | openat | `/etc/gai.conf` |
| 738 | 62.132 | 8010 | python3 | openat | `/etc/nsswitch.conf` |
| 742 | 62.242 | 8010 | python3 | openat | `/etc/host.conf` |
| 746 | 62.335 | 8010 | python3 | openat | `/etc/resolv.conf` |
| 750 | 62.435 | 8010 | python3 | openat | `/etc/hosts` |
| 754 | 62.539 | 8010 | python3 | openat | `/etc/hosts` |
| 759 | 512.308 | 8011 | sleep | exit_group | `code=0` |
| 761 | 512.943 | 8007 | bash | clone | `` |
| 763 | 513.440 | 8014 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 765 | 513.627 | 8014 | bash | execve | `/usr/bin/curl` |
| 861 | 525.275 | 8014 | curl | openat | `/etc/gnutls/config` |
| 879 | 527.988 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 881 | 528.130 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 885 | 528.517 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 887 | 528.788 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 889 | 529.334 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 891 | 529.407 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 893 | 529.490 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 895 | 529.544 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 897 | 529.610 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 899 | 529.658 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 901 | 529.722 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 903 | 529.773 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 905 | 529.854 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 907 | 529.901 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 909 | 530.046 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 911 | 530.139 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 913 | 530.185 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 915 | 530.247 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 917 | 530.289 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 919 | 530.349 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 921 | 530.391 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 923 | 530.444 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 925 | 530.487 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 927 | 530.549 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 929 | 530.590 | 8014 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 931 | 530.655 | 8014 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 932 | 530.680 | 8014 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 935 | 530.788 | 8014 | curl | openat | `/etc/nsswitch.conf` |
| 939 | 530.891 | 8014 | curl | openat | `/etc/passwd` |
| 942 | 530.965 | 8014 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 943 | 531.330 | 8010 | python3 | clone3 | `` |
| 944 | 531.752 | 8015 | python3 | openat | `/etc/mime.types` |
| 957 | 533.881 | 8015 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 964 | 534.207 | 8014 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 968 | 534.298 | 8015 | python3 | exit | `code=0` |
| 969 | 534.490 | 8014 | curl | exit_group | `code=0` |
| 971 | 535.086 | 8007 | bash | clone | `` |
| 973 | 535.355 | 8016 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 978 | 535.493 | 8016 | bash | execve | `/usr/bin/cat` |
| 988 | 536.160 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 990 | 536.198 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 994 | 536.304 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 996 | 536.338 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 998 | 536.388 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1000 | 536.424 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1002 | 536.470 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1004 | 536.505 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1006 | 536.551 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1008 | 536.590 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1010 | 536.635 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1012 | 536.669 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1014 | 536.725 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1016 | 536.759 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1018 | 536.797 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1020 | 536.844 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1022 | 536.879 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1024 | 536.927 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1026 | 536.961 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1028 | 537.016 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1030 | 537.055 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1032 | 537.101 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1034 | 537.135 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1036 | 537.181 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 537.215 | 8016 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 537.289 | 8016 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1046 | 537.400 | 8016 | cat | exit_group | `code=0` |
| 1048 | 537.555 | 8007 | bash | clone | `` |
| 1050 | 537.716 | 8017 | bash | execve | `/usr/bin/chmod` |
| 1060 | 538.294 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1062 | 538.330 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1066 | 538.421 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1068 | 538.455 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1070 | 538.503 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1072 | 538.536 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1074 | 538.582 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1076 | 538.616 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1078 | 538.662 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1080 | 538.696 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1082 | 538.740 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1084 | 538.774 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1086 | 538.828 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1088 | 538.867 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1090 | 538.903 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1092 | 538.949 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1094 | 538.985 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1096 | 539.033 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1098 | 539.083 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1100 | 539.148 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1102 | 539.189 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1104 | 539.242 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1106 | 539.283 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1108 | 539.337 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1110 | 539.379 | 8017 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1112 | 539.440 | 8017 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1115 | 539.550 | 8017 | chmod | exit_group | `code=0` |
| 1117 | 539.678 | 8007 | bash | clone | `` |
| 1119 | 539.831 | 8018 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1125 | 540.279 | 8018 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 540.395 | 8018 | runme.sh | exit_group | `code=0` |
| 1139 | 541.709 | 8007 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 26.034 ms |
| Workload CPU (user+sys) | 69.445 ms |
| Tracer peak memory | 29236 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.410 ms |
| Evidence size | 423005 bytes |

