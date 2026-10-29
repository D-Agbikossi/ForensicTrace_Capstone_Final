# ForensicTrace prototype — C11, -Wall -Wextra, links OpenSSL for SHA-256 sidecar.
CC      := gcc
CFLAGS  := -Wall -Wextra -std=c11 -O2 -D_GNU_SOURCE -I src
LDFLAGS := -lcrypto

SRCS := src/main.c \
        src/collector.c \
        src/normaliser.c \
        src/correlator.c \
        src/reconstructor.c \
        src/metrics.c \
        src/report.c \
        src/json_writer.c \
        src/integrity.c

OBJS := $(SRCS:.c=.o)

BIN := forensictrace

.PHONY: all clean test asan

all: $(BIN)

$(BIN): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

src/%.o: src/%.c src/forensictrace.h
	$(CC) $(CFLAGS) -c -o $@ $<

# Memory/UB-checked build for development: make asan && ./forensictrace_asan ...
asan: $(SRCS) src/forensictrace.h
	$(CC) $(CFLAGS) -g -O1 -fsanitize=address,undefined -o forensictrace_asan $(SRCS) $(LDFLAGS)

clean:
	rm -f $(OBJS) $(BIN) forensictrace_asan

test: $(BIN)
	./tests/run_tests.sh
