def degree5(n:int) -> int:
    if n == 1:
        return 0
    if n % 5 != 0:
        return -1
    sub = degree5(n // 5)
    return -1 if sub == -1 else sub + 1
