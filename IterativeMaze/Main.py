"""This program generates a maze of any columns and rows,
    then, it mark 2 random spaces as initial position and goal.
    After generating the maze, we use the A* algorithm to check
    every possible path and select the optimus one. If no path is
    available, a message is printed on screen saying it."""

import Maze # Maze generator and printer
import Astar # A* algorithm calculator

rows = 60 # Number of rows
columns = 80 # Number of columns
ObstaclesPercent = 40 # percent of obstacles in the maze
Iterations = 100
win = 0
block = 0
for i in range(Iterations):
    # Generate the random maze
    MazeInfo = Maze.mazeGenerator(rows,columns,
    ObstaclesPercent) # Saving the information of the maze, where 1 is obstacle, 0 is no obstacle, 2 is initial position and 3 is goal
    
    if MazeInfo != []:
        # Execute A* algorithm
        Path = Astar.Astar_func(MazeInfo, rows, columns) #The A* algorithm that calculates the path

        if (Path !=[]): # If the path is empty, do not print the solved maze, instead, print the maze without path
            win = win+1
    else:
        block = block + 1
    
print(win)
print(block)
print("With " + str(Iterations) + " We obtained " + str(win)\
     +  " wins, and the goal or initial position were blocked " + str(block) + " times.")
