def make_payment(p: float) -> None:
    if 20 <= p <= 1000:
        print('Успех')
    else:
        print('Повторите попытку')
