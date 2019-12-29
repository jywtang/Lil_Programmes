import turtle
from time import sleep

def circle_area(r):
    return 3.14*r*r

def draw_circle(t_name, r, col='blue', x=0, y=0):
    t_name.penup()
    t_name.color(col)
    t_name.goto(x,y)
    t_name.dot(r*2)

    t_name.penup()
    t_name.goto(x, y+5)
    t_name.color('white')
    t_name.write("Area of circle = " + str(circle_area(r)) , align ='center')

    t_name.penup()
    t_name.goto(x, y-5)
    t_name.write("Circumference of circle = " + str(2*3.14*r) , align ='center')


scn = turtle.Screen()
john = turtle.Turtle()

draw_circle(john, int(input("Circle size: ")), input('Colour: '),
            int(input('x position: ')), int(input('y position: ')))

scn.mainloop()
