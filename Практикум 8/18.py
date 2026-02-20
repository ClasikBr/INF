def justify(text, width):
    words = text.split()
    lines = []
    line = []

    for w in words:
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