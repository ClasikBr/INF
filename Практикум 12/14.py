def numbers(x:int) -> None:
    print(x % 10)
    if x >= 10:
        numbers(x // 10)
