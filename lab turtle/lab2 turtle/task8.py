import turtle as tt

tt.shape("turtle")
n = 10

for i in range(n):
    tt.forward(10 * (i * 2 + 1))
    tt.left(90)
    tt.forward(10 * (i * 2 + 1))
    tt.left(90)
    tt.forward(10 * (i * 2 + 2))
    tt.left(90)
    tt.forward(10 * (i * 2 + 2))
    tt.left(90)