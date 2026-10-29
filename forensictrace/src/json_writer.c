/* json_writer.c — serialise one experiment (config, metrics, events, links) to JSON. */
#include "forensictrace.h"

#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

static void json_escape(FILE *f, const char *s)
{
    for (; *s; s++) {
        unsigned char c = (unsigned char)*s;

        switch (c) {
        case '"':
            fputs("\\\"", f);
            break;
        case '\\':
            fputs("\\\\", f);
            break;
        case '\n':
            fputs("\\n", f);
            break;
        case '\r':
            fputs("\\r", f);
            break;
        case '\t':
            fputs("\\t", f);
            break;
        default:
            if (c < 0x20) {
                fprintf(f, "\\u%04x", c);
            } else {
                fputc(c, f);
            }
            break;
        }
    }
}

/* Create missing parent directories for output_path (mkdir -p behaviour). */
int ft_ensure_parent_dirs(const char *filepath)
{
    char path[1024];
    size_t len;
    size_t i;

    if (!filepath || !filepath[0]) {
        return -1;
    }

    len = strlen(filepath);
    if (len >= sizeof(path)) {
        return -1;
    }
    memcpy(path, filepath, len + 1);

    for (i = len; i > 0; i--) {
        if (path[i] == '/') {
            path[i] = '\0';
            break;
        }
    }
    if (i == 0) {
        return 0;
    }
    if (path[0] == '\0') {
        return 0;
    }

    for (i = 1; path[i] != '\0'; i++) {
        if (path[i] != '/') {
            continue;
        }
        path[i] = '\0';
        if (path[0] != '\0' && mkdir(path, 0755) != 0 && errno != EEXIST) {
            return -1;
        }
        path[i] = '/';
    }
    if (mkdir(path, 0755) != 0 && errno != EEXIST) {
        return -1;
    }
    return 0;
}

static void str_field(FILE *f, const char *indent, const char *key, const char *val)
{
    fprintf(f, "%s\"%s\": \"", indent, key);
    json_escape(f, val);
    fprintf(f, "\",\n");
}

static int write_once(FTContext *c)
{
    FILE *f = fopen(c->output_path, "w");

    if (!f) {
        fprintf(stderr, "[ForensicTrace] cannot write %s: %s\n",
                c->output_path, strerror(errno));
        return -1;
    }

    fprintf(f, "{\n");
    fprintf(f, "  \"schema_version\": 2,\n");
    fprintf(f, "  \"tool\": \"ForensicTrace %s\",\n", FT_VERSION);
    str_field(f, "  ", "scenario", c->scenario);
    str_field(f, "  ", "command", c->command);
    str_field(f, "  ", "config", c->config);
    str_field(f, "  ", "collection_mode", c->mode);
    fprintf(f, "  \"event_count\": %d,\n", c->count);
    fprintf(f, "  \"raw_event_count\": %d,\n", c->raw_count);
    fprintf(f, "  \"dropped_failed_exec\": %d,\n", c->dropped_failed_exec);
    fprintf(f, "  \"truncated\": %s,\n", c->truncated ? "true" : "false");
    fprintf(f, "  \"untraced_processes\": %d,\n", c->untraced);
    fprintf(f, "  \"duration_ns\": %llu,\n",
            (unsigned long long)(c->end_ns - c->start_ns));
    fprintf(f, "  \"storage_bytes\": %ld,\n", c->storage_bytes);

    fprintf(f, "  \"resource_metrics\": {\n");
    fprintf(f, "    \"wall_ns\": %llu,\n", (unsigned long long)c->res.wall_ns);
    fprintf(f, "    \"tracer_user_us\": %llu,\n", (unsigned long long)c->res.tracer_user_us);
    fprintf(f, "    \"tracer_sys_us\": %llu,\n", (unsigned long long)c->res.tracer_sys_us);
    fprintf(f, "    \"workload_user_us\": %llu,\n", (unsigned long long)c->res.workload_user_us);
    fprintf(f, "    \"workload_sys_us\": %llu,\n", (unsigned long long)c->res.workload_sys_us);
    fprintf(f, "    \"tracer_maxrss_kb\": %ld,\n", c->res.tracer_maxrss_kb);
    fprintf(f, "    \"workload_maxrss_kb\": %ld\n", c->res.workload_maxrss_kb);
    fprintf(f, "  },\n");

    fprintf(f, "  \"processing\": {\n");
    fprintf(f, "    \"normalise_ns\": %llu,\n", (unsigned long long)c->normalise_ns);
    fprintf(f, "    \"correlate_ns\": %llu,\n", (unsigned long long)c->correlate_ns);
    fprintf(f, "    \"reconstruct_ns\": %llu,\n", (unsigned long long)c->reconstruct_ns);
    fprintf(f, "    \"total_ns\": %llu\n", (unsigned long long)c->process_ns);
    fprintf(f, "  },\n");

    fprintf(f, "  \"events\": [\n");
    for (int i = 0; i < c->count; i++) {
        Event *e = &c->events[i];

        fprintf(f, "    {\n");
        fprintf(f, "      \"id\": %d,\n", e->id);
        fprintf(f, "      \"ts_ns\": %llu,\n", (unsigned long long)e->ts_ns);
        fprintf(f, "      \"type\": \"%s\",\n", ft_type_name(e->type));
        fprintf(f, "      \"syscall\": \"%s\",\n", e->syscall);
        fprintf(f, "      \"pid\": %d,\n", e->pid);
        fprintf(f, "      \"ppid\": %d,\n", e->ppid);
        fprintf(f, "      \"uid\": %d,\n", e->uid);
        str_field(f, "      ", "exe", e->exe);
        str_field(f, "      ", "target", e->target);
        str_field(f, "      ", "detail", e->detail);
        if (e->ret_valid) {
            fprintf(f, "      \"ret\": %ld,\n", e->ret);
        } else {
            fprintf(f, "      \"ret\": null,\n");
        }
        fprintf(f, "      \"parent_event\": %d,\n", c->parent_event[i]);
        fprintf(f, "      \"resource_event\": %d\n", c->resource_event[i]);
        fprintf(f, "    }%s\n", (i < c->count - 1) ? "," : "");
    }
    fprintf(f, "  ]\n");
    fprintf(f, "}\n");

    if (fflush(f) != 0 || ferror(f)) {
        fprintf(stderr, "[ForensicTrace] error writing %s\n", c->output_path);
        fclose(f);
        return -1;
    }
    fclose(f);
    return 0;
}

static long file_size(const char *path)
{
    struct stat st;

    if (stat(path, &st) != 0) {
        return -1;
    }
    return (long)st.st_size;
}

int ft_write_json(FTContext *c)
{
    if (!c || !c->output_path[0]) {
        return -1;
    }

    if (ft_ensure_parent_dirs(c->output_path) != 0) {
        fprintf(stderr, "[ForensicTrace] cannot create output directory for %s: %s\n",
                c->output_path, strerror(errno));
        return -1;
    }

    /*
     * The file records its own size (storage_bytes). Re-write until the value
     * embedded in the file equals the file's real size; this converges after
     * at most a couple of passes because only the digit count can change.
     */
    c->storage_bytes = 0;
    for (int pass = 0; pass < 6; pass++) {
        long size;

        if (write_once(c) != 0) {
            return -1;
        }
        size = file_size(c->output_path);
        if (size <= 0) {
            fprintf(stderr, "[ForensicTrace] output file is empty: %s\n", c->output_path);
            return -1;
        }
        if (size == c->storage_bytes) {
            return 0;
        }
        c->storage_bytes = size;
    }
    fprintf(stderr, "[ForensicTrace] warning: storage_bytes did not converge\n");
    return 0;
}
