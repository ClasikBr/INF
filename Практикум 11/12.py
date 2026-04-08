holes = set('abdegopq')

words = input().split()

hole_ct = sum(ch in holes for w in words for ch in w)
nohole_ct = sum(ch.isalpha() and ch not in holes for w in words for ch in w)

ans = [w for w in words if sum(ch in holes for ch in w) >= 2]

print(hole_ct, nohole_ct)
print(ans)
