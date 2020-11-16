import turtle as tt
import numpy as np

# Место для постоянных
VX_0 = 30.0
VY_0 = 50.0
g = 9.80665
DRAG_C = 0.05

STEP = 0.05
TIME = 100

x = 0.0
y = 0.0
vx = VX_0
vy = VY_0
ax = 0.0
ay = 0.0
dt = STEP
c = DRAG_C

tt.shape("circle")

# рассчёт координат
for i in np.arange(0, TIME, STEP):
    ax = - vx * c
    ay = - vy * c - g

    x += vx * dt + (dt ** 2) * ax / 2
    y += vy * dt + (dt ** 2) * ay / 2
    vy += ay * dt
    vx += ax * dt
    tt.goto(x, y)

    if y < 0:
        vy = - vy
        y = 0

    if np.abs(x) > 400:
        x = 400 * np.sign(x)
        vx = -vx
