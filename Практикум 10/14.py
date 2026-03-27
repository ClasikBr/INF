def find(s, sub, start=0, end=None):
    if end is None:
        end = len(s)

    n = len(sub)
    limit = end - n

    for i in range(start, limit + 1):
        if s[i:i + n] == sub:
            return i
    return -1


def find_ind(s,sub):
    ind = []
    pos = 0

    while True:
        pos = find(s, sub, pos)

        if pos == -1:
            break

        ind.append(str(pos))
        pos += 1

    return ','.join(ind)