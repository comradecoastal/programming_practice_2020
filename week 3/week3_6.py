nums = [int(s) for s in input().split()]

nums_used = set([])

for num in nums:
    if num in nums_used:  # есть чи число в множестве уже втретившихся чисел?
        print("YES", end=' ')
    else:
        print("NO", end=' ')
        nums_used |= {num}  # добавляем число в это множество
