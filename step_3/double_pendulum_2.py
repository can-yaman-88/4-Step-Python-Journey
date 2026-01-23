import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as od

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
y01 = [np.pi/2, 0.0, np.pi/2, 0.0]
y02 = [np.pi/2 + 0.00001, 0.0, np.pi/2, 0.0]
y1 = od(derive, y01, t)
y2 = od(derive, y02, t)
Q1_1 = y1[:, 0]
Q2_1 = y1[:, 2]
Q1_2 = y2[:, 0]
Q2_2 = y2[:, 2]
x1_1 = L1 * np.sin(Q1_1)
y1_1 = -L1 * np.cos(Q1_1)
x2_1 = x1_1 + L2 * np.sin(Q2_1)
y2_1 = y1_1 - L2 * np.cos(Q2_1)
x1_2 = L1 * np.sin(Q1_2)
y1_2 = -L1 * np.cos(Q1_2)
x2_2 = x1_2 + L2 * np.sin(Q2_2)
y2_2 = y1_2 - L2 * np.cos(Q2_2)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(x2_1, y2_1,
         color='blue',
         label="Pendulum 1")
ax1.set(ylabel="y position",
        title="Pendulum 1",)
ax1.grid(True)
ax1.plot(x2_2, y2_2,
         color='red',
         label="Pendulum 2")
ax1.legend()
ax2.plot(t, np.abs(Q1_1 - Q1_2))
ax2.set(ylabel="Angle Difference(rad)",
        xlabel="Time(s)")

plt.savefig("double_pendulum_2.png")