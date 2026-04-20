def function1(x:int, d: int = 2) -> int:
    if x < 2:
        return 0
    if d * d > x:
        return 1
    if x % d == 0:
        return 0
    return function1(x, d + 1)
