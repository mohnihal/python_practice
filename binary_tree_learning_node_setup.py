class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        # print (self.data)

    def __str__(self):
        return str(self.data)

    def insert(self,data):
        pass



node1 = Node(10)
print (node1)