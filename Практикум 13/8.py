from itertools import combinations

nums = input().split()
for r in range(len(nums) + 1):
    for c in combinations(nums, r):
        print(*c)