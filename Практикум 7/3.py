while True:
    a=int(input())
    n=int(a**0.5)
    if n*n==a:
        print("Число является полным квадратом")
        break
    else:print("Введи другое число")