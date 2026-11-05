/*
 * collector.c — ptrace syscall collection (x86_64 Linux).
 *
 * Each syscall is recorded at ENTRY (arguments are valid) and its return value
 * is attached at EXIT. The return value lets later stages tell failed calls from
 * successful ones and link a fork/clone to the exact child it created.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <time.h>
#include <sys/ptrace.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/user.h>
#include <sys/syscall.h>
#include <sys/uio.h>
#include <sys/stat.h>
#include <stddef.h>
#include <linux/limits.h>
#include <linux/audit.h>
#include <linux/filter.h>
#include <linux/seccomp.h>
#include <sys/prctl.h>

#include "forensictrace.h"

#ifndef __WALL
#define __WALL 0x40000000
#endif

#ifndef PTRACE_O_TRACESECCOMP
#define PTRACE_O_TRACESECCOMP 0x00000080
#endif
#ifndef PTRACE_EVENT_SECCOMP
#define PTRACE_EVENT_SECCOMP 7
#endif

#ifndef SYS_clone3
#define SYS_clone3 435   /* glibc >= 2.34 uses clone3 for pthread_create */
#endif

typedef struct {
    pid_t pid;
    int   in_syscall;
    int   pending_init;   /* suppress next stop signal (new fork child) */
    int   last_event;     /* index of event recorded at the current entry stop, or -1 */
    int   sec_stage;      /* seccomp mode: 1 = event recorded, waiting for syscall-exit stop */
} Tracee;


/*
 * The 22 syscalls ForensicTrace records, with their category. This table is the
 * single source of truth for the evidence configurations (Table 7 of the
 * proposal): ft_config_accepts() and the seccomp filter are both built from it.
 * Any other syscall is category EV_OTHER and is recorded only by configuration D.
 */
typedef struct {
    const char *name;
    long        nr;
    EventType   type;
} SyscallDef;

static const SyscallDef k_syscalls[] = {
    {"execve", SYS_execve, EV_PROCESS},   {"execveat", SYS_execveat, EV_PROCESS},
    {"clone", SYS_clone, EV_PROCESS},     {"clone3", SYS_clone3, EV_PROCESS},
    {"fork", SYS_fork, EV_PROCESS},       {"vfork", SYS_vfork, EV_PROCESS},
    {"exit", SYS_exit, EV_PROCESS},       {"exit_group", SYS_exit_group, EV_PROCESS},
    {"open", SYS_open, EV_FILE},          {"openat", SYS_openat, EV_FILE},
    {"close", SYS_close, EV_FILE},        {"read", SYS_read, EV_FILE},
    {"write", SYS_write, EV_FILE},        {"unlink", SYS_unlink, EV_FILE},
    {"unlinkat", SYS_unlinkat, EV_FILE},  {"chmod", SYS_chmod, EV_FILE},
    {"fchmodat", SYS_fchmodat, EV_FILE},  {"connect", SYS_connect, EV_NETWORK},
    {"accept", SYS_accept, EV_NETWORK},   {"accept4", SYS_accept4, EV_NETWORK},
    {"sendto", SYS_sendto, EV_NETWORK},   {"recvfrom", SYS_recvfrom, EV_NETWORK},
};
#define N_SYSCALLS ((int)(sizeof(k_syscalls) / sizeof(k_syscalls[0])))

/* A=0, B=1, C=2, D=3; -1 for anything else. Configurations are cumulative. */
static int config_rank(const char *config) {
    if (!config || config[0] < 'A' || config[0] > 'D' || config[1] != '\0') return -1;
    return config[0] - 'A';
}

const char *ft_type_name(EventType t) {
    switch (t) {
    case EV_PROCESS: return "process";
    case EV_FILE:    return "file";
    case EV_NETWORK: return "network";
    default:         return "other";
    }
}

static Tracee g_tracees[FT_MAX_TRACEES];
static int    g_tracee_count = 0;
static int    g_untraced = 0;     /* processes that did not fit in g_tracees */
static int    g_seccomp = 0;      /* 1 = seccomp-bpf collection mode */

static Tracee *tracee_find(pid_t pid) {
    for (int i = 0; i < g_tracee_count; i++)
        if (g_tracees[i].pid == pid) return &g_tracees[i];
    return NULL;
}

static Tracee *tracee_add(pid_t pid, int pending_init) {
    if (g_tracee_count >= FT_MAX_TRACEES) {
        if (g_untraced++ == 0)
            fprintf(stderr, "[ForensicTrace] warning: more than %d concurrent processes; "
                            "events of the extra processes are lost\n", FT_MAX_TRACEES);
        return NULL;
    }
    Tracee *t = &g_tracees[g_tracee_count++];
    t->pid = pid;
    t->in_syscall = 0;
    t->pending_init = pending_init;
    t->last_event = -1;
    t->sec_stage = 0;
    return t;
}

static void tracee_remove(pid_t pid) {
    for (int i = 0; i < g_tracee_count; i++) {
        if (g_tracees[i].pid == pid) {
            g_tracees[i] = g_tracees[--g_tracee_count];
            return;
        }
    }
}

uint64_t ft_now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)ts.tv_sec * 1000000000ULL + (uint64_t)ts.tv_nsec;
}

static int read_string(pid_t pid, unsigned long addr, char *out, size_t outlen) {
    if (addr == 0 || outlen == 0) { if (outlen) out[0] = '\0'; return -1; }

    struct iovec local  = { .iov_base = out, .iov_len = outlen - 1 };
    struct iovec remote = { .iov_base = (void*)addr, .iov_len = outlen - 1 };
    ssize_t n = process_vm_readv(pid, &local, 1, &remote, 1, 0);
    if (n > 0) {
        out[n] = '\0';
        /* process_vm_readv copies a fixed length; cut at the first NUL */
        out[strnlen(out, (size_t)n)] = '\0';
        return 0;
    }

    size_t i = 0;
    while (i + sizeof(long) <= outlen - 1) {
        errno = 0;
        long word = ptrace(PTRACE_PEEKDATA, pid, addr + i, NULL);
        if (errno != 0) { out[i] = '\0'; return (i > 0) ? 0 : -1; }
        memcpy(out + i, &word, sizeof(long));
        for (size_t j = 0; j < sizeof(long); j++)
            if (out[i + j] == '\0') return 0;
        i += sizeof(long);
    }
    out[outlen - 1] = '\0';
    return 0;
}

static void fd_to_path(pid_t pid, int fd, char *out, size_t outlen) {
    char link[64], path[PATH_MAX];
    snprintf(link, sizeof(link), "/proc/%d/fd/%d", pid, fd);
    ssize_t n = readlink(link, path, sizeof(path) - 1);
    if (n < 0) { snprintf(out, outlen, "fd:%d", fd); return; }
    path[n] = '\0';
    strncpy(out, path, outlen - 1);
    out[outlen - 1] = '\0';
}

/*
 * Read a path argument and make it absolute using the tracee's cwd (or dirfd).
 * This must happen at collection time: the process may have exited or changed
 * directory by the time the trace is analysed. The raw string is kept in detail.
 */
static void path_arg(Event *e, pid_t pid, int dirfd, unsigned long addr) {
    char raw[FT_STR];
    if (read_string(pid, addr, raw, sizeof(raw)) != 0) { e->target[0] = '\0'; return; }

    if (raw[0] == '\0' || raw[0] == '/') {
        snprintf(e->target, sizeof(e->target), "%s", raw);
        return;
    }

    char link[64], base[PATH_MAX];
    if (dirfd == AT_FDCWD) snprintf(link, sizeof(link), "/proc/%d/cwd", pid);
    else                   snprintf(link, sizeof(link), "/proc/%d/fd/%d", pid, dirfd);
    ssize_t n = readlink(link, base, sizeof(base) - 1);
    if (n <= 0) { snprintf(e->target, sizeof(e->target), "%s", raw); return; }
    base[n] = '\0';

    snprintf(e->target, sizeof(e->target), "%.255s/%.250s", base, raw);

    size_t l = strlen(e->detail);
    snprintf(e->detail + l, sizeof(e->detail) - l, "%sraw=%.200s", l ? " " : "", raw);
}

static void classify_event(Event *e, long syscall_num,
                           unsigned long a0, unsigned long a1,
                           unsigned long a2, unsigned long a3,
                           pid_t pid, pid_t ppid) {
    e->pid  = pid;
    e->ppid = ppid;

    switch (syscall_num) {
    case SYS_execve:
        snprintf(e->syscall, sizeof(e->syscall), "execve");
        e->type = EV_PROCESS;
        path_arg(e, pid, AT_FDCWD, a0);
        break;
    case SYS_execveat:
        snprintf(e->syscall, sizeof(e->syscall), "execveat");
        e->type = EV_PROCESS;
        path_arg(e, pid, (int)a0, a1);
        break;

    case SYS_open:
        snprintf(e->syscall, sizeof(e->syscall), "open");
        e->type = EV_FILE;
        snprintf(e->detail, sizeof(e->detail), "flags=0x%lx", a1);
        path_arg(e, pid, AT_FDCWD, a0);
        break;
    case SYS_openat:
        snprintf(e->syscall, sizeof(e->syscall), "openat");
        e->type = EV_FILE;
        snprintf(e->detail, sizeof(e->detail), "dirfd=%d flags=0x%lx", (int)a0, a2);
        path_arg(e, pid, (int)a0, a1);
        break;
    case SYS_close:
        snprintf(e->syscall, sizeof(e->syscall), "close");
        e->type = EV_FILE;
        fd_to_path(pid, (int)a0, e->target, sizeof(e->target));
        break;
    case SYS_read:
        snprintf(e->syscall, sizeof(e->syscall), "read");
        e->type = EV_FILE;
        fd_to_path(pid, (int)a0, e->target, sizeof(e->target));
        snprintf(e->detail, sizeof(e->detail), "count=%lu", a2);
        break;
    case SYS_write:
        snprintf(e->syscall, sizeof(e->syscall), "write");
        e->type = EV_FILE;
        fd_to_path(pid, (int)a0, e->target, sizeof(e->target));
        snprintf(e->detail, sizeof(e->detail), "count=%lu", a2);
        break;
    case SYS_unlink:
        snprintf(e->syscall, sizeof(e->syscall), "unlink");
        e->type = EV_FILE;
        path_arg(e, pid, AT_FDCWD, a0);
        break;
    case SYS_unlinkat:
        snprintf(e->syscall, sizeof(e->syscall), "unlinkat");
        e->type = EV_FILE;
        snprintf(e->detail, sizeof(e->detail), "dirfd=%d", (int)a0);
        path_arg(e, pid, (int)a0, a1);
        break;
    case SYS_chmod:
        snprintf(e->syscall, sizeof(e->syscall), "chmod");
        e->type = EV_FILE;
        snprintf(e->detail, sizeof(e->detail), "mode=0%lo", a1);
        path_arg(e, pid, AT_FDCWD, a0);
        break;
    case SYS_fchmodat:
        snprintf(e->syscall, sizeof(e->syscall), "fchmodat");
        e->type = EV_FILE;
        snprintf(e->detail, sizeof(e->detail), "dirfd=%d mode=0%lo", (int)a0, a2);
        path_arg(e, pid, (int)a0, a1);
        break;

    case SYS_connect:
        snprintf(e->syscall, sizeof(e->syscall), "connect");
        e->type = EV_NETWORK;
        {
            unsigned char sa[128];
            struct iovec local  = { .iov_base = sa, .iov_len = sizeof(sa) };
            struct iovec remote = { .iov_base = (void*)a1, .iov_len = sizeof(sa) };
            ssize_t n = process_vm_readv(pid, &local, 1, &remote, 1, 0);
            if (n >= 8 && sa[0] == 2 /* AF_INET */) {
                unsigned int port = ((unsigned)sa[2] << 8) | sa[3];
                snprintf(e->target, sizeof(e->target),
                         "%u.%u.%u.%u:%u",
                         sa[4], sa[5], sa[6], sa[7], port);
            } else if (n >= 8 && sa[0] == 10 /* AF_INET6 */) {
                snprintf(e->target, sizeof(e->target), "ipv6:[...]");
            } else if (n >= 3 && sa[0] == 1 /* AF_UNIX */) {
                snprintf(e->target, sizeof(e->target), "unix:%.100s",
                         (const char *)&sa[2]);
            } else {
                snprintf(e->target, sizeof(e->target), "sockfd=%ld", (long)a0);
            }
        }
        break;
    case SYS_accept:
        snprintf(e->syscall, sizeof(e->syscall), "accept");
        e->type = EV_NETWORK;
        snprintf(e->target, sizeof(e->target), "sockfd=%ld", (long)a0);
        break;
    case SYS_accept4:
        snprintf(e->syscall, sizeof(e->syscall), "accept4");
        e->type = EV_NETWORK;
        snprintf(e->target, sizeof(e->target), "sockfd=%ld", (long)a0);
        break;
    case SYS_sendto:
        snprintf(e->syscall, sizeof(e->syscall), "sendto");
        e->type = EV_NETWORK;
        fd_to_path(pid, (int)a0, e->target, sizeof(e->target));
        snprintf(e->detail, sizeof(e->detail), "count=%lu", a2);
        break;
    case SYS_recvfrom:
        snprintf(e->syscall, sizeof(e->syscall), "recvfrom");
        e->type = EV_NETWORK;
        fd_to_path(pid, (int)a0, e->target, sizeof(e->target));
        snprintf(e->detail, sizeof(e->detail), "count=%lu", a2);
        break;

    case SYS_clone:
        snprintf(e->syscall, sizeof(e->syscall), "clone");
        e->type = EV_PROCESS;
        break;
    case SYS_clone3:
        snprintf(e->syscall, sizeof(e->syscall), "clone3");
        e->type = EV_PROCESS;
        break;
    case SYS_fork:
        snprintf(e->syscall, sizeof(e->syscall), "fork");
        e->type = EV_PROCESS;
        break;
    case SYS_vfork:
        snprintf(e->syscall, sizeof(e->syscall), "vfork");
        e->type = EV_PROCESS;
        break;

    case SYS_exit:
        snprintf(e->syscall, sizeof(e->syscall), "exit");
        e->type = EV_PROCESS;
        snprintf(e->target, sizeof(e->target), "code=%ld", (long)a0);
        break;
    case SYS_exit_group:
        snprintf(e->syscall, sizeof(e->syscall), "exit_group");
        e->type = EV_PROCESS;
        snprintf(e->target, sizeof(e->target), "code=%ld", (long)a0);
        break;

    default:
        snprintf(e->syscall, sizeof(e->syscall), "syscall_%ld", syscall_num);
        e->type = EV_OTHER;
        break;
    }
    (void)a3;
}

/* Returns the stored index, or -1 if the event was filtered out or dropped. */
static int record_event(FTContext *c, const Event *e) {
    /* Evidence configuration first: events a config rejects must never count
     * against the cap (otherwise config A could be reported as truncated). */
    if (!ft_config_accepts(c->config, e->syscall)) return -1;

    if (c->count >= FT_MAX_EVENTS) {
        if (!c->truncated) {
            c->truncated = 1;
            fprintf(stderr,
                    "[ForensicTrace] warning: event cap %d reached; further events dropped\n",
                    FT_MAX_EVENTS);
        }
        return -1;
    }

    int idx = c->count;
    Event *dst = &c->events[idx];
    *dst = *e;
    dst->id = idx + 1;
    c->count++;

    if (c->verbose) {
        fprintf(stderr, "[FT] #%-4d %-11s pid=%-6d %s\n",
                dst->id, dst->syscall, dst->pid, dst->target);
    }
    return idx;
}

/* Record the entry of a syscall (arguments are valid). Returns the event index or -1. */
static int record_entry(FTContext *c, pid_t pid, const struct user_regs_struct *regs) {
    Event e;
    memset(&e, 0, sizeof(e));
    e.ts_ns = ft_now_ns();

    pid_t ppid = 0;
    char statpath[64], buf[512];
    snprintf(statpath, sizeof(statpath), "/proc/%d/stat", pid);
    FILE *fp = fopen(statpath, "r");
    if (fp) {
        if (fgets(buf, sizeof(buf), fp)) {
            char *rp = strrchr(buf, ')');
            if (rp) sscanf(rp + 2, "%*c %d", &ppid);
        }
        fclose(fp);
    }

    {   /* owner of /proc/<pid> is the process's effective uid */
        struct stat st;
        char procdir[32];
        snprintf(procdir, sizeof(procdir), "/proc/%d", pid);
        e.uid = (stat(procdir, &st) == 0) ? (int)st.st_uid : -1;
    }

    classify_event(&e, (long)regs->orig_rax,
                   regs->rdi, regs->rsi, regs->rdx, regs->r10,
                   pid, ppid);
    return record_event(c, &e);
}

/* Attach the return value to the entry event (and the child pid for spawns). */
static void attach_return(FTContext *c, int idx, const struct user_regs_struct *regs) {
    if (idx < 0 || idx >= c->count) return;
    Event *ev = &c->events[idx];
    ev->ret = (long)regs->rax;
    ev->ret_valid = 1;
    if (ev->ret > 0 &&
        (!strcmp(ev->syscall, "clone") || !strcmp(ev->syscall, "clone3") ||
         !strcmp(ev->syscall, "fork") || !strcmp(ev->syscall, "vfork"))) {
        size_t l = strlen(ev->detail);
        snprintf(ev->detail + l, sizeof(ev->detail) - l,
                 "%schild=%ld", l ? " " : "", ev->ret);
    }
}

/* ptrace mode: every syscall stops twice (entry, exit). */
static void handle_syscall_stop(FTContext *c, pid_t pid,
                                const struct user_regs_struct *regs) {
    Tracee *t = tracee_find(pid);
    if (!t) return;

    if (!t->in_syscall) {
        t->in_syscall = 1;
        t->last_event = record_entry(c, pid, regs);
    } else {
        t->in_syscall = 0;
        attach_return(c, t->last_event, regs);
        t->last_event = -1;
    }
}

/*
 * seccomp mode: a kernel BPF filter returns SECCOMP_RET_TRACE only for the
 * syscalls the evidence configuration collects; every other syscall runs at
 * full speed with no tracer stop. A syscall we DO collect stops once at the
 * seccomp event (entry, arguments valid); we then resume with PTRACE_SYSCALL
 * to catch its exit stop (return value) and go back to PTRACE_CONT.
 */
static int config_syscalls(const char *config, long *out, int max) {
    int rank = config_rank(config), n = 0;
    for (int i = 0; i < N_SYSCALLS && n < max; i++)
        if ((int)k_syscalls[i].type <= rank) out[n++] = k_syscalls[i].nr;
    return n;
}

static int install_seccomp(const char *config) {
    struct sock_filter prog[N_SYSCALLS + 8];
    long nrs[N_SYSCALLS];
    int n = 0, k = 0;
    int all = (config_rank(config) == 3);

    prog[k++] = (struct sock_filter)BPF_STMT(BPF_LD | BPF_W | BPF_ABS,
                    offsetof(struct seccomp_data, arch));
    if (all) {
        prog[k++] = (struct sock_filter)BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K,
                        AUDIT_ARCH_X86_64, 1, 0);
        prog[k++] = (struct sock_filter)BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW);
        prog[k++] = (struct sock_filter)BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_TRACE);
    } else {
        n = config_syscalls(config, nrs, N_SYSCALLS);
        /* [1] arch check: if not x86_64 jump to ALLOW (n + 1 instructions ahead) */
        prog[k++] = (struct sock_filter)BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K,
                        AUDIT_ARCH_X86_64, 0, (unsigned char)(n + 1));
        prog[k++] = (struct sock_filter)BPF_STMT(BPF_LD | BPF_W | BPF_ABS,
                        offsetof(struct seccomp_data, nr));
        for (int i = 0; i < n; i++) {
            /* match -> jump to TRACE (the last instruction) */
            prog[k] = (struct sock_filter)BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K,
                            (unsigned)nrs[i], (unsigned char)(n - i), 0);
            k++;
        }
        prog[k++] = (struct sock_filter)BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW);
        prog[k++] = (struct sock_filter)BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_TRACE);
    }

    struct sock_fprog fp = { .len = (unsigned short)k, .filter = prog };
    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) != 0) return -1;
    return prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &fp);
}

/* Resume a tracee: seccomp mode runs free (CONT) except while waiting for an exit stop. */
static void resume(Tracee *t, pid_t pid, int sig) {
    int req = (g_seccomp && !(t && t->sec_stage)) ? PTRACE_CONT : PTRACE_SYSCALL;
    ptrace(req, pid, NULL, (void *)(long)sig);
}

int ft_collect(FTContext *c, char *const argv[]) {
    g_tracee_count = 0;
    g_untraced = 0;
    g_seccomp = (strcmp(c->mode, "seccomp") == 0);
    c->start_ns = ft_now_ns();

    pid_t child = fork();
    if (child < 0) { perror("fork"); return -1; }

    if (child == 0) {
        if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) < 0) {
            perror("PTRACE_TRACEME"); _exit(1);
        }
        raise(SIGSTOP);            /* let parent set options */
        if (g_seccomp && install_seccomp(c->config) != 0) {
            perror("seccomp");     /* installed after the stop so setup syscalls are not traced */
            _exit(1);
        }
        execvp(argv[0], argv);
        perror("execvp");
        _exit(127);
    }

    int status;
    waitpid(child, &status, 0);
    if (!WIFSTOPPED(status)) {
        fprintf(stderr, "child did not stop as expected\n");
        return -1;
    }

    long options = PTRACE_O_TRACESYSGOOD  |
                   PTRACE_O_TRACEFORK     |
                   PTRACE_O_TRACEVFORK    |
                   PTRACE_O_TRACECLONE    |
                   PTRACE_O_TRACEEXEC     |
                   PTRACE_O_EXITKILL;
    if (g_seccomp) options |= PTRACE_O_TRACESECCOMP;
    if (ptrace(PTRACE_SETOPTIONS, child, NULL, options) < 0)
        perror("PTRACE_SETOPTIONS");

    tracee_add(child, 0);
    resume(tracee_find(child), child, 0);

    while (g_tracee_count > 0) {
        pid_t pid = waitpid(-1, &status, __WALL);
        if (pid < 0) {
            if (errno == ECHILD) break;
            if (errno == EINTR) continue;
            perror("waitpid");
            break;
        }

        if (WIFEXITED(status) || WIFSIGNALED(status)) {
            tracee_remove(pid);
            continue;
        }
        if (!WIFSTOPPED(status)) continue;

        int sig   = WSTOPSIG(status);
        int event = (status >> 16) & 0xffff;
        Tracee *t = tracee_find(pid);

        /* seccomp mode: a selected syscall is about to run (entry, args valid) */
        if (sig == SIGTRAP && event == PTRACE_EVENT_SECCOMP) {
            struct user_regs_struct regs;
            if (t && ptrace(PTRACE_GETREGS, pid, NULL, &regs) == 0) {
                t->last_event = record_entry(c, pid, &regs);
                t->sec_stage = (t->last_event >= 0) ? 1 : 0;
            }
            resume(t, pid, 0);
            continue;
        }

        /* New child from fork/vfork/clone */
        if (sig == SIGTRAP &&
            (event == PTRACE_EVENT_FORK  ||
             event == PTRACE_EVENT_VFORK ||
             event == PTRACE_EVENT_CLONE)) {
            unsigned long new_pid = 0;
            if (ptrace(PTRACE_GETEVENTMSG, pid, NULL, &new_pid) == 0 &&
                !tracee_find((pid_t)new_pid))
                tracee_add((pid_t)new_pid, 1);
            resume(t, pid, 0);
            continue;
        }

        /* PTRACE_EVENT_EXEC — nothing to record, just continue */
        if (sig == SIGTRAP && event == PTRACE_EVENT_EXEC) {
            resume(t, pid, 0);
            continue;
        }

        /*
         * Race: a new child's initial SIGSTOP can be reported BEFORE the
         * parent's fork/clone event. Adopt it here (initial stop already seen)
         * instead of injecting a bogus SIGSTOP into the child.
         */
        if (!t && sig == SIGSTOP) {
            t = tracee_add(pid, 0);
            resume(t, pid, 0);
            continue;
        }

        /* New tracee's initial stop: suppress the synthetic signal */
        if (t && t->pending_init && sig == SIGSTOP) {
            t->pending_init = 0;
            resume(t, pid, 0);
            continue;
        }

        /* Syscall stop (SIGTRAP | 0x80 with TRACESYSGOOD) */
        if (sig == (SIGTRAP | 0x80)) {
            struct user_regs_struct regs;
            if (ptrace(PTRACE_GETREGS, pid, NULL, &regs) == 0) {
                if (!g_seccomp) {
                    handle_syscall_stop(c, pid, &regs);
                } else if (t && t->sec_stage == 1 && (long)regs.rax != -ENOSYS) {
                    /* exit stop of a collected syscall (an entry stop has rax == -ENOSYS) */
                    attach_return(c, t->last_event, &regs);
                    t->last_event = -1;
                    t->sec_stage = 0;
                }
            }
            resume(t, pid, 0);
            continue;
        }

        /* Otherwise, deliver the signal to the tracee */
        resume(t, pid, sig);
    }

    c->end_ns = ft_now_ns();
    c->untraced = g_untraced;
    c->raw_count = c->count;
    return 0;
}

FTContext *ft_ctx_create(const char *config, const char *output, int verbose) {
    FTContext *c = calloc(1, sizeof(FTContext));
    if (!c) return NULL;
    snprintf(c->config, sizeof(c->config), "%s", config);
    snprintf(c->output_path, sizeof(c->output_path), "%s", output);
    snprintf(c->mode, sizeof(c->mode), "ptrace");
    c->verbose = verbose;
    for (int i = 0; i < FT_MAX_EVENTS; i++) {
        c->parent_event[i] = -1;
        c->resource_event[i] = -1;
    }
    return c;
}

void ft_ctx_destroy(FTContext *c) { free(c); }

int ft_config_accepts(const char *config, const char *syscall_name) {
    int rank = config_rank(config);
    if (rank < 0) return 0;
    if (rank == 3) return 1;                 /* D: every syscall */
    for (int i = 0; i < N_SYSCALLS; i++)
        if (!strcmp(k_syscalls[i].name, syscall_name))
            return (int)k_syscalls[i].type <= rank;
    return 0;                                /* uncategorised syscalls: D only */
}
