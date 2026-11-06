#!/bin/sh
# Closes azimuth.exe without cutting a save short: asks it to close, then, if it's still there,
# force-closes it only once the saves folder has been quiet for 15 s (a kill mid-save leaves a
# revision Azimuth rejects).
SAVES=/d/Games/FH2/azimuth-windows/data/titles/1A96545B/saves
running() { tasklist //FI "IMAGENAME eq azimuth.exe" | grep -q azimuth; }
running || exit 0
taskkill //IM azimuth.exe >/dev/null 2>&1
for i in $(seq 1 10); do running || exit 0; sleep 1; done
for i in $(seq 1 60); do
  newest=$(find "$SAVES" -type f -printf '%T@\n' 2>/dev/null | sort -n | tail -1 | cut -d. -f1)
  now=$(date +%s)
  if [ $((now - ${newest:-0})) -ge 15 ]; then
    taskkill //IM azimuth.exe //F >/dev/null 2>&1
    for j in $(seq 1 10); do running || exit 0; sleep 1; done
  fi
  sleep 1
done
echo "azimuth.exe is still running" >&2
exit 1
