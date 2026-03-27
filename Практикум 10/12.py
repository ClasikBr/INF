import turtle as t

#t.tracer(0, 0)
t.speed(0)

def circle():
    t.fillcolor("cyan")
    t.begin_fill()
    t.circle(40)
    t.end_fill()


def square():
    t.fillcolor("violet")
    t.begin_fill()
    for _ in range(4):
        t.forward(60)
        t.right(90)
    t.end_fill()


def triangle():
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(3):
        t.forward(60)
        t.right(120)
    t.end_fill()


def ornament():
    for _ in range(35):
        circle()
        square()
        triangle()
        t.right(10)


ornament()
t.done()
