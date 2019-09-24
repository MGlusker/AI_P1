# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    start = stateClass(problem.getStartState(), "Stop", 0,  None)

    # if the the initial state is the same as the goal state
    if(problem.isGoalState(start.getCoords())):
        return Directions.STOP
    

    frontier = util.Stack() #create a stack called frontier to store the states that are on the frontier
    frontier.push(start) #Add the init state to the frontier 

    explored = [] #create an explored set
    toReturn = []
    
    while not frontier.isEmpty(): #loop through frontier as long as a frontier exits

        #pop the next state off the frontier 
        #this is the state we're investigating over this loop
        #state takes a tuple format (x,y)
        state = frontier.pop()

        

        # add the state's state to explored
        # this deals with adding the inital state in properly
        explored.append(state)
       

        #find the children of the popped off state state 
        #Successor of format ((x, y), 'Direction', Cost)
        #SuccessorsToStates(listOfSuccessors, parentState)
        convertedNeighbors = successorsToStates(problem.getSuccessors(state.getCoords()), state)
       
        
        # iterate through each child / action
        for child in convertedNeighbors:
            
            # add each child to the frontier if it's not in explored or frontier
            if not ((child.getCoords() in classToState(explored)) or (child.getCoords() in classToState(frontier.list))):

                # return the solution by going through all the State/actions
                if problem.isGoalState(child.getCoords()): 
                    current = child
                    while not (current.getCoords() == start.getCoords()):

                        toReturn.append(current.getDirection())
                        current = current.getParent()

                    toReturn.reverse()
                    return toReturn
                    

                frontier.push(child)

    print "FAILURE: No Solution Found"
    return Directions.STOP
                


#myWrapperState
class stateClass():

    def __init__(self, coords, direct, cost, parent):
        self.coords = coords
        self.direction = direct
        self.parent = parent
        self.cost = cost #cost from parent to this State

    def getCoords(self):
        return self.coords

    def getParent(self):
        return self.parent

    def getDirection(self):
        return self.direction



def classToState(myList):
    toReturn =[]

    for wrapperClass in myList:
        toReturn.append(wrapperClass.getCoords())

    return toReturn

def printStateList(wrapperClassList):
    print"*******"

    for i in wrapperClassList:
        print "(",i.state, ",", i.parent, ")"
    print"*******"

def successorsToStates(myList, parent):

    toReturn = []
    states = []
    directions = []
    costs = []

    for triple in myList:
        states.append(triple[0])
        directions.append(triple[1])
        costs.append(triple[2])
    
    i = 0
    while i < len(states):
        toReturn.append(stateClass(states[i], directions[i], costs[i], parent))
        i += 1

    
    return toReturn
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    """*** YOUR CODE HERE ***"""
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #"*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #"*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
