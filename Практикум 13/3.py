s = set(input().split())
n = int(input())

for _ in range(n):
    s -= set(input().split())
print(len(s))