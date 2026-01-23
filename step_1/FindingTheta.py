import math
print("Bitirmek için 'q' tuşuna basın.")
r=int(input("R^n uzayında çalışmak istediğiniz n değerini giriniz: "))
if r <= 1:
    print("Uzay boyutu en az 1 olmalıdır.")
    exit()
y1=[]
y2=[]
for i in range(r):
    u = input("Vektör 1 için bileşen giriniz: ")
    if u == ' ' or u == '':
        print("Boş giriş geçersizdir. Lütfen bir sayı giriniz.")
    elif u != 'q':
        u = int(u)
        y1.append(u)
    else:
        break
for j in range(r):
    u = input("Vektör 2 için bileşen giriniz: ")
    if u == ' ' or u == '':
        print("Boş giriş geçersizdir. Lütfen bir sayı giriniz.")
    elif u != 'q':
        u = int(u)
        y2.append(u)
    else:
        break
sonuc_dot = 0
for d in range(r):
    sonuc_dot += y1[d]*y2[d]
sonuc_norm1 = 0
for k1 in range(r):
    sonuc_norm1 += y1[k1]*y1[k1]
if sonuc_norm1 == 0:
    print("Birinci vektörün normu sıfır olduğu için açı tanımsızdır.")
    exit()
norm1 = math.sqrt(sonuc_norm1)
sonuc_norm2 = 0
for k2 in range(r):
    sonuc_norm2 += y2[k2]*y2[k2]
if sonuc_norm2 == 0:
    print("İkinci vektörün normu sıfır olduğu için açı tanımsızdır.")
    exit()
norm2 = math.sqrt(sonuc_norm2)
theta = math.acos(sonuc_dot / (norm1 * norm2))
theta_degrees = math.degrees(theta)
print(f"Vektörler arasındaki açı (radyan cinsinden): {theta}")
print(f"Vektörler arasındaki açı (derece cinsinden): {theta_degrees}")