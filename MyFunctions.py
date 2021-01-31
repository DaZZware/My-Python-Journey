# My FUnctions

import turtle
shell = turtle.Turtle()

# Square function
def square():
    for i in range(4):
        shell.forward(100)
        shell.left(90)

square() #calling the function
shell.forward(100)
square()
shell.forward(100)
square()

input()