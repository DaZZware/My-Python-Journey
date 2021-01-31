# My FUnctions part 2

import turtle
shell = turtle.Turtle()

# Square function
def square(s): # Not defind size
    for i in range(4):
        shell.forward(s) # not defind distance
        shell.left(90)

square(60) #calling the function and in brackets size
shell.forward(60)#Distance can be defind
square(76)
shell.forward(76)
square(150)

input()