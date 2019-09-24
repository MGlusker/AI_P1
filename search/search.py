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

    # get the start state and convert it into a node
    startNode = nodeClass(problem.getStartState(), "Stop", 0,  None)

    #create a stack to store the nodes that are on the frontier
    frontier = util.Stack()

    frontier.push(startNode) 

    # create an explored set that keeps track of explored states 
    explored = set()

    # loop through frontier as long as it contains at least one node
    while not frontier.isEmpty(): 

        # pop the next node off the frontier
        node = frontier.pop()

        # if the popped off node's state is the goal state, return the solution
        if problem.isGoalState(node.getState()): 
            return getSolution(node, startNode)
       
        # if the node's state isn't in explored 
        if node.getState() not in explored:

            # then add the nodes state to explored
            explored.add(node.getState())

            # and add its children to the frontier 
            # convertedNeighbors is a list of the succesor nodes
            convertedNeighbors = successorsToNodes(problem.getSuccessors(node.getState()), node)
            for child in convertedNeighbors:
                frontier.push(child)

    print "FAILURE: No Solution Found"
    return Directions.STOP
  

def breadthFirstSearch(problem):

    # get the start state and convert it into a node
    startNode = nodeClass(problem.getStartState(), "Stop", 0,  None)

    #create a stack to store the nodes that are on the frontier
    frontier = util.PriorityQueue()

    frontier.push(startNode) 

    # create an explored set that keeps track of explored states 
    explored = set() 

    # loop through frontier as long as it contains at least one node
    while not frontier.isEmpty(): 

        # pop the next node off the frontier
        node = frontier.pop()
        
        # if the popped off node's state is the goal state, return the solution
        if problem.isGoalState(node.getState()): 
            return getSolution(node, startNode)
       
        # if the node's state isn't in explored 
        if node.getState() not in explored:

            # then add the nodes state to explored
            explored.add(node.getState())

            # and add its children to the frontier 
            # convertedNeighbors is a list of the succesor nodes
            convertedNeighbors = successorsToNodes(problem.getSuccessors(node.getState()), node)
            for child in convertedNeighbors:
                frontier.push(child)

    print "FAILURE: No Solution Found"
    return Directions.STOP

class nodeClass():

    def __init__(self, state, direct, cost, parent):
        self.state = state
        self.direction = direct
        self.parent = parent
        self.cost = cost #cost from parent to this State

    def getState(self):
        return self.state

    def getDirection(self):
        return self.direction

    def getCost(self):
        return self.cost

    def getParent(self):
        return self.parent

    def printNode(self):
        print "*State:",self.state,"*Direction:",self.direction,"*Cost:",self.cost
        


# returns a list of directions to take by expanding the goal state down to the start state
def getSolution(node, startNode):
    currentNode = node
    toReturn = []

    while not (currentNode.getState() == startNode.getState()):
        toReturn.append(currentNode.getDirection())
        currentNode = currentNode.getParent()

    toReturn.reverse()
    return toReturn

"""
def classToState(myList):
    toReturn =[]

    for wrapperClass in myList:
        toReturn.append(wrapperClass.getState())

    return toReturn

def printStateList(wrapperClassList):
    print"*******"

    for i in wrapperClassList:
        print "(",i.state, ",", i.parent, ")"
    print"*******"
"""

def successorsToNodes(myList, parent):

    listOfNodes = []
    states = []
    directions = []
    costs = []

    for triple in myList:
        states.append(triple[0])
        directions.append(triple[1])
        costs.append(triple[2])
    
    for i in range(len(states)):
        listOfNodes.append(nodeClass(states[i], directions[i], costs[i], parent))
        
    
    return listOfNodes
    




def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #"*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    # get the start state and convert it into a node
    startNode = nodeClass(problem.getStartState(), "Stop", 0,  None)

    #create a stack to store the nodes that are on the frontier
    frontier = util.Queue()

    frontier.push(startNode) 

    # create an explored set that keeps track of explored states 
    explored = [] 

    # loop through frontier as long as it contains at least one node
    while not frontier.isEmpty(): 

        # pop the next node off the frontier
        node = frontier.pop()
        
        # if the popped off node's state is the goal state, return the solution
        if problem.isGoalState(node.getState()): 
            return getSolution(node, startNode)
       
        # if the node's state isn't in explored 
        if node.getState() not in explored:

            # then add the nodes state to explored
            explored.append(node.getState())

            # and add its children to the frontier 
            # convertedNeighbors is a list of the succesor nodes
            convertedNeighbors = successorsToNodes(problem.getSuccessors(node.getState()), node)
            for child in convertedNeighbors:
                frontier.push(child)

    print "FAILURE: No Solution Found"
    return Directions.STOP

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
