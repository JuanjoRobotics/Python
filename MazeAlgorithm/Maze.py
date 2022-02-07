# Maze Generation for A* algorithm
# 60 rows and 80 columns, 4800 characters
# Works with any size

import sys
import random # for random probabilities
import math as m # for math rounding up
import colorama
from termcolor import colored #for terminal colors
import os # To print colors in a windows terminal

os.system('color') # These lines allows coloring in windows terminal
colorama.init()

def FailMessage(fail,f): # Print a message if the maze generation fails
    if fail == 1:
        print("\n\nsorry, an obstacle blocked the initial position")
    elif fail ==0:
        print("\n\nSorry, an obstacle blocked the goal position")
    if f != 1:  
        input("\nPress a key to finish...")
    sys.exit() 

def searchObstacle(list, state): # Search in a list function
    for i in range(len(list)):
        if list[i] == state:
            return True
    return False

def mazeGenerator(rows,columns, ObstaclesPercent,f):

    state = 0 # To count the number of the current position in left-to-right then up-to-down order
    Total = rows*columns # Total number of spaces
    MazeInfo = [[0 for x in range(columns)] for y in range(rows)] # Initialize the information of the maze

    InitialState = random.randint(0, Total-1) # Random initial position
    FinalState = random.randint(0,Total-1) # Random Final position

    while FinalState == InitialState: # If the initial position coincide with the goal position, re-roll 
        FinalState = random.randint(0,Total)

    number = InitialState
    indi = m.ceil(float(number)/columns) # Calculate the indexes of the initial position
    indj = number - columns*(indi-1)

    print("Index starts on 0")
    print("")
    print("Initial position= " + str(indi-1) + ", " + str(indj)) # Print the initial position indexes

    number = FinalState
    indi = m.ceil(float(number)/columns) #Calculate the indexes of the final position
    indj = number - columns*(indi-1)

    print("Final State= " + str(indi-1) + ", " + str(indj)) # Print the goal position indexes
    print("")

    obstaclesPosition = random.sample(range(Total),m.ceil((ObstaclesPercent/100)*Total)) # Generate the indicated percent of obstacles in random position without repeating

    print(" *****MAZE*****")
    print("")

    for i in range(0,columns+2): # Going through rows 
        print(end="#")       
    print("")

    for i in range(0,rows): # Going through rows
        print(end="#") 
        for j in range(0,columns): # Going through columns        

            if searchObstacle(obstaclesPosition,state) == True and state == InitialState: # Check if initial state coincide with an obstacle
                return FailMessage(1,f) # Halt and return fail message
            elif searchObstacle(obstaclesPosition,state) == True and state == FinalState: #Check if goal concide with an obstacle
                return FailMessage(0,f) #Halt and return fail message

            if state == (InitialState):
                if f == 1:
                    print(end="I")
                else:
                    print(end=colored("I",'green')) # Print the initial state position
                MazeInfo[i][j] = 2 # Annotates 2 to indicate the initial position

            elif state == FinalState:
                if f == 1:
                    print(end="G")
                else:
                    print(end=colored("G", 'red')) # Print the final state position
                MazeInfo[i][j] = 3 # Annotates 3 to indicate goal position

            elif searchObstacle(obstaclesPosition,state) == True: # obstacle selection
                print(end="#") # Printing obstacle
                MazeInfo[i][j] = 1 # Annotates 1 to indicate obstacle

            else:
                print(end=" ") # Printing empty space
                MazeInfo[i][j] = 0 # Annotates 0 to indicate empty space
            state = state + 1 # The current position in grid

        print("#") 

    for i in range(0,columns+2): # Going through rows 
        print(end="#")

    return MazeInfo

def search(list, point): # Search in a list function
    for i in range(len(list)):
        if list[i].Row == point[0] and list[i].Col == point[1]:
            return True
    return False

def MazePrinter(Path, MazeInfo, rows, columns,f): #This function takes an already defined maze and print it again with the path
    
    print("*****SOLVED MAZE*****")
    print("\n")
    if f != 1:
        print(end="Goal = "); print(end=colored("G",'red')); print(end=(", Initial position = ")); print(end=colored("I",'green'))
        print(end=", Obstacle = #, "); print(end="Path = "); print(end=colored("o",'blue'))
    else:
        print(end="Goal = G, Initial position = I, Obstacle = #, Path = o")
    print("")
    for i in range(0,columns+2): # Going through rows 
        print(end="#")       
    print("")
    for i in range(0,rows): # Going through rows 
        print(end="#")      
        for j in range(0,columns): # Going through columns

            if MazeInfo[i][j] == 0: # Print no obstacle
                if search(Path,[i, j]) == True:
                    if f == 1:
                        print(end="o")
                    else:
                        print(end=colored("o",'blue')) # print step of the path
                else:
                    print(end=" ")   # Print empty space                 
            elif MazeInfo[i][j] == 1: # Print obstacle
                print(end="#")
            elif MazeInfo[i][j] == 2: #Print initial point
                if f == 1:
                    print(end="I")
                else:
                    print(end=colored("I",'green'))
            elif MazeInfo[i][j] == 3: # Print Goal point
                if f == 1:
                    print(end="G")
                else:
                    print(end=colored("G", 'red'))

        print("#")
    for i in range(0,columns+2): # Going through rows 
        print(end="#")

def MazeErrorPrint(MazeInfo, rows, columns,f): #This function takes an already defined maze and print it again with the path
    
    print("\n*****MAZE COULD NOT BE SOLVED*****")
    print("")
    for i in range(0,columns+2): # Going through rows 
        print(end="#")       
    print("")
    for i in range(0,rows): # Going through rows 
        print(end="#")    
        for j in range(0,columns): # Going through columns

            if MazeInfo[i][j] == 0: # Print no obstacle
                    print(end=" ")   # Print empty space                 
            elif MazeInfo[i][j] == 1: # Print obstacle
                if f == 1:
                    print(end="#")
                else:
                    print(end=colored("#",'blue')) 
            elif MazeInfo[i][j] == 2: #Print initial point
                if f == 1:
                    print(end="I")
                else:
                    print(end=colored("I",'green'))
            elif MazeInfo[i][j] == 3: # Print Goal point
                if f == 1:
                    print(end="G")
                else:
                    print(end=colored("G", 'red'))
        print("#")
    for i in range(0,columns+2): # Going through rows 
        print(end="#") 
    print("\n\nObstacles are in blue to show the block between goal (G) and Initial position (I)")     