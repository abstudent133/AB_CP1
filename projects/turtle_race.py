#AB 1st Turtle Race
#Get the turtle library
import turtle as t
#Get the random library
import random as r


#Set up turtle one
t1 = t.Turtle()
#Set up turtle two
t2 = t.Turtle()
#set up turtle three
t3 = t.Turtle()
#set up turtle four
t4 = t.Turtle()
#set up turtle five
t5 = t.Turtle()
#set up finish line
t6 = t.Turtle()
#put all the turtles in one, easy to access location called turtles
turtles = [t1, t2, t3, t4, t5]
#set color,shape, and position of turtle one
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.setposition(0,300)
t1.pendown()

#set color, shape, and position of turtle two
t2.color("orange")
t2.shape("turtle")
t2.penup()
t2.setposition(0,250)
t2.pendown()

#set color, shapem, and postion of turtle three
t3.color("yellow")
t3.shape("turtle")
t3.penup()
t3.setposition(0,200)
t3.pendown()

#set color, shape, and position of turtle four
t4.color("green")
t4.shape("turtle")
t4.penup()
t4.setposition(0,150)
t4.pendown()

#set color, shape, and position of turtle five
t5.color("blue")
t5.shape("turtle")
t4.penup()
t5.setposition(0,100)
t5.pendown()

#set color, shape and position of the finish line
t6.color("black")
t6.shape("arrow")
t6.penup()
t6.setposition(500,0)
t6.pendown()

# draw finish line
t6.left(90)
t6.forward(290)
#create the value for the finish line
finish_line = 500
#make the race on be true
race_on = True
#while the race is on
while race_on: 
    # for each turtle in the turtles catigory  
    for turtle in turtles:
        #the turtle will move forward a small random amount
        turtle.forward(r.randint(1,10))
        #if the turtle reaches the finish line
        if turtle.xcor() >= finish_line:
            #then the race is over
            race_on = False
            #the winner color is the turtles color
            winner_color = turtle.pencolor()
            #show who the winner is
            print(f"The winner is {winner_color} turtle!")
            #exit loop
            break
#end turtle
t.done()


