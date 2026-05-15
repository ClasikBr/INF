from itertools import permutations

let = 'ХОДМАТ'
for p in permutations('0123456789', 6):
    d = dict(zip(let, p))
    if d['Х'] == '0' or d['М'] == '0':
        continue

    hod = int(d['Х'] + d['О'] + d['Д'])
    mat = int(d['М'] + d['А'] + d['Т'])

    if hod * 3 == mat:
        print(f"{hod}+{hod}+{hod}={mat}")