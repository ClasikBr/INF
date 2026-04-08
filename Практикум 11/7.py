num = [int(x) for x in input().split()]

even = sum(n for n in num if n % 2 == 0)
odd = sum(n for n in num if n % 2 != 0)

print(even, odd)
