def price(cost: float, card: bool, holiday: bool) -> float:
    dis = 0

    if cost > 30000:
        dis += 10
    elif cost > 20000:
        dis += 7
    elif cost > 15000:
        dis += 5
    elif cost > 5000:
        dis += 3

    if card:
        dis += 5
    if holiday:
        dis += 3

    dis = min(dis, 15)
    price = cost * (1 - dis / 100)

    return round(price, 2)
