with open("input.txt", encoding = "utf-8") as fin, \
     open("output.txt", "w", encoding = "utf-8") as fout:
    fout.write(fin.read().upper())
