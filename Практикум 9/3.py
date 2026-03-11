letters = []

with open("input.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line.strip()
        if line:
            letters.append(line[0])

with open("output.txt", "w", encoding="utf-8") as fout:
    fout.write("".join(letters))
