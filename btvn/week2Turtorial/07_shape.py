import turtle as t

shape = str(input("Which shape do you want? triangle or square? "))
if shape == "triangle" or shape == "Triangle":
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.exitonclick()

elif shape == "square" or shape == "Square":
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.exitonclick()
else:
    print("Sorry, I don't recognize that shape.")