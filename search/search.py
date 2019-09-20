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
        #node where the exit to the maze is 
    node = problem.getStartState()

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
        #starting node will always be in the solution
    """    
        mazeGraph.nodes[0].inSolution = true;

        Stack nodeStack = new Stack();
        Node[] toReturn;

        nodeStack.push(startingNode); 

        #while the list of vertices to explore isn't empty
        while(!nodeStack.isEmpty()) {
            #remove the next vertice in the stack
            Node vertice = nodeStack.pop();
            
           #if the vertice hasn't been visited
            if(!vertice.visited) {
                #find all of its neighbors 
                Stack neighbors = findAllNeighbors(vertice, mazeGraph);
                
                #while the neighbors list isn't empty, add all neighbors to nodeStack
                while(!neighbors.isEmpty()) {
                    
                    nodeStack.push(neighbors.pop());

                    #if this is the first time visiting the neighbor then update parent
                    if(!nodeStack.peek().visited) {
                        nodeStack.peek().parent = vertice;
                    }
                }
                
                #now mark that this vertice has been visited
                vertice.visited = true;
            }
            
            #if we're at the exit node
            if(vertice.index == mazeExit.index) {
                #then go back up the path we just went down
                #and add all of the nodes along the way to be in the list
                Stack solutionStack = new Stack();
                Node currentNode = vertice;
                while(currentNode != null) {
                    solutionStack.push(currentNode);
                    //currentNode.inSolution = true;
                    currentNode = currentNode.parent;
                }

                toReturn = new Node[solutionStack.size()];

                #now fill in node array with the nodes from our solution stack
                for(int i = 0; i < toReturn.length; i++){
                    toReturn[i] = solutionStack.pop();
                }

                return toReturn;
            
        
        return null;
    




"""
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
