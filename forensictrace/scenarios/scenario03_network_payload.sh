#!/usr/bin/env bash
# Scenario 3: Network fetch -> write payload -> execute
set -e

WORKDIR="/tmp/ft_scenario03"
rm -rf "$WORKDIR"; mkdir -p "$WORKDIR"; cd "$WORKDIR"

echo "hello from server" > served.txt
python3 -m http.server 8766 --directory "$WORKDIR" >/dev/null 2>&1 &
SERVER=$!
# FT_CURL_RETRY (unset in the study) lets a slow host, such as the online demo, retry until the
# local server is up. The trap stops the servers if a step fails, so the trace always ends.
trap 'kill $SERVER 2>/dev/null || true' EXIT
sleep 0.5

curl -s ${FT_CURL_RETRY:-} "http://127.0.0.1:8766/served.txt" > fetched.txt

cat > runme.sh <<'EOF'
#!/bin/sh
echo "network payload executed"
EOF
chmod +x runme.sh
./runme.sh

kill $SERVER 2>/dev/null || true
wait $SERVER 2>/dev/null || true
