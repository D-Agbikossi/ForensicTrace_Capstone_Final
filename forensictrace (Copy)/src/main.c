/* main.c — command-line interface and orchestration of the pipeline:
 * collect -> normalise -> correlate -> reconstruct -> measure -> store. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "forensictrace.h"

static void usage(void) {
    fprintf(stderr,
        "ForensicTrace 1.0 - Linux incident reconstruction (final product)\n"
        "\n"
        "Usage: forensictrace --config <A|B|C|D> --output <file.json> [options] -- <cmd> [args...]\n"
        "       forensictrace verify <file.json> [--pubkey <key.pub>] [--json] [--no-audit]\n"
        "                     [--investigator <name>]\n"
        "       forensictrace export <file.json> --to <dir> [--pubkey <key.pub>] [--investigator <name>]\n"
        "       forensictrace keygen --key <file.key>\n"
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
        "  --investigator <id>  Investigator recorded in the evidence (default: OS user)\n"
        "  --case <id>          Case identifier recorded in the evidence\n"
        "  --sign-key <file>    Sign the evidence manifest with this Ed25519 key (see keygen)\n"
        "  --baseline-format    Write the schema 2 file used by the published experiments:\n"
        "                       no custody chain, manifest, audit log or socket details\n"
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

/* forensictrace verify|export|keygen ... */
static int custody_command(int argc, char *argv[]) {
    const char *cmd = argv[1];
    const char *file = NULL, *pubkey = NULL, *investigator = NULL, *to = NULL, *key = NULL;
    int json = 0, audit = 1;

    for (int i = 2; i < argc; i++) {
        if (!strcmp(argv[i], "--pubkey") && i + 1 < argc) pubkey = argv[++i];
        else if (!strcmp(argv[i], "--investigator") && i + 1 < argc) investigator = argv[++i];
        else if (!strcmp(argv[i], "--to") && i + 1 < argc) to = argv[++i];
        else if (!strcmp(argv[i], "--key") && i + 1 < argc) key = argv[++i];
        else if (!strcmp(argv[i], "--json")) json = 1;
        else if (!strcmp(argv[i], "--no-audit")) audit = 0;
        else if (argv[i][0] != '-' && !file) file = argv[i];
        else { fprintf(stderr, "Unknown option: %s\n", argv[i]); usage(); return FT_VERIFY_ERROR; }
    }
    if (!strcmp(cmd, "keygen")) {
        if (!key) { usage(); return FT_VERIFY_ERROR; }
        return ft_keygen(key) == 0 ? 0 : FT_VERIFY_ERROR;
    }
    if (!file || (!strcmp(cmd, "export") && !to)) { usage(); return FT_VERIFY_ERROR; }
    if (!strcmp(cmd, "export")) return ft_export(file, to, pubkey, investigator);
    return ft_verify(file, pubkey, json, 0, audit, investigator, NULL, 0);
}

int main(int argc, char *argv[]) {
    const char *config   = NULL;
    const char *output   = NULL;
    const char *report   = NULL;
    const char *scenario = NULL;
    const char *mode     = "ptrace";
    const char *investigator = NULL;
    const char *case_id  = NULL;
    const char *sign_key = NULL;
    int         baseline = 0;
    int         verbose  = 0;
    int         quiet    = 0;
    int         cmd_idx  = -1;

    if (argc >= 2 && (!strcmp(argv[1], "verify") || !strcmp(argv[1], "export") ||
                      !strcmp(argv[1], "keygen"))) {
        return custody_command(argc, argv);
    }

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
        } else if (!strcmp(argv[i], "--investigator") && i + 1 < argc) {
            investigator = argv[++i];
        } else if (!strcmp(argv[i], "--case") && i + 1 < argc) {
            case_id = argv[++i];
        } else if (!strcmp(argv[i], "--sign-key") && i + 1 < argc) {
            sign_key = argv[++i];
        } else if (!strcmp(argv[i], "--baseline-format")) {
            baseline = 1;
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
    if (baseline && (investigator || case_id || sign_key)) {
        fprintf(stderr, "--baseline-format cannot be combined with custody options\n");
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

    /* A bad signing key must fail before tracing, not after evidence is collected. */
    if (!baseline && ft_custody_begin(c, investigator, case_id, sign_key) != 0) {
        ft_ctx_destroy(c);
        return 1;
    }

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

    /* After the resource capture, so custody work is not charged to the workload metrics. */
    if (c->custody && ft_custody_finalize(c) != 0) {
        fprintf(stderr, "[ForensicTrace] failed to build the evidence hash chain\n");
        ft_ctx_destroy(c);
        return 1;
    }

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

    if (c->custody && ft_manifest_write(c) != 0) {
        fprintf(stderr, "[ForensicTrace] failed to write evidence manifest\n");
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
