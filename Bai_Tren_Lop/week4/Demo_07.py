import turtle as t

n = int(input('nhap so canh n giac deu : '))
goc = 180-((1-(2/n))*180)
for i in range (n):
    t.pensize(3)
    t.forward(100)
    t.left(goc)
t.exitonclick()