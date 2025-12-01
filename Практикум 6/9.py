import math
import turtle
def draw(t,x,y,r):
    t.penup(); t.goto(x*k,(y-r)*k); t.pd()
    t.circle(r*k)
    t.penup();t.goto(x*k,y*k);t.dot(5)
x1,y1,r1=map(float,input().split())
x2,y2,r2=map(float,input().split())
d=math.hypot(x1-x2,y1-y2)
sum_r,dif_r=r1+r1,abs(r1-r2)
if d>sum_r:print('Лежат отдельно')
elif math.isclose(d,sum_r):print('Внешнее касание')
elif d<dif_r:print('Одна внутри другой')
elif math.isclose(d,dif_r):print('Внутреннее касание')
else:print('Пересекаются')
k=20
t=turtle.Turtle()
t.speed(0)
draw(t,x1,y1,r1)
draw(t,x2,y2,r2)
turtle.done()