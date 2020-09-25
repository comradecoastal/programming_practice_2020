m1 = -1
m2 = -1

while 1:
    x = int(input())
    if x == 0:
        break
    if x > m1:
        m2 = m1
        m1 = x
    elif x > m2:
        m2 = x

print(m2)
