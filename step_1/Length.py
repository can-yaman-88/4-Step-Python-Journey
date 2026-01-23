import math
print("Bitirmek için 'q' tuşuna basın.")
r=int(input("R^n uzayında çalışmak istediğiniz n değerini giriniz: "))
y=[]
for i in range(r):
    u = input("Vektör için bileşen giriniz: ")
    if u != 'q':
        u = int(u)
        y.append(u)
    else:
        break
sonuc=0
for k in range(r):
    sonuc += y[k]*y[k]
print(math.sqrt(sonuc))