import unittest

from BT_LowestCommonAncestor import TreeNode
from BT_LowestCommonAncestor import lowestCommonAncestor

class test_lowestCommonAncestorTestCase(unittest.TestCase):

    def test_TreeNode(self):
        #Assume
        root = TreeNode(6)
        #Action
        #Assert
        self.assertEqual(root.value, 6, "Roots value is = 6")

    def test_AddingNodes(self):
        #Assume
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        #Action
        #Assert
        self.assertEqual(root.left.value, 2, "Nodes value is = 2")
        self.assertEqual(root.left.left.value, 0, "Node value is = 0")

        #Assume
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        #Action
        #Assert
        self.assertEqual(root.left.right.value, 4, "Nodes value is = 4")
        self.assertEqual(root.left.right.left.value, 3, "Nodes value is = 3")

    
    def test_lowestCommonAncestor(self):
        #Assume
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        #Action
        p = root.left.left
        q = root.left.right.right
        result = lowestCommonAncestor(root, p, q).value #2
        
        #Assert
        self.assertEqual(result, 2, "lowestCommonAncestor(0,5) = 2")

        #Action
        p = root.left.left
        q = root.left.right.right
        result = lowestCommonAncestor(root, p, q).value

        #Assert
        self.assertEqual(result, 2, "lowestCommonAncestor(0, 5) = 2")
        self.assertEqual(6, lowestCommonAncestor(root, root.right.left, root.left.right.left).value, "lowestCommonAncestor(9, 3) = 6")
   


