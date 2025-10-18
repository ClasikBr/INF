n=int(input())
if 999<n<10000:
    if not(1900<=n<=2050):
        if len(set(str(n)))==4:
         print("OK")
        else:print("ERROR")
    else: print("ERROR")
else:print("ERROR")