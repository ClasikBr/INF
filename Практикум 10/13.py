import turtle as t

t.tracer(0,0)


def triangle(a,b,c, color):
    t.fillcolor(color)
    t.begin_fill()
    t.pu()
    t.goto(a)
    t.goto(b)
    t.goto(c)
    t.goto(a)
    t.end_fill()


def square(x, y, size, color1, color2):
    a = (x,y)
    b = (x + size, y)
    c = (x + size, y + size)
    d = (x, y + size)

    triangle(a, b, c, color1)
    triangle(a, c, d, color2)


def draw():
    size = 60
    rows = 6
    cols = 6

    colors = [
        ("#8ecae6", "#219ebc"),
        ("#219ebc", "#023047"),
        ("#ffb703", "#fb8500"),
        ("#8ecae6", "#023047"),
    ]

    st_x = -180
    st_y = -180

    for r in range(rows):
        for c in range(cols):
            x = st_x + c * size
            y = st_y + r * size
            color1, color2 = colors[(r + c) % len(colors)]
            square(x, y, size, color1, color2)

    t.update()


draw()
t.done()