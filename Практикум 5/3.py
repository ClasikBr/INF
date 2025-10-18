num=int(input())
rev_num=(num%10)*1000 + ((num//10)%10) * 100 + ((num//100)%10)*10 + (num//1000)
if num==rev_num:
    print("настоящее")
else:
    print('кривое')