/*
 * verify.c — evidence verification and the append-only audit log.
 *
 * ft_verify() recomputes the evidence hash chain record by record and compares
 * the result with the sidecar, the (optionally signed) manifest and the audit
 * log. Findings name the record concerned: modified, missing, duplicated or out
 * of order. A small strict JSON parser is included so the file is never trusted
 * to keep the layout the writer gave it.
 */
#include "forensictrace.h"

#include <errno.h>
#include <fcntl.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>
#include <unistd.h>

const char *const ft_audit_fields[FT_N_AUDIT_FIELDS] = {
    "seq", "ts_utc", "action", "session_id", "investigator", "os_user",
    "evidence_sha256", "outcome", "detail"
};

/* ---- minimal JSON DOM ---------------------------------------------------- */

typedef enum { JV_SCALAR, JV_STRING, JV_ARRAY, JV_OBJECT } JvType;

typedef struct Jv {
    JvType      type;
    char       *text;      /* string value, or the raw token of a number/true/false/null */
    char      **keys;      /* objects */
    struct Jv **items;     /* arrays and objects */
    int         n, cap;
} Jv;

typedef struct {
    const char *p, *end;
    int depth;
} JvParser;

static void *xrealloc(void *ptr, size_t n)
{
    void *out = realloc(ptr, n);

    if (!out) {
        fprintf(stderr, "[verify] out of memory\n");
        exit(FT_VERIFY_ERROR);
    }
    return out;
}

static void jv_free(Jv *v)
{
    if (!v) {
        return;
    }
    for (int i = 0; i < v->n; i++) {
        if (v->keys) {
            free(v->keys[i]);
        }
        jv_free(v->items[i]);
    }
    free(v->keys);
    free(v->items);
    free(v->text);
    free(v);
}

static void skip_ws(JvParser *s)
{
    while (s->p < s->end && (*s->p == ' ' || *s->p == '\n' || *s->p == '\t' || *s->p == '\r')) {
        s->p++;
    }
}

static int put_utf8(char *o, unsigned cp)
{
    if (cp < 0x80) { o[0] = (char)cp; return 1; }
    if (cp < 0x800) { o[0] = (char)(0xC0 | (cp >> 6)); o[1] = (char)(0x80 | (cp & 63)); return 2; }
    if (cp < 0x10000) {
        o[0] = (char)(0xE0 | (cp >> 12)); o[1] = (char)(0x80 | ((cp >> 6) & 63));
        o[2] = (char)(0x80 | (cp & 63));
        return 3;
    }
    o[0] = (char)(0xF0 | (cp >> 18)); o[1] = (char)(0x80 | ((cp >> 12) & 63));
    o[2] = (char)(0x80 | ((cp >> 6) & 63)); o[3] = (char)(0x80 | (cp & 63));
    return 4;
}

static int hex4(JvParser *s, unsigned *out)
{
    unsigned v = 0;

    if (s->end - s->p < 4) {
        return -1;
    }
    for (int i = 0; i < 4; i++) {
        char c = *s->p++;

        v <<= 4;
        if (c >= '0' && c <= '9') v |= (unsigned)(c - '0');
        else if (c >= 'a' && c <= 'f') v |= (unsigned)(c - 'a' + 10);
        else if (c >= 'A' && c <= 'F') v |= (unsigned)(c - 'A' + 10);
        else return -1;
    }
    *out = v;
    return 0;
}

/* Rejects \u0000: a C string would silently stop there and hide what follows. */
static char *parse_string(JvParser *s)
{
    const char *q = s->p + 1;
    char *out, *o;

    while (q < s->end && *q != '"') {
        q += (*q == '\\') ? 2 : 1;
    }
    if (q >= s->end) {
        return NULL;
    }
    o = out = xrealloc(NULL, (size_t)(q - s->p) * 2 + 8);
    s->p++;
    while (*s->p != '"') {
        char c = *s->p++;

        if (c != '\\') {
            if ((unsigned char)c < 0x20) { free(out); return NULL; }
            *o++ = c;
            continue;
        }
        c = *s->p++;
        switch (c) {
        case '"': case '\\': case '/': *o++ = c; break;
        case 'n': *o++ = '\n'; break;
        case 't': *o++ = '\t'; break;
        case 'r': *o++ = '\r'; break;
        case 'b': *o++ = '\b'; break;
        case 'f': *o++ = '\f'; break;
        case 'u': {
            unsigned cp, lo;

            if (hex4(s, &cp) != 0 || cp == 0) { free(out); return NULL; }
            if (cp >= 0xD800 && cp < 0xDC00 && s->end - s->p >= 6 &&
                s->p[0] == '\\' && s->p[1] == 'u') {
                s->p += 2;
                if (hex4(s, &lo) != 0) { free(out); return NULL; }
                cp = 0x10000 + ((cp - 0xD800) << 10) + (lo - 0xDC00);
            }
            o += put_utf8(o, cp);
            break;
        }
        default:
            free(out);
            return NULL;
        }
    }
    s->p++;
    *o = '\0';
    return out;
}

static Jv *parse_value(JvParser *s)
{
    Jv *v;

    skip_ws(s);
    if (s->p >= s->end || s->depth > 32) {
        return NULL;
    }
    v = xrealloc(NULL, sizeof(Jv));
    memset(v, 0, sizeof(*v));

    if (*s->p == '"') {
        v->type = JV_STRING;
        v->text = parse_string(s);
        if (!v->text) { jv_free(v); return NULL; }
        return v;
    }
    if (*s->p == '{' || *s->p == '[') {
        int is_obj = *s->p == '{';
        char close = is_obj ? '}' : ']';

        v->type = is_obj ? JV_OBJECT : JV_ARRAY;
        s->p++;
        s->depth++;
        skip_ws(s);
        if (s->p < s->end && *s->p == close) {
            s->p++;
            s->depth--;
            return v;
        }
        for (;;) {
            char *key = NULL;
            Jv *item;

            if (is_obj) {
                skip_ws(s);
                if (s->p >= s->end || *s->p != '"' || !(key = parse_string(s))) {
                    jv_free(v);
                    return NULL;
                }
                skip_ws(s);
                if (s->p >= s->end || *s->p != ':') { free(key); jv_free(v); return NULL; }
                s->p++;
            }
            item = parse_value(s);
            if (!item) { free(key); jv_free(v); return NULL; }
            if (v->n == v->cap) {
                v->cap = v->cap ? v->cap * 2 : 8;
                v->items = xrealloc(v->items, (size_t)v->cap * sizeof(Jv *));
                if (is_obj) {
                    v->keys = xrealloc(v->keys, (size_t)v->cap * sizeof(char *));
                }
            }
            v->items[v->n] = item;
            if (is_obj) {
                v->keys[v->n] = key;
            }
            v->n++;
            skip_ws(s);
            if (s->p < s->end && *s->p == ',') { s->p++; continue; }
            if (s->p < s->end && *s->p == close) { s->p++; s->depth--; return v; }
            jv_free(v);
            return NULL;
        }
    }
    {
        const char *b = s->p;
        size_t l;

        while (s->p < s->end && !strchr(",}] \n\t\r", *s->p)) {
            s->p++;
        }
        l = (size_t)(s->p - b);
        if (l == 0) { jv_free(v); return NULL; }
        v->type = JV_SCALAR;
        v->text = xrealloc(NULL, l + 1);
        memcpy(v->text, b, l);
        v->text[l] = '\0';
        if (strcmp(v->text, "null") && strcmp(v->text, "true") && strcmp(v->text, "false") &&
            !strchr("-0123456789", v->text[0])) {
            jv_free(v);
            return NULL;
        }
    }
    return v;
}

/* Last duplicate key wins, as in Python and JavaScript: a duplicated field must
 * hash to the same value that every reader of the file would actually display. */
static const Jv *jv_get(const Jv *o, const char *key)
{
    if (!o || o->type != JV_OBJECT) {
        return NULL;
    }
    for (int i = o->n - 1; i >= 0; i--) {
        if (!strcmp(o->keys[i], key)) {
            return o->items[i];
        }
    }
    return NULL;
}

static const char *jv_text(const Jv *o, const char *key)
{
    const Jv *v = jv_get(o, key);

    return (v && v->text) ? v->text : NULL;
}

static Jv *parse_buffer(const char *buf, size_t len)
{
    JvParser s = { buf, buf + len, 0 };
    Jv *v = parse_value(&s);

    if (v) {
        skip_ws(&s);
        if (s.p != s.end) {
            jv_free(v);
            return NULL;
        }
    }
    return v;
}

static char *read_all(const char *path, size_t *len)
{
    FILE *f = fopen(path, "rb");
    char *buf;
    long size;

    if (!f) {
        return NULL;
    }
    if (fseek(f, 0, SEEK_END) != 0 || (size = ftell(f)) < 0 || fseek(f, 0, SEEK_SET) != 0) {
        fclose(f);
        return NULL;
    }
    buf = xrealloc(NULL, (size_t)size + 1);
    if (fread(buf, 1, (size_t)size, f) != (size_t)size) {
        free(buf);
        fclose(f);
        return NULL;
    }
    fclose(f);
    buf[size] = '\0';
    *len = (size_t)size;
    return buf;
}

/* A report name holding a path would let a forged manifest read files elsewhere. */
static const char *safe_report_name(const Jv *man)
{
    const char *name = jv_text(jv_get(man, "report"), "file");

    return (name && !strchr(name, '/')) ? name : NULL;
}

/* Session id and report file name of a manifest; both empty if it is unreadable. */
void ft_manifest_info(const char *manifest_path, char *session, size_t session_len,
                      char *report, size_t report_len)
{
    size_t len = 0;
    char *buf = read_all(manifest_path, &len);
    Jv *man = buf ? parse_buffer(buf, len) : NULL;
    const char *s = jv_text(man, "session_id");
    const char *r = safe_report_name(man);

    snprintf(session, session_len, "%s", s ? s : "");
    snprintf(report, report_len, "%s", r ? r : "");
    jv_free(man);
    free(buf);
}

/* ---- audit log ------------------------------------------------------------ */

#define AUDIT_GENESIS "ForensicTrace-audit-v1"

static int audit_entry_hash(const Jv *e, const char *prev, char hex[FT_HASH_HEX])
{
    const char *vals[FT_N_AUDIT_FIELDS];

    for (int i = 0; i < FT_N_AUDIT_FIELDS; i++) {
        vals[i] = jv_text(e, ft_audit_fields[i]);
        if (!vals[i]) {
            return -1;
        }
    }
    return ft_hash_fields(prev, ft_audit_fields, vals, FT_N_AUDIT_FIELDS, hex);
}

/* Walks the log. Returns entries seen, -1 if unreadable; bad_line is the first
 * broken entry (0 if none); last_hash and gen_sha describe what was read. */
static int audit_scan(const char *path, char *last_hash, size_t last_len, int *bad_line,
                      int *has_generated, char *gen_sha, size_t gen_sha_len)
{
    size_t len = 0;
    char *buf = read_all(path, &len);
    char prev[FT_HASH_HEX + 32];
    char *line, *save = NULL;
    int n = 0;

    *bad_line = 0;
    if (has_generated) {
        *has_generated = 0;
    }
    if (!buf) {
        return -1;
    }
    snprintf(prev, sizeof(prev), "%s", AUDIT_GENESIS);
    for (line = strtok_r(buf, "\n", &save); line; line = strtok_r(NULL, "\n", &save)) {
        Jv *e = parse_buffer(line, strlen(line));
        const char *stored = jv_text(e, "entry_hash");
        const char *sprev = jv_text(e, "prev_hash");
        const char *seq = jv_text(e, "seq");
        const char *action = jv_text(e, "action");
        char hex[FT_HASH_HEX];

        n++;
        if (!e || !stored || !sprev || !seq || atoi(seq) != n || strcmp(sprev, prev) ||
            audit_entry_hash(e, prev, hex) != 0 || strcmp(hex, stored)) {
            if (!*bad_line) {
                *bad_line = n;
            }
        }
        if (has_generated && action && !strcmp(action, "generated")) {
            *has_generated = 1;
            if (gen_sha && jv_text(e, "evidence_sha256")) {
                snprintf(gen_sha, gen_sha_len, "%s", jv_text(e, "evidence_sha256"));
            }
        }
        if (stored) {
            snprintf(prev, sizeof(prev), "%.64s", stored);
        }
        jv_free(e);
    }
    free(buf);
    if (last_hash) {
        snprintf(last_hash, last_len, "%s", prev);
    }
    return n;
}

int ft_audit_append(const char *audit_path, const char *action, const char *session_id,
                    const char *investigator, const char *evidence_sha256,
                    const char *outcome, const char *detail)
{
    char prev[FT_HASH_HEX + 32], hex[FT_HASH_HEX], seq[16], now[40], user[64];
    int bad = 0, n, fd;
    FILE *f;

    fd = open(audit_path, O_WRONLY | O_CREAT | O_APPEND, 0644);
    if (fd < 0 || flock(fd, LOCK_EX) != 0) {
        fprintf(stderr, "[audit] cannot open %s: %s\n", audit_path, strerror(errno));
        if (fd >= 0) close(fd);
        return -1;
    }
    n = audit_scan(audit_path, prev, sizeof(prev), &bad, NULL, NULL, 0);
    if (n <= 0) {
        n = 0;
        snprintf(prev, sizeof(prev), "%s", AUDIT_GENESIS);
    }
    snprintf(seq, sizeof(seq), "%d", n + 1);
    ft_now_utc(now, sizeof(now));
    ft_current_user(user, sizeof(user));

    const char *vals[FT_N_AUDIT_FIELDS] = {
        seq, now, action, session_id, investigator, user, evidence_sha256, outcome, detail
    };
    if (ft_hash_fields(prev, ft_audit_fields, vals, FT_N_AUDIT_FIELDS, hex) != 0) {
        close(fd);
        return -1;
    }
    f = fdopen(fd, "a");
    if (!f) {
        close(fd);
        return -1;
    }
    /* seq stays a string: all hashed audit values are text, exactly as hashed */
    fputc('{', f);
    for (int i = 0; i < FT_N_AUDIT_FIELDS; i++) {
        fprintf(f, "\"%s\":\"", ft_audit_fields[i]);
        ft_json_escape(f, vals[i]);
        fputs("\",", f);
    }
    fprintf(f, "\"prev_hash\":\"%s\",\"entry_hash\":\"%s\"}\n", prev, hex);
    if (fclose(f) != 0) {
        return -1;
    }
    return 0;
}

/* ---- verification ---------------------------------------------------------- */

#define MAX_LISTED_ISSUES 200

typedef struct {
    const char *kind;
    int   first_id, last_id;     /* event ids, 0 when not record-specific */
    char  text[320];
} Issue;

typedef struct {
    Issue list[MAX_LISTED_ISSUES];
    int   total;
    int   record_level;          /* modified, broken, missing, duplicate, out of order */
} Issues;

__attribute__((format(printf, 5, 6)))
static void add_issue(Issues *is, const char *kind, int first, int last, const char *fmt, ...)
{
    if (is->total < MAX_LISTED_ISSUES) {
        Issue *i = &is->list[is->total];
        va_list ap;

        i->kind = kind;
        i->first_id = first;
        i->last_id = last;
        va_start(ap, fmt);
        vsnprintf(i->text, sizeof(i->text), fmt, ap);
        va_end(ap);
    }
    is->total++;
    if (first > 0) {
        is->record_level++;
    }
}

typedef struct {
    const char *name;
    const char *state;           /* ok | warn | fail | skip */
    char        text[320];
} Check;

__attribute__((format(printf, 4, 5)))
static void add_check(Check *k, const char *name, const char *state, const char *fmt, ...)
{
    va_list ap;

    k->name = name;
    k->state = state;
    va_start(ap, fmt);
    vsnprintf(k->text, sizeof(k->text), fmt, ap);
    va_end(ap);
}

static const char *header_value(const Jv *doc, const Jv *cust, const char *name)
{
    const char *v = jv_text(doc, name);

    return v ? v : jv_text(cust, name);
}

/* Record-by-record chain check. Leaves the hash of the last record in tail. */
static void verify_records(const Jv *events, const char *genesis, int expected_count,
                           Issues *is, char tail[FT_HASH_HEX], int *checked)
{
    int count = events ? events->n : 0;
    int max_id = expected_count;
    char *seen;
    const char *prev = genesis;
    int last_id = 0;

    for (int i = 0; i < count; i++) {
        const char *t = jv_text(events->items[i], "id");
        int id = t ? atoi(t) : 0;

        if (id > max_id && id <= FT_MAX_EVENTS) {
            max_id = id;
        }
    }
    seen = xrealloc(NULL, (size_t)max_id + 2);
    memset(seen, 0, (size_t)max_id + 2);

    for (int i = 0; i < count; i++) {
        const Jv *e = events->items[i];
        const char *idt = jv_text(e, "id");
        const char *stored = jv_text(e, "event_hash");
        const char *sprev = jv_text(e, "prev_hash");
        int id = idt ? atoi(idt) : 0;
        const char *vals[FT_N_EVENT_FIELDS];
        char hex[FT_HASH_HEX];
        int complete = 1;

        for (int k = 0; k < FT_N_EVENT_FIELDS; k++) {
            vals[k] = jv_text(e, ft_event_fields[k]);
            if (!vals[k]) {
                complete = 0;
            }
        }
        (*checked)++;
        if (id < 1 || id > max_id) {
            add_issue(is, "record_invalid_id", i + 1, i + 1,
                      "record at position %d has an invalid id", i + 1);
        } else if (seen[id]) {
            add_issue(is, "record_duplicate", id, id, "event %d appears more than once", id);
        } else {
            seen[id] = 1;
            if (id < last_id) {
                add_issue(is, "record_out_of_order", id, id,
                          "event %d is stored after event %d", id, last_id);
            }
        }
        if (id > 0) {
            last_id = id;
        }
        if (!stored || !sprev || !complete) {
            add_issue(is, "record_modified", id > 0 ? id : i + 1, id > 0 ? id : i + 1,
                      "event %d has missing fields", id);
        } else if (ft_hash_fields(sprev, ft_event_fields, vals, FT_N_EVENT_FIELDS, hex) != 0 ||
                   strcmp(hex, stored)) {
            add_issue(is, "record_modified", id, id,
                      "event %d (%.32s %.200s): content does not match its stored hash",
                      id, vals[5], vals[10]);
        }
        if (sprev && strcmp(sprev, prev)) {
            add_issue(is, "chain_break", id > 0 ? id : i + 1, id > 0 ? id : i + 1,
                      "event %d does not link to the record stored before it", id);
        }
        prev = stored ? stored : "";
    }
    snprintf(tail, FT_HASH_HEX, "%.64s", prev);

    for (int id = 1; id <= max_id; id++) {
        if (!seen[id]) {
            int end = id;

            while (end + 1 <= max_id && !seen[end + 1]) {
                end++;
            }
            if (end == id) {
                add_issue(is, "record_missing", id, end, "event %d is missing", id);
            } else {
                add_issue(is, "record_missing", id, end, "events %d to %d are missing", id, end);
            }
            id = end;
        }
    }
    free(seen);
}

int ft_verify(const char *evidence, const char *pubkey, int json_output, int quiet,
              int write_audit, const char *investigator, char *status_out, size_t statuslen)
{
    static Issues is;
    Check checks[8];
    int nc = 0, checked = 0, rc;
    char sidecar[1300], manifest_path[1300], sig_path[1300], audit_path[1300];
    char file_hash[FT_HASH_HEX] = "", side_hash[FT_HASH_HEX] = "", tail[FT_HASH_HEX] = "";
    char fingerprint[FT_HASH_HEX] = "", who[128];
    long file_size = 0;
    const char *status;
    Jv *doc = NULL, *man = NULL;
    size_t len = 0, mlen = 0;
    char *buf, *mbuf;
    const Jv *cust = NULL, *events = NULL;
    const char *session = "";
    int legacy = 0, signed_ok = 0, pinned = 0, have_manifest = 0;

    memset(&is, 0, sizeof(is));
    snprintf(sidecar, sizeof(sidecar), "%s.sha256", evidence);
    snprintf(manifest_path, sizeof(manifest_path), "%s.manifest.json", evidence);
    snprintf(sig_path, sizeof(sig_path), "%s.manifest.sig", evidence);
    snprintf(audit_path, sizeof(audit_path), "%s.audit.jsonl", evidence);

    if (ft_sha256_file(evidence, file_hash, &file_size) != 0 || !(buf = read_all(evidence, &len))) {
        fprintf(stderr, "[verify] cannot read %s\n", evidence);
        if (status_out) snprintf(status_out, statuslen, "error");
        return FT_VERIFY_ERROR;
    }
    doc = parse_buffer(buf, len);
    free(buf);

    /* 1. sidecar */
    {
        FILE *f = fopen(sidecar, "r");

        if (f && fscanf(f, "%64s", side_hash) == 1 && !strcmp(side_hash, file_hash)) {
            add_check(&checks[nc++], "sidecar", "ok", "file matches its SHA-256 sidecar");
        } else if (!f) {
            add_check(&checks[nc++], "sidecar", "fail", "sidecar file is missing");
            add_issue(&is, "sidecar_missing", 0, 0, "%s is missing", sidecar);
        } else {
            add_check(&checks[nc++], "sidecar", "fail", "file does not match its SHA-256 sidecar");
            add_issue(&is, "sidecar_mismatch", 0, 0, "file hash differs from the sidecar");
        }
        if (f) fclose(f);
    }

    if (!doc || doc->type != JV_OBJECT) {
        add_check(&checks[nc++], "structure", "fail", "file is not valid JSON");
        add_issue(&is, "not_json", 0, 0, "evidence file cannot be parsed");
    } else {
        cust = jv_get(doc, "custody");
        events = jv_get(doc, "events");
        if (events && events->type != JV_ARRAY) {
            events = NULL;
        }
        legacy = !cust;
    }

    /* A manifest proves the file used to have a chain, even if "custody" was stripped. */
    mbuf = read_all(manifest_path, &mlen);
    if (mbuf) {
        have_manifest = 1;
        man = parse_buffer(mbuf, mlen);
        free(mbuf);
    }
    if (legacy && have_manifest) {
        legacy = 0;
    }
    /* Whoever pins a key expects signed evidence: stripping everything is no way out. */
    if (legacy && pubkey) {
        legacy = 0;
    }

    if (legacy) {
        status = is.total ? "failed" : "legacy_sidecar_ok";
        add_check(&checks[nc++], "chain", "skip", "schema 2 evidence: no hash chain to check");
    } else {
        const Jv *mev = jv_get(man, "evidence");
        const Jv *msig = jv_get(man, "signature");
        const char *mcount = jv_text(mev, "event_count");
        const char *genesis = jv_text(cust, "chain_genesis");
        int expected = mcount ? atoi(mcount) : 0;
        int before;

        if (expected < 0 || expected > FT_MAX_EVENTS) {
            expected = 0;
        }
        session = jv_text(cust, "session_id") ? jv_text(cust, "session_id") :
                  (jv_text(man, "session_id") ? jv_text(man, "session_id") : "");

        /* 2. session header */
        if (doc && cust && genesis) {
            const char *vals[FT_N_HEADER_FIELDS];
            char hex[FT_HASH_HEX];
            int complete = 1;

            for (int i = 0; i < FT_N_HEADER_FIELDS; i++) {
                vals[i] = header_value(doc, cust, ft_header_fields[i]);
                if (!vals[i]) {
                    complete = 0;
                }
            }
            if (complete && ft_hash_fields("ForensicTrace-chain-v1", ft_header_fields, vals,
                                           FT_N_HEADER_FIELDS, hex) == 0 && !strcmp(hex, genesis)) {
                add_check(&checks[nc++], "session_header", "ok",
                          "session, case, investigator and run summary match the chain genesis");
            } else {
                add_check(&checks[nc++], "session_header", "fail", "session header was modified");
                add_issue(&is, "header_modified", 0, 0,
                          "session header fields do not match the chain genesis");
            }
        } else if (doc) {
            add_check(&checks[nc++], "session_header", "fail", "custody block is missing");
            add_issue(&is, "custody_block_missing", 0, 0, "custody block was removed from the file");
        }

        /* 3. records */
        before = is.total;
        if (doc && genesis) {
            verify_records(events, genesis, expected, &is, tail, &checked);
            if (is.total == before) {
                add_check(&checks[nc++], "chain", "ok", "%d records verified, every link intact", checked);
            } else {
                add_check(&checks[nc++], "chain", "fail", "%d problem(s) in %d records",
                          is.total - before, checked);
            }
        } else if (doc) {
            add_check(&checks[nc++], "chain", "fail", "no chain to check");
        }

        /* 4. manifest binding */
        if (!man) {
            add_check(&checks[nc++], "manifest", "fail",
                      have_manifest ? "manifest is not valid JSON" : "manifest is missing");
            add_issue(&is, "manifest_missing", 0, 0, "%s", have_manifest ?
                      "manifest cannot be parsed" : "evidence manifest is missing");
        } else {
            const char *msha = jv_text(mev, "sha256");
            const char *mhead = jv_text(mev, "chain_head");
            const char *mgen = jv_text(mev, "chain_genesis");
            const char *mreport = safe_report_name(man);
            int mok = 1;

            /* Compare chain ends first: a recomputed chain is the sharper diagnosis. */
            if (genesis && is.record_level == 0 && mhead && mgen &&
                (strcmp(mhead, tail) || strcmp(mgen, genesis))) {
                mok = 0;
                add_issue(&is, "chain_rewritten", 0, 0,
                          "the chain is self-consistent but its ends differ from the manifest: "
                          "records were changed and the chain was recomputed");
            }
            if (!msha || strcmp(msha, file_hash)) {
                if (mok && is.record_level == 0) {
                    add_issue(&is, "file_modified", 0, 0,
                              "file differs from the manifest hash, but every record verifies: "
                              "the change is outside the chained fields or in the formatting");
                }
                mok = 0;
            }
            if (mreport) {
                char report_path[1600], rhex[FT_HASH_HEX];
                const char *rsha = jv_text(jv_get(man, "report"), "sha256");
                const char *slash = strrchr(evidence, '/');
                int dirlen = slash ? (int)(slash - evidence) + 1 : 0;

                snprintf(report_path, sizeof(report_path), "%.*s%s", dirlen, evidence, mreport);
                if (ft_sha256_file(report_path, rhex, NULL) != 0) {
                    /* reports may legitimately live elsewhere (--report can be any path) */
                    add_check(&checks[nc++], "report", "skip", "report %.200s not found next to the evidence", mreport);
                } else if (!rsha || strcmp(rsha, rhex)) {
                    add_check(&checks[nc++], "report", "fail", "report differs from the manifest hash");
                    add_issue(&is, "report_modified", 0, 0, "report %.200s was modified", mreport);
                } else {
                    add_check(&checks[nc++], "report", "ok", "report matches the manifest hash");
                }
            }
            add_check(&checks[nc++], "manifest", mok ? "ok" : "fail", "%s",
                      mok ? "evidence hash and chain ends match the manifest"
                          : "evidence does not match the manifest");
        }

        /* 5. signature */
        if (man && msig && msig->type == JV_OBJECT) {
            char err[160] = "";

            if (ft_signature_check(manifest_path, sig_path, pubkey,
                                   jv_text(msig, "public_key_b64"), fingerprint, err, sizeof(err)) == 0) {
                signed_ok = 1;
                pinned = pubkey != NULL;
                if (pinned) {
                    add_check(&checks[nc++], "signature", "ok", "manifest signed by the pinned key %.16s...", fingerprint);
                } else {
                    add_check(&checks[nc++], "signature", "warn",
                              "signature valid for the key in the manifest (%.16s...); pass --pubkey to prove who signed",
                              fingerprint);
                }
            } else {
                add_check(&checks[nc++], "signature", "fail", "%.300s", err);
                add_issue(&is, "signature_invalid", 0, 0, "%.300s", err);
            }
        } else if (man && pubkey) {
            add_check(&checks[nc++], "signature", "fail", "a pinned key was given but the manifest is unsigned");
            add_issue(&is, "signature_missing", 0, 0,
                      "manifest is unsigned although a signature was expected (--pubkey)");
        } else if (man) {
            add_check(&checks[nc++], "signature", "warn",
                      "manifest is unsigned: someone who rewrites every file would not be detected");
        }

        /* 6. audit log */
        {
            int bad = 0, gen = 0;
            char gen_sha[FT_HASH_HEX] = "";
            int n = audit_scan(audit_path, NULL, 0, &bad, &gen, gen_sha, sizeof(gen_sha));

            if (n < 0) {
                add_check(&checks[nc++], "audit_log", "fail", "audit log is missing");
                add_issue(&is, "audit_missing", 0, 0, "audit log is missing");
            } else if (bad) {
                add_check(&checks[nc++], "audit_log", "fail", "audit log is broken at entry %d", bad);
                add_issue(&is, "audit_broken", 0, 0, "audit log entry %d was modified or removed", bad);
            } else if (!gen) {
                add_check(&checks[nc++], "audit_log", "fail", "audit log has no generation entry");
                add_issue(&is, "audit_broken", 0, 0, "audit log has no generation entry");
            } else if (strcmp(gen_sha, file_hash)) {
                add_check(&checks[nc++], "audit_log", "fail",
                          "%d %s intact, but the file differs from the hash logged at generation",
                          n, n == 1 ? "entry" : "entries");
                add_issue(&is, "audit_hash_mismatch", 0, 0,
                          "file hash differs from the hash recorded at generation");
            } else {
                add_check(&checks[nc++], "audit_log", "ok", "%d %s, chain intact", n, n == 1 ? "entry" : "entries");
            }
        }

        if (is.total) {
            status = "failed";
        } else if (signed_ok && pinned) {
            status = "verified_signed_pinned";
        } else if (signed_ok) {
            status = "verified_signed_unpinned";
        } else {
            status = "verified_unsigned";
        }
    }

    rc = (!strcmp(status, "failed")) ? FT_VERIFY_FAILED : FT_VERIFY_OK;

    if (json_output) {
        printf("{\n  \"status\": \"%s\",\n  \"evidence_sha256\": \"%s\",\n", status, file_hash);
        printf("  \"session_id\": \"");
        ft_json_escape(stdout, session);
        printf("\",\n  \"records_checked\": %d,\n  \"key_fingerprint\": \"%s\",\n", checked, fingerprint);
        printf("  \"checks\": [\n");
        for (int i = 0; i < nc; i++) {
            printf("    {\"name\": \"%s\", \"state\": \"%s\", \"text\": \"", checks[i].name, checks[i].state);
            ft_json_escape(stdout, checks[i].text);
            printf("\"}%s\n", i + 1 < nc ? "," : "");
        }
        printf("  ],\n  \"issue_total\": %d,\n  \"issues\": [\n", is.total);
        for (int i = 0; i < is.total && i < MAX_LISTED_ISSUES; i++) {
            const Issue *u = &is.list[i];

            printf("    {\"kind\": \"%s\", \"first_event\": %d, \"last_event\": %d, \"text\": \"",
                   u->kind, u->first_id, u->last_id);
            ft_json_escape(stdout, u->text);
            printf("\"}%s\n", (i + 1 < is.total && i + 1 < MAX_LISTED_ISSUES) ? "," : "");
        }
        printf("  ]\n}\n");
    } else if (!quiet) {
        printf("Evidence : %s\nSHA-256  : %s\n", evidence, file_hash);
        if (session[0]) {
            printf("Session  : %s\n", session);
        }
        printf("\n");
        for (int i = 0; i < nc; i++) {
            const char *mark = !strcmp(checks[i].state, "ok") ? "PASS" :
                               !strcmp(checks[i].state, "fail") ? "FAIL" :
                               !strcmp(checks[i].state, "warn") ? "WARN" : "SKIP";

            printf("[%s] %-15s %s\n", mark, checks[i].name, checks[i].text);
        }
        if (is.total) {
            printf("\n%d problem(s):\n", is.total);
            for (int i = 0; i < is.total && i < MAX_LISTED_ISSUES; i++) {
                printf("  - %-20s %s\n", is.list[i].kind, is.list[i].text);
            }
            if (is.total > MAX_LISTED_ISSUES) {
                printf("  ... and %d more\n", is.total - MAX_LISTED_ISSUES);
            }
        }
        printf("\nResult: %s\n", status);
    }

    if (write_audit && !legacy) {
        char detail[96];

        snprintf(who, sizeof(who), "%s", investigator ? investigator : "");
        if (!who[0]) {
            ft_current_user(who, sizeof(who));
        }
        snprintf(detail, sizeof(detail), "%d records checked, %d problem(s)", checked, is.total);
        if (ft_audit_append(audit_path, "verified", session, who, file_hash, status, detail) != 0) {
            fprintf(stderr, "[verify] warning: could not record this verification in the audit log\n");
        }
    }
    if (status_out) {
        snprintf(status_out, statuslen, "%s", status);
    }
    jv_free(doc);
    jv_free(man);
    return rc;
}
