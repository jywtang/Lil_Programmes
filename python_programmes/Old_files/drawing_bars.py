import turtle
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    if height <0:
        t.penup()
        t.backward(20)
    t.write("  "+ str(height))    
    if height <0:
        t.forward(20)
        t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.penup()
    t.forward(10)
    t.pendown()
    

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)


xs = [48,117,-50,200,240,160,260,220]

for a in xs:
    if a >= 200:
        col = "red"
    elif a>= 100:
        col = "yellow"
    else:
        col = "green"
    tess.color("blue",col)
    draw_bar(tess, a)

wn.mainloop()
