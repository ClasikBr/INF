def calc(s):
    s = s.replace(" ", "")
    i = 0
    def simple_expr():
        nonlocal i
        val = complex_expr()
        while i < len(s) and s[i] in "+-":
            op = s[i]; i += 1
            x = complex_expr()
            val = val + x if op == "+" else val - x
        return val

    def complex_expr():
        nonlocal i
        val = degree()
        while i < len(s) and s[i] in "*/":
            op = s[i]; i += 1
            x = degree()
            val = val * x if op == "*" else val / x
        return val

    def degree():
        nonlocal i
        val = parenthesis()
        while i < len(s) and s[i] == "^":
            i += 1
            x=degree()
            val = val ** x
        return val

    def parenthesis():
        nonlocal i
        if s[i] == "-":
            i += 1
            return -parenthesis()

        if s[i] == "(":
            i += 1
            val = simple_expr()
            i += 1
            return val

        j = i
        while j < len(s) and (s[j].isdigit() or s[j] == "."):
            j += 1
        val = float(s[i:j])
        i = j
        return val

    return simple_expr()


expr = input()
print(calc(expr))