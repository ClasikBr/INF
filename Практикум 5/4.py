n=int(input())
def count(n):
    if 10<n%100<15:
        return "попугаев"
    elif n%10==1:
        return "попугай"
    elif 1<n%10<5:
        return "попугая"
    else:
        return "попугаев"
print(f"{n} {count(n)}")