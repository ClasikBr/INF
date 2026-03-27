def fibonacchi(n: int) -> None:
    a, b = 1, 1

    for _ in range(n):
        print(a, end=' ')
        a, b = b, a+b
