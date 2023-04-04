from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_circles(size_gap):
    count = 0
    while count < 360:
        tim.color(random_color())
        tim.right(count)
        tim.circle(80)
        tim.home()
        count += size_gap   

draw_circles(10)

screen = Screen()
screen.exitonclick()
