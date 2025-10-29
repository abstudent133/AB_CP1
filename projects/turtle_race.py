#AB 1st Turtle Race

import turtle as t
import random as r

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()

turtles = [t1, t2, t3, t4, t5]

t1.color("red")
t1.shape("turtle")
t1.penup()
t1.setposition(0,300)
t1.pendown()


t2.color("orange")
t2.shape("turtle")
t2.penup()
t2.setposition(0,250)
t2.pendown()


t3.color("yellow")
t3.shape("turtle")
t3.penup()
t3.setposition(0,200)
t3.pendown()


t4.color("green")
t4.shape("turtle")
t4.penup()
t4.setposition(0,150)
t4.pendown


t5.color("blue")
t5.shape("turtle")
t4.penup()
t5.setposition(0,100)
t5.pendown()


t6.color("black")
t6.shape("arrow")
t6.penup()
t6.setposition(500,0)
t6.pendown()


t6.left(90)
t6.forward(290)

while t1.pos() > 500 and t2.pos() > 500:
    for turtle in turtles:
        turtle.forward(r.randint(5,10))


