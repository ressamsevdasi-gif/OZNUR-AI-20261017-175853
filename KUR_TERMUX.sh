#!/data/data/com.termux/files/usr/bin/bash
set -eu
cd "$(dirname "$0")"
command -v python >/dev/null || { echo "Python gerekli: pkg install python"; exit 1; }
python api/server.py
