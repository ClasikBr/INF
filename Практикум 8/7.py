text=input().split()
mn=10**100
cur=0
for s in text:
    cur=len(s)
    mn=min(mn,cur)
print(mn)