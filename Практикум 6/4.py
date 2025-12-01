a=input()
let=a[0]
num=int(a[1])
let_1=ord(let)-ord('a')+1
print(let_1)
if (let_1+num)%2==0:print('чёрный')
else:print('белый')