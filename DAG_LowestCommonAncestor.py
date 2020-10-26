
# Python program to find single source shortest paths 
# for Directed Acyclic Graphs Complexity :OV(V+E) 
from collections import defaultdict 
  
# Graph is represented using adjacency list. Every 
# node of adjacency list contains vertex number of 
# the vertex to which edge connects. It also contains 
# weight of the edge 

class DAG_Graph: 
    def __init__(self,vertices,E=0): 
  
        self.V = vertices # No. of vertices 
        self.E = E
        # dictionary containing adjacency List 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.incE()
    
    def incE (self):
        self.E = self.E + 1
        return

    # I wasn't able to think of a way to create a lowestCommonAncestor function using
    # recursion so I went an used a matrix method instead
    def lowestCommonAncestor(self, v, w):
        if(self.checkIfAcyclic()):
            return None

        vArr = [0] * self.E
        wArr = [0] * self.E
        vMarked = [False] *self.V
        wMarked = [False] *self.V
        vCount =0
        wCount =0
        vArr[vCount]=v
        wArr[wCount]=w
        #//mark all vertices as not been visited yet
        for j in range(0, self.V):
            vMarked[j]=False
            wMarked[j]=False

        
        for i in range(self.V):
            vMarked[v] =True
            wMarked[w] =True
            j =0
            for j in range(len(self.graph[i])):
                if(self.graph[i][j] !=None and vMarked[i]):
                    vCount = vCount + 1
                    vArr[vCount]=j
                    vMarked[j]=True
        
                if(self.graph[i][j]!=None and wMarked[i]):
                    wCount = wCount + 1
                    wArr[wCount]=j
                    wMarked[j]=True
                
                if(wArr[wCount]==vArr[vCount]):
                    #return wArr[wCount]
                    return self.graph[i][wArr[wCount]]

        return None #/returns -1 if no ancestor found
    
    # Cyclic Actual
    def isCyclic(self, i, visited, recStack):

        # Mark the current node as visited and
        # part of recursion stack
        if (recStack[i]):
            return True

        if (visited[i]):
            return False

        visited[i] = True

        recStack[i] = True

        for c in self.graph[i]:
            if ( self.isCyclic(c, visited, recStack)):
                return True

        recStack[i] = False

        return False
    # Cyclic Check #1
    def checkIfAcyclic (self):
        visited = [False] *self.V
        recStack =[False] *self.V

        for i in range (self.V):
            if(self.isCyclic(i, visited, recStack)):
                return True

        return False
    def printGraph(self):
        for i in range(self.V):
            if(len(self.graph[i]) != 0):
                print(format(i) + "-> " + format(self.graph[i]) + "")
    

print("\n\n\nHello\n\n\n")
b = DAG_Graph(9)
b.addEdge(0, 1)
b.addEdge(0, 2)
b.addEdge(1, 3)
b.addEdge(2, 4)
b.addEdge(3, 5)
b.addEdge(4, 6)
b.addEdge(5, 7)
b.addEdge(6, 7)
b.addEdge(7, 8)
b.printGraph()
if(b.checkIfAcyclic()):
    print("Hey Mama!")

cycle = DAG_Graph(9)
cycle.addEdge(0, 1)
cycle.addEdge(0, 2)
cycle.addEdge(2, 1)
cycle.addEdge(1, 2)
cycle.addEdge(2, 4)
cycle.addEdge(4, 3)
cycle.addEdge(3, 1)
cycle.addEdge(3, 6)
cycle.addEdge(6, 8)
cycle.addEdge(7, 8)
b.printGraph()
if(cycle.checkIfAcyclic()):
    print("Hey Son!")

b.lowestCommonAncestor(1, 5)
print(format(b.lowestCommonAncestor(1, 5))) #7 "LCA of 5,1 = 7"
print(format(b.lowestCommonAncestor(5, 1))) #7 "LCA of 1,5 = 7"
print(format(b.lowestCommonAncestor(0, 2))) #4 "LCA of 0,2 = 4"
print(format(b.lowestCommonAncestor(0, 0))) #1 "LCA of 0,0 = 1"
print(format(b.lowestCommonAncestor(0, 7))) #8 "LCA of 0,7 = 8"
