# SHIFTING OF 2 SIGNALS

import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots()
dt = 0.01
t = np.arange(0, 10, dt)
x1 = np.sin(4 * np.pi * t)

y1 = x1*(t-3);
y2 = x1*(t+4);
axs.set_title("Time Shifting of Signals")
axs.plot(y1,y2, color='C0')
axs.set_xlabel("Time")
axs.set_ylabel("Amplitude")

plt.show()
