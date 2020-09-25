print("введите 3 целых числа через пробел")

a, b, c = map(abs, map(int, input().split()))

print("kon" * a + "stan" * b + "tin" * c)
