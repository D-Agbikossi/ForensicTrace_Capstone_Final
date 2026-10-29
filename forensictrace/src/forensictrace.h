#ifndef FORENSICTRACE_H
#define FORENSICTRACE_H

#include <stdint.h>
#include <stdio.h>
#include <sys/types.h>

#define FT_VERSION      "1.0"
#define FT_MAX_EVENTS   20000
#define FT_MAX_TRACEES  4096
#define FT_STR          512
#define FT_EXE          128

typedef enum {
    EV_PROCESS = 0,
    EV_FILE    = 1,
    EV_NETWORK = 2,
    EV_OTHER   = 3
} EventType;

typedef struct {
    int       id;               /* 1-based, assigned after normalisation */
    uint64_t  ts_ns;            /* CLOCK_MONOTONIC at syscall entry */
    EventType type;
    char      syscall[32];
    pid_t     pid;
    pid_t     ppid;
    int       uid;              /* effective uid of the acting process, -1 if unknown */
    long      ret;              /* return value, valid only if ret_valid */
    int       ret_valid;        /* 0 for calls that never return (exit_group) */
    char      exe[FT_EXE];      /* executable of the acting process (normaliser) */
    char      target[FT_STR];   /* path / address / "code=N" */
    char      detail[FT_STR];   /* flags, byte counts, child pid, errors */
} Event;

/* FR10: resource measurements for one monitored run. */
typedef struct {
    uint64_t wall_ns;               /* duration of the traced run */
    uint64_t tracer_user_us;        /* CPU used by ForensicTrace itself */
    uint64_t tracer_sys_us;
    uint64_t workload_user_us;      /* CPU used by the traced process tree */
    uint64_t workload_sys_us;
    long     tracer_maxrss_kb;      /* peak resident memory of ForensicTrace */
    long     workload_maxrss_kb;    /* peak resident memory of largest traced child */
} FTResources;

typedef struct {
    Event    events[FT_MAX_EVENTS];
    int      count;
    int      parent_event[FT_MAX_EVENTS];    /* process/causal predecessor index or -1 */
    int      resource_event[FT_MAX_EVENTS];  /* previous event on same resource or -1 */

    char     config[8];
    char     mode[12];           /* collection mode: "ptrace" (stop on every syscall)
                                  * or "seccomp" (kernel filter, stop only on selected) */
    char     output_path[1024];
    char     report_path[1024];  /* optional --report target */
    char     scenario[64];       /* optional --scenario label */
    char     command[512];       /* traced command line */
    int      verbose;
    int      quiet;              /* suppress stdout timeline */

    uint64_t start_ns;
    uint64_t end_ns;
    uint64_t normalise_ns;
    uint64_t correlate_ns;
    uint64_t reconstruct_ns;
    uint64_t process_ns;         /* normalise + correlate + reconstruct */

    long     storage_bytes;      /* final size of the JSON file */
    int      truncated;          /* 1 if events were dropped at FT_MAX_EVENTS */
    int      untraced;           /* processes seen beyond FT_MAX_TRACEES (their events are lost) */
    int      raw_count;          /* events before normalisation */
    int      dropped_failed_exec;/* failed execve (PATH search) removed by normaliser */

    FTResources res;
    char     sha256_hex[65];
} FTContext;

uint64_t    ft_now_ns(void);
const char *ft_type_name(EventType t);

int         ft_config_accepts(const char *config, const char *syscall_name);

FTContext  *ft_ctx_create(const char *config, const char *output, int verbose);
void        ft_ctx_destroy(FTContext *c);
int         ft_collect(FTContext *c, char *const argv[]);

void        ft_normalize(FTContext *c);
void        ft_canonicalize_path(const char *in, char *out, size_t outlen);
void        ft_correlate(FTContext *c);
void        ft_reconstruct(FTContext *c);
void        ft_resources_capture(FTContext *c);
int         ft_write_json(FTContext *c);
int         ft_integrity_write(FTContext *c);
int         ft_report_write(FTContext *c);
int         ft_ensure_parent_dirs(const char *filepath);


/* Syscall-name predicates shared by the normaliser and correlator. */
#include <string.h>
static inline int ft_is_exec(const char *s)
{
    return !strcmp(s, "execve") || !strcmp(s, "execveat");
}
static inline int ft_is_fork(const char *s)
{
    return !strcmp(s, "fork") || !strcmp(s, "vfork") ||
           !strcmp(s, "clone") || !strcmp(s, "clone3");
}

#endif
