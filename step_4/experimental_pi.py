import matplotlib.pyplot as plt
import numpy as np

N = 10000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
inside_x = []
inside_y = []
outside_x = []
outside_y = []

for i in range(N):
    if x[i]**2 + y[i]**2 <= 1:
        inside_x.append(x[i])
        inside_y.append(y[i])
    else:
        outside_x.append(x[i])
        outside_y.append(y[i])

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set(xlim = (-1.2, 1.2), ylim = (-1.2, 1.2))
ax.scatter(inside_x, inside_y, c='red', s=0.1)
ax.scatter(outside_x, outside_y, c='blue', s=0.1)
#S parametresi nokta büyüklüğünü ayarlıyor.
#Burada 1 yaparak çok küçük olmasını sağlıyorum.
circle = plt.Circle((0, 0), 1, color='black', fill=False)
#Daireyi çizdiriyorum. İçi boş bir şekilde.
#Merkezi orijin, yarıçapı 1 olacak şekilde.
ax.add_artist(circle)
#Daireyi grafiğe ekliyorum.

pi = 4 * len(inside_x) / N
#Burada toplam nokta sayısını dairenin içindeki nokta sayısına bölüyorum.
plt.title(f"Pi Approximation: {pi}")
plt.savefig("monte_carlo_pi.png")



# Tüm diziyi tek seferde işle (Döngü yok, sadece matris matematiği)
#radius_squared = x**2 + y**2
#inside_count = np.sum(radius_squared <= 1)
#pi = 4 * inside_count / N

#Yapay zeka for döngüsüne alternatif ve çok daha hızlı bir yöntem olarak bu kodu önerdi.
#Aslında tek farkı numpy kullanması.