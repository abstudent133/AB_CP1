#AB 1st Draw
import turtle

def draw_branch(length):
    if length > 5:
        for i in range(1,3):
            turt.forward(length)
            draw_branch(length/3)
            turt.backward(length)
            turt.right(60)

turt = turtle.Turtle()
turt.speed(3)
turt.color("light blue")
turt.penup()
turt.setposition(0,0)
turt.pendown()

for i in range(1,6):
    draw_branch(100)
    turt.right(60)

turt.hideturtle()

