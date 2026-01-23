import numpy as np
import matplotlib.pyplot as plt

g = 9.81
k = 0.01
m = 1.0
dt = 0.01
v0 = 20.0
theta = np.pi / 4
#Burada başlangıç değerlerini verdim.
#Hatam açıyı ilk başta 90 derece seçmek olmuş.

vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)
#Başlangıç için hız vektörlerini buldum

x_s = [0]
y_s = [0]
x = 0
y = 0
#Burada ilk değerleri verdim.

t_ideal = np.linspace(0, 5)
xi = vx0 * t_ideal
yi= vy0 * t_ideal - 0.5 * g * t_ideal**2

t = 0
vx = vx0
vy = vy0
while y >= 0:
    v = np.sqrt(vx**2 + vy**2)
    ax = -k * v * vx / m
    #m'ye bölmeyi unutmuşum
    ay = -g - (k * v * vy / m)
    vx = vx + ax * dt
    vy = vy + ay * dt
    x = x + vx * dt
    y = y + vy * dt
    x_s.append(x)
    y_s.append(y)
    t += dt
#Fark ettiğim bir şey de y değerlerimin çok büyükken x değerlerimin çok küçük olması.
#Bunun nedenini bilmiyorum.
#Nedeni buldum, açıyı büyük seçmemmiş.

plt.plot(x_s, y_s,
          color='blue',
          label="Experimental")
plt.title(f"Projecile Motion")
plt.plot(xi, yi,
           linestyle='dashed',
           label="Ideal")
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.legend()
plt.ylim(0, 20)
plt.xlim(0, 50)
plt.grid(True)
plt.savefig("projectile_motion")
