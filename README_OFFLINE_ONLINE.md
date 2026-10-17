# ÖZNUR AI — Çevrimdışı + Çevrimiçi

- Çevrimdışı ZIP okuma ve proje haritası
- Çevrimiçi/yerel API modu
- Otomatik mod: API varsa kullanır, yoksa yerel analize döner
- PWA ve responsive mobil/PC arayüzü
- ZIP sürükle-bırak
- Dosya arama
- Yerel proje hafızası
- Analiz JSON dışa aktarma
- PWA kurulum desteği
- Windows ve Termux kurulum başlatıcıları
- Kod çalıştırma katmanı yoktur

Windows: KUR_WINDOWS.bat
Termux: bash KUR_TERMUX.sh
Çalıştır: run_pwa_windows.bat veya bash run_pwa_android_termux.sh
Adres: http://127.0.0.1:8788


## Windows kurulum notu
`KUR_WINDOWS.bat` bağımsızdır ve `KUR_WINDOWS.ps1` dosyasına ihtiyaç duymaz. ZIP içinden veya geçici Windows klasöründen çalıştırıldığında da PS1 yol hatasına düşmemesi için Python ve `.venv` işlemlerini doğrudan BAT üzerinden yapar.
