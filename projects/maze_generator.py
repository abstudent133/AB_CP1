#AB 1st Maze Generator

#import libraries(turtle and random)
import turtle as t
import random as r

cell_size = 50
rows = 2
columns = 2

top = []
bottom = []
left = []
right = []
visited = []



#set up turtle
def setup_turtle():
    t.setup(columns * cell_size + 50, rows * cell_size + 50)
    t.title("Maze")
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    t.penup()
def grid_setup():
    for i in range(rows*columns):
        top.append(1)
        bottom.append(1)
        left.append(1)
        right.append(1)
        visited.append(0)

def draw_grid():
    t.setpos(0,columns * cell_size)
    
def main():
    setup_turtle()
    t.done()
main()   

    



#function of creating the lines on a column(col_coordinate, column)
    #
    #for each 

    