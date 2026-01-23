import numpy as np
import matplotlib.pyplot as plt

m = 1.0
k = 10.0
c = 0.5
x0 = 1.0
v0 = 0.0
dt = 0.05
t_max = 10.0

t_l = np.arange(0, t_max, dt)

v_l = [v0]
x_l = [x0]
x = x0
v = v0
t_e = 0.0

while t_e < t_max:
    a = (-k*x - c*v) / m
    v = v + a*dt
    x = x + v*dt
    v_l.append(v)
    x_l.append(x)
    t_e = t_e + dt

x_l_c = x_l[:len(t_l)]
v_l_c = v_l[:len(t_l)]
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t_l, x_l_c,
         color='blue',
         label="Position (x)")
ax1.set(ylabel="Position (x)",
        title="Spring-Damper System",)
ax1.grid(True)
ax2.plot(t_l, v_l_c,
         color='red',
         label="Velocity (v)")
ax2.set(ylabel="Velocity (v)",
        xlabel="Time (s)")
ax2.grid(True)

plt.savefig("spring_damper.png")