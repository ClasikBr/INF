from itertools import permutations

nums = sorted(input().split(), key=int)
for p in permutations(nums):
    print(*p)