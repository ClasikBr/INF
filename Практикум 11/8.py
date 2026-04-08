def string(s):
    chars = list(s)
    chars.sort()
    return ''.join(chars)

text = input()
print(string(text))
