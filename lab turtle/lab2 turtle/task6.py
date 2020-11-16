import turtle as tt

#n = int(input())
n = 20

tt.shape("turtle")

for i in range(n):
    tt.forward(150)
    tt.stamp()
    tt.back(150)
    tt.left(360/n)
