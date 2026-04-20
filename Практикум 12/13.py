def odd_list(a:list,n:int) -> list:
    if n == 0:
        return []
    end = odd_list(a, n - 1)
    return end + [a[n-1]] if a[n-1] % 2 == 0 else end
