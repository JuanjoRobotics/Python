"""This program generates a maze of any columns and rows,
    then, it mark 2 random spaces as initial position and goal.
    After generating the maze, we use the A* algorithm to check
    every possible path and select the optimus one. If no path is
    available, a message is printed on screen saying it.
    
    Author: Juan Jose Garcia Quiles"""

import Maze # Maze generator and printer
import Astar # A* algorithm calculator
import sys

rows = 80 # Number of rows
columns = 60 # Number of columns
ObstaclesPercent = 30 # percent of obstacles in the maze
file = 0 # Decide to write on file or on terminal 0 - no; 1 - yes

if file == 1:
    sys.stdout = open("MazeOutput.txt","w") # If file option is activated, write only in file

if file != 1:
    input("Press a key to start...") # enable inputs only in no-file mode

# Generate the random maze

print("\nGenerating Maze...")
print("")

MazeInfo = Maze.mazeGenerator(rows,columns,
 ObstaclesPercent, file) # Saving the information of the maze, where 1 is obstacle, 0 is no obstacle, 2 is initial position and 3 is goal

if file !=1:
    input("\n\nPress a key to start solving...") # Press a key to reprint the maze with the solution

# Execute A* algorithm
print("\n\nCalculating with A*...")
print("")

Path = Astar.Astar_func(MazeInfo, rows, columns) #The A* algorithm that calculates the path

if (Path !=[]): # If the path is empty, do not print the solved maze, instead, print the maze without path
    Maze.MazePrinter(Path, MazeInfo, rows, columns,file) # Call the function that prints the entire maze with the path
else:
    Maze.MazeErrorPrint(MazeInfo,rows,columns)

if file !=1:
    input("\n\nPress a key to finish...") # Finish the program an close (if executing .exe)


