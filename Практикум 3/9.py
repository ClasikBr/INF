ATT= int(input())
COMP=int(input())
YDS=int(input())
TD=int(input())
INT=int(input())
rating = ((
    max(0, min(2.375, ((COMP / ATT) - 0.3) * 5)) +
    max(0, min(2.375, ((YDS / ATT) - 3) * 0.25)) +
    max(0, min(2.375, (TD / ATT) * 20)) +
    max(0, min(2.375, 2.375 - (INT / ATT) * 25))
) / 6) * 100
print(rating)