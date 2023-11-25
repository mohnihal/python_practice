"""Reverse LL"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlist:

    def __init__(self, head):
        self.head=head

    def reverse_linked_list(self):
        print("Reversing Linked List:")
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def print_linked_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

def create_linked_list():
    node1 = Node(5)
    node1.next = Node(10)
    node1.next.next = Node(15)
    node1.next.next.next = Node(20)
    node1.next.next.next.next = Node(25)
    return node1

if __name__=='__main__':
    node = create_linked_list()
    ll = Linkedlist(node)
    ll.print_linked_list()
    ll.reverse_linked_list()
    ll.print_linked_list()
