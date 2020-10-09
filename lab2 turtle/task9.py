import turtle as tt
import numpy as np


def polyturtle(n, r):
    n = int(n)
    r = float(r)
    a = r / (2 * np.sin(2 * np.pi / (2 * n)))
    tt.left(180)
    tt.right(180 - (180 - 360 / n) / 2)
    for i in range(n):
        tt.forward(a)
        tt.left(180 - 360 / n)


for i in range(100):
    tt.forward(10)
    polyturtle(i + 2, i * 20)
