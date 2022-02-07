# A* function using the information of a maze
# 0 - No obstacle
# 1 - Obstacle
# 2 - Initial
# 3 - Goal

import numpy as np

# Classes definition
class MazePoint:
    """A class to save a point with important values"""
    def __init__(self, Position):
        self.Row = Position[0] # Row position
        self.Col = Position[1] # Column position
        self.Parent = [] # Parent point of this point
        self.g = 0 # g value for this point
        self.f = 0 # f value for this point
    
    def __lt__(self, other): # lesser than method definition
         return self.f < other.f # Compare the f value to sort


# Functions definition

def search(list, neighbour): # Search in a list an specific
    for i in range(len(list)):
        if list[i].Row == neighbour[0] and list[i].Col == neighbour[1]:
            return True
    return False


def dist(PointA, PointB): # Manhattan Distance calculation
   distance = abs(PointA[0] - PointB[0]) + abs(PointA[1] - PointB[1])
   return distance


def neighbours(CurrentPoint): # Calculate the possible neighbours of a given point
    Point = []
    Point.append(CurrentPoint.Row)
    Point.append(CurrentPoint.Col)
    PointNeighbours = [[0 for i in range(2)]for j in range(4)] # Each point has 4 possible neighbours
    PointNeighbours = [[Point[0]-1,Point[1]],[Point[0],Point[1]-1], #each neighbour is in the square next to the point in the 4 directions
                [Point[0]+1,Point[1]],[Point[0],Point[1]+1]]
    return PointNeighbours


def Heuristics(Current, Goal, Neighbours, Closed_Set, Open_Set, rows, columns, MazeInfo): # A* core algorithm
    for neighbour in Neighbours: # Inspect every neighbour

        if search(Closed_Set,neighbour) == False: # Study only those points out of closed set
            if neighbour[0] >= 0 and neighbour[0] < rows and neighbour[1] >= 0\
             and neighbour[1] < columns and MazeInfo[neighbour[0]][neighbour[1]] != 1: # Discard every neighbour with obstacles or out of the map
                tent_g = Current.g + dist([Current.Row, Current.Col],neighbour)

                if (search(Open_Set, neighbour) == False): #Check if the point is already in open set, if not, generate a new MazePoint
                   NewPoint = MazePoint([neighbour[0], neighbour[1]])
                   NewPoint.g = tent_g
                   NewPoint.f = tent_g + dist([Current.Row, Current.Col], Goal)
                   NewPoint.Parent.append([Current.Row, Current.Col])
                   Open_Set.append(NewPoint) # Insert the new point into the open set

                else: # If the point is in the open set, search it position and update it values

                   for i in range(len(Open_Set)):
                        if Open_Set[i].Row == neighbour[0] and Open_Set[i].Col == neighbour[1]:
                            if tent_g < Open_Set[i].g: # Update the values only if the tentative_g is minor than the previous g                     
                                Open_Set[i].g = tent_g
                                Open_Set[i].f = tent_g + dist([Current.Row, Current.Col], Goal)
                                Open_Set[i].Parent.append([Current.Row, Current.Col])                                     
    return Open_Set

def Reconstruct(Closed_set, Init, MazeInfo, rows, columns):
    Path = []
    # Sort from last to first
    Closed_set.reverse()

    # Add first to list (Goal)
    Path.append(Closed_set[0])

    # Check the current parents
    ParentCheck = [0, 0]
    ParentCheck[0] = Closed_set[0].Parent[0][0]
    ParentCheck[1] = Closed_set[0].Parent[0][1]
    Closed_set.pop(0) # Remove the already taken value

    # Check position and parent of point
    while(1): # This loop does not end until return is called

        for i,point in enumerate(Closed_set):
            if (point.Row == ParentCheck[0]) and (point.Col == ParentCheck[1]): # Check if the current point is equal to the previous point's parents
                Path.append(point) # if is equal, add to the path and remove from closed set
                Closed_set.pop(i)

                if point.Row == Init[0] and point.Col == Init[1]: # If initial point is reached, end while loop
                    Path.reverse()
                    return PathPrint(Path, MazeInfo, rows, columns) # Call the function that print the path

                ParentCheck[0] = point.Parent[0][0] # Update the current parent to look for
                ParentCheck[1] = point.Parent[0][1]       


def PathPrint(Path, MazeInfo, rows, columns): # Print the path
   print("The path to follow is: ")
   print("")
   for i in Path:
        print(str(i.Row) + ", " + str(i.Col)) 
   print("")
   return Path #Return the path info to the main file, which will print the maze with the path


def Astar_func(MazeInfo, rows, columns): # Main function of the A* algorithm
   
    arr = np.array(MazeInfo) # Transforming MazeInfo into numpy array to apply index searching
    Init = np.where(arr == 2)
    Init = [int(Init[0]), int(Init[1])] # The position of the initial point

    Goal = np.where(arr == 3) # The position of the goal
    Goal = [int(Goal[0]), int(Goal[1])]

    Open_set = []   # The open set contains the initial position at first
    Open_set.append(MazePoint(Init))
    Closed_set = [] # The closed set initializer

    while Open_set != []: # While there is some value in open set, keep going

        Current = Open_set.pop(0) # Remove first point from open set

        if Current.Row == Goal[0] and Current.Col == Goal[1]: # If the current point is the goal, finish
            Closed_set.append(Current)       
            return Reconstruct(Closed_set, Init, MazeInfo, rows, columns) # Call the function that reconstruct the path using the closed set
            
        Closed_set.append(Current) # We include that point in the closed set
        CurrentNeighbours = neighbours(Current) # Search current point neighbours
        Open_set = Heuristics(Current, Goal, CurrentNeighbours, Closed_set, Open_set, rows, columns, MazeInfo) # Heuristic part of the algorithm
        Open_set.sort() # sort by f value

    print("Sorry, cannot find a valid path, the goal is blocked")
    Path = [] # Return an empty path to say that the goal is unreachable.
    return Path 
    

    
    
    
        

    

    


