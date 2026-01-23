import my_liner_algebra_library as myla
import my_liner_algebra_library as myla

# Denklem Sistemi:
# 1x + 1y + 1z = 6
# 0x + 2y + 5z = -4
# 2x + 5y - 1z = 27

A = [
    [1.0, 1.0, 1.0],
    [0.0, 2.0, 5.0],
    [2.0, 5.0, -1.0]
]
B = [6.0, -4.0, 27.0]

print("--- DENKLEM SİSTEMİ ÇÖZÜCÜ ---")
print("A Matrisi:", A)
print("B Vektörü:", B)

# 1. Genişletilmiş Matris Yap (Bunu kodlamıştın değil mi?)
# Eğer fonksiyon adın farklıysa düzelt.
M = myla.augmented_matrix(A, B) 

# 2. Echelon Forma Getir (Gaussian Elimination)
M_echelon = myla.echelon_form(M)

# 3. Geriye Doğru Çöz (Back Substitution)
sonuc_x = myla.back_substitution(A, B) # Senin fonksiyon A, B alıyor görünüyor görselde.

print("\nBULUNAN SONUÇLAR (x, y, z):")
print(sonuc_x)

# Beklenen: x=5, y=3, z=-2
# Sağlaması: 5 + 3 - 2 = 6 (Doğru)









A = [
    [2.0, 4.0, -2.0],
    [4.0, 9.0, -3.0],
    [-2.0, -3.0, 7.0]
]

B = [1,2,3]
sonuc_solution = myla.back_substitution(A,B)
print(sonuc_solution)


print("BAŞLANGIÇ:")
myla.matrix_show(A)

# Büyü başlasın
myla.echelon_form(A)

print("SONUÇ (ECHELON FORM):")
myla.matrix_show(A)

# BEKLENEN SONUÇ:
# [2.0,  4.0, -2.0]
# [0.0,  1.0,  1.0]
# [0.0,  0.0,  4.0]
# (Küçük ondalık farklar olabilir, önemli değil)



#A = [[0,2,5],[4,5,6],[7,8,9]]
#sonuc = myla.echelon_form(A)
#print(sonuc)



print("--- TEST 1: Liste Matris Çevirici ---")
liste = [1, 2, 3, 4]
matris_A = myla.list_to_matrix(liste, 2, 3)
print(f"Girdi Listesi: {liste}")
print(f"Oluşan Matris (2x3): {matris_A}")

print("\n--- TEST 2: İç Çarpım (Dot Product) ---")
v1 = [1, 2, 3]
v2 = [4, 5, 6]
# Beklenen: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
sonuc_dot = myla.dot_product(v1, v2)
print(f"Vektör 1: {v1}")
print(f"Vektör 2: {v2}")
print(f"İç Çarpım Sonucu: {sonuc_dot}")
if sonuc_dot == 32:
    print("✅ TEST BAŞARILI")
else:
    print("❌ TEST BAŞARISIZ")

print("\n--- TEST 3: Matris Çarpımı (THE BOSS) ---")
# Matris X (2x3)
X = [
    [1, 2, 3],
    [4, 5, 6]
]
# Matris Y (3x2)
Y = [
    [7, 8],
    [9, 1],
    [2, 3]
]
# Beklenen Hesap:
# [1*7+2*9+3*2,  1*8+2*1+3*3]   -> [31, 19]
# [4*7+5*9+6*2,  4*8+5*1+6*3]   -> [85, 55]

carpim_sonucu = myla.matrix_çarpım(X, Y)
print("Matris X:")
print(X)
print("Matris Y:")
print(Y)
print("Çarpım Sonucu:")
print(carpim_sonucu)

beklenen = [[31, 19], [85, 55]]
if carpim_sonucu == beklenen:
    print("✅ TEST BAŞARILI")
else:
    print("❌ TEST BAŞARISIZ")