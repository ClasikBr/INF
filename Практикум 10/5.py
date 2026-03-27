def value(cost: int) -> int:
    bonus = {5: 0, 10: 0, 25: 3, 50: 8, 100: 20}

    if cost not in bonus:
        raise ValueError('Недопустимая стоимость')

    return cost + bonus[cost]
