#AB 1st Maze Generator

#import libraries(turtle and random)
import turtle as t
import random as r
#set variables
cell_size = 50
rows = 6
columns = 6
row_grid = []
column_grid = []
visited = []
#set origin points
origin_x = -columns * cell_size/2
origin_y = rows * cell_size/2

#fuction to randomize walls

#function to check maze solveable

#function





#set up turtle
def setup_turtle():
    t.title("Maze")
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    t.penup()

def grid_setup(row_):
    


    
        
        
        
def draw_grid():
    t.setpos(0,0)
    for i in range(rows +1):
        t.pendown()
        for j in range(1,5):
            t.forward(cell_size)
            t.left(90)
        

    

setup_turtle()
grid_setup(boxes)
randomize_walls(boxes)

t.done()


    



#function of creating the lines on a column(col_coordinate, column)
    #
    #for each 

    