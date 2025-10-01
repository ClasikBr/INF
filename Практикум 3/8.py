import math
a=int(input())
b=int(input())
c=int(input())
def angle(a, b, c):
    A = math.degrees(math.acos((b*b + c*c - a*a) / (2 * b * c)))
    B = math.degrees(math.acos((a*a + c*c - b*b) / (2 * a * c)))
    C = 180 - A - B
    return A, B, C
print(angle(a,b,c))
