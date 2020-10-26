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