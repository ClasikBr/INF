text=input()
for c in set(text):
    if text.count(c)==3:
        print(c)
        break