#!/data/data/com.termux/files/usr/bin/bash
set -eu
cd "$(dirname "$0")"
python api/server.py
