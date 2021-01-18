# Turtle Graphics

import turtle

shelly = turtle.Turtle()
shelly.forward(100)
shelly.right(90)
shelly.left(60)
shelly.backward(100)
shelly.color('red') # Changes colour of line, americanized spelling
shelly.circle(10) # Draws a circle to size 10
shelly.penup()  # stops drawing if moves agai
shelly.pendown() # restarts drawing
shelly.reset() # Clears screen and returns to original start point
shelly.goto(35, 80) # moves to this coordenate
shelly.hideturtle() # Hides pen/turtle pointer

# lists for storing data

colors = ['red', 'green' ,'blue']

colors[0]
colors[1]


shelly.shape('turtle') # changes from pointer to turtle shape
print(shelly.xcor(), shelly.ycor()) # Shoes location of turtle to screen coordinates
turtle.screensize() # checks size of screen

input()