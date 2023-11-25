'''Find maximum sum root to leaf'''
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        pass


class BinaryTree:
    def __init__(self):
        self.max_sum_ref = -32676
        self.maxSumLeaf = None
        pass

    def treeTraverse(self, root, sum = 0, node_path = []):
        if root is None:
            return (0, [])
        
        sum_left, node_path_left = self.treeTraverse(root.left, sum)
        sum_right, node_path_right = self.treeTraverse(root.right, sum)
        if sum_left> sum_right:
            return (sum_left + root.data, node_path_left + [root.data])
        else:
            return (sum_right + root.data, node_path_right + [root.data])

    def maxSumCalculate(self, root):
        return self.treeTraverse(root)

# Constructing tree given in the above figure 
root = Node(10)
root.left = Node(-2)
root.right = Node(7)
root.right.right = Node(2)
root.left.left = Node(8)
root.left.right = Node(-4)
BT = BinaryTree()
sum, path = BT.maxSumCalculate(root)
print( "\nSum of the nodes is " , sum)  
print("Following are the nodes on the maximum sum path:")
print(path)