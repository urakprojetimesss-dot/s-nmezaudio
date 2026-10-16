import sounddevice as sd
import numpy as np
import keyboard
import time
import threading
import tkinter as tk

# Ayarlar
THRESHOLD = 0.445  # Ortamına göre buradaki eşik değerini değiştirebilirsin
SAMPLE_RATE = 44100

class SesKontrolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Riskli Ses Dedektörü")
        self.root.geometry("320x220")
        self.root.config(bg="#f0f0f0")
        
        self.is_running = False

        # Başlık Etiketi
        self.title_label = tk.Label(root, text="Kulaklık Ses Dedektörü", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=15)

        # Durum Göstergesi
        self.status_label = tk.Label(root, text="Durum: Durduruldu", font=("Arial", 11), fg="red", bg="#f0f0f0")
        self.status_label.pack(pady=5)

        # Başlat Butonu
        self.btn_start = tk.Button(root, text="BAŞLAT", font=("Arial", 12, "bold"), bg="green", fg="white", width=15, command=self.baslat)
        self.btn_start.pack(pady=5)

        # Durdur Butonu
        self.btn_stop = tk.Button(root, text="DURDUR", font=("Arial", 12, "bold"), bg="gray", fg="white", width=15, command=self.durdur, state=tk.DISABLED)
        self.btn_stop.pack(pady=5)

    def baslat(self):
        if not self.is_running:
            self.is_running = True
            self.status_label.config(text="Durum: Ses Dinleniyor...", fg="green")
            self.btn_start.config(state=tk.DISABLED, bg="gray")
            self.btn_stop.config(state=tk.NORMAL, bg="red")
            
            # Ses dinleme işlemini arayüzü dondurmasın diye arka planda (thread) başlatıyoruz
            self.thread = threading.Thread(target=self.ses_dinle_dongusu, daemon=True)
            self.thread.start()

    def durdur(self):
        if self.is_running:
            self.is_running = False
            self.status_label.config(text="Durum: Durduruldu", fg="red")
            self.btn_start.config(state=tk.NORMAL, bg="green")
            self.btn_stop.config(state=tk.DISABLED, bg="gray")

    def ses_dinle_dongusu(self):
        def callback(indata, frames, time_info, status):
            if not self.is_running:
                return
            volume_norm = np.linalg.norm(indata) / np.sqrt(len(indata))
            
            if volume_norm > THRESHOLD and self.is_running:
                print(f"⚠️ Yüksek ses tespit edildi! Seviye: {volume_norm:.4f}")
                keyboard.send("stop media")
                time.sleep(1)

        try:
            with sd.InputStream(callback=callback, channels=1, samplerate=SAMPLE_RATE):
                while self.is_running:
                    time.sleep(0.1)
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SesKontrolApp(root)
    root.mainloop()