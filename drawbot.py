import turtle


draw_bot = turtle.Turtle()


draw_bot.speed(5)


def draw_square():
    for _ in range(4):
        draw_bot.forward(100)
        draw_bot.right(90)


def draw_circle():
    draw_bot.circle(50)

def draw_triangle():
    for _ in range(3):
        draw_bot.forward(100)
        draw_bot.left(120)


draw_bot.penup()
draw_bot.goto(-200, 0)
draw_bot.pendown()


draw_square()


draw_bot.penup()
draw_bot.goto(-50, 0)
draw_bot.pendown()


draw_circle()


draw_bot.penup()
draw_bot.goto(100, 0)
draw_bot.pendown()


draw_triangle()


draw_bot.hideturtle()


turtle.exitonclick()
