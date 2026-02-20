num=0
while True:
    num+=1
    bilet=input()
    mid=len(bilet)//2
    if len(bilet)%2==0 and (sum(map(int,bilet[:mid])) == sum(map(int,bilet[mid:]))):
        print(num)
        break