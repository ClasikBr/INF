nums = list(map(int, input().split()))
x = int(input())

rep = {n for n in nums if nums.count(n) > 1}
print(x in rep)