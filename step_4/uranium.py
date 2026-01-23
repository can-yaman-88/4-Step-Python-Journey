import numpy as np
import matplotlib.pyplot as plt

N0 = 1000
lam = 0.05
N = N0
t_s = 100
t = 0
N_list = [N0]

#Fark ettim ki yine bir 100 elemanlı zaman listesi oluşturmam gerek.
t_list = np.arange(0, t_s + 1, 1)
#t_s'i alması için bir ekledim.

while t < t_s:
    n1 = np.random.random(N) < lam
    #random.random 0 ile 1 arasında rastgele sayılar seçiyor.
    #Burada N parametresini girerek bunu N tane sayı için yapmasını söylüyorum.
    N = N - n1.sum()
    t += 1
    N_list.append(N)

N_t = N0 * np.exp(-lam * t_list)

plt.plot(t_list, N_list,
         color='blue')
plt.plot(t_list, N_t,
         color='red',)
plt.title("Uranium Decay Simulation")
plt.xlabel("Time")
plt.ylabel("Number of Nuclei")
plt.grid(True)
#Başlıkları yapay zeka söyledi.
plt.savefig("uranium")