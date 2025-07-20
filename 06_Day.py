# site: https://reeborg.ca/reeborg.html

# Alone
# Free Exploration

# Home 1 and 2
move()
move()

# Home 3
move()
move()
turn_left()
move()

# Home 4 
#-------------Simple-------------#
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move3():
    move()
    move()
    move()
    
move3()
turn_left()
move3()
turn_right()
move()
turn_right()
move3()
turn_left()
move3()
turn_right()
move()
turn_right()
move3()
turn_left()
move3()
turn_right()
move()
turn_right()
move3()
turn_left()
move3()

#-------------Advanced-------------#
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def L_shape():
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()

def next_L():
    turn_right()
    move()
    turn_right()

repeat 3:
    L_shape()
    next_L()
L_shape()    

# Around 1
put()
repeat 4:
    while not wall_in_front():
        move()
    turn_left() 

# Around 1- Variable (Also works for Around 1)
put()
move()
while not object_here():
    while not wall_in_front():
        move()
        if object_here():
            done()
    turn_left()

# Around 1- Apple
repeat 4:
    while front_is_clear():
        if object_here():
            take()
        move()
    turn_left()

# Around 2 (Also works for Around 1)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

put()
move()
while not object_here():
    while front_is_clear():
        move()
        if object_here():
            done()
        if right_is_clear():
            turn_right()
    turn_left()

# Around 3 (Also works for Around 1 & 2)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def climb_wall():
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    turn_left()
    
put()
if wall_in_front():
    climb_wall()
else:
    move()
while not object_here():
    while front_is_clear():
        move()
        if object_here():
            done()
        if right_is_clear():
            turn_right()
        if wall_in_front():
            turn_left()
    turn_left()

# Around 4 (Also works for Around 3)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def opp_way():
    turn_left()
    turn_left()
    
opp_way()
if front_is_clear():   # "not front_is_clear()" for Around 1 & Around 2 
    pass
else:
    opp_way()
    
if front_is_clear() and not right_is_clear():
    move()
    opp_way()
    toss()
    turn_left()
    
elif front_is_clear() and right_is_clear():
    put()
    turn_right()
    move()
    turn_right()
  
else:
    put()
    opp_way()
    move()
while not object_here():
    while front_is_clear():
        move()
        if object_here():
            done()
        if right_is_clear():
            turn_right()
        if wall_in_front():
            turn_left()
    turn_left()

# Centre 1

    
    
    
    
    






    
    
    
    
    
    






    
        



    



