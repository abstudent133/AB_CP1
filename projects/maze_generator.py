#AB 1st Maze Generator

#import libraries(turtle and random)
import turtle as t
import random as r

cell_size = 50
rows = 6
columns = 6
boxes = [[],[],[],[]]
visited = []
row_grid = []
column_grid = []






#set up turtle
def setup_turtle():
    t.title("Maze")
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    t.penup()
def grid_setup():
    for i in range(1, 36):
        boxes[0].append(1)
        boxes[1].append(1)
        boxes[2].append(1)
        boxes[3].append(1)

def randomize_walls():
    grid_setup()
    for n in boxes[0]:
        choice = r.randint(0,1)
        if choice == 0:
            n = 0
        else:
            continue
    for n in boxes[1]:
        choice = r.randint(0,1)
        if choice == 0:
            n = 0
        else:
            continue
    for n in boxes[2]:
        choice = r.randint(0,1)
        if choice == 0:
            n = 0
        else:
            continue
    for n in boxes[3]:
        choice = r.randint(0,1)
        if choice == 0:
            n = 0
        else:
            continue
    return boxes
    
        
        
        
def draw_grid():
    t.setpos(0,0)
    for i in range(rows +1):
        t.pendown()
        for l in range(1,5):
            t.forward(50)
            t.left(90)
        

    

setup_turtle()
grid_setup()
print(grid_setup())
randomize_walls()
print(randomize_walls())
t.done()


    



#function of creating the lines on a column(col_coordinate, column)
    #
    #for each 

    