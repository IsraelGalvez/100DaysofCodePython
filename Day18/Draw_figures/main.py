from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')

sides_of_figures = [3, 4, 5, 6, 7, 8, 9]
dictionary_of_figures = { 
                          'Triangle': { 
                            'sides': 3, 
                            'color': 'blue'
                          }, 
                          'Square': { 
                            'sides': 4, 
                            'color': 'red'
                          },
                          'Pentagon': { 
                            'sides': 5, 
                            'color': 'yellow'
                          }, 
                          'Hexagon': { 
                            'sides': 6, 
                            'color': 'orange'
                          },
                          'Heptagon': { 
                            'sides': 7, 
                            'color': 'black'
                          }, 
                          'Nonagon': { 
                            'sides': 8, 
                            'color': 'purple'
                          },
                          'decagon': { 
                            'sides': 9, 
                            'color': 'green'
                          }, 
                        }

def figures():
    count = 2
    for figure in dictionary_of_figures:
        tim.color(dictionary_of_figures[figure]['color'])
        angle = 360 / dictionary_of_figures[figure]['sides']
        for num in range(count):
            tim.forward(100)
            tim.left(angle * count)
        tim.forward(100)
        tim.right(angle)
        count += 1

figures()


screen = Screen()
screen.exitonclick()