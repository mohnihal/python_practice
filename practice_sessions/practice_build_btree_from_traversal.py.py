from typing import Any

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BuildTree:

    def __init__(self):
        self.preIndex = 0

    def buildTree(self, inOrder, preOrder, startIndex, endIndex):
        if endIndex < startIndex:
            return 
        root_node = Node(preOrder[self.preIndex])
        self.preIndex+=1
        if startIndex == endIndex:
            return (root_node)
        in_order_index = self.inSearch(inOrder, startIndex, endIndex, root_node.data)
        root_node.left = self.buildTree(inOrder, preOrder, startIndex, in_order_index-1)
        root_node.right = self.buildTree(inOrder, preOrder, in_order_index+1, endIndex)
        return root_node
    
    def inSearch(self, inO, sI, eI, root):
        for i in range(sI, eI+1):
            if inO[i] == root:
                return i
    
    def printInorder(self, root=None):
        if root is None:
            return
        self.printInorder(root.left)
        print(root.data)
        self.printInorder(root.right)


inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildTree1 = BuildTree()
root = buildTree1.buildTree(inOrder, preOrder, 0, len(inOrder)-1)
# Let us test the build tree by printing Inorder traversal
print ("Inorder traversal of the constructed tree is")
buildTree1.printInorder(root)