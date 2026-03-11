try:
    with open("input.txt", encoding="utf-8") as fin:
        a, b, c = map(int, fin.read().split())

    ans = a / b + c

    with open("output.txt", "w", encoding="utf-8") as fout:
        fout.write(str(ans))

except ValueError:
    with open("output.txt", "w", encoding="utf-8") as fout:
        fout.write("ValueError")

except ZeroDivisionError:
    with open("output.txt", "w", encoding="utf-8") as fout:
        fout.write("ZeroDivisionError")
