import turtle
mw = turtle.Screen()
mw.bgcolor("light blue")
mw.title("Turtle")
mp = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        mp.fd(size + 1)
        mp.left(90)
        size = size - 5 
    size = size + 1