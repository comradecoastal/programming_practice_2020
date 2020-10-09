nums = [int(s) for s in input().split()]
count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
        count += 1

print(count)

# тут всё очевидно
