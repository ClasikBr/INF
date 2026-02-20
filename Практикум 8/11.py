city=input().split()
winner=None
for i in range(1,len(city)):
    prev=city[i-1]
    cur=city[i]
    if cur[0].lower() != prev[-1].lower():
        if i%2==0:winner='Петя'
        else:winner='Вася'
        break
if winner is None:
    if (len(city)-1)%2==0:winner='Петя'
    else:winner='Вася'
print(winner)