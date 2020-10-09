nums = [int(s) for s in input().split()]

for num in nums:
    if nums.count(num) == 1:  # если количество этого элемента в спике равно одному, то его выводим
        print(num, end=' ')
