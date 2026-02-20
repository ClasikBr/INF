text=input().split()
first=text[0]
for word in text:
    if word!=first and len(word)==len(set(word)):
        print(word)