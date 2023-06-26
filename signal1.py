# DISPLAYING FIRST SIGNAL

import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots()
dt = 0.01
t = np.arange(0, 10, dt)
x1 = np.cos(6 * np.pi * t)
axs.set_title("Signal1")
axs.plot(x1, color='C0')
axs.set_xlabel("Time")
axs.set_ylabel("Amplitude")
plt.show()

