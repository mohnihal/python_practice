'''Python Linked List Implementation'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        if data is None:
            return 
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
    
    def printLinkedList(self):
        if self.head is None:
            return
        
        if self.head:
            temp=self.head
            while(temp):
                print (temp.data)
                temp=temp.next
    
    def deleteFromPosition(self,position):
        if self.head==None or position==None:
            return
        
        temp = self.head
        prev = self.head
        index = 0
        while(temp):
            if index==position:
                print (temp.data)
                # prev = temp
                break
            prev = temp
            temp = temp.next
            index+=1
        
        if prev.next:
            print (prev.next.data,temp.next.data)
            prev.next = temp.next
            return self.head
        else:
            print ("Out of index")


ll = LinkedList()
ll.head = Node(1)
# ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(9)
ll.push(5)

ll.printLinkedList()
ll.deleteFromPosition(4)

ll.printLinkedList()


        