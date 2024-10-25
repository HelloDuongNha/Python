# draw two squares, side by side, not touching

import turtle as t


def draw_square():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)


draw_square()

t.penup()
t.forward(150)
t.pendown()

draw_square()

t.exitonclick()

print()
input("Press return to continue ...")
