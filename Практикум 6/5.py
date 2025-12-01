start,end=input().split('-')
dx=abs(ord(start[0]) -ord(end[0]))
dy=abs(int(start[1])-int(end[1]))
print('верно' if dx*dy==2 else 'ошибка')