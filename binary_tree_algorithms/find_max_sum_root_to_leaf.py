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

    def printMaxSumPath(self,root):
        if root is None or self.maxSumLeaf is None:
            return root
        # print ("X"*5)
        # print (root.data)
        # print ("H"*5)

        if root:
            if (root==self.maxSumLeaf or self.printMaxSumPath(root.left)==self.maxSumLeaf or self.printMaxSumPath(root.right)==self.maxSumLeaf):
                print (root.data)
                return self.maxSumLeaf
        
        return False

    def getTargetLeaf(self,root,current_sum):
        if root is None:
            return None
        
        current_sum+=root.data
        if (root.left==None and root.right==None):
            if current_sum > self.max_sum_ref:
                self.max_sum_ref=current_sum
                self.maxSumLeaf = root

        self.getTargetLeaf(root.left,current_sum)
        self.getTargetLeaf(root.right,current_sum)



    def maxSumCalculate(self,root):
        if root is None:
            return root
        
        current_sum = 0
        self.getTargetLeaf(root,current_sum)
        self.printMaxSumPath(root)
        return self.max_sum_ref

  
# Constructing tree given in the above figure 
root = Node(10)
# print (root.data)
root.left = Node(-2)
root.right = Node(7)
root.right.right = Node(2)
root.left.left = Node(8)
root.left.right = Node(-4)
  
print("Following are the nodes on the maximum sum path ")
BT = BinaryTree()
sum = BT.maxSumCalculate(root)
print( "\nSum of the nodes is " , sum)  