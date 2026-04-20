def simmetr(s: str, i: int, j: int) -> bool:
    if i > j:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)
