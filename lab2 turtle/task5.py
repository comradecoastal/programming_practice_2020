import turtle as tt

tt.shape("turtle")

for i in range(10):
    tt.pendown()
    tt.forward(10 * (2 * i + 1))
    tt.left(90)
    tt.forward(10 * (2 * i + 1))
    tt.left(90)
    tt.forward(10 * (2 * i + 1))
    tt.left(90)
    tt.forward(10 * (2 * i + 1))
    tt.right(45)
    tt.penup()
    tt.forward(14)
    tt.left(135)

