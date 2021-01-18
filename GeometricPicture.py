# Making Geometric paterns with Turtle and loops
import turtle # import to import libraries to use

pat = turtle.Turtle()
turtle.bgcolor('black') # background changed to black
colors = ['pink','green','blue','orange','purple','pink']
pat.speed(100)

for a in range(10): # this creates 36 hexagon's to create a pattern, turtle is 2D with 360 degrees to print
    for a in range(6):
        pat.color(colors[a])
        pat.forward(50)
        pat.left(60)
    pat.right(40)
for i in range(36):
    pat.penup()
    pat.color('white')
    pat.forward(220)
    pat.pendown()
    pat.circle(10)
    pat.penup()
    pat.backward(220)
    pat.right(10)
    pat.hideturtle()
    
input()