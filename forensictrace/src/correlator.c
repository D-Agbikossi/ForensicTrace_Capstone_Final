/*
 * correlator.c — associate related events (timestamps, PIDs, PPIDs and
 * affected resources). Two kinds of backward links are produced; both always
 * point to an EARLIER event, so the result is a DAG that can be walked to
 * explain how an event came about.
 *
 *   parent_event[i]   process/causal predecessor
 *       1. previous event of the same PID (per-PID chain, no window limit);
 *       2. for the FIRST event of a PID: the parent's fork/clone/vfork whose
 *          recorded return value is exactly this PID;
 *       3. fallback when that return value was not captured: the parent's most
 *          recent spawn event (fork/clone/vfork/execve) within FT_LOOKBACK.
 *
 *   resource_event[i] data/resource predecessor
 *       the most recent earlier event, from ANY process, that touched the same
 *       resource (canonical file path, pipe, or ip:port). This is what links a
 *       write by one process to a chmod or exec of the same file by another.
 */
#include "forensictrace.h"

#include <string.h>

#define FT_LOOKBACK      200
#define FT_RES_LOOKBACK  5000
#define COR_MAX_PIDS     4096

/* fork-family or exec: the events that can introduce a new PID or program */
static int is_spawn_syscall(const char *name)
{
    return ft_is_fork(name) || ft_is_exec(name);
}

/* Targets worth linking on: real paths, pipes and network endpoints. */
static int linkable_target(const Event *e)
{
    const char *t = e->target;

    if (e->type == EV_OTHER || t[0] == '\0') {
        return 0;
    }
    if (strncmp(t, "code=", 5) == 0 || strncmp(t, "fd:", 3) == 0 ||
        strncmp(t, "sockfd=", 7) == 0) {
        return 0;
    }
    if (strcmp(t, "/dev/null") == 0 || strcmp(t, "/dev/tty") == 0) {
        return 0;
    }
    return 1;
}

void ft_correlate(FTContext *c)
{
    static pid_t pid_tab[COR_MAX_PIDS];
    static int   last_tab[COR_MAX_PIDS];
    int pid_n = 0;

    if (!c) {
        return;
    }

    for (int i = 0; i < c->count; i++) {
        Event *ev = &c->events[i];
        int slot = -1;
        int link = -1;

        c->parent_event[i] = -1;
        c->resource_event[i] = -1;

        for (int k = 0; k < pid_n; k++) {
            if (pid_tab[k] == ev->pid) {
                slot = k;
                break;
            }
        }

        if (slot >= 0) {
            /* 1. same-PID chain */
            link = last_tab[slot];
        } else {
            /* 2. exact fork/clone that created this PID */
            for (int j = i - 1; j >= 0; j--) {
                const Event *p = &c->events[j];

                if (ft_is_fork(p->syscall) && p->ret_valid &&
                    p->ret == (long)ev->pid) {
                    link = j;
                    break;
                }
            }
            /* 3. fallback: parent's most recent spawn event */
            if (link < 0) {
                int limit = i - FT_LOOKBACK;

                if (limit < 0) {
                    limit = 0;
                }
                for (int j = i - 1; j >= limit; j--) {
                    const Event *p = &c->events[j];

                    if (p->pid == ev->ppid && is_spawn_syscall(p->syscall)) {
                        link = j;
                        break;
                    }
                }
            }
            if (pid_n < COR_MAX_PIDS) {
                slot = pid_n++;
                pid_tab[slot] = ev->pid;
            }
        }
        c->parent_event[i] = link;
        if (slot >= 0) {
            last_tab[slot] = i;
        }

        /* resource link */
        if (linkable_target(ev)) {
            int limit = i - FT_RES_LOOKBACK;

            if (limit < 0) {
                limit = 0;
            }
            for (int j = i - 1; j >= limit; j--) {
                const Event *p = &c->events[j];

                if (p->target[0] && strcmp(p->target, ev->target) == 0 &&
                    linkable_target(p)) {
                    c->resource_event[i] = j;
                    break;
                }
            }
        }
    }
}
