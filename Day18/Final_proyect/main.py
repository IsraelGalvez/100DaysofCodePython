import turtle as t
import random

rgb_colors = [(249, 248, 248), (238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17),
              (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32),
              (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145),
              (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216),
              (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

tim = t.Turtle()
t.colormode(255)

def draw_dots(cordenadas_x, cordenadas_y, separacion, num_dot_x, num_dot_y):
    tim.setpos(cordenadas_x, cordenadas_y)

    for _ in range(num_dot_y):
        for _ in range(num_dot_x):
            tim.color(random.choice(rgb_colors))
            tim.pendown()
            tim.forward(.1)
            tim.penup()
            tim.forward(separacion)
        cordenadas_y += separacion
        tim.setpos(cordenadas_x, cordenadas_y)
    tim.hideturtle()

def main():
    tim.pensize(15)
    tim.speed("fastest")
    tim.penup()
    draw_dots(-250, -250, 50, 10, 10)

main()

screen = t.Screen()
screen.exitonclick()


