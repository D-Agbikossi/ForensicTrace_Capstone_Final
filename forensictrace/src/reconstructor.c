/* reconstructor.c — print the human-readable incident timeline. */
#include "forensictrace.h"

#include <inttypes.h>
#include <stdio.h>
#include <string.h>

void ft_reconstruct(FTContext *c)
{
    uint64_t duration_us;
    uint64_t base;
    FILE *out;
    int i;

    if (!c) {
        return;
    }

    /* With --quiet the same formatting work is done but sent to /dev/null, so
     * processing-time measurements are comparable between quiet and normal runs. */
    out = c->quiet ? fopen("/dev/null", "w") : stdout;
    if (!out) {
        out = stdout;
    }

    if (c->end_ns > c->start_ns) {
        duration_us = (c->end_ns - c->start_ns) / 1000ULL;
    } else {
        duration_us = 0;
    }

    fprintf(out, "=== ForensicTrace Reconstructed Timeline ===\n");
    fprintf(out, "Config: %s | Events: %d | Duration: %" PRIu64 ".%03" PRIu64 " ms\n\n",
            c->config, c->count, (uint64_t)(duration_us / 1000ULL),
            (uint64_t)(duration_us % 1000ULL));

    if (c->count == 0) {
        fprintf(out, "(no events captured)\n");
        goto done;
    }

    base = c->events[0].ts_ns;

    fprintf(out, "%-5s %-10s %-9s %-8s %-8s %-12s %s\n",
            "#", "Delta(ms)", "Type", "PID", "PPID", "Syscall", "Target");
    fprintf(out, "---------------------------------------------------------------------------------\n");

    for (i = 0; i < c->count; i++) {
        Event *e = &c->events[i];
        double d = (double)(e->ts_ns - base) / 1e6;
        const char *target = e->target[0] ? e->target : e->detail;
        const char *failed = "";

        if (e->ret_valid && e->ret < 0 && e->ret > -4096 &&
            strcmp(e->syscall, "connect") != 0) {
            failed = "  [FAILED]";
        }

        fprintf(out, "%-5d %-10.3f %-9s %-8d %-8d %-12s %s%s\n",
                e->id, d, ft_type_name(e->type), (int)e->pid, (int)e->ppid,
                e->syscall, target, failed);
    }
    fprintf(out, "---------------------------------------------------------------------------------\n");

done:
    if (out != stdout) {
        fclose(out);
    }
}
