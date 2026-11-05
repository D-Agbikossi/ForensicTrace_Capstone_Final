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
#define FT_HASH_HEX     65      /* SHA-256 as lowercase hex + NUL */

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
    int       sock_fd;          /* collector only: connect()'s fd, resolved at syscall exit */
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

/* Chain-of-custody state for one investigation session (schema 3 evidence). */
typedef struct {
    char     session_id[37];     /* random UUID, unique per run */
    char     case_id[128];
    char     investigator[128];
    char     os_user[64];
    char     hostname[128];
    char     kernel[128];
    char     started_utc[40];
    char     finished_utc[40];
    int64_t  wall_offset_ns;     /* CLOCK_REALTIME - CLOCK_MONOTONIC at session start */
    char     genesis[FT_HASH_HEX];
    char     head[FT_HASH_HEX];
    uint64_t chain_ns;
    char     sign_key_path[1024];
    char     (*event_hash)[FT_HASH_HEX];  /* one per event, allocated at finalise */
} FTCustody;

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

    int      custody;            /* 1 = schema 3 evidence; 0 = --baseline-format (schema 2) */
    FTCustody cust;
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
void        ft_json_escape(FILE *f, const char *s);

/* integrity.c */
int         ft_sha256_file(const char *path, char hex[FT_HASH_HEX], long *size);

/* custody.c: session identity, hash chain, signed manifest, keys, export */
#define FT_N_EVENT_FIELDS  15
#define FT_N_HEADER_FIELDS 17
#define FT_N_AUDIT_FIELDS  9
extern const char *const ft_event_fields[FT_N_EVENT_FIELDS];
extern const char *const ft_header_fields[FT_N_HEADER_FIELDS];
extern const char *const ft_audit_fields[FT_N_AUDIT_FIELDS];

int         ft_custody_begin(FTContext *c, const char *investigator, const char *case_id,
                             const char *sign_key);
int         ft_custody_finalize(FTContext *c);
int         ft_manifest_write(FTContext *c);
int         ft_hash_fields(const char *prefix, const char *const *names,
                           const char *const *values, int n, char hex[FT_HASH_HEX]);
void        ft_format_utc(int64_t wall_ns, char *out, size_t outlen);
void        ft_now_utc(char *out, size_t outlen);
void        ft_current_user(char *out, size_t outlen);
void        ft_event_uid(const char *session_id, int id, char *out, size_t outlen);
int         ft_keygen(const char *key_path);
int         ft_export(const char *evidence, const char *to_dir, const char *pubkey,
                      const char *investigator);
int         ft_signature_check(const char *manifest_path, const char *sig_path,
                               const char *pubkey_path, const char *embedded_b64,
                               char fingerprint[FT_HASH_HEX], char *err, size_t errlen);

/* verify.c: evidence verification and the append-only audit log */
#define FT_VERIFY_OK     0      /* no problem found (status says how strong the proof is) */
#define FT_VERIFY_FAILED 1      /* evidence was modified, or custody files are missing */
#define FT_VERIFY_ERROR  2      /* could not run (usage, unreadable input) */
int         ft_verify(const char *evidence, const char *pubkey, int json_output, int quiet,
                      int write_audit, const char *investigator, char *status, size_t statuslen);
int         ft_audit_append(const char *audit_path, const char *action, const char *session_id,
                            const char *investigator, const char *evidence_sha256,
                            const char *outcome, const char *detail);
void        ft_manifest_info(const char *manifest_path, char *session, size_t session_len,
                             char *report, size_t report_len);


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
