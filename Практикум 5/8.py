def money(n):
    g=n//(17*29)
    s=(n//29)%17
    k=n%29
    ans=[]
    if g: ans.append(f"{g} галлеонов")
    if s: ans.append(f"{s} сиклей")
    if k: ans.append(f"{k} кнатов")
    print("\n".join(ans))
money(int(input()))