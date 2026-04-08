lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]

l, r = map(int, input().split())

l -= 1
r -= 1

frag = lst1[l:r+1]

lst2.extend(frag[::-1])

del lst1[l:r+1]

print(lst1)
print(lst2)
