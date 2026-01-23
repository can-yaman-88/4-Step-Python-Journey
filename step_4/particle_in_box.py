import numpy as np
import matplotlib.pyplot as plt

L = 1
N = np.linspace(0, 1, 1000)
dx = L / len(N)

matrix = np.zeros((len(N), len(N)))
n_1 = np.ones(len(N))
n_2 = 2*n_1
n_3 = -1 * n_1
M = np.diag(n_2) + np.diag(n_3[:-1], k=1) + np.diag(n_3[:-1], k=-1)
#np_diag ile 2'yi köşegene diğer değerleri de köşegenin yanlarına yerleştirdim.

c = 1 / (2 * (dx**2))
H = c * M

eigenvalues, eigenvectors = np.linalg.eigh(H)
#eigh simetrik matrisler için kullanılıyormuş.
psi_0 = eigenvectors[:, 0]
psi_1 = eigenvectors[:, 1]
psi_2 = eigenvectors[:, 2]
#ilk üç özvektörü aldım.

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(N, psi_0,
         color='blue',
         label="n=0")
ax1.plot(N, psi_1,
         color='red',
         label="n=1")
ax1.plot(N, psi_2,
         color='green',
         label="n=2")
ax1.set(ylabel="Wavefunction",
        title="Particle in a Box Wavefunctions")
ax1.legend()
#İsimleri yapay zekadan aldım.
ax1.grid(True)

ax2.plot(N, psi_0**2,
         color='blue',
         label="n=0")
ax2.plot(N, psi_1**2,
         color='red',
         label="n=1")
ax2.plot(N, psi_2**2,
         color='green',
         label="n=2")
ax2.set(ylabel="Probability Density")
#İsimleri tekrardan yapay zekadan alınma.
ax2.grid(True)

plt.savefig("particle_in_box")