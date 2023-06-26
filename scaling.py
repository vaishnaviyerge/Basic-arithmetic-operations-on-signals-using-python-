# AMPLITUDE SCALING OF 2 SIGNALS

import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots()
dt = 0.01
t = np.arange(0, 10, dt)
x1 = np.sin(6 * np.pi * t)
x2 = np.sin(2 * np.pi * t)
a = 10
y1 = a*x2
axs.set_title(" Amplitude Scaling of Signals")
axs.plot(t, y1, color='C0')
axs.set_xlabel("Time")
axs.set_ylabel("Amplitude")

plt.show()
