# from turtle import Turtle, Screen


# timmy = Turtle()

# timmy.shape("turtle")

# timmy.color("red")

# timmy.pendown()

# timmy.forward(100)

# my_screen = Screen()

# my_screen.exitonclick()

from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["Pokemon Name", "Type"]
x.add_row(["Pikachu", "Electric"])
x.add_row(["Ratata", "Animal"])
x.add_row(["Charisar", "Fire"])

print(x)