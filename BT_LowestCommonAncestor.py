
class TreeNode: 
    def __init__(self, value): 
        self.value =  value 
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if p.value < root.value and q.value < root.value:
        return lowestCommonAncestor(root.left, p, q)

    elif p.value > root.value and q.value > root.value:
        return lowestCommonAncestor(root.right, p, q)

    return root


root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)

root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = root.left.left
q = root.left.right.right
result = lowestCommonAncestor(root, p, q)
p = p.value
q = q.value
result = result.value
print("\nLowest Common Ancestor of Node " + format(p) + " and Node " +
format(q) + " is: Node " + format(result) + "\n")

#Adding more testing
