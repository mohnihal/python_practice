"""The following code adds 2 linked list assuming each linkedlist holds values for its place eg ll - 1-2-3-4-5 = 54321"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def __init__(self):
        self.finalLl = ListNode()

    def printResult(self,ll):
        while(ll):
            print(ll.val, end='')
            ll = (ll.next)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_value = 0
        l2_value = 0
        decimal_in_10 = 0
        while(l1 or l2):
            if l1:
                l1_value += l1.val*(10**decimal_in_10)
                l1 = l1.next
            if l2:
                l2_value += l2.val*(10**decimal_in_10)
                l2 = l2.next
            decimal_in_10+=1
        
        print (l1_value)
        print (l2_value)
        sum =  l1_value+l2_value
        print (sum)
        temp_sum = sum*1
        cur = finalLL = ListNode()
        result_length = len(str(sum))
        while(result_length):
            cur.val = temp_sum%10
            # print (cur.val)
            if temp_sum//10:
                cur.next = ListNode()
            else:
                cur.next = None
            temp_sum = temp_sum//10
            cur = cur.next
            result_length-=1
        self.printResult(finalLL)
        return finalLL





Node1 = ListNode(0)
Node2 = ListNode(0)
Node3 = ListNode(0)
Node4 = ListNode(0)
Node5 = ListNode(0)
Node6 = ListNode(0)
Node7 = ListNode(1)

Node8 = ListNode(9)
Node9 = ListNode(9)
Node10 = ListNode(9)
Node11 = ListNode(9)



Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
Node6.next = Node7

Node8.next = Node9
Node9.next = Node10
Node10.next = Node11
# Node6.next = Node7


# Node1.next = Node2
# Node1.next = Node2
# Node1.next = Node2
sol = Solution()
sol.addTwoNumbers(Node1,Node8)
# resultLL = ListNode()
# a = Solution() 
# a.createSumLL(807//10,resultLL)
# print (resultLL.val,resultLL.next.val)
            
            
