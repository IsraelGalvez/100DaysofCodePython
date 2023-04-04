from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.pensize(15)
tim.speed("fastest")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

list_of_degrees = [90, 180, 270, 360]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", 
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", 
           "SeaGreen"]

for i in range(200):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(list_of_degrees))


screen = Screen()
screen.exitonclick()