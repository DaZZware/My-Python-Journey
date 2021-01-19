# 6 Squares 6 colours

import turtle

bert = turtle.Turtle()
colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']
turtle.bgcolor('black')

for o in range(6):
    bert.color(colors[o])
    print(colors[o])
    for a in range(4):
	    bert.forward(50)
	    bert.left(90)
    bert.penup()
    bert.forward(70)
    bert.pendown()

bert.hideturtle()
input()