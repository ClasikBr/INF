X,Y,N=map(int,input().split())
money=((X*100+Y)*N)
R=money//100
K=money%100
print(R,'руб. ',K,'коп.')