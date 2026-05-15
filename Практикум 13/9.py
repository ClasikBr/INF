from itertools import combinations

nums = input().split()
k = int(input())
for c in combinations(nums, k):
    print(*c)