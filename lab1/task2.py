import matplotlib.pyplot as plt
import numpy as np


def y(x):
    return x * x - x - 6


x = np.arange(-5, 5.01, 0.01)

plt.plot(x, y(x), x, x*0)
plt.grid(True)
plt.show()
