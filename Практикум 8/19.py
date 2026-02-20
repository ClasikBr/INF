vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

def split_russian_word(word, width):
    if len(word) <= width:
        return [word]

    parts = []
    while len(word) > width:
        cut = width
        while cut > 1 and word[cut] not in vowels:
            cut -= 1

        if cut <= 1:
            cut = width

        parts.append(word[:cut] + "-")
        word = word[cut:]

    parts.append(word)
    return parts


def justify(text, width):
    words = text.split()
    lines = []
    line = []

    for w in words:

        if len(w) > width:
            chunks = split_russian_word(w, width)

            for ch in chunks[:-1]:
                if line:
                    if len(line) == 1:
                        lines.append(line[0].ljust(width))
                    else:
                        total_spaces = width - sum(len(x) for x in line)
                        gaps = len(line) - 1
                        base = total_spaces // gaps
                        extra = total_spaces % gaps

                        result = ""
                        for i in range(gaps):
                            result += line[i] + " " * (base + (1 if i < extra else 0))
                        result += line[-1]

                        lines.append(result)
                    line = []

                lines.append(ch.ljust(width))

            w = chunks[-1]

        if len(" ".join(line + [w])) <= width:
            line.append(w)
        else:
            if len(line) == 1:
                lines.append(line[0].ljust(width))
            else:
                total_spaces = width - sum(len(x) for x in line)
                gaps = len(line) - 1
                base = total_spaces // gaps
                extra = total_spaces % gaps

                result = ""
                for i in range(gaps):
                    result += line[i] + " " * (base + (1 if i < extra else 0))
                result += line[-1]

                lines.append(result)

            line = [w]

    last = " ".join(line)
    lines.append(last.ljust(width))

    return "\n".join(lines)


text = input()
width = int(input())
print(justify(text, width))