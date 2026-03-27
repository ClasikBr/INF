import random
import turtle
from typing import Tuple

WIDTH, HEIGHT = 900, 600
BASE_Y = -HEIGHT // 2 + 30


def setup() -> None:
    turtle.setup(WIDTH, HEIGHT)
    turtle.title("Ночной город")
    turtle.colormode(255)
    turtle.bgcolor((18, 20, 50))
    turtle.hideturtle()
    turtle.tracer(0, 0)


def move(x: float, y: float) -> None:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def setc(c: Tuple[int, int, int]) -> None:
    turtle.color(c)


def draw_stars(n: int = 100) -> None:
    setc((255, 255, 255))
    for _ in range(n):
        x = random.randint(-WIDTH // 2 + 10, WIDTH // 2 - 10)
        y = random.randint(0, HEIGHT // 2 - 20)
        move(x, y)
        turtle.dot(random.choice([2, 3]))


def draw_moon(x: int = 260, y: int = 180, r: int = 50) -> None:
    for i, col in enumerate([(255, 245, 210), (240, 225, 180)]):
        move(x, y - (r + i * 10))
        setc(col)
        turtle.begin_fill()
        turtle.circle(r + i * 10)
        turtle.end_fill()

    move(x, y - r)
    setc((250, 235, 200))

    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

    move(x + int(r * 0.45), y - r)
    setc((18, 20, 50))

    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def window_square(x: float, y: float, s: int = 10) -> None:
    move(x, y)
    setc(random.choice([(255, 210, 110), (255, 230, 140)]))
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(s)
        turtle.left(90)
    turtle.end_fill()


def window_round(x: float, y: float, d: int = 12) -> None:
    move(x + d / 2, y)
    setc(random.choice([(255, 210, 110), (255, 230, 140)]))
    turtle.begin_fill()
    turtle.circle(d / 2)
    turtle.end_fill()


def window_bar(x: float, y: float, w: int = 14, h: int = 6) -> None:
    move(x, y)
    setc(random.choice([(255, 210, 110), (255, 230, 140)]))
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()


def draw_building(x: float, w: int, h: int, color: Tuple[int, int, int]) -> None:
    move(x, BASE_Y)
    setc(color)

    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()

    move(x, BASE_Y + h)
    setc((30, 30, 50))

    if random.random() < 0.6:
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(6)
            turtle.left(90)
        turtle.end_fill()
    else:
        turtle.begin_fill()
        turtle.forward(w)
        turtle.left(135)
        turtle.forward(w / 1.414)
        turtle.left(90)
        turtle.forward(w / 1.414)
        turtle.left(135)
        turtle.end_fill()

    rows = max(1, h // 30)
    cols = max(1, w // 22)

    for r in range(rows):
        for c in range(cols):
            if random.random() < 0.55:
                wx = x + 6 + c * 22
                wy = BASE_Y + 8 + r * 30
                t = random.random()

                if t < 0.45:
                    window_square(wx, wy)
                elif t < 0.75:
                    window_round(wx, wy)
                else:
                    window_bar(wx, wy)


def draw_city() -> None:
    x = -WIDTH // 2 + 10
    colors_far = [(18, 20, 36), (22, 24, 44)]
    colors_near = [(28, 30, 56), (36, 38, 72)]

    while x < WIDTH // 2 - 40:
        w = random.randint(60, 110)
        h = random.randint(110, 170)
        draw_building(x, w, h - 20, random.choice(colors_far))
        x += w + random.randint(6, 16)

    x = -WIDTH // 2 + 5

    while x < WIDTH // 2 - 20:
        w = random.randint(80, 140)
        h = random.randint(160, 260)
        draw_building(x, w, h, random.choice(colors_near))
        x += w + random.randint(8, 20)


def main() -> None:
    setup()
    draw_stars(120)
    draw_moon()
    draw_city()
    move(-WIDTH // 2, BASE_Y - 6)
    setc((8, 8, 12))
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(WIDTH)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)

    turtle.end_fill()
    turtle.update()
    turtle.done()


if __name__ == "__main__":
    main()
