a, b, c = map(int, [input(), input(), input()])

if b < a and b < c:
    a = b
elif c < a:
    a = c

print(a)