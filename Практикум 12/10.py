def maxlist(a:list) -> int:
    if len(a) == 1:
        return a[0]
    m = maxlist(a[1:])
    return a[0] if a[0] > m else m
