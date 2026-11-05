/*
 * report.c — for human-readable forensic report.
 *
 * The report is derived only from the stored evidence (events + correlation
 * links), so what it can say depends on the evidence configuration used.
 * Sections that need evidence the configuration did not collect say so
 * explicitly instead of silently being empty.
 */
#include "forensictrace.h"

#include <errno.h>
#include <stdlib.h>
#include <string.h>

#define RP_MAX_PROCS  512
#define RP_MAX_PATHS  128
#define RP_MAX_CHAIN  12
#define RP_TIMELINE_CAP 400

static const char *base_name(const char *p)
{
    const char *s = strrchr(p, '/');

    return s ? s + 1 : p;
}

static int starts(const char *s, const char *prefix)
{
    return strncmp(s, prefix, strlen(prefix)) == 0;
}

static int in_temp_dir(const char *p)
{
    return starts(p, "/tmp/") || starts(p, "/var/tmp/") || starts(p, "/dev/shm/");
}

/* Loader, locale, pseudo-filesystem and pipe activity: present in every run. */
static int noise_target(const char *t)
{
    static const char *const prefixes[] = {
        "/usr/lib/", "/lib/", "/lib64/", "/etc/ld.so", "/usr/share/locale",
        "/usr/share/zoneinfo", "/proc/", "/sys/", "/dev/", "pipe:", "socket:",
        "anon_inode:", "fd:", NULL
    };

    if (t[0] == '\0') {
        return 1;
    }
    for (int i = 0; prefixes[i]; i++) {
        if (starts(t, prefixes[i])) {
            return 1;
        }
    }
    return strstr(t, ".so") != NULL;
}

static int sensitive_target(const char *t)
{
    static const char *const needles[] = {
        "/etc/shadow", "/etc/gshadow", "/etc/passwd", "/etc/sudoers",
        "/.ssh/", "/etc/group", NULL
    };

    for (int i = 0; needles[i]; i++) {
        if (strstr(t, needles[i])) {
            return 1;
        }
    }
    return 0;
}

static double rel_ms(const FTContext *c, const Event *e)
{
    return c->count ? (double)(e->ts_ns - c->events[0].ts_ns) / 1e6 : 0.0;
}

static const char *actor(const Event *e)
{
    return e->exe[0] ? base_name(e->exe) : "?";
}

static int has_file_evidence(const char *cfg) { return strcmp(cfg, "A") != 0; }
static int has_net_evidence(const char *cfg)  { return strcmp(cfg, "A") && strcmp(cfg, "B"); }

typedef struct {
    pid_t pid;
    pid_t ppid;
    char  prog[FT_EXE];
    int   first_idx;
} Proc;

static void print_tree(FILE *f, const Proc *procs, int n, pid_t pid, int depth)
{
    for (int i = 0; i < n; i++) {
        if (procs[i].pid != pid) {
            continue;
        }
        for (int d = 0; d < depth; d++) {
            fputs("  ", f);
        }
        fprintf(f, "- `%d` %s\n", (int)pid, procs[i].prog[0] ? procs[i].prog : "(unknown)");
        break;
    }
    if (depth >= 8) {
        return;
    }
    for (int i = 0; i < n; i++) {
        if (procs[i].ppid == pid && procs[i].pid != pid) {
            print_tree(f, procs, n, procs[i].pid, depth + 1);
        }
    }
}

/* Walk the resource links backwards: the history of one file. */
static void print_provenance(FILE *f, const FTContext *c, int idx)
{
    int chain[RP_MAX_CHAIN];
    int n = 0;
    int cur = idx;

    while (cur >= 0 && n < RP_MAX_CHAIN) {
        chain[n++] = cur;
        cur = c->resource_event[cur];
    }
    if (n < 2) {
        return;
    }
    fprintf(f, "  - history of `%s`:\n", c->events[idx].target);
    for (int k = n - 1; k >= 0; k--) {
        const Event *e = &c->events[chain[k]];

        fprintf(f, "    - +%.3f ms #%d `%s` by pid %d (%s)\n",
                rel_ms(c, e), e->id, e->syscall, (int)e->pid, actor(e));
    }

    /* Did the process that first touched the file talk to the network just before? */
    {
        const Event *origin = &c->events[chain[n - 1]];

        for (int j = chain[n - 1] - 1; j >= 0; j--) {
            const Event *p = &c->events[j];

            if (p->pid == origin->pid && p->type == EV_NETWORK &&
                strcmp(p->syscall, "connect") == 0) {
                fprintf(f, "  - the creating process (pid %d, %s) had connected to `%s`"
                           " at +%.3f ms: likely source of the content\n",
                        (int)origin->pid, actor(origin), p->target, rel_ms(c, p));
                break;
            }
        }
    }
}

int ft_report_write(FTContext *c)
{
    FILE *f;
    Proc procs[RP_MAX_PROCS];
    int nproc = 0;

    struct { char path[256]; int first; int writes; long bytes; int created; } paths[RP_MAX_PATHS];
    int npaths = 0;
    int found;

    if (!c || !c->report_path[0]) {
        return 0;
    }
    ft_ensure_parent_dirs(c->report_path);
    f = fopen(c->report_path, "w");
    if (!f) {
        fprintf(stderr, "[report] cannot write %s: %s\n", c->report_path, strerror(errno));
        return -1;
    }

    /* ---- process table ---- */
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];
        int k;

        for (k = 0; k < nproc; k++) {
            if (procs[k].pid == e->pid) {
                break;
            }
        }
        if (k == nproc && nproc < RP_MAX_PROCS) {
            procs[nproc].pid = e->pid;
            procs[nproc].ppid = e->ppid;
            procs[nproc].first_idx = i;
            snprintf(procs[nproc].prog, sizeof(procs[nproc].prog), "%.*s",
                     (int)sizeof(procs[nproc].prog) - 1, e->exe);
            nproc++;
        }
        if (k < nproc && strncmp(e->syscall, "exec", 4) == 0 && e->target[0]) {
            snprintf(procs[k].prog, sizeof(procs[k].prog), "%.*s",
                     (int)sizeof(procs[k].prog) - 1, e->target);
        }
    }

    fprintf(f, "# ForensicTrace incident report\n\n");
    fprintf(f, "| | |\n|---|---|\n");
    fprintf(f, "| Scenario | %s |\n", c->scenario[0] ? c->scenario : "(not labelled)");
    fprintf(f, "| Command | `%s` |\n", c->command);
    fprintf(f, "| Evidence configuration | %s |\n", c->config);
    fprintf(f, "| Events recorded | %d%s |\n", c->count,
            c->truncated ? " (TRUNCATED at event cap)" : "");
    fprintf(f, "| Failed exec attempts removed | %d |\n", c->dropped_failed_exec);
    fprintf(f, "| Duration | %.3f ms |\n", (double)(c->end_ns - c->start_ns) / 1e6);
    fprintf(f, "| Evidence file | `%s` (%ld bytes) |\n", c->output_path, c->storage_bytes);
    fprintf(f, "| SHA-256 | `%s` |\n\n", c->sha256_hex[0] ? c->sha256_hex : "(not computed)");
    fprintf(f, "Verify integrity: `sha256sum -c %s.sha256`\n\n", c->output_path);

    /* ---- process tree ---- */
    fprintf(f, "## 1. Process tree\n\n");
    if (nproc == 0) {
        fprintf(f, "No processes observed.\n\n");
    } else {
        for (int i = 0; i < nproc; i++) {
            int has_parent = 0;

            for (int k = 0; k < nproc; k++) {
                if (procs[k].pid == procs[i].ppid && k != i) {
                    has_parent = 1;
                    break;
                }
            }
            if (!has_parent) {
                print_tree(f, procs, nproc, procs[i].pid, 0);
            }
        }
        fprintf(f, "\n%d process(es) observed.\n\n", nproc);
    }

    /* ---- executed programs ---- */
    fprintf(f, "## 2. Programs executed\n\n");
    found = 0;
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];

        if (strncmp(e->syscall, "exec", 4) != 0) {
            continue;
        }
        fprintf(f, "- +%.3f ms pid %d (%s) executed `%s`%s\n",
                rel_ms(c, e), (int)e->pid, actor(e), e->target,
                in_temp_dir(e->target) ? " **(from a temporary directory)**" : "");
        found = 1;
    }
    if (!found) {
        fprintf(f, "None observed.\n");
    }
    fprintf(f, "\n");

    /* ---- network ---- */
    fprintf(f, "## 3. Network activity\n\n");
    found = 0;
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];

        if (e->type != EV_NETWORK || strcmp(e->syscall, "connect") != 0) {
            continue;
        }
        fprintf(f, "- +%.3f ms pid %d (%s) connected to `%s`\n",
                rel_ms(c, e), (int)e->pid, actor(e), e->target);
        found = 1;
    }
    if (!found) {
        fprintf(f, has_net_evidence(c->config)
                       ? "None observed.\n"
                       : "Not available: configuration %s does not record network events.\n",
                c->config);
    }
    fprintf(f, "\n");

    /* ---- files created / modified ---- */
    fprintf(f, "## 4. Files created or modified\n\n");
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];
        int k;
        int is_write = strcmp(e->syscall, "write") == 0;
        int is_open = strcmp(e->syscall, "open") == 0 || strcmp(e->syscall, "openat") == 0;
        unsigned long flags = 0;
        const char *fl;

        if (e->type != EV_FILE || (!is_write && !is_open) || e->target[0] != '/' ||
            noise_target(e->target)) {
            continue;
        }
        if (is_open) {
            fl = strstr(e->detail, "flags=0x");
            if (!fl) {
                continue;
            }
            flags = strtoul(fl + 8, NULL, 16);
            if (!((flags & 3UL) || (flags & 0x40UL))) {
                continue; /* read-only open */
            }
        }
        for (k = 0; k < npaths; k++) {
            if (strcmp(paths[k].path, e->target) == 0) {
                break;
            }
        }
        if (k == npaths) {
            if (npaths >= RP_MAX_PATHS) {
                continue;
            }
            snprintf(paths[npaths].path, sizeof(paths[npaths].path), "%.*s",
                     (int)sizeof(paths[npaths].path) - 1, e->target);
            paths[npaths].first = i;
            paths[npaths].writes = 0;
            paths[npaths].bytes = 0;
            paths[npaths].created = 0;
            npaths++;
        }
        if (is_open && (flags & 0x40UL)) {
            paths[k].created = 1;
        }
        if (is_write) {
            paths[k].writes++;
            if (e->ret_valid && e->ret > 0) {
                paths[k].bytes += e->ret;
            }
        }
    }
    if (npaths == 0) {
        fprintf(f, has_file_evidence(c->config)
                       ? "None observed.\n"
                       : "Not available: configuration %s does not record file events.\n",
                c->config);
    }
    for (int k = 0; k < npaths; k++) {
        const Event *e = &c->events[paths[k].first];

        fprintf(f, "- `%s` first touched +%.3f ms by pid %d (%s)%s; %d write call(s), %ld byte(s)\n",
                paths[k].path, rel_ms(c, e), (int)e->pid, actor(e),
                paths[k].created ? ", created/truncated" : "", paths[k].writes, paths[k].bytes);
    }
    fprintf(f, "\n");

    /* ---- permission changes ---- */
    fprintf(f, "## 5. Permission changes\n\n");
    found = 0;
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];

        if (strcmp(e->syscall, "chmod") != 0 && strcmp(e->syscall, "fchmodat") != 0) {
            continue;
        }
        fprintf(f, "- +%.3f ms pid %d (%s) changed permissions of `%s` (%s)\n",
                rel_ms(c, e), (int)e->pid, actor(e), e->target, e->detail);
        found = 1;
    }
    if (!found) {
        fprintf(f, has_file_evidence(c->config)
                       ? "None observed.\n"
                       : "Not available: configuration %s does not record file events.\n",
                c->config);
    }
    fprintf(f, "\n");

    /* ---- deletions ---- */
    fprintf(f, "## 6. Deletions\n\n");
    found = 0;
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];

        if (strncmp(e->syscall, "unlink", 6) != 0) {
            continue;
        }
        fprintf(f, "- +%.3f ms pid %d (%s) deleted `%s`\n",
                rel_ms(c, e), (int)e->pid, actor(e), e->target);
        found = 1;
    }
    if (!found) {
        fprintf(f, has_file_evidence(c->config)
                       ? "None observed.\n"
                       : "Not available: configuration %s does not record file events.\n",
                c->config);
    }
    fprintf(f, "\n");

    /* ---- sensitive resources ---- */
    fprintf(f, "## 7. Access to sensitive resources\n\n");
    found = 0;
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];
        int dup = 0;

        if (e->type != EV_FILE || !sensitive_target(e->target)) {
            continue;
        }
        if (strncmp(e->syscall, "open", 4) != 0 && strncmp(e->syscall, "unlink", 6) != 0 &&
            strncmp(e->syscall, "chmod", 5) != 0 && strncmp(e->syscall, "fchmod", 6) != 0) {
            continue;
        }
        for (int j = 0; j < i; j++) {
            if (c->events[j].pid == e->pid && strcmp(c->events[j].target, e->target) == 0 &&
                strcmp(c->events[j].syscall, e->syscall) == 0) {
                dup = 1;
                break;
            }
        }
        if (dup) {
            continue;
        }
        fprintf(f, "- +%.3f ms pid %d (%s) `%s` on `%s`%s\n",
                rel_ms(c, e), (int)e->pid, actor(e), e->syscall, e->target,
                (e->ret_valid && e->ret < 0) ? " — **attempt failed** (access denied or missing)" : "");
        found = 1;
    }
    if (!found) {
        fprintf(f, has_file_evidence(c->config)
                       ? "None observed.\n"
                       : "Not available: configuration %s does not record file events.\n",
                c->config);
    }
    fprintf(f, "\n");

    /* ---- provenance of executed temp files ---- */
    fprintf(f, "## 8. Provenance of files executed from temporary directories\n\n");
    found = 0;
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];

        if (strncmp(e->syscall, "exec", 4) != 0 || !in_temp_dir(e->target)) {
            continue;
        }
        fprintf(f, "- +%.3f ms `%s` executed by pid %d (%s)\n",
                rel_ms(c, e), e->target, (int)e->pid, actor(e));
        print_provenance(f, c, i);
        found = 1;
    }
    if (!found) {
        fprintf(f, "None.\n");
    }
    fprintf(f, "\n");

    /* ---- notable timeline ---- */
    fprintf(f, "## 9. Notable timeline\n\n");
    fprintf(f, "Process, network, open/write/delete/chmod events; loader, locale, pipe and\n"
               "read/close noise is omitted (full timeline: JSON file).\n\n");
    fprintf(f, "| # | +ms | PID | Actor | Syscall | Target |\n|---|---|---|---|---|---|\n");
    {
        int shown = 0;

        for (int i = 0; i < c->count; i++) {
            const Event *e = &c->events[i];

            if (e->type == EV_OTHER) {
                continue;
            }
            if (e->type == EV_FILE &&
                (noise_target(e->target) || strcmp(e->syscall, "read") == 0 ||
                 strcmp(e->syscall, "close") == 0)) {
                continue;
            }
            if (shown >= RP_TIMELINE_CAP) {
                fprintf(f, "| | | | | | (truncated after %d rows) |\n", RP_TIMELINE_CAP);
                break;
            }
            fprintf(f, "| %d | %.3f | %d | %s | %s | `%s`%s |\n", e->id, rel_ms(c, e),
                    (int)e->pid, actor(e), e->syscall, e->target,
                    (e->ret_valid && e->ret < 0 && strcmp(e->syscall, "connect") != 0)
                        ? " (failed)" : "");
            shown++;
        }
    }
    fprintf(f, "\n");

    /* ---- resource cost ---- */
    fprintf(f, "## 10. Collection cost\n\n");
    fprintf(f, "| Metric | Value |\n|---|---|\n");
    fprintf(f, "| Tracer CPU (user+sys) | %.3f ms |\n",
            (double)(c->res.tracer_user_us + c->res.tracer_sys_us) / 1000.0);
    fprintf(f, "| Workload CPU (user+sys) | %.3f ms |\n",
            (double)(c->res.workload_user_us + c->res.workload_sys_us) / 1000.0);
    fprintf(f, "| Tracer peak memory | %ld KiB |\n", c->res.tracer_maxrss_kb);
    fprintf(f, "| Processing time (normalise+correlate+reconstruct) | %.3f ms |\n",
            (double)c->process_ns / 1e6);
    fprintf(f, "| Evidence size | %ld bytes |\n\n", c->storage_bytes);

    fclose(f);
    fprintf(stderr, "[report] written to %s\n", c->report_path);
    return 0;
}
