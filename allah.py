import turtle
#from  random import randint

wn = turtle.Screen()
wn.setup(width = 1.0, height = 1.0)
wn.bgcolor("black")

star = turtle.Pen()

star.color('black')
star.goto(400,250)

star.color('white')
for x in range(90):
    star.forward(1)
    star.left(1)
star.right(180)
star.forward(270)

star.color('black')
star.right(90)
star.forward(30)
star.goto(380,300)

star.color('white')
star.left(90)
star.forward(200)
for x in range(180):
    star.forward(1)
    star.right(1)
star.forward(30)

star.left(180)
star.forward(30)
for x in range(180):
    star.forward(1)
    star.right(1)
star.forward(30)

star.left(180)
star.forward(30)
for x in range(90):
    star.forward(1)
    star.right(1)
star.forward(30)

star.color('black')
star.goto(290,220)
star.color('white')
star.left(90)
star.forward(2)
for x in range(180):
    star.forward(0.2)
    star.right(1)
star.left(170)
star.forward(2)
for x in range(180):
    star.forward(0.2)
    star.right(1)
star.forward(9)
star.color('black')

