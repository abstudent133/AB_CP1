#AB 1st Maze Generator

#import libraries(turtle and random)
import turtle as t
import random as r

# setup basic variables
cell_size = 50
rows = 6
columns = 6

# lists for maze and visited cells
maze = []
visited = []

# where the maze drawing starts
origin_x = -columns * cell_size / 2
origin_y = rows * cell_size / 2

#turtle setup
def setup_turtle():
    t.setup(800, 600)
    t.title("Maze")
    t.speed(0)
    t.hideturtle()
    t.pensize(2)
    t.color("black")
    t.penup()

# make the grid of walls and visited spots
def make_grid():
    #for the number of walls in a row
    for row_index in range(rows):
        #put in maze rows
        maze_row = []
        #put in the visited row
        visited_row = []
        #do the number of walls in a column
        for col_index in range(columns):
            #This is the structure for each box top bottom left and right
            maze_row.append([1, 1, 1, 1])  
            #This is just saying that that spot has been visited
            visited_row.append(0) 
        #have to add maze row to the maze         
        maze.append(maze_row)
        #have to put the visited row in the visited list
        visited.append(visited_row)

#carve the maze
def carve_maze(row_index, col_index):
    #hav to keep track of what has been visited
    visited[row_index][col_index] = 1

    # directions: this is the order of the numbers (row_change, col_change, current_wall, opposite_wall)
    directions = [
        #this is how to move right
        (0, 1, 1, 3),  
        #this is how to move down
        (1, 0, 2, 0),   
        #this is how to move left
        (0, -1, 3, 1),
        #This is how to move up
        (-1, 0, 0, 2)   
    ]

    r.shuffle(directions)   # randomize direction order

    for direction in directions:
        row_change = direction[0]
        col_change = direction[1]
        wall_index = direction[2]
        opposite_wall_index = direction[3]

        new_row = row_index + row_change
        new_col = col_index + col_change

        # check if new position is inside maze
        if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < columns:
            if visited[new_row][new_col] == 0:  # not visited yet
                # remove walls between cells
                maze[row_index][col_index][wall_index] = 0
                maze[new_row][new_col][opposite_wall_index] = 0
                carve_maze(new_row, new_col)
# draw the maze 
def draw_maze():
    #for each row index in the range of the rows
    for row_index in range(rows):
        #for the column index for the amoutn of columns
        for col_index in range(columns):
            #the wall is the index of row index and column index
            walls = maze[row_index][col_index]
            #have to set the x and y position
            x_position = origin_x + col_index * cell_size
            y_position = origin_y - row_index * cell_size

            # draw top wall
            if walls[0] == 1:
                t.goto(x_position, y_position)
                t.setheading(0)
                t.pendown()
                t.forward(cell_size)
                t.penup()

            # draw right wall
            if walls[1] == 1:
                t.goto(x_position + cell_size, y_position)
                t.setheading(-90)
                t.pendown()
                t.forward(cell_size)
                t.penup()

            # draw bottom wall
            if walls[2] == 1:
                t.goto(x_position, y_position - cell_size)
                t.setheading(0)
                t.pendown()
                t.forward(cell_size)
                t.penup()

            # draw left wall
            if walls[3] == 1:
                t.goto(x_position, y_position)
                t.setheading(-90)
                t.pendown()
                t.forward(cell_size)
                t.penup()

#run the functions
setup_turtle()
make_grid()
carve_maze(0, 0)
draw_maze()
t.done()

    