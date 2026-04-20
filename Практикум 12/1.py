def pownum(a: float,n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        return 1 / pownum(a, -n)

    return a * pownum(a, n-1)

