from random import randint
import random
import turtle

VELOCITY = 20

number_of_turtles = 25
steps_of_time_number = 100

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(random.random() * VELOCITY)  # случайное перемещение от 0 до VELOCITY
        unit.left((random.random() - 0.5) * 180)  # случайный поворот от -180 до 180
