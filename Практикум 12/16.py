def ten_to_n(x:int,n:int) -> str:
    digits = '0123456789ABCDEF'
    if x < n:
        return digits[x]
    return ten_to_n(x // n, n) + digits[x % n]
