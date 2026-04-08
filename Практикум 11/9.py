import string

freq = {}
order = []

while True:
    line = input()
    if line == "":
        break

    for w in line.split():
        w = w.strip(string.punctuation).lower()
        if not w:
            continue

        if w not in freq:
            freq[w] = 0
            order.append(w)
        freq[w] += 1

order.sort(key=lambda x: freq[x], reverse=True)
for w in order:
    print(w)
