n = int(input())
s = set(input().split())

for _ in range(n-1):
    s &= set(input().split())
print(len(s))