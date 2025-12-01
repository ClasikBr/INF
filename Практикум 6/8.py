c=int(input())
for x in range(201):
    if x<10:len=1
    elif x<100:len=2
    else:len=3
    if c<=len:
        if len==1:print(x)
        elif len==2:
            if c==1:print(x//10)
            else:print(x%10)
        else:
            if len==1:print(x//100)
            elif len==2:print((x//10)%10)
            else:print(x%10)
        break
    else:c-=len