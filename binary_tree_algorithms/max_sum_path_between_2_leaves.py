'''max sum path between 2 leaves'''
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
        
        ls = self.maxSumPathUtil(root.left,res)
        rs = self.maxSumPathUtil(root.right,res)

        if root.left is not None and root.right is not None:
            res[0] = max(res[0],ls+rs+root.data)
            return max(ls,rs)+root.data
        
        if root.left is None:
            return rs+root.data
        else:
            return ls+root.data

    def maxSumPath(self,root):
        res = [self.MAX_SUM_DEF]
        self.maxSumPathUtil(root,res)
        return (res[0])



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