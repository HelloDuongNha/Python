import turtle as t

n = int(input('nhap n : '))
goc = 360/n
for i in range (n):
    t.pensize(3)
    t.pencolor((255,45,45))
    t.forward(100)
    t.backward(100)
    t.left(goc)
t.exitonclick()