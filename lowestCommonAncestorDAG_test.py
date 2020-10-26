import unittest
#Imported Libraries
from collections import defaultdict 
#My Structures
from DAG_LowestCommonAncestor import DAG_Graph

class test_DAGlowestCommonAncestorTestCase(unittest.TestCase):

    def test_DAG(self):
        #Assume
        graph = DAG_Graph(6)
        #Action
        #Assert
        self.assertEqual(graph.V, 6, "Total Vertices = 6")

    def test_EdgesAndVertices(self):
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
        self.assertEquals(9,  b.E, "Number of Edges is 9")
        self.assertEquals(9,  b.V, "Number of Vertices is 9")

    def test_LCAofDAG(self):
        g = DAG_Graph(9)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 3)
        g.addEdge(2, 4)
        g.addEdge(3, 5)
        g.addEdge(4, 6)
        g.addEdge(5, 7)
        g.addEdge(6, 7)
        g.addEdge(7, 8)
        self.assertEquals(7,  g.lowestCommonAncestor(5, 1), "LCA of 5,1 = 7")
        self.assertEquals(7,  g.lowestCommonAncestor(1, 5), "LCA of 1,5 = 7")
        self.assertEquals(4,  g.lowestCommonAncestor(0, 2), "LCA of 0,2 = 4")
        self.assertEquals(1,  g.lowestCommonAncestor(0, 0), "LCA of 0,0 = 1")
        self.assertEquals(8,  g.lowestCommonAncestor(0, 7), "LCA of 0,7 = 8")
    
    def test_IsCyclic(self):
        g = DAG_Graph(9)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 3)
        g.addEdge(2, 4)
        g.addEdge(3, 5)
        g.addEdge(4, 6)
        g.addEdge(5, 7)
        g.addEdge(6, 7)
        g.addEdge(7, 8)

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

        self.assertEquals(True,  cycle.checkIfAcyclic(), "Cyclic Graph contains a Cycle")
        self.assertEquals(False,  g.checkIfAcyclic(), "G Graph does not contains a Cycle")
    