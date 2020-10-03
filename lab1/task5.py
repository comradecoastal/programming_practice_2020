import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p, v = np.polyfit(x, y, deg=1, cov=True)
p2, v2 = np.polyfit(x, y, deg=2, cov=True)

p_f = np.poly1d(p)
p_f2 = np.poly1d(p2)

x_f = np.arange(1, 6, 0.01)

plt.plot(x, y, x_f, p_f(x_f), x_f, p_f2(x_f))
plt.grid(True)
plt.show()
