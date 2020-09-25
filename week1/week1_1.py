minutes = int(input())

minutes %= 1440

print(minutes // 60, minutes % 60)