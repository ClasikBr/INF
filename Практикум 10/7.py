def CM(a:int, b:int, n:int) -> None:
    for x in range(1, n + 1):
        if x % a == 0 and x % b == 0:
            print(x)
