#Yapay zekanın oluşturduğu benim kodlarımın numpy kütüphanesi karşısında ne kadar yavaş çalıştığını göstermek için yazılmış bir kod.
import time
import numpy as np
import my_linear_algebra_library_V2 as mylib # Senin dosyanın adı

# 1. Matris Boyutu (Bilgisayarın çok yavaşsa 200 yap, iyiyse 500)
N = 300 
print(f"--- SİMÜLASYON BAŞLATILIYOR: {N}x{N} Matris Çarpımı ---")

# 2. Veri Oluşturma (NumPy arrayleri)
A_np = np.random.rand(N, N)
B_np = np.random.rand(N, N)

# 3. Listeye Çevirme (Senin fonksiyonun array kabul etmez, liste ister)
A_list = A_np.tolist()
B_list = B_np.tolist()

# --- RAUND 1: SENİN KÜTÜPHANEN ---
print("1. Senin Kodun çalışıyor... (Bekleyin, donabilir)")
start_manual = time.time()
# Senin fonksiyonunun adı 'matrix_multiplier'
res_manual = mylib.matrix_multiplier(A_list, B_list) 
end_manual = time.time()
manual_time = end_manual - start_manual
print(f"   TAMAMLANDI. Süre: {manual_time:.5f} saniye")

# --- RAUND 2: NUMPY ---
print("2. NumPy çalışıyor...")
start_numpy = time.time()
res_numpy = np.dot(A_np, B_np)
end_numpy = time.time()
numpy_time = end_numpy - start_numpy
print(f"   TAMAMLANDI. Süre: {numpy_time:.5f} saniye")

# --- SONUÇ ---
speedup = manual_time / numpy_time
print("-" * 30)
print(f"KAZANAN: NumPy")
print(f"HIZ FARKI: NumPy tam {speedup:.2f} KAT daha hızlı.")