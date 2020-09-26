import numpy as np


def y(x):
    return np.log((1 / (np.exp(np.sin(x) + 1))) / (1.25 + 1 / (x ** 15))) / np.log(1 + x ** 2)


print(y(float(input())))
