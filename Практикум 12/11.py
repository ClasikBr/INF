def ind_maxlist(a:list) -> int:
    if len(a) == 1:
        return 0
    idx = ind_maxlist(a[1:])
    return 0 if a[0] >= a[idx + 1] else idx + 1
