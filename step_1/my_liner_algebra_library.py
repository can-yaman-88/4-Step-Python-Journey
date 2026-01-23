def augmented_matrix(A, B):
    M = [row[:] for row in A]
    for i in range(len(M)):
        M[i].append(B[i])
    return M



def back_substitution(A,B):
    M = augmented_matrix(A, B)
    M = echelon_form(M)
    n = len(M)
    x = [0.0] * n
    for i in range(n-1,-1,-1):
        toplam = 0
        for j in range(i+1,n):
            toplam += M[i][j] * x[j]
        x[i] = (M[i][n] - toplam)/M[i][i]
    return x
#İtiraf etmeliyim ki bu fonksiyonu yazarken yapay zekadan fazlaca yardım aldım.
#Çünkü o toplam mantığını anlamadım ve toplam değişkenini sürekli yanlış yere koydum.
#Şimdi yazdıktan sonra bile diğer tüm kodların aksine nasıl çalıştığını pek anlamış değilim.
#Augmented fonksiyonu fazlasıyla kolaydı fakat bunu anlamak bir hayli zor.


    
        



def echelon_form(M):
    rows = len(M)
    columns = len(M[0])
    for j in range(columns):
        for i in range(j+1,rows):
            if M[j][j] == 0:
                for k in range(j+1,rows):
                    if M[k][j] != 0:
                        row_exchange(M, j, k)
                        break
            c = -M[i][j] / M[j][j]
            row_addition(M, i, j, c)
    return M





def matrix_show(M):
    for i in M:
        print(i)

def row_exchange(M, r1, r2):
    M[r1], M[r2] = M[r2], M[r1]
    return M

def row_multiplier(M, r, c):
    for i in range(len(M[r])):
        M[r-1][i] *= c
    return M

def row_addition(M, main_row, added_row, coefficient):
    for i in range(len(M[main_row])):
        M[main_row][i] += coefficient * M[added_row][i]
    return M



def matrix_çarpım(matrix1, matrix2):
    matrix_product = []
    m = len(matrix1)
    p = len(matrix2[0])
    n= len(matrix1[0])
    for i in range(m):
        row = []
        for j in range(p):
            toplam = 0
            for k in range(n):
                toplam += matrix1[i][k] * matrix2[k][j]
            row.append(toplam)
        matrix_product.append(row)
    return matrix_product




def list_to_matrix(items_g, m, n):
    uzunluk = len(items_g)
    if uzunluk > m*n:
        print("Listenin eleman sayısı matris boyutlarından büyük.")
        return None
        #yapay zeka burada "None"u return etmemi söyledi.
        #Fakat bunun ne olduğunu inan bilmiyorum.
        #Sonrasında anladım, boş değer çıkması için.
    while uzunluk < m*n:
        items_g.append(0)
        uzunluk = uzunluk + 1
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(items_g[i*n+j])
        matrix.append(row)
    return matrix




def dot_product(y1, y2):
    r = len(y1)
    product = 0
    for i in range(r):
        product += int(y1[i]*y2[i])
        #int koymamın sebebi burada hata almamdı.
    return product





#Echelon formuna getirecek bir fonksiyon yazmak istiyorum
#Bunun için aklımda iki yol var
#Yapay zekanın dediği gibi çarpan kullanmak
#Kendi düşündüğüm hedef satırla diğer satırın elemanının bölümü kadar döngüyü kullanıp kalanı çıkarmak.
#İlk yöntemi deneyeceğim.
#def echelon_form(M):
    #ilk başta ikinci satıra geçip aralarındaki oran kadar çarpıp geçici bir satır oluşturması lazım.
    #Sonra bu satırı ikinci satıra eklemeli.
    #Bu işlem en aşağıya kadar devam etmeli.
    #if M[0][0] != 0:
        #rows = len(M)
        #columns = len(M[0])
        #for j in range(columns):
            #for i in range(j+1,rows):
                #c = -M[i][j] / M[j][j]
                #row_addition(M, i, j, c)
                #Yapay zekaya ana fonksiyonun doğru olduğunu teyit ettirdikten sonra hatanın addition fonksiyonunda olduğunu anladım.
                #Onu değiştirdim fakat sadece kendi başına kullanıldığında yine hata verecektir
                #Çünkü kullanıcı 1. satır dediğinde aslında fonksiyon 2. satrı ile işlem yapacaktır.
                #Şimdilik bu sorunu görmezden geleceğim.
    #else:
        #print("Matrisin ilk elemanı sıfır.")
    #return M




#m = int(input("Enter the number of rows: "))
#n = int(input("Enter the number of columns: "))
#def matrix_builder(m, n):
    #matrix = []
    #for i in range(m):
        #row = []
        #for j in range(n):
            #a = int(input(f"Enter element for matrix [{i+1},{j+1}]: "))
            #row.append(a)
        #matrix.append(row)
    #return matrix
#Burada input komutunu fonksiyonun dışına koymalıyım
#Çünkü bu durumda fonksiyon oluşturmamın bir anlamı yok.
#Fakat değerleri dışarıdan almak istersem de bu durumda fonksiyona ihtiyacım yok.
#Çünkü hepsini zaten eklemiş oluyorum.
#O zaman kullanıcıdan bir liste alıp bu listeyi matrise çeviren bir fonksiyon yazabilirim.


#Liste oluşturma işini daha sonra for döngüsü içine alabilirim.
#def list_to_matrix_old(items_g, m, n):
    #Burada tek satır bir listeyi alıp onu matrise çevireceğim.
    #Kalan kısımlar sıfır olacak şekilde girilecek.
    #items_f[:] = items_g
    #uzunluk = len(items_g)
    #if uzunluk == m * n:
    #buranın altına direkt olarak for döngülerini yerleştirebilirim.
    #Çünkü herhangi bir sorun çıkmayacaktır.
        #matrix = []
        #burada uzunluk lazım.
        #for i in range(m):
            #row = []
            #kullanıcının istediği kadar satır eklemek için m değerini kullandım.
            #bu durumda hata alma ihtimalim yüksek.
            #for j in range(n):
                #row.append(items_f[i*n+j])
                #burada j değerini de eklemem gerektiğini fark ettim.
            #matrix.append(row)
#Şimdi çarpım ile liste uzunluğunun eşit olduğu değerler için bir fonksiyon oluşturdum. 
#Olmayan değerler için de bir şeyler yapmam gerek.
    #elif uzunluk < m * n:
        #matrix = []
        #tekrardan klasik bir döngü oluşturmak istersem hata verir. 
        #Listedeki elemaları tüketir. O yüzden bir if bloğu daha ekleyeceğim.
        #for i in range(m):
            #ayrıca buraya bir if bloğu eklemek iyi olcaktır.,
            #if items_f:
                #if bloğu mantıklı çünkü liste altta boşalırsa bu blok tekrar çalışmayacak.
                #boşalmazsa da tekrar çalışacak ve eleman eklemeye devam edecek.
                #row = []
                #for j in range(n):
                #if bloğunu for döngüsünün içine eklemek daha mantıklı.
                    #if items_f:
                        #row.append(items_f[i*n+j])
                        #Burada listeyi kopyalayıp işlem yapmanın daha mantıklı olduğunu görüyorum.
                        #list.remove(items_f[i*n+j])
                    #else:
                        #j = k
                    #burada hata verdi. j=k kısmını değiştirmem gerek.
                        #for k in range(n-j):
                            #row.append(0)
                        #break
                        #burada break eklemek gerek çünkü listedeki elemanlar bitti.
                #matrix.append(row)
#Şimdi geriye tek kalan liste elemanları matrix uzunluğundan büyükse hata mesajı eklemek kalıyor.
    #if len(items_f) > m*n:
        #print("Hata: Liste eleman sayısı matris boyutlarından büyük olamaz.")
    #return matrix