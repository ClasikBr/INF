N,K,M=map(int,input().split())
fw=(M-K)%N
bw=(K-M)%N
ans=min(fw,bw)-1
print(ans)