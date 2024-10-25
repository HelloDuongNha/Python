# draw a bowtie

import turtle as t

t.pensize(7)
t.fillcolor("blue")
t.begin_fill()
t.goto(0,-100)
t.goto(-100,-100)
t.goto(-100,0)
t.goto(0,0)
t.end_fill()
t.fillcolor("yellow")
t.begin_fill()
t.goto(100,0)
t.goto(100,100)
t.goto(0,100)
t.goto(0,0)
t.end_fill()





t.exitonclick()
