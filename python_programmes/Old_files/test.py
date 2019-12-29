import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")   
tess.shape("turtle")
tess.penup()
tess.pensize(3)

for i in range(12):
    
    tess.forward(80)
    tess.pendown()
    tess.forward(20)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.backward(120)
    tess.left(30)

