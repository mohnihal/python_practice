'''Binary Tree Search and Insertion'''

class Node:
    def __init__(self,data):
        self.left = None
        self.right=None
        self.data = data
    

class binaryTree:
    def __init__(self):
        pass

    def insert(self,root,key):
        if root is None or key==root.data:
            return Node(key)
        
        else:
            if root.data==key:
                return root
            if key < root.data:
                root.left = self.insert(root.left,key)
            else:
                root.right = self.insert(root.right,key)
        return root 

    def printInOrder(self,root):
        if root is None:
            return 
        
        self.printInOrder(root.left)
        print (root.data)
        self.printInOrder(root.right)

    def minNodeValue(self,root):
        current = root
        while (current.left!=None):
            current = current.left
        return current

    def deleteNode(self,root,key):
        if root is None:
            return root
        
        if key < root.data:
            root.left=self.deleteNode(root.left,key)
        elif key > root.data:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root.data = None
                return temp
            if root.right is None:
                temp = root.left
                root.data = None
                return temp

            temp = self.minNodeValue(root.right)
            root.data = temp.data

            root.right = self.deleteNode(root.right, temp.data)

        return root

r = Node(50)
bt = binaryTree()
r = bt.insert(r, 30)
r = bt.insert(r, 20)
r = bt.insert(r, 40)
r = bt.insert(r, 70)
r = bt.insert(r, 60)
r = bt.insert(r, 80)
r2 = bt.deleteNode(r,70)
bt.printInOrder(r2)
