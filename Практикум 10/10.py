def special_num(a: int, b: int) -> None:
    if a > b:
        a, b = b, a

    allowed = {'1','3','4','8','9'}

    nums = [str(x) for x in range(a, b + 1)
            if set(str(x)).issubset(allowed)]

    print(', '.join(nums))
