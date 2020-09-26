import numpy as np
import matplotlib.pyplot as plt

fstring = input("Please input python function:")

x = np.arange(-10, 10.01, 0.01)

plt.plot(x, eval(fstring))
plt.grid(True)
plt.show()
