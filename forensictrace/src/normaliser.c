/*
 * normaliser.c — turn raw collector events into the common event representation
 * described in the proposal (section 3.2.3):
 *
 *   1. drop failed execve/execveat calls. execvp() tries every PATH directory,
 *      so a trace starts with a burst of failed exec attempts that executed
 *      nothing and would mislead a reconstruction;
 *   2. canonicalise absolute paths (collapse //, /./ and /../);
 *   3. resolve the executable of the acting process for every event
 *      (inherited across fork/clone, replaced by a successful exec);
 *   4. annotate other failed syscalls with their errno text;
 *   5. renumber event ids so they are contiguous.
 *
 * Failed calls other than exec are KEPT: an attempt (e.g. open /etc/shadow
 * denied) is itself forensic evidence.
 */
#include "forensictrace.h"

#include <errno.h>
#include <string.h>

#define NORM_MAX_PIDS 4096

typedef struct {
    pid_t pid;
    char  exe[FT_EXE];
} PidExe;

void ft_canonicalize_path(const char *in, char *out, size_t outlen)
{
    const char *comps[128];
    size_t lens[128];
    int n = 0;
    char tmp[FT_STR];
    size_t o = 0;

    if (!out || outlen == 0) {
        return;
    }
    if (!in || in[0] != '/') {
        snprintf(out, outlen, "%s", in ? in : "");
        return;
    }

    for (const char *p = in; *p;) {
        const char *s;
        size_t l;

        while (*p == '/') {
            p++;
        }
        if (!*p) {
            break;
        }
        s = p;
        while (*p && *p != '/') {
            p++;
        }
        l = (size_t)(p - s);
        if (l == 1 && s[0] == '.') {
            continue;
        }
        if (l == 2 && s[0] == '.' && s[1] == '.') {
            if (n > 0) {
                n--;
            }
            continue;
        }
        if (n < 128) {
            comps[n] = s;
            lens[n] = l;
            n++;
        }
    }

    if (n == 0) {
        snprintf(out, outlen, "/");
        return;
    }
    for (int i = 0; i < n; i++) {
        if (o + 1 + lens[i] >= sizeof(tmp)) {
            break;
        }
        tmp[o++] = '/';
        memcpy(tmp + o, comps[i], lens[i]);
        o += lens[i];
    }
    tmp[o] = '\0';
    snprintf(out, outlen, "%s", tmp);
}

static PidExe *exe_lookup(PidExe *map, int *n, pid_t pid, pid_t inherit_from)
{
    PidExe *src = NULL;

    for (int i = 0; i < *n; i++) {
        if (map[i].pid == pid) {
            return &map[i];
        }
    }
    if (*n >= NORM_MAX_PIDS) {
        return NULL;
    }
    map[*n].pid = pid;
    map[*n].exe[0] = '\0';
    if (inherit_from > 0) {
        for (int i = 0; i < *n; i++) {
            if (map[i].pid == inherit_from) {
                src = &map[i];
                break;
            }
        }
        if (src) {
            memcpy(map[*n].exe, src->exe, sizeof(map[*n].exe));   /* distinct elements */
        }
    }
    return &map[(*n)++];
}

void ft_normalize(FTContext *c)
{
    static PidExe map[NORM_MAX_PIDS];
    int map_n = 0;
    int out = 0;

    if (!c) {
        return;
    }
    c->dropped_failed_exec = 0;

    for (int i = 0; i < c->count; i++) {
        Event e = c->events[i];
        PidExe *pe;

        /* 1. failed exec attempts executed nothing */
        if (ft_is_exec(e.syscall) && e.ret_valid && e.ret < 0) {
            c->dropped_failed_exec++;
            continue;
        }

        /* 2. canonical paths */
        if ((e.type == EV_FILE || e.type == EV_PROCESS) && e.target[0] == '/') {
            ft_canonicalize_path(e.target, e.target, sizeof(e.target));
        }

        /* 3. actor executable */
        pe = exe_lookup(map, &map_n, e.pid, e.ppid);
        if (pe) {
            snprintf(e.exe, sizeof(e.exe), "%s", pe->exe);
        }
        if (pe && ft_is_fork(e.syscall) && e.ret_valid && e.ret > 0) {
            exe_lookup(map, &map_n, (pid_t)e.ret, e.pid);
        }
        if (pe && ft_is_exec(e.syscall) && e.target[0]) {
            snprintf(pe->exe, sizeof(pe->exe), "%.127s", e.target);
        }

        /* 4. errno text for failed calls (kept as evidence) */
        if (e.ret_valid && e.ret < 0 && e.ret > -4096) {
            size_t l = strlen(e.detail);
            snprintf(e.detail + l, sizeof(e.detail) - l, "%serr=%s",
                     l ? " " : "", strerror((int)-e.ret));
        }

        /* 5. contiguous ids */
        c->events[out] = e;
        c->events[out].id = out + 1;
        out++;
    }
    c->count = out;
}
