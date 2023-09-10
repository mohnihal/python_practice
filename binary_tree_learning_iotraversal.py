class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        # print (self.data)

    def __str__(self):
        return str(self.data)

    def insert(self,data):
        # print ("received vaue for insertion: ",data)
        if self.data > data:
            if self.left==None:
                self.left=Node(data)
                print ("data inserted to left of ",self.data,data)
            else:
                self.left.insert(data)
        elif self.data < data:
            if self.right==None:
                self.right=Node(data)
                print ("data inserted to right of ",self.data,data)
            else:
                self.right.insert(data)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


    def inOrderTraversal(self,root):
        res = []
        if root:
            res += root.inOrderTraversal(root.left)
            res.append(root.data)
            res += root.inOrderTraversal(root.right)
        return res

    def preOrderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res += root.preOrderTraversal(root.left)
            res += root.preOrderTraversal(root.right)
        return res

    def postOrderTraversal(self,root):
        res = []
        if root:
            res += root.postOrderTraversal(root.left)
            res += root.postOrderTraversal(root.right)
            res.append(root.data)
        return res



node1 = Node(10)
print (node1)
node1.insert(5)
node1.insert(7)
node1.insert(12)
node1.insert(4)
print (node1.inOrderTraversal(node1))
print (node1.preOrderTraversal(node1))
print (node1.postOrderTraversal(node1))