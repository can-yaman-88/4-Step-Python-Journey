print("u in Linear Combination of v1, v2, ..., vn with weights c1, c2, ..., cn\nu= c1*v1 + c2*v2 + ... + cn*vn")
print("Başka bir vektör eklemek için 'e' tuşuna basın, bitirmek için 'q' tuşuna basın.")
r=int(input("R^n uzayında çalışmak istediğiniz n değerini giriniz: "))
n=int(input("Vektör sayısını giriniz: "))
y=[0]*r
vs=[]
for i in range(n):
    while len(vs) < r:
        u = input(f"Vektör {i+1} için bileşen giriniz: ")
        if u != 'q':
            u = int(u)
            vs.append(u)
        else:
            break
#break dedikten sonra döngüden çıkıp c sayısını girmekle devam ediyor.
#vs listesindeki bir değişken eksik olduğu için hata veriyor.
#yapay zeka bunu düzeltmenin en temiz yolunun fonksiyon kullanmak olduğunu söyledi.
#fakat ben fonksiyon kullanmayı bilmediğim için şimdilik bu şekilde bırakacağım.

    c=int(input(f"Vektör {i+1} için ağırlık katsayısını giriniz: "))
    for k in range(r):
        y[k] += c*(vs[k])
        #burada for döngüsü ekleyip r kadar bileşen oluşturuyorum.
    vs=[]
#yapay zeka burada vs listesini sonradan tekrar boşaltmam gerektiğini söyledi.
#Fakat bunun neden olduğunu tam olarak anlayamadım.

print(y)

#burada if döngüsünü kullanmadan r değerine göre hareket ettim.
#iki veya başka belirli bir sayıda takılıp kalmadım.
#while döngüsünü kulllanarak da vektörlerin aynı sayıda bileşene sahip olmasını garantiledim.


#Yapay zekanın önerdiği kod:
    #print("u = c1*v1 + c2*v2 + ... + cn*vn")

    # 1. Uzay boyutunu ve vektör sayısını al
        #r = int(input("Hangi uzayda çalışacaksınız (R^n için n): "))
        #n = int(input("Kaç adet vektör toplayacaksınız: "))

    # 2. Sonuç vektörünü (y) dinamik olarak sıfırlarla başlat
    # Eğer r=3 ise y = [0, 0, 0] olur.
        #y = [0] * r 

    # 3. Ana döngü: Her vektör için döner
        #for i in range(n):
            #print(f"\n--- {i+1}. Vektör İşlemleri ---")
        
        # Geçici vektör deposunu (vs) her turda sıfırla
            #vs = [] 
        
        # Vektör bileşenlerini al
            #print(f"Vektör {i+1} bileşenlerini giriniz:")
            #for j in range(r):
                #bilesen = int(input(f"  {j+1}. bileşen: "))
                #vs.append(bilesen)
        
        # Ağırlık katsayısını (c) al
            #c = int(input(f"Vektör {i+1} için ağırlık (c{i+1}): "))
        
        # 4. Hesaplama ve Üzerine Ekleme (Logic Fix)
            #for k in range(r):
            # Eski değerin üzerine, yeni vektörün k katkısını ekle
                #y[k] += c * vs[k] 

    #print("\nSonuç Vektörü (Lineer Kombinasyon):")
    #print(y)