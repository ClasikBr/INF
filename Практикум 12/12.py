def search(a:list,x:int) -> int:
    if len(a) == 0:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)
