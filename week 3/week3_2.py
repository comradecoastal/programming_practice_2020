nums = [int(s) for s in input().split()]

# при помощи хитрой питоновской функции находим максимум и минимум
nmax = max(nums)
nmin = min(nums)

# при помощи хитрой питоновского метода находим где они
inmax = nums.index(nmax)
inmin = nums.index(nmin)

nums[inmax], nums[inmin] = nmin, nmax

for num in nums:
    print(num, end=' ')
