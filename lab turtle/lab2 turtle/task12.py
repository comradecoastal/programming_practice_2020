import turtle as tt

# рисует полукруги
def semicircle(value):
    for i in range(value):
        tt.forward(5)
        tt.left(180 / value)


tt.left(90)

N = 6
SMALL = 10
LARGE = 30

for i in range(N):
    semicircle(LARGE)
    semicircle(SMALL)
