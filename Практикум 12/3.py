def progress(a1:int, r:int, n:int) -> int:
    if n == 1:
        return a1
    return progress(a1,r,n-1) + r
