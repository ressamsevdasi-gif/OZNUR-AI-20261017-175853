from dataclasses import dataclass
from typing import Callable, Optional
import json
import urllib.request
import urllib.error

@dataclass
class StageResult:
    number: int
    name: str
    value: str

class LocalAI:
    """Yalnızca kullanıcının cihazındaki yerel OpenAI-uyumlu uç noktaya bağlanır."""
    def __init__(self, endpoint="http://127.0.0.1:8080/v1/chat/completions",
                 model="local-model", timeout=120):
        self.endpoint = endpoint
        self.model = model
        self.timeout = timeout

    def generate(self, instruction: str, text: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": (
                    "Sen çevrimdışı çalışan bir kod ve metin asistanısın. "
                    "Yalnızca verilen görevi yap. Bilmediğin şeyi uydurma. "
                    "Kod çalıştırma; kodu analiz et ve açıkla."
                )},
                {"role": "user", "content": instruction + "\n\nGİRDİ:\n" + text}
            ],
            "temperature": 0.2
        }
        req = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"].strip()
        except urllib.error.URLError as exc:
            raise RuntimeError(
                "Yerel AI modeline bağlanılamadı. Model sunucusunu cihazda başlatın. "
                "Bu uygulama bulut servisine bağlanmaz. Ayrıntı: " + str(exc)
            ) from exc
        except (KeyError, IndexError, ValueError) as exc:
            raise RuntimeError("Yerel model beklenen yanıt biçimini döndürmedi.") from exc

class Sistem:
    """Kullanıcının 11 işlem aşamasını aynı sırayla koruyan işlem hattı."""
    STAGES = [
        (1, "İnsan metni"),
        (3, "Metin analiz sistemi"),
        (5, "Bilgisayar dili"),
        (7, "Kod dosyası"),
        (9, "Kod okuma sistemi"),
        (11, "Kod → insan dili"),
        (13, "Anlaşılır açıklama"),
        (15, "Biçimsel dil"),
        (17, "İşlem"),
        (19, "Sonuç"),
        (21, "İnsan dili"),
    ]

    def __init__(self, ai: Optional[LocalAI] = None, progress: Optional[Callable] = None):
        self.ai = ai or LocalAI()
        self.progress = progress

    def _run(self, number, name, instruction, value):
        output = self.ai.generate(instruction, value)
        if self.progress:
            self.progress(StageResult(number, name, output))
        return output

    def calistir(self, giris_verisi: str) -> str:
        if not isinstance(giris_verisi, str) or not giris_verisi.strip():
            raise ValueError("Lütfen işlenecek bir metin veya kod girin.")

        adim_01 = giris_verisi
        if self.progress:
            self.progress(StageResult(1, "İnsan metni", adim_01))

        adim_03 = self._run(3, "Metin analiz sistemi",
            "Metni analiz et. Amacı, türünü, ana unsurlarını ve belirsizlikleri kısa maddelerle belirle.", adim_01)
        adim_05 = self._run(5, "Bilgisayar dili",
            "Analizden hareketle bilgisayarın işleyebileceği açık, yapılandırılmış bir görev tanımı oluştur. Gerekirse JSON benzeri biçim kullan; geçerli JSON şart değil.", adim_03)
        adim_07 = self._run(7, "Kod dosyası",
            "Görev bir kod dosyasıyla ilgiliyse dosya türünü, olası dosya adını ve gereken içeriği belirt. Dosya içeriği verilmediyse bunu açıkça söyle; dosya uydurma.", adim_05)
        adim_09 = self._run(9, "Kod okuma sistemi",
            "Verilen kodu veya yapılandırılmış içeriği satır/sorumluluk düzeyinde incele. Kod verilmemişse hangi bilginin eksik olduğunu belirt.", adim_07)
        adim_11 = self._run(11, "Kod → insan dili",
            "Önceki çıktıyı teknik doğruluğu koruyarak anlaşılır Türkçeye çevir.", adim_09)
        adim_13 = self._run(13, "Anlaşılır açıklama",
            "Açıklamayı düzenle: amaç, nasıl çalıştığı, girdiler, çıktılar ve sınırlamalar.", adim_11)
        adim_15 = self._run(15, "Biçimsel dil",
            "Açıklamayı kesin ve sıralı işlem adımlarına dönüştür. Gereksinim uydurma; belirsizlikleri işaretle.", adim_13)
        adim_17 = self._run(17, "İşlem",
            "Bu aşamada yalnızca görev tanımını değerlendir. Harici komut çalıştırma, dosya değiştirme veya sistemde işlem yapma. Uygulanabilir adımları ve doğrulamaları yaz.", adim_15)
        adim_19 = self._run(19, "Sonuç",
            "Önceki değerlendirmeden sonucu, yapılan ve yapılmayan işlemleri ayırarak çıkar.", adim_17)
        adim_21 = self._run(21, "İnsan dili",
            "Kullanıcıya verilecek nihai yanıtı açık, kısa ve anlaşılır Türkçe ile yaz. Varsayımları ve sınırlamaları belirt.", adim_19)
        return adim_21
