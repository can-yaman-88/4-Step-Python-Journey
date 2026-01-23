def pace_hesapla(mesafe_km, sure_dakika):
    pace = sure_dakika / mesafe_km
    return pace
def efor_hesapla(yukseklik_m, mesafe_km):
    efor = yukseklik_m / 100 +mesafe_km
    return efor
def kaydet(pace, efor):
    with open("öncekiveriler.txt", "a", encoding="utf-8") as dosya:
        """open ... adlı dosyayı açar ya da yoksa oluşturur.
        a ekleme yapar, append anlamındadır.
        encoding="utf-8" Türkçe karakterleri kullanabilmek için eklenir."""
        dosya.write(f"Pace: {pace} dk/km, Efor Puanı: {efor} \n")
        """Yukarıda as dosya diyerek dosyaya geçici bir isim verdim, dosya dedim.
        as file deseydim aşağıda file.write diyecektim.
        write dosyaya yazma işlemi yapar, yaptıktan sonra kapatır.
        \n yeni satır ekler."""
        """Metin kutusunun altına bir kod eklyemiyorum. Aynı sütunda olmaları gerek.
        Tab tuşuna basıp kod yazarsam hata veriyor."""
while True:
    islem=input("""Yapmak istediğiniz işlemi girin (pace, efor)
Çıkmak için 'q' ya basın: """).lower()
    """Burada .lover kullanarak kullanıcının girdiği metindeki tüm harfleri 
    küçük harfe çeviriyorum. Böylece Shift tuşuna basılıp basılmadığı önemsiz oluyor."""
    if islem == "pace":
        mesafe_km = float(input("Mesafe (km): "))
        sure_dakika = float(input("Süre (dakika): "))
        pace = pace_hesapla(mesafe_km, sure_dakika)
        print(f"Parkur Pace: {pace} dk/km")
        kaydet(pace, "N/A")
        """Burada anlıyorum ki fonksiyonun içindeki parametreleri
        fonksiyonun içinde tanımlamama gerek yok.
        O parametreleri fonksiyonu çağırırken verebiliyorum."""
    elif islem == "efor":
        yukseklik_m = float(input("Yükseklik (m): "))
        mesafe_km = float(input("Mesafe (km): "))
        efor = efor_hesapla(yukseklik_m, mesafe_km)
        print(f"Tahmini Efor Puanı: {efor}")
        kaydet("N/A", efor)
    elif islem == "q":
        break
    else:
        print("Geçersiz işlem. Lütfen 'pace', 'efor' veya 'q' girin.")