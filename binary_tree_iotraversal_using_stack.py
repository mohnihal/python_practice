'''Inorder Traversal Using stack'''
class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data = data
    
    def inOrderTraversal(self, root):
        stack = []
        current = root
        while(True):
            if current is not None:
                stack.append(current)
                current = current.left
            elif (stack):
                current = stack.pop()
                print (current)
                current = current.right
            else:
                break
            
