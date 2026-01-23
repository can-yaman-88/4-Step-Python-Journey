import numpy as np

# 1. MATRİSLERİ TANIMLA
# Katsayılar Matrisi (A)
# Cos135, Cos45
# Sin135, Sin45
A = np.array([
    [-0.7071, 0.7071], 
    [ 0.7071, 0.7071]
])

# Sonuç Vektörü (B)
# Yatayda net kuvvet 0
# Dikeyde yük 1000 Newton
B = np.array([0, 1000])

# 2. DENKLEMİ ÇÖZ (SOLVER)
# Bilgisayar burada "Back Substitution" yapıyor ama ışık hızında.
x = np.linalg.solve(A, B)

# 3. SONUCU YAZDIR
print("--- SONUÇLAR ---")
print(f"Halat 1 (T1) Gerilmesi: {x[0]:.2f} Newton")
print(f"Halat 2 (T2) Gerilmesi: {x[1]:.2f} Newton")

# SAĞLAMA (Opsiyonel ama önerilir)
print("\n--- SAĞLAMA ---")
print(f"Yatay Net Kuvvet: {np.dot(A[0], x):.2f} (0 olmalı)")
print(f"Dikey Net Kuvvet: {np.dot(A[1], x):.2f} (1000 olmalı)")