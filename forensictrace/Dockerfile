# Public demo of the ForensicTrace dashboard, for a hosting platform.
# Visitors can browse the recorded evidence and trace the five built-in scenarios
# (no command of their own). If the host does not permit ptrace, the server detects
# it at start-up and the demo stays read-only.
FROM debian:bookworm-slim AS build
RUN apt-get update && apt-get install -y --no-install-recommends gcc make libc6-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /src
COPY Makefile ./
COPY src ./src
RUN make

FROM python:3.12-slim-bookworm
# curl: the scenarios download their payloads with it. tini: reaps the processes traces leave behind.
RUN apt-get update && apt-get install -y --no-install-recommends curl tini \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
COPY --from=build /src/forensictrace ./forensictrace
RUN mkdir -p cases exports && chown nobody:nogroup cases exports
ENV PORT=8377 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HOME=/tmp/ft-home
# A small hosted instance can start the scenarios' local servers slowly; let curl wait for them.
ENV FT_CURL_RETRY="--retry 30 --retry-connrefused --retry-delay 1"
EXPOSE 8377
USER nobody
# A new signing key per container: evidence traced online is signed and verifiable,
# and the key never leaves the container.
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["sh", "-c", "mkdir -p \"$HOME/.config/forensictrace\" && ./forensictrace keygen --key \"$HOME/.config/forensictrace/investigator.key\" >/dev/null && exec python3 dashboard/server.py --public --allow-tracing"]
