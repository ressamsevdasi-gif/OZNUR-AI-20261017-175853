# OZNUR AI — Windows / Android / Offline / Online FULL PRO

## Temel çalışma modeli
- PWA arayüzü: `web/index.html`
- Yerel API: `api/server.py`
- Windows kurulum: `KUR_WINDOWS.bat`
- Windows başlatma: `run_pwa_windows.bat`
- Android/Termux kurulum: `KUR_TERMUX.sh`
- ZIP analizi: yalnızca okuma ve yapısal analiz
- Kod çalıştırma: KAPALI

## Windows
1. ZIP'i tamamen bir klasöre çıkartın.
2. `OZcod_Offline_Sistem\KUR_WINDOWS.bat` dosyasını çalıştırın.
3. Kurulum testi tamamlanınca `E` seçerek PWA/API'yi başlatabilirsiniz.
4. Tarayıcıdan `http://127.0.0.1:8788/` adresini açın.

`KUR_WINDOWS.bat` artık `KUR_WINDOWS.ps1` dosyasına bağımlı değildir.

## Özellikler
- Offline PWA arayüzü
- Online/API modu için API URL ayarı
- ZIP sürükle-bırak/yükleme
- ZIP dosya ağacı
- Kod/metin dosyası sayımı
- Satır ve karakter sayımı
- Dosya arama
- Proje özeti
- Mesaj alanı
- Yerel geçmiş/localStorage
- PWA kurulumu
- JSON analiz çıktısı
- Responsive mobil/masaüstü arayüz

## Güvenlik / sınır
ZIP içindeki dosyalar okunur ve analiz edilir; Python, JavaScript, shell veya başka proje kodu çalıştırılmaz. Yerel API `127.0.0.1:8788` üzerinde çalışır.


## Windows kurulum notu
KUR_WINDOWS.bat ZIP icinden calistirilirsa dosya secici acilir ve gercek ZIP secilerek tam paket cikartilir. Gömülü Base64/payload kullanılmaz.
