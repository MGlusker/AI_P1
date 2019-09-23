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
        
    from game import Directions
    from game import Actions
    #print "Start:", problem.getStartState()
    # (5, 5)
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print
    # [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    #print "solution is: " 

    #Set startNode to the startState (initial state; place where pacman starts)
    
    startNode = myWrapperState(problem.getStartState(), None, None)

    # if the the initial state is the same as the goal state
    if(problem.isGoalState(startNode.getState())):
        return Directions.STOP
    

    frontier = util.Stack() #create a stack called frontier to store the states that are on the frontier
    frontierStates = util.Stack()

    frontier.push(startNode) #Add the init node to the frontier 
    frontierStates.push(startNode.getState())

    explored = [] #create an explored set
    exploredStates = []
    #print "initial frontier", frontier.list
  

    while not frontier.isEmpty(): #loop through frontier as long as a frontier exits

        #pop the next node off the frontier 
        #this is the node we're investigating over this loop
        #node takes a tuple format (x,y)
        node = frontier.pop()
        nodeState = frontierStates.pop()

        

        # add the node's state to explored
        # this deals with adding the inital state in properly
        explored.append(node)
        exploredStates.append(nodeState)

        #find the children of the popped off node state 
        #Successor of format ((x, y), 'Direction', Cost)
        #SuccessorsToStates(listOfSuccessors, parent node)
     
        convertedNeighbors = successorsToStates(problem.getSuccessors(node.getState()), node)
        #print convertedNeighbors.__class__
        #print convertedNeighbors[0].__class__

        #printWrapperList(convertedNeighbors)
        
        # iterate through each child / action
        for child in convertedNeighbors:

            
            # add each child to the frontier if it's not in explored or frontier
            if not ((child.getState() in exploredStates) or (child.getState() in frontierStates.list)):

                # return the solution by going through all the nodes/actions
                if problem.isGoalState(child.getState()):
                    print "**"
                    print "** Solution is: " 
                    print child.getState()
                    print "**"
                    solution = child

                frontier.push(child)
                frontierStates.push(child.getState())

              
            #else:
            #   print "child is in explored or frontier already"
            #   print child.getState()

    toReturn = []

    current = solution
    print "YEet"
    #print not(current.getState() == startNode)
    #print current.__class__
    #print startNode.__class__
    

    while not (current.getState() == startNode.getState()):
        print "loop"

        toReturn.append(current.getDirection())
        #print current.__class__
        current = current.getParent()
        #print current.__class__

   
    toReturn.reverse()
    toReturn.append("Stop")
    print toReturn
   
    return toReturn


        



class myWrapperState():

    def __init__(self, sta, dir, par):
        self.state = sta
        self.direction = dir
        self.parent = par

    def getState(self):
        return self.state

    def getParent(self):
        return self.parent

    def getDirection(self):
        return self.direction





def printWrapperList(wrapperClassList):
    print"*******"

    for i in wrapperClassList:
        print "(",i.state, ",", i.parent, ")"
    print"*******"

def successorsToStates(myList, parent):

    toReturn = []
    states = []
    directions = []

    for triple in myList:
        
        states.append(triple[0])
        directions.append(triple[1])

    
    i = 0
   
    while i < len(states):
        toReturn.append(myWrapperState(states[i], directions[i], parent))
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
