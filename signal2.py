# DISPLAYING SECOND SIGNAL

import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots()
dt = 0.01
t = np.arange(0, 10, dt)
x2 = np.sin(2 * np.pi * t)
axs.set_title("Signal2")
axs.plot(x2, color='C0')
axs.set_xlabel("Time")
axs.set_ylabel("Amplitude")
plt.show()
