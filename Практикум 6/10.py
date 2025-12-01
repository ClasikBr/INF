def check(r1,r2):
    left1=min(r1[0],r1[2])
    right1=max(r1[0],r1[2])
    top1=max(r1[1],r1[3])
    bot1=min(r1[1],r1[3])
    left2=min(r2[0],r2[2])
    right2=max(r2[0],r2[2])
    top2=max(r2[1],r2[3])
    bot2=min(r2[1],r2[3])
    if right1<left2 or left1>right2 or top1<bot2 or bot1>top2:
        return 'Лежат вне друг друга, не касаясь'
    r1_in_r2= left1>left2 and right1<right2 and top1<top2 and bot1>bot2
    r2_in_r1= left2>left1 and right1>right2 and top1>top2 and bot1<bot2
    if r1_in_r2 or r2_in_r1:
        return 'Один прямоугольник лежит внутри другого, не касаясь'
    if right1==left2 or left1==right2 or top1==bot2 or bot1==top2:
        return 'Прямоугольники имеют касание'
    return 'Прямоугольники имеют пересечение'
r1=list(map(int,input().split()))
r2=list(map(int,input().split()))
print(check(r1,r2))