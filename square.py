import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
p = turtle.Turtle()

ns = 4
sl = 70
a = 360.0 / ns
for i in range(ns):
    p.forward(sl)
    p.right(a)

turtle.done()
