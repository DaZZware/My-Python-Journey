# Circle face using turtle for loops

import turtle

shelly = turtle.Turtle()
turtle.speed(60)
turtle.bgcolor('black')

shelly.goto(0,-150)
shelly.pendown()
shelly.begin_fill()
shelly.color('dark green')
shelly.circle(200)
shelly.end_fill()

shelly.goto(0,-100)
shelly.pendown()
shelly.begin_fill()
shelly.color('green')
shelly.circle(100)
shelly.end_fill()

shelly.penup()
shelly.goto(-30,100)
shelly.pendown()
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(10)
shelly.end_fill()
shelly.penup()
shelly.goto(30,100)
shelly.pendown()
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(10)
shelly.end_fill()
shelly.penup()
shelly.goto(0,20)
shelly.pendown()
shelly.begin_fill()
shelly.color('red')
shelly.circle(20)
shelly.end_fill()
shelly.penup()



input()