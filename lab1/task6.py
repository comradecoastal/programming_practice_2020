import numpy as np
import matplotlib.pyplot as plt


def w(x, a, b, iter):
    s = 0.0
    for i in range(iter):
        s += b ** i * np.cos(a ** i * np.pi * x)
    return s


x = np.arange(-3, 3.01, 0.01)
a, b = 3, 0.5
iter = 100

plt.plot(x, w(x, a, b, iter))
plt.grid(True)
plt.show()
