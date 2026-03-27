def prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def print_prime() -> None:
    n = int(input())

    for num in range(1, n + 1):
        if prime(num):
            print(num)


print_prime()
