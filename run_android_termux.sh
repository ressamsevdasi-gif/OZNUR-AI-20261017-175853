#!/data/data/com.termux/files/usr/bin/bash
set -eu
cd "$(dirname "$0")"
echo "ÖZcod çekirdek dosyaları hazır."
echo "Android'de yerel model sunucusunu ayrı başlatın; örnek endpoint:"
echo "http://127.0.0.1:8080/v1/chat/completions"
echo "Python arayüzünü Termux'ta çalıştırmak için: python -m ozcod.android_cli"
