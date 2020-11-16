import turtle as tt

# задаём константи
WIDTH = 20
HEIGHT = 20
STEP = 10
INDEX = '13374206900'


# функция которая соединяет две точки
def drawline(pos1, pos2):
    """

    positions:

    2   5
    4   1
    6   3

    """

    x0, y0 = tt.pos()
    x1, y1 = (pos1 % 2) * WIDTH, (pos1 % 3) * HEIGHT
    x2, y2 = (pos2 % 2) * WIDTH, (pos2 % 3) * HEIGHT
    tt.penup()
    tt.goto(x0 + x1, y0 + y1)
    tt.pendown()
    tt.goto(x0 + x2, y0 + y2)
    tt.penup()
    tt.goto(x0, y0)
    tt.pendown()


# соединение многих точек чтобы получить число
def drawnumber(number: int):
    lines = [((3, 6), (6, 4), (4, 2), (2, 5), (5, 1), (1, 3)),
             ((4, 5), (5, 1), (1, 3)),
             ((2, 5), (5, 1), (1, 6), (6, 3)),
             ((2, 5), (5, 4), (4, 1), (1, 6)),
             ((2, 4), (4, 1), (1, 5), (1, 3)),
             ((2, 5), (2, 4), (4, 1), (1, 3), (6, 3)),
             ((5, 4), (4, 1), (1, 3), (3, 6), (6, 4)),
             ((2, 5), (5, 4), (4, 6)),
             ((6, 4), (4, 2), (2, 5), (5, 1), (1, 3), (4, 1)),
             ((4, 2), (2, 5), (5, 1), (1, 6), (4, 1))]

    for apos, bpos in lines[number]:
        drawline(apos, bpos)


# выполняем
for i in INDEX:
    tt.color("blue")
    drawnumber(int(i))
    tt.penup()
    tt.forward(WIDTH + STEP)
    tt.pendown()
