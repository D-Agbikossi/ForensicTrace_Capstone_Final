/* main.c — command-line interface and orchestration of the pipeline:
 * collect -> normalise -> correlate -> reconstruct -> measure -> store. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "forensictrace.h"

static void usage(void) {
    fprintf(stderr,
        "ForensicTrace - ptrace-based incident reconstruction prototype\n"
        "\n"
        "Usage: forensictrace --config <A|B|C|D> --output <file.json> [options] -- <cmd> [args...]\n"
        "\n"
        "Configurations:\n"
        "  A  Process events only\n"
        "  B  Process + file events\n"
        "  C  Process + file + network events\n"
        "  D  All events (full syscall trace)\n"
        "\n"
        "Options:\n"
        "  --mode <ptrace|seccomp>  Collection mode (default ptrace). seccomp installs a\n"
        "                       kernel BPF filter so only the selected syscalls stop the tracee\n"
        "  --report <file.md>   Also write a human-readable forensic report\n"
        "  --scenario <label>   Label stored in the JSON (e.g. scenario04)\n"
        "  --quiet, -q          Do not print the timeline on stdout\n"
        "  --verbose, -v        Per-event log on stderr\n"
        "  --help, -h           Show this help\n"
        "\n"
        "Example:\n"
        "  forensictrace --config B --output /tmp/run.json -- /bin/ls /tmp\n");
}

static void join_command(char *out, size_t outlen, char *const argv[]) {
    size_t used = 0;
    out[0] = '\0';
    for (int i = 0; argv[i]; i++) {
        int n = snprintf(out + used, outlen - used, "%s%s", i ? " " : "", argv[i]);
        if (n < 0 || (size_t)n >= outlen - used) break;
        used += (size_t)n;
    }
}

int main(int argc, char *argv[]) {
    const char *config   = NULL;
    const char *output   = NULL;
    const char *report   = NULL;
    const char *scenario = NULL;
    const char *mode     = "ptrace";
    int         verbose  = 0;
    int         quiet    = 0;
    int         cmd_idx  = -1;

    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--help") || !strcmp(argv[i], "-h")) {
            usage(); return 0;
        } else if (!strcmp(argv[i], "--config") && i + 1 < argc) {
            config = argv[++i];
        } else if (!strcmp(argv[i], "--output") && i + 1 < argc) {
            output = argv[++i];
        } else if (!strcmp(argv[i], "--report") && i + 1 < argc) {
            report = argv[++i];
        } else if (!strcmp(argv[i], "--mode") && i + 1 < argc) {
            mode = argv[++i];
        } else if (!strcmp(argv[i], "--scenario") && i + 1 < argc) {
            scenario = argv[++i];
        } else if (!strcmp(argv[i], "--verbose") || !strcmp(argv[i], "-v")) {
            verbose = 1;
        } else if (!strcmp(argv[i], "--quiet") || !strcmp(argv[i], "-q")) {
            quiet = 1;
        } else if (!strcmp(argv[i], "--")) {
            cmd_idx = i + 1; break;
        } else {
            fprintf(stderr, "Unknown option: %s\n", argv[i]);
            usage(); return 1;
        }
    }

    if (!config || !output || cmd_idx < 0 || cmd_idx >= argc) {
        usage(); return 1;
    }
    if (strcmp(config, "A") && strcmp(config, "B") &&
        strcmp(config, "C") && strcmp(config, "D")) {
        fprintf(stderr, "Invalid config '%s' (must be A, B, C, or D)\n", config);
        return 1;
    }

    if (strcmp(mode, "ptrace") && strcmp(mode, "seccomp")) {
        fprintf(stderr, "Invalid mode '%s' (must be ptrace or seccomp)\n", mode);
        return 1;
    }

    /* Operational messages go to stderr; stdout is reserved for the timeline. */
    fprintf(stderr, "[ForensicTrace]\n");
    fprintf(stderr, "  config  : %s\n", config);
    fprintf(stderr, "  mode    : %s\n", mode);
    fprintf(stderr, "  output  : %s\n", output);
    fprintf(stderr, "  command : %s\n", argv[cmd_idx]);

    FTContext *c = ft_ctx_create(config, output, verbose);
    if (!c) { fprintf(stderr, "out of memory\n"); return 1; }
    c->quiet = quiet;
    snprintf(c->mode, sizeof(c->mode), "%s", mode);
    if (report)   snprintf(c->report_path, sizeof(c->report_path), "%s", report);
    if (scenario) snprintf(c->scenario, sizeof(c->scenario), "%s", scenario);
    join_command(c->command, sizeof(c->command), &argv[cmd_idx]);

    if (ft_collect(c, &argv[cmd_idx]) < 0) {
        fprintf(stderr, "collection failed\n");
        ft_ctx_destroy(c);
        return 1;
    }

    /* Per-stage timing: "processing time" = normalise + correlate + reconstruct. */
    uint64_t t0 = ft_now_ns();
    ft_normalize(c);
    uint64_t t1 = ft_now_ns();
    ft_correlate(c);
    uint64_t t2 = ft_now_ns();
    ft_reconstruct(c);
    uint64_t t3 = ft_now_ns();
    c->normalise_ns   = t1 - t0;
    c->correlate_ns   = t2 - t1;
    c->reconstruct_ns = t3 - t2;
    c->process_ns     = t3 - t0;

    ft_resources_capture(c);

    if (ft_write_json(c) != 0) {
        fprintf(stderr, "[ForensicTrace] failed to write experiment JSON\n");
        ft_ctx_destroy(c);
        return 1;
    }

    if (ft_integrity_write(c) != 0) {
        fprintf(stderr, "[ForensicTrace] failed to write integrity sidecar\n");
        ft_ctx_destroy(c);
        return 1;
    }

    if (ft_report_write(c) != 0) {
        fprintf(stderr, "[ForensicTrace] failed to write report\n");
        ft_ctx_destroy(c);
        return 1;
    }

    fprintf(stderr, "\n[ForensicTrace] %d events written to %s (%ld bytes)\n",
            c->count, output, c->storage_bytes);
    if (c->truncated) {
        fprintf(stderr,
                "[ForensicTrace] note: trace was truncated (see truncated in JSON)\n");
    }

    ft_ctx_destroy(c);
    return 0;
}
