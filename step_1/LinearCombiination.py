y=[0,0]
print("u in Linear Combination of v1, v2, ..., vn with weights c1, c2, ..., cn\nu= c1*v1 + c2*v2 + ... + cn*vn")
n=int(input("Vektör girdilerinin sayısını giriniz: "))
for i in range(len(range(n))):
    v=[int(input(f"Vektör {i+1} için ilk bileşeni giriniz: ")), int(input(f"Vektör {i+1} için ikinci bileşeni giriniz: "))]
    c=int(input(f"Vektör {i+1} için ağırlık katsayısını giriniz: "))
    u1=c*v[0]
    u2=c*v[1]

    #ya her döngünün sonunda toplama yaparsam?
    #bu sayede her döngünün sonunda u vektörünün sıfırlanması sorununu aşabilirim.

    y[0] += c * v[0]
    y[1] += c * v[1]

    #yapay zekaya sordum ve bana bu şekilde yapmamı önerdi. 
    #sanırım burada döngünün sonunda bir önceki döngüdeki y değerini koruyup üzerine ekleme yapıyor.

print(y)

#şimdi bu döngüyü tekrar bir döngüye almam gerek ki vektörler arasında işlem yapabileyim.
#tekrar döngüye almama gerek kalmadı sanırım.
#evet kalmadı. Kod bu haliyle sorunnsuz çalışıyor. 
#Eklemeler yapılabilir ama şu an aklıma başka bir şey gelmiyor.