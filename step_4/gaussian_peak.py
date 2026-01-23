import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

def gauss(x, A, mu, sigma):
    f = A *  np.exp(- (x - mu)**2 / (2* sigma**2))
    return f

x_axes = np.linspace(0, 10, 1000)
A_real = 5
mu_real = 5
sigma_real = 1
y_clean = gauss(x_axes, A_real, mu_real, sigma_real)

y_noise = y_clean + np.random.normal(0, 0.5, len(x_axes))
#Burada ortalaması 0 olan rastgele sayılar ekliyorum.
#Bu sayıların standart sapması 0.1, uzunluğu ise x aksisi ile aynı.

#g = cf(gauss, x_axes, y_noise)
#Burada ilk değerleri vermeden deneyeceğim. Bir de değerleri vererek deneyeceğim.
g_with_initial = cf(gauss, x_axes, y_noise, p0=[5, 5, 1])
#İlk değerleri p0 parametresi ile verdim ve şimdi aradaki farkı görmek istiyorum.

curve = gauss(x_axes, *g_with_initial[0])
#curve2 = gauss(x_axes, *g[0])
#cf fonksiyonu optimize edilmiş parametreleri bir matriste veriyor.
#O yüzden burada o listenin elemanlarını kullanmam gerek.
# * işareti listenin elemanlarını tek tek fonksiyona parametre olarak veriyor.

plt.scatter(x_axes, y_noise,
            s=1,
            color='blue',
            label="Experimental Data")
plt.plot(x_axes, curve,
         color='red',
         label="Fitted Curve")
plt.title("Gaussian Peak")
plt.xlabel("x")
plt.savefig("gaussian_peak")

print(f"""Fitted parameters: 
A: {g_with_initial[0][0]}, 
mu: {g_with_initial[0][1]}, 
sigma: {g_with_initial[0][2]}""")
print(f"""Real parameters:
A: {A_real},
mu: {mu_real},
sigma: {sigma_real}""")

#fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

#ax1.scatter(x_axes, y_noise,
            #s=1,
            #color='blue',
            #label="Experimental Data")
#ax1.plot(x_axes, curve,
         #color='red',
         #label="Theoretical Curve")
#ax1.legend()

#ax2.scatter(x_axes, y_noise,
            #s=1,
            #color='blue',
            #label="Experimental Data")
#ax2.plot(x_axes, curve2,
         #color='green',
         #label="Curve without Initial Guess")
#ax2.legend()

#fark ettim ki aslında ilk değerleri vermek burada çok da bir şey değiştirmedi.
#Bu kod bloğunu şimdilik çıkaracağım çünkü burası sadece merakım içindi.