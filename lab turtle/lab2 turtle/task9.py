import turtle as tt
import numpy as np


def polyturtle(n, r):
    n = int(n)
    r = float(r)
    a = 2 * r * np.sin(2 * np.pi / (2 * n))
    for i in range(n):
        tt.left(360 / n)
        tt.forward(a)


for i in range(100):
    polyturtle(i + 2, i * 20)
    tt.forward(3)
