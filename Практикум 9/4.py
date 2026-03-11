with open("input.txt", encoding="utf-8") as fin, \
     open("output.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        text = line.rstrip("\n")
        if len(text) > 20:
            fout.write(line)
