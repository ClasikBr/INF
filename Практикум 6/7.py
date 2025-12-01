def chech(c):
    for i in range((c//7)+1):
        a=c-i*7
        if a%5==0:
            return 'да'
    return 'нет'
c=int(input())
print(chech(c))