# ÖZNUR AI — Profesyonel PWA/API sürümü

Bu sürüm mevcut ÖZcod çekirdeğini koruyarak bağımsız bir web arayüzü ve yerel API katmanı ekler.

## Çalıştırma
Windows:
`run_pwa_windows.bat`

Android/Termux:
`bash run_pwa_android_termux.sh`

Tarayıcı:
`http://127.0.0.1:8788`

## Tasarım
- Responsive mobil / tablet / PC
- Sol menü + mobil alt menü
- ÖZNUR AI logo alanı
- ZIP yükleme
- Proje özeti
- Dosya haritası
- Mesaj ekranı
- PWA manifest + service worker
- Yerel API

## Çalıştırma politikası
ZIP içeriği yalnızca okunur. API kodu execute/subprocess/eval/exec kullanmaz.
Kod dosyaları çalıştırılmaz.

## Platform
Web/PWA aynı UI çekirdeğidir. Windows EXE için WebView2/Tauri/Electron gibi bir kabuk kullanılabilir; iOS için PWA ana ekrana eklenebilir veya aynı web çekirdeği native shell'e alınabilir.
