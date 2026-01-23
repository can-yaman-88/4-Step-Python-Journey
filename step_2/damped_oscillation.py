import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0, 10, 500)
a = 5
omega = np.pi*2
xt = a * np.exp(-0.5*time) * np.cos(omega*time)


fig, ax = plt.subplots()
ax.plot(time, xt, 
         color="red",
         linestyle="dashed",
         )
ax.set(xlabel="Time(s)",
       ylabel="Magnitude(m)",
       title="Damped Oscillation")
ax.grid(True)

plt.show()
plt.savefig("damped_oscillation.png")