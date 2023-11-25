'''Python Circular Linked List Implementation'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
    
class CircularLinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        if data is None:
            return 
        new_node = Node(data)
        ptr = new_node
        ptr.next = self.head
        temp = self.head
        if self.head:
            while(temp.next!=self.head):
                temp = temp.next
            temp.next=ptr
        else:
            ptr.next = ptr

        self.head = ptr
    
    def printList(self):
        if self.head is None:
            return
        
        if self.head:
            temp=self.head
            while(True):
                print (temp.data)
                if temp.next==self.head:
                    break
                # print (temp.data)
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

    def splitList(self, head1, head2):
        slow_ptr = self.head
        fast_ptr = self.head
        while(fast_ptr.next!=self.head and fast_ptr.next.next!=self.head):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        if fast_ptr.next.next==self.head:
            fast_ptr = fast_ptr.next

        if self.head.next != self.head:
            head1.head = self.head

        head2.head = slow_ptr.next

        fast_ptr.next = slow_ptr.next

        slow_ptr.next = self.head

# Driver program to test above functions
 
# Initialize lists as empty
head = CircularLinkedList()
head1 = CircularLinkedList()
head2 = CircularLinkedList()
 
head.push(12)
head.push(56)
head.push(2)
head.push(11)
 
print ("Original Circular Linked List")
head.printList()
 
# Split the list
head.splitList(head1 , head2)
 
print ("\nFirst Circular Linked List")
head1.printList()
 
print ("\nSecond Circular Linked List")
head2.printList()


        