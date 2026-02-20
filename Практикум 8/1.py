text=input()
spaces=0
cur=0
for ch in text:
    if ch.isspace():
        cur+=1
        spaces=max(spaces,cur)
    else:
        cur=0
print(spaces)