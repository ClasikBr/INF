def nod(a:int, b:int) -> int:
    if b == 0:
        return a
    return nod(b, a % b)
