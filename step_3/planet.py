import numpy as np
import matplotlib.pyplot as plt

GM = 1
x = 1.0
y = 0.0
v0x = 0.0
v0y = 1.0
#Burada fark ettim ki sıfırları ters değerlere vermem gerekli.
#Eğer hem x'e hem de hızına 0 verirsem düz bir çizgi oluyor.
dt = 0.1

t_max = 100.0

t = 0.0
x_l = [x]
y_l = [y]
vx = v0x
vy = v0y

while t < t_max:
    r = np.sqrt(x**2 + y**2)
    ax = -GM * x / r**3
    ay = -GM * y / r**3
    vx = vx + ax * dt
    vy = vy + ay * dt
    x = x + vx * dt
    y = y + vy * dt
    x_l.append(x)
    y_l.append(y)
    t = t + dt

plt.plot(x_l, y_l,
         color='blue')
plt.title("Planet")
plt.xlabel("x position")
plt.ylabel("y position")
plt.plot(0, 0, 
         'yo', 
         markersize=10,
         label="Sun")
plt.legend()
#Bu kodu yapay zekadan aldım, ortada güneş olması için.
plt.grid(True)
plt.axis('equal')
plt.savefig("planet")