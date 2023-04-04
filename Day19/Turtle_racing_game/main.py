from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue"]
turtles = []
dic = {'red': 0, 'orange': 1, 'yellow': 2, 'green': 3, 'blue': 4}


def making_turtles():
    height = -85

    for turtle_index in range(0, 5):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.goto(x=-220, y=height)
        new_turtle.color(colors[turtle_index])
        height += 40
        turtles.append(new_turtle)


def racing_tutle():
    is_race_on = True
    index = -1
    while (is_race_on):
        index += 1
        name_turtle = turtles[index]
        name_turtle.forward(random.randint(0, 10))
        name_turtle.speed(5)
        if name_turtle.xcor() >= 210:
            winner(index, name_turtle.pencolor())
            is_race_on = False
        if index == 4:
            index = -1


def winner(index, winner_color):
    if dic[user_bet] == index:
        print(f"You've won! The {winner_color} turtle is the winner!")
    else:
        print(f"You've lost! The {winner_color} turtle is the winner!")


def main():
    making_turtles()
    racing_tutle()


main()


screen.exitonclick()
