import turtle as t
from random import randint

goc=90
size=200
n = int(input('nhap n: '))
gocxoay = 360/(n*4)
t.speed(5)
t.pensize(2)
t.colormode(255)
for j in range(n):
    color = (randint(0,255), randint(0,255), randint(0,255))
    t.pencolor(color)
    for i in range(4):
        t.forward(size)
        t.left(goc)
        t.forward(size)
        t.left(goc)
        t.forward(size)
        t.left(goc)
        t.forward(size)
        t.left(180)
    t.left(gocxoay)


t.exitonclick()