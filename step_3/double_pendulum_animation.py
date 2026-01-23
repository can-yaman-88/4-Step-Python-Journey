import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as od
import matplotlib.animation as ant

L1 = 1.0
L2 = 1.0
m1 = 1.0
m2 = 1.0
g = 9.81

def derive(state, t):
    Q1, w1, Q2, w2 = state
    delta = Q2 - Q1
    denominator = L1*(2*m1+m2-m2*np.cos(2*Q1-2*Q2))
    w1_dot = (-g*(2*m1 + m2)*np.sin(Q1) - m2*g*np.sin(Q1-2*Q2)
              -2*np.sin(Q1-Q2)*m2*(w2**2*L2+w1**2*L1*np.cos(Q1-Q2))) / denominator
    w2_dot = 2*np.sin(Q1-Q2)*(w1**2*L1*(m1+m2)+g*(m1+m2)*np.cos(Q1)+w2**2*L2*m2*np.cos(Q1-Q2)) / denominator
    return w1, w1_dot, w2, w2_dot

t = np.arange(0, 20, 0.05)
y0 = [np.pi/2, 0.0, np.pi/2, 0.0]

y = od(derive, y0, t)
Q1 = y[:, 0]
Q2 = y[:, 2]

x1 = L1 * np.sin(Q1)
y1 = -L1 * np.cos(Q1)
x2 = x1 + L2 * np.sin(Q2)
y2 = y1 - L2 * np.cos(Q2)

fig, ax = plt.subplots()
ax.set(xlim=(-(L1+L2), (L1+L2)), ylim=(-(L1+L2), (L1+L2)))
ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=2)
#İlk parametre boş, x ekseni boş
#İkinci parametre boş, y ekseni boş
#'o-' nokta ve çizgi ile çiz anlamına geliyor.

def update(i):
    x = [0, x1[i], x2[i]]
    y = [0, y1[i], y2[i]]
    #Sanırım burada sıfırlar orijini temsil ediyor.
    #Fakat neden onu da listeye dahil ettik ki?
    line.set_data(x, y)
    return line,
#Fonksiyonda 3 nokta arasında 2 çizgi çizdiriyorum.
#Orijin ile ilk sarkaç ucu,
#İlk sarkaç ile ikinci sarkacın ucu arasında bire çizgi.
#Bu da nede 0 koyduğumuzu açıklıyor.


animation = ant.FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)
plt.show()
animation.save("double_pendulum_animation.gif", writer='pillow')
#Bu kodu yapay zeka kendisi önerdi. GIF oluşturmak için pillow kütüphanesini kullanıyormuş.