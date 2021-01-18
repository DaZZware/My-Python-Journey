# Turtle Loop Pattern demo

import turtle

paul = turtle.Turtle()
paul.shape('turtle')
paul.begin_fill() # Starts colouring line
paul.color('red')

# nested loop a loop with a loop to repeat one loop multiple times, this was orignally set to 6 in book
for n in range (100):
    # i is a variable and could easily be name alternative
    for i in range (4): # this will repeat the loop 4 times with for loop, this can be increased or decreased.
        paul.forward(100)
        paul.left(90)
    paul.right(35) # changes position on starting point but degrees noted this was at 60 and end result was a pettle in shape

   # paul.end_fill() # fills the end shape first time
    
     # print(i) # shows how many times loop has completed. if needed


input()