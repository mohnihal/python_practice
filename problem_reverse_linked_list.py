'''Reverse LinkedList'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None,list_items=[]):
        self.val = val
        self.next = next

    @staticmethod
    def createLLLFromList(list_items):
        head=None
        iNodeList = []
        for i in list_items:
            iNode = ListNode(val=i)
            iNodeList.append(iNode)
        for j in xrange(len(iNodeList)-2):
            if not head:
                head=iNodeList[j]
            iNodeList[j].next=iNodeList[j+1]
        return head

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr=curr2 = head
        s = None
        prev=s
        temp=None
        while(curr):
            temp=prev
            try:
                print (curr.val,prev.val,temp.val,head.val,curr2.val,s,"  ********  ")
            except:
                print (curr.val,prev,temp,head.val,curr2.val,s,"  ********  ")
                pass
            prev=curr
            prev.next=3
            curr=curr.next
            try:
                print (curr.val,prev.val,temp.val,head.val,curr2.val,s,"  &&&&&&&&&  ")
            except:
                print (curr,prev.val,temp,head.val,curr2.val,s,"  &&&&&&&&&  ")
                pass
        return prev


# ll = list_nod = ListNode(list_items=[1,2,3,4,5])
t = ListNode()
list_nod = ListNode.createLLLFromList(list_items=[1,2,3,4,5])
sol=Solution()
ll= sol.reverseList(list_nod)
if ll:
    while(ll):
        print (ll.val)
        ll=ll.next