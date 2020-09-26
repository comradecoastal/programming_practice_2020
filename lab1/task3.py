import numpy as np
import matplotlib.pyplot as plt


def y(x):
    return (np.log(x ** 2 + 1) / np.log(1 + np.tan(1 / (1 + (np.sin(x) ** 2))))) * np.exp(-abs(x) / 10)


x = np.arange(-20, 20.01, 0.01)
plt.plot(x, y(x))
plt.grid(True)
plt.show()
