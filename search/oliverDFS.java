/*-----------------------------------------------------------------------------------------
ANSWER THE QUESTIONS FROM THE DOCUMENT HERE

(1) Which graph representation did you choose, and why?
I chose to use an adjacency matrix because we will never have to resize the matrix due to 
the fact that the size of the maze will never change. An adjacency matrix will take constant 
time to add an edge (as well as remove or find if an edge exists) and because we will never 
have to resize the matrix we don't have to worry about the potential for slow runtime of the 
matrix. This makes the adjacency matrix faster in terms of runtime than an adjacency list in 
this application.

(2) Which search algorithm did you choose, and why?
I chose to use Depth-First Search because in this application we want to solve the maze. This
means that we will need to go to the end of the maze (the last index in the maze) anyways, 
meaning that it makes sense to go all the way to the end of the maze as opposed to checking
the neighbors. In other words, becasue we have to go to the bottom of the maze to solve it,
we wouldn't save any time by checking all of the neighbors by using a Breadth-First Search
(therefore a Depth-First Search would be faster than a Breadth-First Search). 
----------------------------------------------------------------------------------------*/

import java.io.*;
import java.lang.Math;
import java.lang.Object;
import java.util.Vector;

public class MazeSolver {

    public void run(String filename) throws IOException {

	// read the input file to extract relevant information about the maze
	String[] readFile = parse(filename);
	int mazeSize = Integer.parseInt(readFile[0]);
	int numNodes = mazeSize*mazeSize;
	String mazeData = readFile[1];

	// construct a maze based on the information read from the file
	Graph mazeGraph = buildGraph(mazeData, numNodes);

	// solve the maze
	Node mazeEntrance = new Node(0);
	// for every node in the final path add it to the solution
	Node[] finalPath = solve(mazeGraph, mazeEntrance);
	for(int i = 0; i < finalPath.length; i++) {
		finalPath[i].inSolution = true;
	}
	// print out the final maze with the solution path
	printMaze(mazeGraph.nodes, mazeData, mazeSize);
    }

    // returns the Nodes included on the path from maze entrance to exit
    public Node[] solve(Graph mazeGraph, Node startingNode) {

    	// node where the exit to the maze is 
		Node mazeExit = new Node(mazeGraph.numNodes-1);
		// starting node will always be in the solution
		mazeGraph.nodes[0].inSolution = true;

    	Stack nodeStack = new Stack();
    	Node[] toReturn;

    	nodeStack.push(startingNode); 

    	// while the list of vertices to explore isn't empty
    	while(!nodeStack.isEmpty()) {
    		// remove the next vertice in the stack
    		Node vertice = nodeStack.pop();
    		
    		// if the vertice hasn't been visited
    		if(!vertice.visited) {
    			// find all of its neighbors 
    			Stack neighbors = findAllNeighbors(vertice, mazeGraph);
    			
    			// while the neighbors list isn't empty, add all neighbors to nodeStack
    			while(!neighbors.isEmpty()) {
    				
    				nodeStack.push(neighbors.pop());

    				// if this is the first time visiting the neighbor then update parent
    				if(!nodeStack.peek().visited) {
    					nodeStack.peek().parent = vertice;
    				}
    			}
    			
    			// now mark that this vertice has been visited
    			vertice.visited = true;
    		}
    		
    		// if we're at the exit node
    		if(vertice.index == mazeExit.index) {
    			// then go back up the path we just went down
    			// and add all of the nodes along the way to be in the list
    			Stack solutionStack = new Stack();
    			Node currentNode = vertice;
    			while(currentNode != null) {
    				solutionStack.push(currentNode);
    				//currentNode.inSolution = true;
    				currentNode = currentNode.parent;
    			}

    			toReturn = new Node[solutionStack.size()];

    			// now fill in node array with the nodes from our solution stack
    			for(int i = 0; i < toReturn.length; i++){
    				toReturn[i] = solutionStack.pop();
    			}

    			return toReturn;
    		}
    	}
    	return null;
    }

    // finds all of the neighbors of a given node / vertice
    public Stack findAllNeighbors(Node vertice, Graph mazeGraph) {

    	Stack neighbors = new Stack();

    	for(int i = 0; i < mazeGraph.adjacencyMatrix.length; i++) {
    		// if there's a connection then add that node to the list of neighbors
    		if(mazeGraph.adjacencyMatrix[vertice.index][i] == true) {
    			neighbors.push(mazeGraph.nodes[i]);
    		}
    	}

    	return neighbors;	
    }

    // prints out the maze in the format used for HW8
    // includes the final path from entrance to exit, if one has been recorded,
    // and which cells have been visited, if this has been recorded
    public void printMaze(Node[] mazeCells, String mazeData, int mazeSize) {
	
	int ind = 0;
	int inputCtr = 0;

	System.out.print("+");
	for(int i = 0; i < mazeSize; i++) {
	    System.out.print("--+");
	}
	System.out.println();

	for(int i = 0; i < mazeSize; i++) {
	    if(i == 0) System.out.print(" ");
	    else System.out.print("|");

	    for(int j = 0; j < mazeSize; j++) {
		System.out.print(mazeCells[ind] + "" + mazeCells[ind] +  mazeData.charAt(inputCtr));
		inputCtr++;
		ind++;
	    }
	    System.out.println();

	    System.out.print("+");
	    for(int j = 0; j < mazeSize; j++) {
		System.out.print(mazeData.charAt(inputCtr) + "" +  mazeData.charAt(inputCtr) + "+");
		inputCtr++;
	    }
	    System.out.println();
	}
	
    }

    // reads in a maze from an appropriately formatted file (this matches the format of the 
    // mazes you generated in HW8)
    // returns an array of Strings, where position 0 stores the size of the maze grid (i.e., the
    // length/width of the grid) and position 1 minimal information about which walls exist
    public String[] parse(String filename) throws IOException {
	FileReader fr = new FileReader(filename);

	// determine size of maze
	int size = 0;
	int nextChar = fr.read();
	while(nextChar >= 48 && nextChar <= 57) {
	    size = 10*size + nextChar - 48;
	    nextChar = fr.read();
	}

	String[] result = new String[2];
	result[0] = size + "";
	result[1] = "";


	// skip over up walls on first row
	for(int j = 0; j < size; j++) {
	    fr.read();
	    fr.read();
	    fr.read();
	}
	fr.read();
	fr.read();

	for(int i = 0; i < size; i++) {
	    // skip over left wall on each row
	    fr.read();
	    
	    for(int j = 0; j < size; j++) {
		// skip over two spaces for the cell
		fr.read();
		fr.read();

		// read wall character
		nextChar = fr.read();
		result[1] = result[1] + (char)nextChar;

	    }
	    // clear newline character at the end of the row
	    fr.read();
	    
	    // read down walls on next row of input file
	    for(int j = 0; j < size; j++)  {
		// skip over corner
		fr.read();
		
		//skip over next space, then handle wall
		fr.read();
		nextChar = fr.read();
		result[1] = result[1] + (char)nextChar;
	    }

	    // clear last wall and newline character at the end of the row
	    fr.read();
	    fr.read();
	    
	}

	return result;
    }
    
    public Graph buildGraph(String maze, int numNodes) {

	Graph mazeGraph = new Graph(numNodes);
	int size = (int)Math.sqrt(numNodes);

	int mazeInd = 0;
	for(int i = 0; i < size; i++) {
	    // create edges for right walls in row i
	    for(int j = 0; j < size; j++) {
		char nextChar = maze.charAt(mazeInd);
		mazeInd++;
		if(nextChar == ' ') {
		    // add an edge corresponding to a right wall, using the indexing convention 
		    // for nodes
		    mazeGraph.addEdge(size*i + j, size*i + j + 1);
		}
	    }

	    // create edges for down walls below row i
	    for(int j = 0; j < size; j++)  {
		char nextChar = maze.charAt(mazeInd);
		mazeInd++;
		if(nextChar == ' ') {
		    // add an edge corresponding to a down wall, using the indexing convention
		    // for nodes
		    mazeGraph.addEdge(size*i + j, size*(i+1) + j);
		}
	    }    
	}

	return mazeGraph;
    }
       
    public static void main(String [] args) {
	if(args.length < 1) {
	    System.out.println("USAGE: java MazeSolver <filename>");
	}
	else{
	    try{
		new MazeSolver().run(args[0]);
	    }
	    catch(IOException e) {
		e.printStackTrace();
	    }
	}
    }

}