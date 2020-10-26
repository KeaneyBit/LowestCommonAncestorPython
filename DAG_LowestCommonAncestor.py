
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
    
    def incE (self):
        self.E = self.E + 1
        return

    # I wasn't able to think of a way to create a lowestCommonAncestor function using
    # recursion so I went an used a matrix method instead
    # def lowestCommonAncestor(self, v, w):
    #     if(self.checkIfAcyclic()):
    #         return null

    #     vArr = [0] * self.E
    #     wArr = [0] * self.E
    #     vMarked = [false] *self.V
    #     wMarked = [false] *self.V
    #     vCount =0
    #     wCount =0
    #     vArr[vCount]=v
    #     wArr[wCount]=w
    #     #//mark all vertices as not been visited yet
    #     for i in range(0, self.V):
    #         vMarked[j]=false
    #         wMarked[j]=false
        
    #     for i in range(0, self.V):
    #         vMarked[v] =true
    #         wMarked[w] =true
    #         for i in range(0, self.graph[i].size()):
    #             if(g.adj[i].get(j)!=null and vMarked[i]):
    #                 vCount = vCount + 1
    #                 vArr[vCount]=j
    #                 vMarked[j]=true
        
    #             if(g.adj[i].get(j)!=null and wMarked[i]):
    #                 wCount = wCount + 1
    #                 wArr[wCount]=j
    #                 wMarked[j]=true
                
    #             if(wArr[wCount]==vArr[vCount]):
    #                 #return wArr[wCount]
    #                 return g.adj[i].get(wArr[wCount])

    #     return null #/returns -1 if no ancestor found
    
# ##
#     def isCyclic(int i, boolean[] visited, boolean[] recStack) {

#         // Mark the current node as visited and
#         // part of recursion stack
#         if (recStack[i]):
#             return true

#         if (visited[i]):
#             return false

#         visited[i] = true

#         recStack[i] = true
#         LinkedList<AdjListNode> children = adj[i];

#         for (AdjListNode c: children)
#             if (isCyclic(c.getV(), visited, recStack))
#                 return true;

#         recStack[i] = false;

#         return false;
#     }
#     boolean checkIfAcyclic () {
#         boolean[] visited = new boolean[V];
#         boolean[] recStack = new boolean[V];

#         for(int i = 0; i<V;i++)
#             if(isCyclic(i, visited, recStack))
#                 return true;

#         return false;
#     }
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


        # if(b.checkIfAcyclic()) {System.out.println("hello there b");}
        # printGraph(b)
        # DAG_LowestCommonAncestor g = new DAG_LowestCommonAncestor(9);
        # g.addEdge(0, 1);
        # g.addEdge(0, 2);
        # g.addEdge(1, 3);
        # g.addEdge(2, 4);
        # g.addEdge(3, 5);
        # g.addEdge(4, 6);
        # g.addEdge(5, 7);
        # g.addEdge(6, 7);
        # g.addEdge(7, 8);
        # //Print Graph
        # DAG_LowestCommonAncestor cycle = new DAG_LowestCommonAncestor(9);
        # cycle.addEdge(0, 1);
        # cycle.addEdge(0, 2);
        # cycle.addEdge(2, 1);
        # cycle.addEdge(1, 2);
        # cycle.addEdge(2, 4);
        # cycle.addEdge(4, 3);
        # cycle.addEdge(3, 1);
        # cycle.addEdge(3, 6);
        # cycle.addEdge(6, 8);
        # cycle.addEdge(7, 8);

        # printGraph(cycle);
        # printGraph(g);
        # if(cycle.checkIfAcyclic()) {
        #     System.out.println("Mama Mia! There's a cycle!");
        # }
        # if(g.checkIfAcyclic()) {
        #     System.out.println("Mama Mia! There's a cycle!");
        # }
        # System.out.println(g.lowestCommonAncestor(g, 1, 5).getV()); //7
        # System.out.println(g.lowestCommonAncestor(g, 5, 2).getV()); //7