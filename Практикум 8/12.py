import keyword
s = input()
print(s.isidentifier() and not keyword.iskeyword(s))