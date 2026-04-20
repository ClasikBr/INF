def mod_number(a:int,b:int) -> int:
    if a < b:
        return a
    return mod_number(a-b,b)
