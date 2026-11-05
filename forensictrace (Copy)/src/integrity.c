/* integrity.c — SHA-256 sidecar for output JSON (GNU sha256sum format). */
#include "forensictrace.h"

#include <openssl/evp.h>
#include <stdio.h>
#include <string.h>

/* SHA-256 of a file as lowercase hex; size receives the byte count if not NULL. */
int ft_sha256_file(const char *path, char hex[FT_HASH_HEX], long *size)
{
    FILE *in = fopen(path, "rb");
    unsigned char buf[8192];
    unsigned char hash[EVP_MAX_MD_SIZE];
    unsigned int hash_len = 0;
    long total = 0;
    size_t n;
    int ok;
    EVP_MD_CTX *mdctx;

    if (!in) {
        return -1;
    }
    mdctx = EVP_MD_CTX_new();
    ok = mdctx && EVP_DigestInit_ex(mdctx, EVP_sha256(), NULL) == 1;
    while (ok && (n = fread(buf, 1, sizeof(buf), in)) > 0) {
        ok = EVP_DigestUpdate(mdctx, buf, n) == 1;
        total += (long)n;
    }
    ok = ok && !ferror(in) && EVP_DigestFinal_ex(mdctx, hash, &hash_len) == 1 && hash_len == 32;
    EVP_MD_CTX_free(mdctx);
    fclose(in);
    if (!ok) {
        return -1;
    }
    for (unsigned int i = 0; i < hash_len; i++) {
        snprintf(hex + i * 2, 3, "%02x", hash[i]);
    }
    if (size) {
        *size = total;
    }
    return 0;
}

int ft_integrity_write(FTContext *c)
{
    char sidecar[1200];
    char hex[FT_HASH_HEX];
    FILE *out;

    if (!c || !c->output_path[0]) {
        return -1;
    }

    if (ft_sha256_file(c->output_path, hex, NULL) != 0) {
        fprintf(stderr, "[integrity] cannot hash %s\n", c->output_path);
        return -1;
    }
    snprintf(c->sha256_hex, sizeof(c->sha256_hex), "%s", hex);

    snprintf(sidecar, sizeof(sidecar), "%s.sha256", c->output_path);
    out = fopen(sidecar, "w");
    if (!out) {
        fprintf(stderr, "[integrity] cannot write %s\n", sidecar);
        return -1;
    }
    fprintf(out, "%s  %s\n", hex, c->output_path);
    fclose(out);

    /* stdout is reserved for the timeline; operational messages go to stderr */
    fprintf(stderr, "[integrity] SHA-256: %s\n", hex);
    fprintf(stderr, "[integrity] written to %s\n", sidecar);
    return 0;
}
