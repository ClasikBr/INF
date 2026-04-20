def count(a:int, b:int) -> int:
    if a == 0 or b == 0:
        return 0
    if a < b:
        return count(b,a)
    return a // b + count(a % b, b)
