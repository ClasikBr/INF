X,Y=map(int,input().split())
print(int(X % Y == 0 or Y % X == 0) or (X%Y))