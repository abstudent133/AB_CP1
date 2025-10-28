#AB 1st Library and built in functions

import turtle as t
import random

colors = ["red","orange","yellow","green","blue","purple","pink"]
side = random.randint(10,500)

t.color(random.choice(colors))
t.shape("turtle")

t.fillcolor(random.choice(colors))
t.begin_fill()
for x in range(1,5):
    t.forward(side)
    t.right(90)
t.end_fill()

t.penup()
t.goto(50,50)

t.pendown()
t.color(random.choice(colors))
t.begin_fill()
for x in range(1,5):
    t.forward(side)
    t.right(90)
t.end_fill()


t.done()