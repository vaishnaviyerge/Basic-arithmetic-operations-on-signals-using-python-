# MULTIPLICATION OF 2 SIGNALS

import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots()
dt = 0.01
t = np.arange(0, 10, dt)
x1 = np.cos(6 * np.pi * t)
x2 = np.sin(2 * np.pi * t)
y1 = x1*x2

axs.plot(x1,x2, color='C0')
axs.set_xlabel("Time")
axs.set_ylabel("Amplitude")
axs.set_title(" Multiplication of Signals")
plt.show()
