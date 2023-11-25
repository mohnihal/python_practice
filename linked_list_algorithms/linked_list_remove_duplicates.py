'''Remove Duplicates From Linked List'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None,list_items=[]):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    @staticmethod
    def createLLLFromList(list_items):
        if not list_items:
            return None
        head=None
        iNodeList = []
        for i in list_items:
            iNode = ListNode(val=i)
            iNodeList.append(iNode)
        head = iNodeList[0]
        for j in range(len(iNodeList)-1):
            if not head:
                head=iNodeList[j]
            iNodeList[j].next=iNodeList[j+1]
        
        
        return head



class Solution:
    def __init__(self):
        self.unique_set = set()

    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.val==cur.next.val:
                cur.next=cur.next.next
            cur=cur.next


        # while head_temp:
        #     print (head_temp.val)
        #     head_temp2=head_temp
        #     self.unique_set.add(head_temp.val)
        #     while head_temp2.next and head_temp2.next.val in self.unique_set:
        #         head_temp2=head_temp2.next
        #     head_temp.next=head_temp2.next
        #     head_temp=head_temp.next
        return head


t = ListNode()
list_nod = ListNode.createLLLFromList(list_items=[1,1,1,2])
sol=Solution()
ll= sol.deleteDuplicates(list_nod)
# ll = list_nod
print ("="*20)
while(ll):
    print (ll.val)
    ll=ll.next