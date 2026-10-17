# ÖZcod — Çevrimdışı Sistem (Windows + Android)

## Özellikler
- Kullanıcının `Sistem` sınıfındaki aşama sırası korunur: 01, 03, 05, 07, 09, 11, 13, 15, 17, 19, 21.
- Windows için Tkinter masaüstü arayüzü.
- Android/Termux için Python çekirdeği ve basit terminal arayüzü.
- Yerel yapay zekâ bağlantısı: OpenAI-uyumlu yerel HTTP endpoint'i. Varsayılan `http://127.0.0.1:8080/v1/chat/completions`.
- Uygulama kodu bulut API'sine bağlanmaz. Model sunucusu ve model dosyası ayrıca cihazda bulunmalıdır.

## Önemli sınırlar
- ZIP'in içine büyük bir yapay zekâ modeli dahil edilmemiştir.
- Yapay zekâ dönüşümü için yerel bir model çalıştırıcısı ve model dosyası gerekir. Örnek: `llama.cpp` server, OpenAI-uyumlu API modunda.
- Yerel model çalışmıyorsa uygulama dönüşüm yapamaz; hata mesajı gösterir. Sahte bir sonuç üretmez.
- 17. aşama güvenlik amacıyla kodu/komutları otomatik çalıştırmaz; yalnızca değerlendirme ve uygulanabilir adımları üretir.
- Android'de Windows masaüstü penceresi çalışmaz. Android tarafında Termux/Python terminal arayüzü sağlanmıştır. Gerçek Android APK için ayrıca Android Studio/Kotlin paketlemesi gerekir.

## Windows kurulumu
1. Python 3.10 veya üstünü kurun; kurulumda Python PATH seçeneğini etkinleştirin.
2. ZIP'i bir klasöre çıkarın.
3. Yerel model sunucunuzu başlatın. Sunucu OpenAI-uyumlu `/v1/chat/completions` endpoint'i sunmalıdır.
4. `run_windows.bat` dosyasına çift tıklayın.
5. Model endpoint'i ve model adını arayüzden ayarlayın.

## Android / Termux
1. ZIP'i Android'de bir klasöre çıkarın.
2. Termux'ta Python kurulu olmalıdır (`pkg install python`).
3. Proje klasörüne geçin.
4. Çekirdeği kullanmak için `python -m ozcod.android_cli` çalıştırın.
5. Yerel model sunucusunu aynı cihazda veya kendi yerel ağınızdaki güvenilir cihazda çalıştırın ve endpoint'i girin. Tamamen çevrimdışı kullanım için endpoint `127.0.0.1` olmalıdır.

## Test
Windows/macOS/Linux Python:
```bash
python -m unittest discover -s tests -v
```

## Aşamalar
- 01 İnsan metni: doğrudan giriş.
- 03 Metin analizi.
- 05 Bilgisayarın işleyebileceği görev tanımı.
- 07 Kod dosyası bağlamı.
- 09 Kod okuma.
- 11 Koddan insan diline çeviri.
- 13 Anlaşılır açıklama.
- 15 Biçimsel/kurallı adımlar.
- 17 Güvenli işlem planı; otomatik komut yürütmez.
- 19 Sonuç.
- 21 Nihai insan dili yanıtı.
