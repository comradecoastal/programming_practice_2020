nums = [int(s) for s in input().split()]

nums_unique = []
pairs = 0

# делаем список чисел без повторений
for num in nums:
    if num not in nums_unique:
        nums_unique.append(num)

# считаем количество пар
for num in nums_unique:
    count = nums.count(num)
    pairs += count * (count - 1) // 2

print(pairs)
