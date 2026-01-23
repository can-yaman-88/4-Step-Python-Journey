import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

k_real = 50
g = 9.81

masses = np.linspace(0.1, 10, 20)
#20 tane kütle oluşturdu. 
#Bu kütleler için teorik katsayı hesaplayacağım.
extension_t = (masses * g)/k_real
extension_e = extension_t + np.random.normal(0, 0.1, len(masses))

def model_f(m, k):
    g = 9.81
    x = (m * g) / k
    return x #(m * g) / k

popt, pcov = cf(model_f, masses, extension_e)
k_c = popt
plt.scatter(masses, extension_e,
            color='red')
plt.title(f"Real k: 50, Calculated k is {k_c[0]}")
curve = model_f(masses, k_c)
plt.plot(masses, curve)
plt.xlabel("Masses (kg)")
plt.ylabel("Extension (m)")

plt.savefig("curve")