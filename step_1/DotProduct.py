print("u and v in R^n then \n u.v = c1*v1 + c2*v2 + ... + cn*vn")
print("Bitirmek için 'q' tuşuna basın.")
r=int(input("R^n uzayında çalışmak istediğiniz n değerini giriniz: "))
y1=[]
y2=[]
for i in range(r):
    u = input("Vektör 1 için bileşen giriniz: ")
    if u != 'q':
        u = int(u)
        y1.append(u)
    else:
        break
for j in range(r):
    u = input("Vektör 2 için bileşen giriniz: ")
    if u != 'q':
        u = int(u)
        y2.append(u)
    else:
        break
sonuc=0
for k in range(r):
    sonuc += y1[k]*y2[k]
print(sonuc)