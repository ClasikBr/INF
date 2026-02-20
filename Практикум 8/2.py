text=input()
mx_len=0
cur=1
for i in range(1,len(text)):
    cur=cur+1 if text[i] == text[i-1] else 1
    mx_len=max(mx_len,cur)
print(mx_len)