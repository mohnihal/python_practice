'''Program to find path between 2 leaves with maximum sum.'''
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    

class BinaryTree:
    def __init__(self):
        self.MAX_SUM_DEF = -2**32

    def maxSumPathUtil(self,root,res):
        if root is None:
            return 0
        sum_left = self.maxSumPathUtil(root.left, res)
        sum_right = self.maxSumPathUtil(root.right, res)
        self.MAX_SUM_DEF = max(self.MAX_SUM_DEF, sum_left + sum_right + root.data) 
        return root.data + max(sum_left, sum_right)

    def maxSumPath(self,root):
        if not root:
            return 
        self.maxSumPathUtil(root, 0)
        return self.MAX_SUM_DEF



root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)

BT = BinaryTree()
print ("Max pathSum of the given binary tree is", BT.maxSumPath(root))