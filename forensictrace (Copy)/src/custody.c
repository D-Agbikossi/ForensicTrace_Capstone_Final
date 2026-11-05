/*
 * custody.c — chain of custody for one investigation session.
 *
 *   hash chain   every event carries event_hash = SHA-256(prev_hash, its fields).
 *                The chain starts from a genesis hash over the session header, so
 *                records cannot be moved to another session unnoticed.
 *   manifest     <evidence>.manifest.json binds file hash, event count and chain
 *                ends. With --sign-key it is signed with Ed25519 into a detached
 *                <evidence>.manifest.sig, checkable with stock OpenSSL.
 *   audit log    <evidence>.audit.jsonl records generation, verification, export.
 *
 * Fields are hashed as "name=<byte length>:<value>\n" so values can never run
 * into each other; docs/custody.md specifies the format for independent checkers.
 */
#include "forensictrace.h"

#include <errno.h>
#include <fcntl.h>
#include <openssl/evp.h>
#include <openssl/pem.h>
#include <pwd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/random.h>
#include <sys/stat.h>
#include <sys/utsname.h>
#include <time.h>
#include <unistd.h>

const char *const ft_event_fields[FT_N_EVENT_FIELDS] = {
    "event_uid", "id", "ts_ns", "ts_wall", "type", "syscall", "pid", "ppid", "uid",
    "exe", "target", "detail", "ret", "parent_event", "resource_event"
};
const char *const ft_header_fields[FT_N_HEADER_FIELDS] = {
    "session_id", "case_id", "investigator", "os_user", "hostname", "kernel",
    "scenario", "command", "config", "collection_mode", "started_utc", "finished_utc",
    "event_count", "raw_event_count", "dropped_failed_exec", "truncated", "untraced_processes"
};

int ft_hash_fields(const char *prefix, const char *const *names,
                   const char *const *values, int n, char hex[FT_HASH_HEX])
{
    unsigned char hash[EVP_MAX_MD_SIZE];
    unsigned int hash_len = 0;
    EVP_MD_CTX *md = EVP_MD_CTX_new();
    int ok = md && EVP_DigestInit_ex(md, EVP_sha256(), NULL) == 1 &&
             EVP_DigestUpdate(md, prefix, strlen(prefix)) == 1 &&
             EVP_DigestUpdate(md, "\n", 1) == 1;

    for (int i = 0; ok && i < n; i++) {
        char len[32];
        size_t vl = strlen(values[i]);
        int ll = snprintf(len, sizeof(len), "=%zu:", vl);

        ok = EVP_DigestUpdate(md, names[i], strlen(names[i])) == 1 &&
             EVP_DigestUpdate(md, len, (size_t)ll) == 1 &&
             EVP_DigestUpdate(md, values[i], vl) == 1 &&
             EVP_DigestUpdate(md, "\n", 1) == 1;
    }
    ok = ok && EVP_DigestFinal_ex(md, hash, &hash_len) == 1 && hash_len == 32;
    EVP_MD_CTX_free(md);
    if (!ok) {
        return -1;
    }
    for (unsigned int i = 0; i < hash_len; i++) {
        snprintf(hex + i * 2, 3, "%02x", hash[i]);
    }
    return 0;
}

void ft_format_utc(int64_t wall_ns, char *out, size_t outlen)
{
    time_t sec = (time_t)(wall_ns / 1000000000LL);
    struct tm tm;
    char base[32];

    gmtime_r(&sec, &tm);
    strftime(base, sizeof(base), "%Y-%m-%dT%H:%M:%S", &tm);
    snprintf(out, outlen, "%.20s.%09lldZ", base, (long long)(wall_ns % 1000000000LL));
}

void ft_now_utc(char *out, size_t outlen)
{
    struct timespec ts;

    clock_gettime(CLOCK_REALTIME, &ts);
    ft_format_utc((int64_t)ts.tv_sec * 1000000000LL + ts.tv_nsec, out, outlen);
}

void ft_current_user(char *out, size_t outlen)
{
    struct passwd *pw = getpwuid(getuid());

    if (pw && pw->pw_name) {
        snprintf(out, outlen, "%s", pw->pw_name);
    } else {
        snprintf(out, outlen, "uid-%d", (int)getuid());
    }
}

void ft_event_uid(const char *session_id, int id, char *out, size_t outlen)
{
    snprintf(out, outlen, "%s-%06d", session_id, id);
}

static EVP_PKEY *load_private_key(const char *path)
{
    struct stat st;
    FILE *f = fopen(path, "r");
    EVP_PKEY *key;

    if (!f) {
        fprintf(stderr, "[custody] cannot open signing key %s: %s\n", path, strerror(errno));
        return NULL;
    }
    if (fstat(fileno(f), &st) == 0 && (st.st_mode & 077)) {
        fprintf(stderr, "[custody] warning: signing key %s is readable by other users\n", path);
    }
    key = PEM_read_PrivateKey(f, NULL, NULL, NULL);
    fclose(f);
    if (!key || EVP_PKEY_base_id(key) != EVP_PKEY_ED25519) {
        fprintf(stderr, "[custody] %s is not an Ed25519 private key (create one with: "
                        "forensictrace keygen --key <file>)\n", path);
        EVP_PKEY_free(key);
        return NULL;
    }
    return key;
}

int ft_custody_begin(FTContext *c, const char *investigator, const char *case_id,
                     const char *sign_key)
{
    FTCustody *u = &c->cust;
    unsigned char r[16];
    struct timespec real, mono;
    struct utsname un;

    if (sign_key) {
        EVP_PKEY *key = load_private_key(sign_key);

        if (!key) {
            return -1;
        }
        EVP_PKEY_free(key);
        snprintf(u->sign_key_path, sizeof(u->sign_key_path), "%s", sign_key);
    }
    if (getrandom(r, sizeof(r), 0) != (ssize_t)sizeof(r)) {
        fprintf(stderr, "[custody] cannot read random bytes for the session id\n");
        return -1;
    }
    r[6] = (unsigned char)((r[6] & 0x0f) | 0x40);   /* UUID version 4 */
    r[8] = (unsigned char)((r[8] & 0x3f) | 0x80);
    snprintf(u->session_id, sizeof(u->session_id),
             "%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x",
             r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7],
             r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15]);

    ft_current_user(u->os_user, sizeof(u->os_user));
    snprintf(u->investigator, sizeof(u->investigator), "%s", investigator ? investigator : u->os_user);
    snprintf(u->case_id, sizeof(u->case_id), "%s", case_id ? case_id : "UNASSIGNED");
    if (gethostname(u->hostname, sizeof(u->hostname) - 1) != 0) {
        snprintf(u->hostname, sizeof(u->hostname), "unknown");
    }
    if (uname(&un) == 0) {
        snprintf(u->kernel, sizeof(u->kernel), "%.60s %.60s", un.release, un.machine);
    }

    /* Events are stamped with CLOCK_MONOTONIC; this offset turns them into UTC. */
    clock_gettime(CLOCK_REALTIME, &real);
    clock_gettime(CLOCK_MONOTONIC, &mono);
    u->wall_offset_ns = ((int64_t)real.tv_sec - (int64_t)mono.tv_sec) * 1000000000LL +
                        ((int64_t)real.tv_nsec - (int64_t)mono.tv_nsec);
    ft_now_utc(u->started_utc, sizeof(u->started_utc));
    c->custody = 1;
    return 0;
}

int ft_custody_finalize(FTContext *c)
{
    FTCustody *u = &c->cust;
    uint64_t t0 = ft_now_ns();
    char n_events[16], n_raw[16], n_drop[16], n_untraced[16];
    const char *prev;

    ft_now_utc(u->finished_utc, sizeof(u->finished_utc));
    snprintf(n_events, sizeof(n_events), "%d", c->count);
    snprintf(n_raw, sizeof(n_raw), "%d", c->raw_count);
    snprintf(n_drop, sizeof(n_drop), "%d", c->dropped_failed_exec);
    snprintf(n_untraced, sizeof(n_untraced), "%d", c->untraced);

    const char *header[FT_N_HEADER_FIELDS] = {
        u->session_id, u->case_id, u->investigator, u->os_user, u->hostname, u->kernel,
        c->scenario, c->command, c->config, c->mode, u->started_utc, u->finished_utc,
        n_events, n_raw, n_drop, c->truncated ? "true" : "false", n_untraced
    };
    if (ft_hash_fields("ForensicTrace-chain-v1", ft_header_fields, header,
                       FT_N_HEADER_FIELDS, u->genesis) != 0) {
        return -1;
    }

    u->event_hash = calloc((size_t)(c->count ? c->count : 1), FT_HASH_HEX);
    if (!u->event_hash) {
        return -1;
    }
    prev = u->genesis;
    for (int i = 0; i < c->count; i++) {
        const Event *e = &c->events[i];
        char uid[64], id[16], ts[24], wall[40], pid[16], ppid[16], uidn[16], ret[24], pe[16], re[16];

        ft_event_uid(u->session_id, e->id, uid, sizeof(uid));
        snprintf(id, sizeof(id), "%d", e->id);
        snprintf(ts, sizeof(ts), "%llu", (unsigned long long)e->ts_ns);
        ft_format_utc((int64_t)e->ts_ns + u->wall_offset_ns, wall, sizeof(wall));
        snprintf(pid, sizeof(pid), "%d", (int)e->pid);
        snprintf(ppid, sizeof(ppid), "%d", (int)e->ppid);
        snprintf(uidn, sizeof(uidn), "%d", e->uid);
        if (e->ret_valid) {
            snprintf(ret, sizeof(ret), "%ld", e->ret);
        } else {
            snprintf(ret, sizeof(ret), "null");
        }
        snprintf(pe, sizeof(pe), "%d", c->parent_event[i]);
        snprintf(re, sizeof(re), "%d", c->resource_event[i]);

        const char *vals[FT_N_EVENT_FIELDS] = {
            uid, id, ts, wall, ft_type_name(e->type), e->syscall, pid, ppid, uidn,
            e->exe, e->target, e->detail, ret, pe, re
        };
        if (ft_hash_fields(prev, ft_event_fields, vals, FT_N_EVENT_FIELDS, u->event_hash[i]) != 0) {
            return -1;
        }
        prev = u->event_hash[i];
    }
    snprintf(u->head, sizeof(u->head), "%s", prev);
    u->chain_ns = ft_now_ns() - t0;
    return 0;
}

static const char *base_name(const char *path)
{
    const char *s = strrchr(path, '/');

    return s ? s + 1 : path;
}

static void mstr(FILE *f, const char *indent, const char *key, const char *val, int comma)
{
    fprintf(f, "%s\"%s\": \"", indent, key);
    ft_json_escape(f, val);
    fprintf(f, "\"%s\n", comma ? "," : "");
}

/* Sign the manifest bytes into the detached .sig. */
static int sign_file(const char *key_path, const char *in_path, const char *sig_path)
{
    EVP_PKEY *key = load_private_key(key_path);
    EVP_MD_CTX *md = NULL;
    unsigned char *msg = NULL, sig[64];
    size_t siglen = sizeof(sig);
    long size = 0;
    int ok = 0;
    FILE *f;

    if (!key) {
        return -1;
    }
    f = fopen(in_path, "rb");
    if (f && fseek(f, 0, SEEK_END) == 0 && (size = ftell(f)) > 0 && fseek(f, 0, SEEK_SET) == 0 &&
        (msg = malloc((size_t)size)) && fread(msg, 1, (size_t)size, f) == (size_t)size) {
        md = EVP_MD_CTX_new();
        ok = md && EVP_DigestSignInit(md, NULL, NULL, NULL, key) == 1 &&
             EVP_DigestSign(md, sig, &siglen, msg, (size_t)size) == 1;
    }
    if (f) {
        fclose(f);
    }
    EVP_MD_CTX_free(md);
    free(msg);
    EVP_PKEY_free(key);
    if (!ok) {
        return -1;
    }
    f = fopen(sig_path, "wb");
    if (!f) {
        return -1;
    }
    ok = fwrite(sig, 1, siglen, f) == siglen;
    if (fclose(f) != 0) {
        ok = 0;
    }
    return ok ? 0 : -1;
}

/* Public key as raw-base64 and fingerprint (SHA-256 of the 32 raw key bytes). */
static int public_key_id(EVP_PKEY *key, char *b64, char fingerprint[FT_HASH_HEX])
{
    unsigned char raw[32], digest[EVP_MAX_MD_SIZE];
    size_t rawlen = sizeof(raw);
    unsigned int dl = 0;

    if (EVP_PKEY_get_raw_public_key(key, raw, &rawlen) != 1 || rawlen != 32) {
        return -1;
    }
    if (b64) {
        EVP_EncodeBlock((unsigned char *)b64, raw, 32);
    }
    if (EVP_Digest(raw, 32, digest, &dl, EVP_sha256(), NULL) != 1) {
        return -1;
    }
    for (unsigned int i = 0; i < dl; i++) {
        snprintf(fingerprint + i * 2, 3, "%02x", digest[i]);
    }
    return 0;
}

int ft_manifest_write(FTContext *c)
{
    FTCustody *u = &c->cust;
    char path[1300], sig[1300], audit[1300], now[40];
    char report_hash[FT_HASH_HEX] = "";
    char key_b64[64] = "", fingerprint[FT_HASH_HEX] = "";
    FILE *f;

    snprintf(path, sizeof(path), "%s.manifest.json", c->output_path);
    snprintf(sig, sizeof(sig), "%s.manifest.sig", c->output_path);
    snprintf(audit, sizeof(audit), "%s.audit.jsonl", c->output_path);

    /* Re-running with the same --output must not inherit the old run's custody files. */
    unlink(sig);
    unlink(audit);

    if (c->report_path[0] && ft_sha256_file(c->report_path, report_hash, NULL) != 0) {
        fprintf(stderr, "[custody] cannot hash report %s\n", c->report_path);
        return -1;
    }
    if (u->sign_key_path[0]) {
        EVP_PKEY *key = load_private_key(u->sign_key_path);

        if (!key || public_key_id(key, key_b64, fingerprint) != 0) {
            EVP_PKEY_free(key);
            return -1;
        }
        EVP_PKEY_free(key);
    }

    f = fopen(path, "w");
    if (!f) {
        fprintf(stderr, "[custody] cannot write %s: %s\n", path, strerror(errno));
        return -1;
    }
    ft_now_utc(now, sizeof(now));
    fprintf(f, "{\n  \"manifest_version\": 1,\n");
    mstr(f, "  ", "tool", "ForensicTrace " FT_VERSION, 1);
    mstr(f, "  ", "session_id", u->session_id, 1);
    mstr(f, "  ", "case_id", u->case_id, 1);
    mstr(f, "  ", "investigator", u->investigator, 1);
    mstr(f, "  ", "os_user", u->os_user, 1);
    mstr(f, "  ", "hostname", u->hostname, 1);
    mstr(f, "  ", "kernel", u->kernel, 1);
    mstr(f, "  ", "started_utc", u->started_utc, 1);
    mstr(f, "  ", "finished_utc", u->finished_utc, 1);
    mstr(f, "  ", "generated_utc", now, 1);
    fprintf(f, "  \"evidence\": {\n");
    mstr(f, "    ", "file", base_name(c->output_path), 1);
    mstr(f, "    ", "sha256", c->sha256_hex, 1);
    fprintf(f, "    \"bytes\": %ld,\n    \"event_count\": %d,\n", c->storage_bytes, c->count);
    mstr(f, "    ", "chain_genesis", u->genesis, 1);
    mstr(f, "    ", "chain_head", u->head, 0);
    fprintf(f, "  },\n");
    if (report_hash[0]) {
        fprintf(f, "  \"report\": {\n");
        mstr(f, "    ", "file", base_name(c->report_path), 1);
        mstr(f, "    ", "sha256", report_hash, 0);
        fprintf(f, "  },\n");
    } else {
        fprintf(f, "  \"report\": null,\n");
    }
    if (u->sign_key_path[0]) {
        fprintf(f, "  \"signature\": {\n");
        mstr(f, "    ", "algorithm", "ed25519", 1);
        mstr(f, "    ", "public_key_b64", key_b64, 1);
        mstr(f, "    ", "key_fingerprint", fingerprint, 1);
        mstr(f, "    ", "file", base_name(sig), 0);
        fprintf(f, "  }\n}\n");
    } else {
        fprintf(f, "  \"signature\": null\n}\n");
    }
    if (fflush(f) != 0 || ferror(f)) {
        fclose(f);
        return -1;
    }
    fclose(f);

    if (u->sign_key_path[0] && sign_file(u->sign_key_path, path, sig) != 0) {
        fprintf(stderr, "[custody] signing failed: %s\n", u->sign_key_path);
        return -1;
    }
    fprintf(stderr, "[custody] session %s, chain head %.16s..., manifest %s\n",
            u->session_id, u->head, u->sign_key_path[0] ? "signed" : "UNSIGNED");
    return ft_audit_append(audit, "generated", u->session_id, u->investigator,
                           c->sha256_hex, u->sign_key_path[0] ? "signed" : "unsigned",
                           "evidence collected and hash chain sealed");
}

/*
 * Check the detached signature over the manifest bytes. With a pinned key the
 * signer is proven; with the embedded key only internal consistency is, because
 * anyone can re-sign with a key of their own and embed that instead.
 */
int ft_signature_check(const char *manifest_path, const char *sig_path,
                       const char *pubkey_path, const char *embedded_b64,
                       char fingerprint[FT_HASH_HEX], char *err, size_t errlen)
{
    EVP_PKEY *key = NULL;
    EVP_MD_CTX *md = NULL;
    unsigned char sig[128], *msg = NULL;
    size_t siglen = 0;
    long size = 0;
    int ok = 0;
    FILE *f;

    if (pubkey_path) {
        f = fopen(pubkey_path, "r");
        if (f) {
            key = PEM_read_PUBKEY(f, NULL, NULL, NULL);
            fclose(f);
        }
        if (!key || EVP_PKEY_base_id(key) != EVP_PKEY_ED25519) {
            snprintf(err, errlen, "cannot read pinned Ed25519 public key %s", pubkey_path);
            goto done;
        }
    } else {
        unsigned char raw[64];

        if (!embedded_b64 || strlen(embedded_b64) != 44 ||
            EVP_DecodeBlock(raw, (const unsigned char *)embedded_b64, 44) < 32) {
            snprintf(err, errlen, "manifest does not hold a valid public key");
            goto done;
        }
        key = EVP_PKEY_new_raw_public_key(EVP_PKEY_ED25519, NULL, raw, 32);
        if (!key) {
            snprintf(err, errlen, "manifest does not hold a valid public key");
            goto done;
        }
    }
    if (public_key_id(key, NULL, fingerprint) != 0) {
        snprintf(err, errlen, "cannot read the public key");
        goto done;
    }

    f = fopen(sig_path, "rb");
    if (!f) {
        snprintf(err, errlen, "signature file is missing");
        goto done;
    }
    siglen = fread(sig, 1, sizeof(sig), f);
    fclose(f);

    f = fopen(manifest_path, "rb");
    if (f && fseek(f, 0, SEEK_END) == 0 && (size = ftell(f)) >= 0 && fseek(f, 0, SEEK_SET) == 0 &&
        (msg = malloc((size_t)size + 1)) && fread(msg, 1, (size_t)size, f) == (size_t)size) {
        md = EVP_MD_CTX_new();
        ok = md && EVP_DigestVerifyInit(md, NULL, NULL, NULL, key) == 1 &&
             EVP_DigestVerify(md, sig, siglen, msg, (size_t)size) == 1;
    }
    if (f) {
        fclose(f);
    }
    if (!ok) {
        snprintf(err, errlen, "signature does not match the manifest and key");
    }
done:
    EVP_MD_CTX_free(md);
    EVP_PKEY_free(key);
    free(msg);
    return ok ? 0 : -1;
}

int ft_keygen(const char *key_path)
{
    char pub_path[1300];
    EVP_PKEY_CTX *pc = EVP_PKEY_CTX_new_id(EVP_PKEY_ED25519, NULL);
    EVP_PKEY *key = NULL;
    char fingerprint[FT_HASH_HEX];
    FILE *f;
    int fd;

    if (!pc || EVP_PKEY_keygen_init(pc) != 1 || EVP_PKEY_keygen(pc, &key) != 1) {
        EVP_PKEY_CTX_free(pc);
        fprintf(stderr, "[custody] key generation failed\n");
        return -1;
    }
    EVP_PKEY_CTX_free(pc);
    snprintf(pub_path, sizeof(pub_path), "%s.pub", key_path);

    if (ft_ensure_parent_dirs(key_path) != 0) {
        fprintf(stderr, "[custody] cannot create directory for %s\n", key_path);
        EVP_PKEY_free(key);
        return -1;
    }
    /* O_EXCL: an existing key may have signed evidence and is never overwritten. */
    fd = open(key_path, O_WRONLY | O_CREAT | O_EXCL, 0600);
    if (fd < 0) {
        fprintf(stderr, "[custody] cannot create %s: %s\n", key_path, strerror(errno));
        EVP_PKEY_free(key);
        return -1;
    }
    f = fdopen(fd, "w");
    if (!f || PEM_write_PrivateKey(f, key, NULL, NULL, 0, NULL, NULL) != 1) {
        fprintf(stderr, "[custody] cannot write %s\n", key_path);
        if (f) fclose(f);
        EVP_PKEY_free(key);
        return -1;
    }
    fclose(f);
    f = fopen(pub_path, "w");
    if (!f || PEM_write_PUBKEY(f, key) != 1) {
        fprintf(stderr, "[custody] cannot write %s\n", pub_path);
        if (f) fclose(f);
        EVP_PKEY_free(key);
        return -1;
    }
    fclose(f);
    public_key_id(key, NULL, fingerprint);
    EVP_PKEY_free(key);
    printf("private key : %s (keep this off the machine under investigation)\n", key_path);
    printf("public key  : %s (give this to whoever verifies the evidence)\n", pub_path);
    printf("fingerprint : %s\n", fingerprint);
    return 0;
}

/* Copy src to dst without overwriting; both hashes must agree afterwards. */
static int copy_exclusive(const char *src, const char *dst)
{
    char a[FT_HASH_HEX], b[FT_HASH_HEX], buf[8192];
    FILE *in = fopen(src, "rb");
    int fd;
    FILE *out;
    size_t n;

    if (!in) {
        return -1;
    }
    fd = open(dst, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0 || !(out = fdopen(fd, "wb"))) {
        fprintf(stderr, "[export] cannot create %s: %s\n", dst, strerror(errno));
        fclose(in);
        return -1;
    }
    while ((n = fread(buf, 1, sizeof(buf), in)) > 0) {
        if (fwrite(buf, 1, n, out) != n) {
            break;
        }
    }
    fclose(in);
    fclose(out);
    if (ft_sha256_file(src, a, NULL) != 0 || ft_sha256_file(dst, b, NULL) != 0 || strcmp(a, b)) {
        fprintf(stderr, "[export] copy of %s does not match the original\n", src);
        return -1;
    }
    return 0;
}

int ft_export(const char *evidence, const char *to_dir, const char *pubkey, const char *investigator)
{
    char status[64] = "", hex[FT_HASH_HEX], who[128], src[1300], dst[1500], session[64] = "";
    char manifest[1300], audit[1300], report[256] = "", report_src[1600], outcome[64];
    const char *base = base_name(evidence);
    FILE *f;
    int rc;

    rc = ft_verify(evidence, pubkey, 0, 1, 0, investigator, status, sizeof(status));
    if (rc == FT_VERIFY_ERROR || !strcmp(status, "legacy_sidecar_ok")) {
        fprintf(stderr, "[export] %s has no custody chain to export\n", evidence);
        return FT_VERIFY_ERROR;
    }
    if (rc == FT_VERIFY_FAILED) {
        fprintf(stderr, "[export] warning: verification FAILED; the failure is recorded and "
                        "travels with the bundle\n");
    }
    if (ft_sha256_file(evidence, hex, NULL) != 0) {
        return FT_VERIFY_ERROR;
    }
    snprintf(manifest, sizeof(manifest), "%s.manifest.json", evidence);
    snprintf(audit, sizeof(audit), "%s.audit.jsonl", evidence);
    ft_manifest_info(manifest, session, sizeof(session), report, sizeof(report));

    if (ft_ensure_parent_dirs(to_dir) != 0 || (mkdir(to_dir, 0755) != 0 && errno != EEXIST)) {
        fprintf(stderr, "[export] cannot create %s: %s\n", to_dir, strerror(errno));
        return FT_VERIFY_ERROR;
    }

    /* Log first, so the bundle's copy of the audit log includes this export. */
    snprintf(outcome, sizeof(outcome), "%s", status);
    snprintf(who, sizeof(who), "%s", investigator ? investigator : "");
    if (!who[0]) {
        ft_current_user(who, sizeof(who));
    }
    snprintf(dst, sizeof(dst), "exported to %s", to_dir);
    if (ft_audit_append(audit, "exported", session, who, hex, outcome, dst) != 0) {
        return FT_VERIFY_ERROR;
    }

    static const char *const suffixes[] = {"", ".manifest.json", ".manifest.sig", ".audit.jsonl"};
    for (size_t i = 0; i < sizeof(suffixes) / sizeof(suffixes[0]); i++) {
        snprintf(src, sizeof(src), "%s%s", evidence, suffixes[i]);
        if (access(src, R_OK) != 0) {
            continue;
        }
        snprintf(dst, sizeof(dst), "%s/%s%s", to_dir, base, suffixes[i]);
        if (copy_exclusive(src, dst) != 0) {
            return FT_VERIFY_ERROR;
        }
    }
    if (report[0]) {
        snprintf(report_src, sizeof(report_src), "%.*s%s", (int)(base - evidence), evidence, report);
        if (access(report_src, R_OK) == 0) {
            snprintf(dst, sizeof(dst), "%s/%s", to_dir, report);
            if (copy_exclusive(report_src, dst) != 0) {
                return FT_VERIFY_ERROR;
            }
        }
    }
    /* Sidecar names the file relative to the bundle, so sha256sum -c works from inside it. */
    snprintf(dst, sizeof(dst), "%s/%s.sha256", to_dir, base);
    f = fopen(dst, "w");
    if (!f) {
        return FT_VERIFY_ERROR;
    }
    fprintf(f, "%s  %s\n", hex, base);
    fclose(f);

    fprintf(stderr, "[export] bundle written to %s (status at export: %s)\n", to_dir, outcome);
    return rc;
}
