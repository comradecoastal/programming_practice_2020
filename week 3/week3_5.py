# создаём множества
set_a = set([int(s) for s in input().split()])
set_b = set([int(s) for s in input().split()])

# делаем список из пересечения множеств и сортируем его
ab_list = list(set_a & set_b)
ab_list.sort()

for num in ab_list:
    print(num, end=' ')