import turtle as tt


def circle(value):
    for i in range(value):
        tt.forward(5)
        tt.left(360 / value)


def semicircle(value):
    for i in range(value):
        tt.forward(5)
        tt.left(180 / value)


# рисуем большой круг

BIG = 200

# уходим из центра
tt.goto(0, -BIG / 1.55)

# рисуем жёлтое лицо
tt.width(5)
tt.begin_fill()
circle(BIG)
tt.color("yellow")
tt.end_fill()
tt.color("black")

# рисуем глаза

EYES = 40

# идём к первому глазу
tt.penup()
tt.goto(-BIG / 3, BIG / 3)
tt.pendown()

# рисуем
tt.width(2)
tt.begin_fill()
circle(EYES)
tt.color("blue")
tt.end_fill()
tt.color("black")

# идём к вторуму глазу
tt.penup()
tt.goto(BIG / 3, BIG / 3)
tt.pendown()

# рисуем
tt.width(2)
tt.begin_fill()
circle(EYES)
tt.color("blue")
tt.end_fill()
tt.color("black")

# рисуем нос

tt.penup()
tt.goto(0, BIG / 4)
tt.pendown()
tt.width(10)
tt.right(90)
tt.forward(BIG / 2)
tt.left(90)

# рисуем рот

tt.penup()
tt.goto(-BIG / 2, 0)
tt.color("red")
tt.pendown()
tt.width(10)
tt.right(90)
semicircle(BIG // 4)
input()
