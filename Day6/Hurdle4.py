def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    
while not at_goal():
    if (wall_in_front() == True) and (wall_on_right() == True):
        turn_left()
        move()
    else:
        move()
    if (right_is_clear() == True):
        jump()
    elif (right_is_clear() == False) and (wall_in_front() == True):
        turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
