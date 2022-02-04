# Maze Generation for A* algorithm
# 60 rows and 80 columns, 4800 characters
# Works with any size

import sys
import random # for random probabilities
import math as m # for math rounding up

def searchObstacle(list, state): # Search in a list function
    for i in range(len(list)):
        if list[i] == state:
            return True
    return False

def mazeGenerator(rows,columns, ObstaclesPercent):

    state = 0 # To count the number of the current position in left-to-right then up-to-down order
    Total = rows*columns # Total number of spaces
    MazeInfo = [[0 for x in range(columns)] for y in range(rows)] # Initialize the information of the maze

    InitialState = random.randint(0, Total-1) # Random initial position
    FinalState = random.randint(0,Total-1) # Random Final position

    while FinalState == InitialState: # If the initial position coincide with the goal position, re-roll 
        FinalState = random.randint(0,Total)


    obstaclesPosition = random.sample(range(Total),m.ceil((ObstaclesPercent/100)*Total)) # Generate the indicated percent of obstacles in random position without repeating


    for i in range(0,rows): # Going through rows
        for j in range(0,columns): # Going through columns        

            if searchObstacle(obstaclesPosition,state) == True and state == InitialState: # Check if initial state coincide with an obstacle
                MazeInfo = []
                return MazeInfo # Halt and return fail message
            elif searchObstacle(obstaclesPosition,state) == True and state == FinalState: #Check if goal concide with an obstacle
                MazeInfo = []
                return MazeInfo # Halt and return fail message

            if state == (InitialState):

                MazeInfo[i][j] = 2 # Annotates 2 to indicate the initial position

            elif state == FinalState:

                MazeInfo[i][j] = 3 # Annotates 3 to indicate goal position

            elif searchObstacle(obstaclesPosition,state) == True: # obstacle selection
                MazeInfo[i][j] = 1 # Annotates 1 to indicate obstacle

            else:
                MazeInfo[i][j] = 0 # Annotates 0 to indicate empty space
            state = state + 1 # The current position in grid

    return MazeInfo

def search(list, point): # Search in a list function
    for i in range(len(list)):
        if list[i].Row == point[0] and list[i].Col == point[1]:
            return True
    return False

 