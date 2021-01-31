# turtle colours

import turtle

murtle = turtle.Turtle()

colors = ['red','green','blue','purple']
for i in range (4): 
    murtle.color(colors[i])
    murtle.forward(100)
    murtle.left(90)
    print(colors[i])

input('Enter to close')
