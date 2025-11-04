#AB 1st Maze Generator

#import libraries(turtle and random)
import turtle as t
import random as r

#set maze height to 300
height = 300
#set maze width to 300
width = 300
#number of boxes
boxes = 36
#row grid
row_grid = [[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)],
        [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)],
        [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5)],
        [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5)],
        [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5)],
        [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)]]
#create a grid that shows if there is a line or not called grid_row
grid_row = [[0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],]
#column grid
col_grid = [[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)],
        [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)],
        [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5)],
        [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5)],
        [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5)],
        [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)]]
#create a grid to show if ther is a line or not in the colums called grid_col
grid_col = [[0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],]
making_maze = True
while making_maze:
        for num in grid_row:
                change_num = r.randint(0,1)
                num_index = num.index(num)
                grid_row[num_index] = change_num
        

    



#function of creating the lines on a column(col_coordinate, column)
    #
    #for each 

    