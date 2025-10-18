import turtle
import math
xc = float(input("xc: "))
yc = float(input("yc: "))
r = float(input("r: "))
x = float(input("x: "))
y = float(input("y: "))

turtle.pu()
turtle.goto(xc, yc - r)
turtle.setheading(0)
turtle.pd()
turtle.circle(r)

turtle.pu()
turtle.goto(x, y)
turtle.dot(10, "red")

dis = math.hypot(x - xc, y - yc)
if abs(dis - r) < 1e-6:
    print("Точка лежит на окружности")
elif dis < r:
    print("Точка внутри окружности")
else:
    print("Точка вне окружности")
turtle.done()