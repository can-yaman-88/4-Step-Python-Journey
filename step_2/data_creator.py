import pandas as pd
import numpy as np

# 1. Sanal Veri Üretimi
np.random.seed(42) # Her seferinde aynı rastgele sayıları üretmek için
zaman = np.arange(0, 600, 1) # 10 dakikalık koşu (600 saniye)

# Yükseklik: Önce düz, sonra yokuş yukarı, sonra iniş
yukseklik = 100 + np.concatenate([
    np.zeros(200),                # Düz
    np.linspace(0, 50, 200),      # Yokuş (50m tırmanış)
    np.linspace(50, 20, 200)      # İniş
]) + np.random.normal(0, 0.5, 600) # GPS Hatası (Gürültü)

# Hız: Yokuşta düşecek, inişte artacak
hiz_base = 4.0 # 4 m/s (yaklaşık 14.4 km/h)
hiz = hiz_base - (yukseklik - 100)/10 # Yükseklik arttıkça hız düşsün
hiz = np.clip(hiz, 1.0, 10.0) # Hız negatif olamaz
hiz += np.random.normal(0, 0.2, 600) # Anlık hız değişimleri

# Nabız: Eforla artar
nabiz = 120 + (hiz * 10) + (yukseklik - 100) * 0.5
nabiz += np.random.normal(0, 2, 600)

# DataFrame oluştur ve kaydet
df = pd.DataFrame({
    "Zaman_sn": zaman,
    "Yukseklik_m": yukseklik,
    "Hiz_ms": hiz,
    "Nabiz_bpm": nabiz
})

df.to_csv("run_data.csv", index=False)
print("Veri seti oluşturuldu: run_data.csv")