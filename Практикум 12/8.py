def fib(k:int) -> int:
    if k <= 2:
        return 1
    return fib(k-1) + fib(k-2)
