import tkinter as tk
from tkinter import ttk, messagebox
import threading
from .core import Sistem, LocalAI

DEFAULT_ENDPOINT = "http://127.0.0.1:8080/v1/chat/completions"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ÖZcod — Çevrimdışı Sistem")
        self.geometry("900x720")
        self.minsize(680, 540)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        ttk.Label(self, text="ÖZcod — Yerel Yapay Zekâ Sistemi",
                  font=("Segoe UI", 16, "bold")).grid(row=0, column=0, sticky="w", padx=14, pady=(12, 4))
        settings = ttk.Frame(self)
        settings.grid(row=1, column=0, sticky="ew", padx=14, pady=6)
        settings.columnconfigure(1, weight=1)
        ttk.Label(settings, text="Yerel model adresi:").grid(row=0, column=0, sticky="w")
        self.endpoint = tk.StringVar(value=DEFAULT_ENDPOINT)
        ttk.Entry(settings, textvariable=self.endpoint).grid(row=0, column=1, sticky="ew", padx=8)
        ttk.Label(settings, text="Model adı:").grid(row=1, column=0, sticky="w", pady=5)
        self.model = tk.StringVar(value="local-model")
        ttk.Entry(settings, textvariable=self.model).grid(row=1, column=1, sticky="ew", padx=8, pady=5)
        ttk.Label(self, text="Girdi — metin veya kod:").grid(row=2, column=0, sticky="w", padx=14, pady=(8, 2))
        self.input = tk.Text(self, height=10, wrap="word")
        self.input.grid(row=3, column=0, sticky="nsew", padx=14, pady=(0, 8))
        bottom = ttk.Frame(self)
        bottom.grid(row=4, column=0, sticky="ew", padx=14, pady=4)
        self.run_button = ttk.Button(bottom, text="Çalıştır", command=self.run)
        self.run_button.pack(side="left")
        ttk.Button(bottom, text="Girdiyi temizle", command=lambda: self.input.delete("1.0", "end")).pack(side="left", padx=8)
        ttk.Label(self, text="Sonuç:").grid(row=5, column=0, sticky="w", padx=14, pady=(8, 2))
        self.output = tk.Text(self, height=12, wrap="word")
        self.output.grid(row=6, column=0, sticky="nsew", padx=14, pady=(0, 14))
        self.rowconfigure(6, weight=1)
        self.status = tk.StringVar(value="Hazır. İnternet gerekmez; yerel model sunucusu çalışıyor olmalıdır.")
        ttk.Label(self, textvariable=self.status, relief="sunken", anchor="w").grid(row=7, column=0, sticky="ew")

    def run(self):
        text = self.input.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Girdi gerekli", "Lütfen metin veya kod girin.")
            return
        self.run_button.configure(state="disabled")
        self.output.delete("1.0", "end")
        self.status.set("Yerel model çalışıyor…")
        def work():
            try:
                ai = LocalAI(self.endpoint.get().strip(), self.model.get().strip() or "local-model")
                result = Sistem(ai=ai).calistir(text)
                self.after(0, lambda: self.show_result(result))
            except Exception as exc:
                self.after(0, lambda: self.show_error(str(exc)))
        threading.Thread(target=work, daemon=True).start()

    def show_result(self, result):
        self.output.insert("1.0", result)
        self.status.set("Tamamlandı.")
        self.run_button.configure(state="normal")

    def show_error(self, error):
        self.output.insert("1.0", "HATA:\n" + error)
        self.status.set("İşlem tamamlanamadı.")
        self.run_button.configure(state="normal")

if __name__ == "__main__":
    App().mainloop()
