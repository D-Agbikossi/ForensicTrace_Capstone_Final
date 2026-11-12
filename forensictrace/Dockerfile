# Read-only public demo of the ForensicTrace dashboard, for a hosting platform.
# Hosting platforms block ptrace, so this image shows recorded evidence and verifies
# it, but cannot run new investigations. For the full tool, run it on Linux.
FROM debian:bookworm-slim AS build
RUN apt-get update && apt-get install -y --no-install-recommends gcc make libc6-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /src
COPY Makefile ./
COPY src ./src
RUN make

FROM python:3.12-slim-bookworm
WORKDIR /app
COPY . .
COPY --from=build /src/forensictrace ./forensictrace
ENV PORT=8377 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
EXPOSE 8377
USER nobody
CMD ["python3", "dashboard/server.py", "--public"]
