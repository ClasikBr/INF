def comp(a: str, b: str, m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    if a[m - 1] == b[n - 1]:
        return 1 + comp(a, b, m - 1, n - 1)
    return max(
        comp(a, b, m - 1, n),
        comp(a, b, m, n - 1)
    )
