# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | B |
| Events recorded | 1139 |
| Failed exec attempts removed | 12 |
| Duration | 555.972 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_B_r3.json` (423005 bytes) |
| SHA-256 | `831591fb4853da6df67675fc9b17823cce9755f5340b0f301f786ff81c85d84d` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs/scenario03_B_r3.json.sha256`

## 1. Process tree

- `7628` /usr/bin/bash
  - `7629` /usr/bin/rm
  - `7630` /usr/bin/mkdir
  - `7631` /usr/bin/python3
  - `7632` /usr/bin/sleep
  - `7634` /usr/bin/curl
  - `7635` /usr/bin/python3
  - `7636` /usr/bin/cat
  - `7637` /usr/bin/chmod
  - `7638` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 7628 (?) executed `/usr/bin/bash`
- +6.077 ms pid 7629 (bash) executed `/usr/bin/rm`
- +10.117 ms pid 7630 (bash) executed `/usr/bin/mkdir`
- +17.553 ms pid 7632 (bash) executed `/usr/bin/sleep`
- +17.642 ms pid 7631 (bash) executed `/usr/bin/python3`
- +526.604 ms pid 7634 (bash) executed `/usr/bin/curl`
- +545.203 ms pid 7636 (bash) executed `/usr/bin/cat`
- +549.012 ms pid 7637 (bash) executed `/usr/bin/chmod`
- +552.389 ms pid 7638 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +15.197 ms by pid 7628 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +526.489 ms by pid 7634 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +545.004 ms by pid 7636 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +551.736 ms pid 7637 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +8.816 ms pid 7629 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +8.861 ms pid 7629 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +8.888 ms pid 7629 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +8.930 ms pid 7629 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +538.198 ms pid 7634 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +552.389 ms `/tmp/ft_scenario03/runme.sh` executed by pid 7638 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +8.861 ms #138 `unlinkat` by pid 7629 (rm)
    - +545.004 ms #973 `openat` by pid 7636 (bash)
    - +545.084 ms #974 `close` by pid 7636 (bash)
    - +547.805 ms #1041 `write` by pid 7636 (cat)
    - +547.892 ms #1044 `close` by pid 7636 (cat)
    - +551.736 ms #1112 `fchmodat` by pid 7637 (chmod)
    - +552.389 ms #1119 `execve` by pid 7638 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 7628 | ? | execve | `/usr/bin/bash` |
| 15 | 1.526 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.571 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.898 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.941 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 2.033 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 2.076 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 2.166 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 2.207 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 2.297 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 2.337 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 2.428 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 2.470 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.571 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 2.614 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 2.673 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 2.768 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 2.810 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.899 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.941 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 3.040 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 3.083 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 3.173 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 3.214 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 3.307 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 3.348 | 7628 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 4.859 | 7628 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 5.612 | 7628 | bash | clone | `` |
| 73 | 6.077 | 7629 | bash | execve | `/usr/bin/rm` |
| 83 | 7.081 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 7.117 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 7.280 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 7.313 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 7.389 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 7.422 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 7.496 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 7.530 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 7.603 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 7.637 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 7.714 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 7.749 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 7.833 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 7.867 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 7.918 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 8.048 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 8.085 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 8.162 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 8.195 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 8.277 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 8.310 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 8.384 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 8.418 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 8.492 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 8.527 | 7629 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 8.652 | 7629 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 8.816 | 7629 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 8.861 | 7629 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 8.888 | 7629 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 8.930 | 7629 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 9.102 | 7629 | rm | exit_group | `code=0` |
| 146 | 9.758 | 7628 | bash | clone | `` |
| 148 | 10.117 | 7630 | bash | execve | `/usr/bin/mkdir` |
| 168 | 12.223 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 12.274 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 12.504 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 12.551 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 12.710 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 12.764 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 12.883 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 12.935 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 13.066 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 13.119 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 13.224 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 13.270 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 13.385 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 13.432 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 13.501 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 13.596 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 13.644 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 13.797 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 13.847 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 13.950 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 13.997 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 14.098 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 14.142 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 14.244 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 14.290 | 7630 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 14.671 | 7630 | mkdir | exit_group | `code=0` |
| 224 | 15.197 | 7628 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 15.426 | 7628 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 15.604 | 7628 | bash | clone | `` |
| 231 | 16.959 | 7628 | bash | clone | `` |
| 236 | 17.553 | 7632 | bash | execve | `/usr/bin/sleep` |
| 238 | 17.642 | 7631 | bash | execve | `/usr/bin/python3` |
| 261 | 19.965 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 263 | 20.029 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 268 | 20.292 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 20.345 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 20.468 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 20.518 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 20.637 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 278 | 20.686 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 280 | 20.799 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 282 | 20.857 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 286 | 20.970 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 289 | 21.022 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 291 | 21.082 | 7631 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 294 | 21.210 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 295 | 21.228 | 7631 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 297 | 21.289 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 300 | 21.385 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 303 | 21.524 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 21.596 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 21.722 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 21.780 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 21.924 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 21.974 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 22.080 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 22.137 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 22.256 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 22.317 | 7632 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 25.507 | 7631 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 25.546 | 7631 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 25.638 | 7631 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 25.662 | 7631 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 25.684 | 7631 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 26.838 | 7631 | python3 | openat | `/etc/localtime` |
| 362 | 33.301 | 7631 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 33.524 | 7631 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 33.831 | 7631 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 35.294 | 7631 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 35.511 | 7631 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 35.735 | 7631 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 45.987 | 7631 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 98.393 | 7631 | python3 | openat | `/etc/gai.conf` |
| 738 | 100.592 | 7631 | python3 | openat | `/etc/nsswitch.conf` |
| 742 | 100.761 | 7631 | python3 | openat | `/etc/host.conf` |
| 746 | 100.884 | 7631 | python3 | openat | `/etc/resolv.conf` |
| 750 | 101.014 | 7631 | python3 | openat | `/etc/hosts` |
| 754 | 101.183 | 7631 | python3 | openat | `/etc/hosts` |
| 759 | 523.520 | 7632 | sleep | exit_group | `code=0` |
| 761 | 525.986 | 7628 | bash | clone | `` |
| 763 | 526.489 | 7634 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 765 | 526.604 | 7634 | bash | execve | `/usr/bin/curl` |
| 861 | 534.919 | 7634 | curl | openat | `/etc/gnutls/config` |
| 879 | 536.380 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 881 | 536.420 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 885 | 536.586 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 887 | 536.621 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 889 | 536.702 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 891 | 536.738 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 893 | 536.810 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 895 | 536.845 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 897 | 536.918 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 899 | 536.951 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 901 | 537.025 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 903 | 537.058 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 905 | 537.141 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 907 | 537.175 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 909 | 537.225 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 911 | 537.300 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 913 | 537.333 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 915 | 537.414 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 917 | 537.449 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 919 | 537.525 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 921 | 537.560 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 923 | 537.633 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 925 | 537.668 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 927 | 537.754 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 929 | 537.788 | 7634 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 931 | 537.867 | 7634 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 932 | 537.886 | 7634 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 935 | 538.085 | 7634 | curl | openat | `/etc/nsswitch.conf` |
| 939 | 538.198 | 7634 | curl | openat | `/etc/passwd` |
| 942 | 538.286 | 7634 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 943 | 539.175 | 7631 | python3 | clone3 | `` |
| 944 | 539.858 | 7635 | python3 | openat | `/etc/mime.types` |
| 957 | 542.249 | 7635 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 965 | 542.741 | 7634 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 966 | 542.827 | 7635 | python3 | exit | `code=0` |
| 969 | 543.271 | 7634 | curl | exit_group | `code=0` |
| 971 | 544.446 | 7628 | bash | clone | `` |
| 973 | 545.004 | 7636 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 978 | 545.203 | 7636 | bash | execve | `/usr/bin/cat` |
| 988 | 546.243 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 990 | 546.282 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 994 | 546.448 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 996 | 546.481 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 998 | 546.556 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1000 | 546.590 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1002 | 546.662 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1004 | 546.706 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1006 | 546.780 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1008 | 546.814 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1010 | 546.887 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1012 | 546.920 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1014 | 547.003 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1016 | 547.035 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1018 | 547.086 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1020 | 547.161 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1022 | 547.195 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1024 | 547.275 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1026 | 547.307 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1028 | 547.389 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1030 | 547.424 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1032 | 547.496 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1034 | 547.530 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1036 | 547.610 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 547.644 | 7636 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 547.805 | 7636 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1046 | 547.931 | 7636 | cat | exit_group | `code=0` |
| 1048 | 548.635 | 7628 | bash | clone | `` |
| 1050 | 549.012 | 7637 | bash | execve | `/usr/bin/chmod` |
| 1060 | 550.160 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1062 | 550.202 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1066 | 550.395 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1068 | 550.443 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1070 | 550.532 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1072 | 550.566 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1074 | 550.640 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1076 | 550.673 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1078 | 550.754 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1080 | 550.789 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1082 | 550.860 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1084 | 550.894 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1086 | 550.975 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1088 | 551.009 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1090 | 551.061 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1092 | 551.134 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1094 | 551.169 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1096 | 551.248 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1098 | 551.283 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1100 | 551.363 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1102 | 551.396 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1104 | 551.469 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1106 | 551.503 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1108 | 551.577 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1110 | 551.612 | 7637 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1112 | 551.736 | 7637 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1115 | 551.819 | 7637 | chmod | exit_group | `code=0` |
| 1117 | 552.065 | 7628 | bash | clone | `` |
| 1119 | 552.389 | 7638 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1125 | 553.351 | 7638 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 553.597 | 7638 | runme.sh | exit_group | `code=0` |
| 1139 | 555.377 | 7628 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 52.770 ms |
| Workload CPU (user+sys) | 80.184 ms |
| Tracer peak memory | 30168 KiB |
| Processing time (normalise+correlate+reconstruct) | 2.443 ms |
| Evidence size | 423005 bytes |

