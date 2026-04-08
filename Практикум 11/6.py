num = int(input())
ans = []

for d in range(2, int(num ** 0.5) + 1):
    if num % d == 0:
        ans.append(d)
        if d * d != num:
            ans.append(num // d)

ans.sort()
print(ans)
