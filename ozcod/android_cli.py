"""Basit çevrimdışı terminal arayüzü; Android/Termux veya masaüstü Python."""
from .core import Sistem, LocalAI

def main():
    endpoint = input("Yerel model endpoint'i [http://127.0.0.1:8080/v1/chat/completions]: ").strip()
    if not endpoint:
        endpoint = "http://127.0.0.1:8080/v1/chat/completions"
    model = input("Model adı [local-model]: ").strip() or "local-model"
    print("Metni/kodu girin. Bitirmek için tek başına EOF kullanın (Termux: Ctrl+D).")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    try:
        print("\nSONUÇ:\n")
        print(Sistem(LocalAI(endpoint, model)).calistir("\n".join(lines)))
    except Exception as exc:
        print("HATA:", exc)

if __name__ == "__main__":
    main()
