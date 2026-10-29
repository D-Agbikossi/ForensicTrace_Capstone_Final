# ForensicTrace incident report

| | |
|---|---|
| Scenario | scenario03 |
| Command | `bash /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| Evidence configuration | B |
| Events recorded | 1139 |
| Failed exec attempts removed | 12 |
| Duration | 537.171 ms |
| Evidence file | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_B_r2.json` (423005 bytes) |
| SHA-256 | `baf209726df70c339f65b0b6f9df074aac9e5f3b7830cf7dc247cc98a83dc419` |

Verify integrity: `sha256sum -c /home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/experiments/runs_seccomp/scenario03_B_r2.json.sha256`

## 1. Process tree

- `8235` /usr/bin/bash
  - `8236` /usr/bin/rm
  - `8237` /usr/bin/mkdir
  - `8238` /usr/bin/python3
  - `8239` /usr/bin/sleep
  - `8241` /usr/bin/curl
  - `8242` /usr/bin/python3
  - `8243` /usr/bin/cat
  - `8244` /usr/bin/chmod
  - `8245` /tmp/ft_scenario03/runme.sh

10 process(es) observed.

## 2. Programs executed

- +0.000 ms pid 8235 (?) executed `/usr/bin/bash`
- +3.517 ms pid 8236 (bash) executed `/usr/bin/rm`
- +7.660 ms pid 8237 (bash) executed `/usr/bin/mkdir`
- +10.661 ms pid 8239 (bash) executed `/usr/bin/sleep`
- +10.787 ms pid 8238 (bash) executed `/usr/bin/python3`
- +514.649 ms pid 8241 (bash) executed `/usr/bin/curl`
- +529.016 ms pid 8243 (bash) executed `/usr/bin/cat`
- +531.607 ms pid 8244 (bash) executed `/usr/bin/chmod`
- +534.209 ms pid 8245 (bash) executed `/tmp/ft_scenario03/runme.sh` **(from a temporary directory)**

## 3. Network activity

Not available: configuration B does not record network events.

## 4. Files created or modified

- `/tmp/ft_scenario03/served.txt` first touched +10.097 ms by pid 8235 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/fetched.txt` first touched +514.473 ms by pid 8241 (bash), created/truncated; 1 write call(s), 18 byte(s)
- `/tmp/ft_scenario03/runme.sh` first touched +528.874 ms by pid 8243 (bash), created/truncated; 1 write call(s), 42 byte(s)

## 5. Permission changes

- +533.767 ms pid 8244 (chmod) changed permissions of `/tmp/ft_scenario03/runme.sh` (dirfd=-100 mode=0775 raw=runme.sh)

## 6. Deletions

- +6.906 ms pid 8236 (rm) deleted `/tmp/ft_scenario03/fetched.txt`
- +6.963 ms pid 8236 (rm) deleted `/tmp/ft_scenario03/runme.sh`
- +6.999 ms pid 8236 (rm) deleted `/tmp/ft_scenario03/served.txt`
- +7.054 ms pid 8236 (rm) deleted `/tmp/ft_scenario03`

## 7. Access to sensitive resources

- +524.539 ms pid 8241 (curl) `openat` on `/etc/passwd`

## 8. Provenance of files executed from temporary directories

- +534.209 ms `/tmp/ft_scenario03/runme.sh` executed by pid 8245 (bash)
  - history of `/tmp/ft_scenario03/runme.sh`:
    - +6.963 ms #138 `unlinkat` by pid 8236 (rm)
    - +528.874 ms #973 `openat` by pid 8243 (bash)
    - +528.934 ms #974 `close` by pid 8243 (bash)
    - +531.130 ms #1041 `write` by pid 8243 (cat)
    - +531.222 ms #1044 `close` by pid 8243 (cat)
    - +533.767 ms #1112 `fchmodat` by pid 8244 (chmod)
    - +534.209 ms #1119 `execve` by pid 8245 (bash)

## 9. Notable timeline

Process, network, open/write/delete/chmod events; loader, locale, pipe and
read/close noise is omitted (full timeline: JSON file).

| # | +ms | PID | Actor | Syscall | Target |
|---|---|---|---|---|---|
| 1 | 0.000 | 8235 | ? | execve | `/usr/bin/bash` |
| 15 | 1.232 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 17 | 1.278 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 21 | 1.398 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 23 | 1.441 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 25 | 1.502 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 27 | 1.546 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 29 | 1.608 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 31 | 1.651 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 33 | 1.735 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 35 | 1.792 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 37 | 1.867 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 39 | 1.922 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 41 | 2.004 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 43 | 2.062 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 45 | 2.120 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 47 | 2.191 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 49 | 2.240 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 51 | 2.300 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 53 | 2.346 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 55 | 2.415 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 57 | 2.462 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 59 | 2.522 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 61 | 2.566 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 63 | 2.631 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 65 | 2.680 | 8235 | bash | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 67 | 3.017 | 8235 | bash | openat | `/home/denaton-agbikossi/Documents/ForensicTrace_Capstone_Final/forensictrace/scenarios/scenario03_network_payload.sh` |
| 71 | 3.254 | 8235 | bash | clone | `` |
| 73 | 3.517 | 8236 | bash | execve | `/usr/bin/rm` |
| 83 | 4.295 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 85 | 4.511 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 89 | 4.775 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 91 | 4.842 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 93 | 5.121 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 95 | 5.171 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 97 | 5.305 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 99 | 5.367 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 101 | 5.457 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 103 | 5.512 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 105 | 5.579 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 107 | 5.632 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 109 | 5.711 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 111 | 5.956 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 113 | 6.117 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 115 | 6.221 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 117 | 6.274 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 119 | 6.382 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 121 | 6.427 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 123 | 6.496 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 125 | 6.540 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 127 | 6.601 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 129 | 6.647 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 131 | 6.706 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 133 | 6.762 | 8236 | rm | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 135 | 6.832 | 8236 | rm | openat | `/tmp/ft_scenario03` |
| 137 | 6.906 | 8236 | rm | unlinkat | `/tmp/ft_scenario03/fetched.txt` |
| 138 | 6.963 | 8236 | rm | unlinkat | `/tmp/ft_scenario03/runme.sh` |
| 139 | 6.999 | 8236 | rm | unlinkat | `/tmp/ft_scenario03/served.txt` |
| 141 | 7.054 | 8236 | rm | unlinkat | `/tmp/ft_scenario03` |
| 145 | 7.192 | 8236 | rm | exit_group | `code=0` |
| 146 | 7.427 | 8235 | bash | clone | `` |
| 148 | 7.660 | 8237 | bash | execve | `/usr/bin/mkdir` |
| 168 | 8.727 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 170 | 8.767 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 174 | 8.861 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 176 | 8.895 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 178 | 8.941 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 180 | 8.976 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 182 | 9.023 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 184 | 9.056 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 186 | 9.102 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 188 | 9.135 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 190 | 9.182 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 192 | 9.216 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 194 | 9.270 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 196 | 9.304 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 198 | 9.339 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 200 | 9.392 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 202 | 9.432 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 204 | 9.486 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 206 | 9.522 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 208 | 9.574 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 210 | 9.609 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 212 | 9.656 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 214 | 9.689 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 216 | 9.741 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 218 | 9.775 | 8237 | mkdir | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 222 | 9.920 | 8237 | mkdir | exit_group | `code=0` |
| 224 | 10.097 | 8235 | bash | openat | `/tmp/ft_scenario03/served.txt` |
| 226 | 10.177 | 8235 | bash | write | `/tmp/ft_scenario03/served.txt` |
| 228 | 10.247 | 8235 | bash | clone | `` |
| 231 | 10.460 | 8235 | bash | clone | `` |
| 234 | 10.661 | 8239 | bash | execve | `/usr/bin/sleep` |
| 238 | 10.787 | 8238 | bash | execve | `/usr/bin/python3` |
| 257 | 11.376 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 260 | 11.426 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 267 | 11.548 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 270 | 11.599 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 272 | 11.662 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 274 | 11.709 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 276 | 11.777 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 278 | 11.822 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 282 | 11.887 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 285 | 11.936 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 288 | 11.990 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 289 | 12.000 | 8238 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 292 | 12.040 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 293 | 12.058 | 8238 | python3 | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 296 | 12.107 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 299 | 12.152 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 302 | 12.197 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 304 | 12.252 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 306 | 12.300 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 308 | 12.364 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 310 | 12.413 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 312 | 12.481 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 314 | 12.528 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 316 | 12.589 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 318 | 12.636 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 320 | 12.698 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 322 | 12.754 | 8239 | sleep | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 337 | 14.817 | 8238 | python3 | openat | `/usr/pyvenv.cfg` (failed) |
| 338 | 14.870 | 8238 | python3 | openat | `/usr/bin/pyvenv.cfg` (failed) |
| 339 | 14.918 | 8238 | python3 | openat | `/usr/bin/python3._pth` (failed) |
| 340 | 14.945 | 8238 | python3 | openat | `/usr/bin/python3.12._pth` (failed) |
| 341 | 14.971 | 8238 | python3 | openat | `/usr/bin/pybuilddir.txt` (failed) |
| 342 | 15.793 | 8238 | python3 | openat | `/etc/localtime` |
| 362 | 19.016 | 8238 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 364 | 19.133 | 8238 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/easy-install.pth` |
| 368 | 19.304 | 8238 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 376 | 20.086 | 8238 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages` |
| 378 | 20.181 | 8238 | python3 | openat | `/home/denaton-agbikossi/.local/lib/python3.12/site-packages/stats_c-1.0-py3.12-linux-x86_64.egg` |
| 380 | 20.254 | 8238 | python3 | openat | `/usr/local/lib/python3.12/dist-packages` |
| 452 | 26.755 | 8238 | python3 | openat | `/tmp/ft_scenario03` |
| 722 | 62.196 | 8238 | python3 | openat | `/etc/gai.conf` |
| 738 | 63.811 | 8238 | python3 | openat | `/etc/nsswitch.conf` |
| 742 | 63.941 | 8238 | python3 | openat | `/etc/host.conf` |
| 746 | 64.046 | 8238 | python3 | openat | `/etc/resolv.conf` |
| 750 | 64.151 | 8238 | python3 | openat | `/etc/hosts` |
| 754 | 64.270 | 8238 | python3 | openat | `/etc/hosts` |
| 759 | 513.462 | 8239 | sleep | exit_group | `code=0` |
| 761 | 513.949 | 8235 | bash | clone | `` |
| 763 | 514.473 | 8241 | bash | openat | `/tmp/ft_scenario03/fetched.txt` |
| 765 | 514.649 | 8241 | bash | execve | `/usr/bin/curl` |
| 861 | 521.797 | 8241 | curl | openat | `/etc/gnutls/config` |
| 879 | 523.063 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 881 | 523.115 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 885 | 523.253 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 887 | 523.301 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 889 | 523.366 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 891 | 523.414 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 893 | 523.476 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 895 | 523.524 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 897 | 523.587 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 899 | 523.636 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 901 | 523.684 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 903 | 523.718 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 905 | 523.789 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 907 | 523.824 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 909 | 523.861 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 911 | 523.915 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 913 | 523.949 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 915 | 523.997 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 917 | 524.032 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 919 | 524.085 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 921 | 524.121 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 923 | 524.168 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 925 | 524.203 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 927 | 524.251 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 929 | 524.286 | 8241 | curl | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 931 | 524.338 | 8241 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 932 | 524.358 | 8241 | curl | openat | `/home/denaton-agbikossi/.config/curlrc` (failed) |
| 935 | 524.454 | 8241 | curl | openat | `/etc/nsswitch.conf` |
| 939 | 524.539 | 8241 | curl | openat | `/etc/passwd` |
| 942 | 524.601 | 8241 | curl | openat | `/home/denaton-agbikossi/.curlrc` (failed) |
| 943 | 524.952 | 8238 | python3 | clone3 | `` |
| 944 | 525.336 | 8242 | python3 | openat | `/etc/mime.types` |
| 957 | 527.467 | 8242 | python3 | openat | `/tmp/ft_scenario03/served.txt` |
| 964 | 527.821 | 8241 | curl | write | `/tmp/ft_scenario03/fetched.txt` |
| 968 | 527.939 | 8242 | python3 | exit | `code=0` |
| 969 | 528.097 | 8241 | curl | exit_group | `code=0` |
| 971 | 528.649 | 8235 | bash | clone | `` |
| 973 | 528.874 | 8243 | bash | openat | `/tmp/ft_scenario03/runme.sh` |
| 978 | 529.016 | 8243 | bash | execve | `/usr/bin/cat` |
| 988 | 529.658 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 990 | 529.698 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 994 | 529.843 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 996 | 529.890 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 998 | 529.952 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1000 | 530.000 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1002 | 530.059 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1004 | 530.107 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1006 | 530.165 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1008 | 530.213 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1010 | 530.272 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1012 | 530.317 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1014 | 530.387 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1016 | 530.433 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1018 | 530.482 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1020 | 530.544 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1022 | 530.590 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1024 | 530.652 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1026 | 530.697 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1028 | 530.770 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1030 | 530.818 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1032 | 530.877 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1034 | 530.925 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1036 | 530.985 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1038 | 531.032 | 8243 | cat | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1041 | 531.130 | 8243 | cat | write | `/tmp/ft_scenario03/runme.sh` |
| 1046 | 531.274 | 8243 | cat | exit_group | `code=0` |
| 1048 | 531.457 | 8235 | bash | clone | `` |
| 1050 | 531.607 | 8244 | bash | execve | `/usr/bin/chmod` |
| 1060 | 532.186 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_IDENTIFICATION` (failed) |
| 1062 | 532.223 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_IDENTIFICATION` |
| 1066 | 532.319 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MEASUREMENT` (failed) |
| 1068 | 532.355 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MEASUREMENT` |
| 1070 | 532.403 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TELEPHONE` (failed) |
| 1072 | 532.438 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TELEPHONE` |
| 1074 | 532.488 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_ADDRESS` (failed) |
| 1076 | 532.523 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_ADDRESS` |
| 1078 | 532.577 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NAME` (failed) |
| 1080 | 532.619 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NAME` |
| 1082 | 532.672 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_PAPER` (failed) |
| 1084 | 532.715 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_PAPER` |
| 1086 | 532.825 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MESSAGES` (failed) |
| 1088 | 532.967 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES` |
| 1090 | 533.025 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MESSAGES/SYS_LC_MESSAGES` |
| 1092 | 533.113 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_MONETARY` (failed) |
| 1094 | 533.172 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_MONETARY` |
| 1096 | 533.245 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_COLLATE` (failed) |
| 1098 | 533.301 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_COLLATE` |
| 1100 | 533.378 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_TIME` (failed) |
| 1102 | 533.431 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_TIME` |
| 1104 | 533.502 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_NUMERIC` (failed) |
| 1106 | 533.555 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_NUMERIC` |
| 1108 | 533.627 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.UTF-8/LC_CTYPE` (failed) |
| 1110 | 533.683 | 8244 | chmod | openat | `/snap/code/266/usr/lib/locale/en_US.utf8/LC_CTYPE` |
| 1112 | 533.767 | 8244 | chmod | fchmodat | `/tmp/ft_scenario03/runme.sh` |
| 1115 | 533.873 | 8244 | chmod | exit_group | `code=0` |
| 1117 | 534.033 | 8235 | bash | clone | `` |
| 1119 | 534.209 | 8245 | bash | execve | `/tmp/ft_scenario03/runme.sh` |
| 1125 | 534.767 | 8245 | runme.sh | openat | `/tmp/ft_scenario03/runme.sh` |
| 1130 | 534.905 | 8245 | runme.sh | exit_group | `code=0` |
| 1139 | 536.449 | 8235 | bash | exit_group | `code=0` |

## 10. Collection cost

| Metric | Value |
|---|---|
| Tracer CPU (user+sys) | 23.739 ms |
| Workload CPU (user+sys) | 66.546 ms |
| Tracer peak memory | 29404 KiB |
| Processing time (normalise+correlate+reconstruct) | 1.454 ms |
| Evidence size | 423005 bytes |

