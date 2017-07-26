import turtle

t=turtle.Turtle()

x = 0
while x<300:
    y=x**2/300
    t.goto(x,y)
    x=x+100
    
