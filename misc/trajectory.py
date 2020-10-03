import numpy as np
import matplotlib.pyplot as plt

x_0, y_0 = 0, 0
v_0 = 7.64
angle_0 = 1
g = 10
step = 0.01
time = 10

steps = int(time/step)

x = [x_0]
y = [y_0]
v = [v_0 * np.cos(angle_0), v_0 * np.sin(angle_0)]

for i in range(1,steps):
    x.append(x[i-1]+v[0])
