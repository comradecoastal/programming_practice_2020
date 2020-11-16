import random
import turtle as tt

VELOCITY = 15

while True:
    tt.forward(random.random() * VELOCITY)  # случайное перемещение от 0 до VELOCITY
    tt.left((random.random() - 0.5) * 180)  # случайный поворот от -180 до 180
