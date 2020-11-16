import turtle as tt


# рисует круги
def circle(value):
    for i in range(value):
        tt.forward(5)
        tt.left(360 / value)


for i in range(6):
    circle(50 + 10 * i)
    tt.left(180)
    circle(50 + 10 * i)
