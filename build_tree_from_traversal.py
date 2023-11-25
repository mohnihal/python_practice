'''Building Tree From Traversals'''
from re import S


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class buildTree:
    def __init__(self):
        self.preIndex=0
    
    def buildTree(self,inOrder,preOrder,inStart,inEnd):
        if inStart > inEnd:
            return None
        
        new_node = Node(preOrder[self.preIndex])
        self.preIndex+=1
        if inStart==inEnd:
            return new_node
        
        inIndex = self.search(inOrder,inStart,inEnd,new_node.data)
        # print (inIndex)
        # print (new_node.left)
        new_node.left = self.buildTree(inOrder,preOrder,inStart,inIndex-1)
        new_node.right = self.buildTree(inOrder,preOrder,inIndex+1,inEnd)
        return new_node
    
    def search(self,inOrder,inStart,inEnd,root):
        for i in range(inStart,inEnd+1):
            if inOrder[i]==root:
                return i
                
    def printInorder(self,node):
        if node is None:
            return
        
        # first recur on left child
        self.printInorder(node.left)
        
        # then print the data of node
        print (node.data)
    
        # now recur on right child
        self.printInorder(node.right)
     
# Driver program to test above function
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildTree1 = buildTree()
buildTree1.preIndex = 0
root = buildTree1.buildTree(inOrder, preOrder, 0, len(inOrder)-1)
 
# Let us test the build tree by printing Inorder traversal
print ("Inorder traversal of the constructed tree is")
buildTree1.printInorder(root)


