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



node1 = Node(10)
print (node1)
node1.insert(5)
node1.insert(7)
node1.insert(12)
node1.insert(4)