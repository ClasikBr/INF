n = int(input())
nums = set(range(2, n))

for i in range(2, int(n**0.5) + 1):
    if i in nums:
        nums -= set(range(i * i, n, i))

print(sorted(nums))