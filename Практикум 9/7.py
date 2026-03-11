with open('input.txt', 'r', encoding='utf-8') as fin:
    lines = fin.readlines()

filt = []

for line in lines:
    strp = line.strip()
    if strp != '100':
        filt.append(line)

with open('input.txt', 'w', encoding='utf-8') as fout:
    fout.writelines(filt)
