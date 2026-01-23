import numpy as np
import matplotlib.pyplot as plt

N0 = 1000
lam = 0.5
dt = 0.1
t_max = 10.0

t_arr = np.arange(0, t_max, dt)

N_analitic = N0 * np.exp(-lam * t_arr)

t = 0.0
N = N0
N_euler = [N0]
t_euler = [t]

while t < t_max:
    dN = -lam * N
    N = N + dN * dt
    t = t + dt
    N_euler.append(N)
    t_euler.append(t)

N_euler = np.array(N_euler)
#N_analitic np ile oluşturulmuş bir liste
#N_euler normal bir liste
#Bu yüzden N_euler listesini np.array ile aynı formata çevirdim.

N_euler_c = N_euler[:len(t_arr)]
#N_analitic ve t_arr ile aynı uzunlukta olması için
error = np.abs(N_analitic - N_euler_c)
#Böyle yaptığımda listedeki veri sayıları eşit olmuyor
#Ben de kısa olan listeyle eşit sayıda eleman olacak şekilde kopyalıyorum.

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t_arr, N_analitic,
         color='blue',
         label="Analitic Solution")
ax1.plot(t_euler, N_euler,
         color='red',
         linestyle='dotted',
         label="Euler Method")
ax1.set_title("Euler Method vs Analitic Solution")
ax1.legend()
ax1.set_ylabel("N")
ax2.plot(t_arr, error,
         color='green',
         label="Error",
         linestyle='dashed')
ax2.set_ylabel("Error")
ax2.set_xlabel("Time")
ax2.set_title("Error between Analitic and Euler Method")
plt.savefig("euler method")

#Kodumda hata fark ediyorum.
#Hesaplama ile analitik çözüm arasındaki fark çok az gözüküyor burada. 
#Hata da çok küçük gözüküyor ve neden bilmiyorum.
#Hata neredeyse sıfır, bu neden oluyor?

#Kod doğruymuş, sorun ölçekteymiş.