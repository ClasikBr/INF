year = int(input())
ans = 366 if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else 365
print(ans)