import sys
from functools import reduce
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def increasingBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """

#         newNode=new_node_current=TreeNode()
#         stack=[]
#         current=root
#         while True:
#             if current is not None:
#                 stack.append(current)
#                 current=current.left
#             elif stack:
#                 current=stack.pop()
#                 new_node_current.right=TreeNode(current.val)
#                 new_node_current=new_node_current.right
#                 current=current.right
#             else:
#                 break
#         return newNode.right

# Node1 = TreeNode(1)
# Node2 = TreeNode(2)
# Node3 = TreeNode(3)
# Node4 = TreeNode(4)
# Node5 = TreeNode(5)
# Node6 = TreeNode(6)
# Node7 = TreeNode(7)
# Node8 = TreeNode(8)
# Node9 = TreeNode(9)

# root=Node5
# Node5.left=Node3
# Node3.left=Node2
# Node2.left=Node1
# Node3.right=Node4
# Node5.right=Node6
# Node6.right=Node8
# Node8.right=Node9
# Node8.left=Node7
# sol=Solution()
# sol.increasingBST(root)
import sys
arr=[10, 3, 5, 6, 20]
arr=[-10, -3, -5, -6, -20]
negative_max_list = []
negative_max_product = -(sys.maxsize - 1)
negative_min_list = []
positive_max_list = []
positive_max_product = 0
all_negative=True
for i in arr:
    if i<0:

        if len(negative_max_list) <2:
            negative_max_list.append(i)
        else:
            if i<max(negative_max_list):
                negative_max_list[negative_max_list.index(max(negative_max_list))] = i

        if len(negative_min_list) <3:
            negative_min_list.append(i)
        else:
            if i>min(negative_min_list):
                negative_min_list[negative_min_list.index(min(negative_min_list))] = i




        print (negative_max_list)
    else:
        all_negative=False
        if len(positive_max_list) <3:
            positive_max_list.append(i)
        else:
            if i>min(positive_max_list):
                positive_max_list[positive_max_list.index(min(positive_max_list))] = i

        print (positive_max_list)

print (negative_max_list,positive_max_list)
if all_negative:
    print(reduce(lambda a,b: a*b,negative_min_list),"final")
    exit()
if not negative_max_list:
    print (reduce(lambda a,b: a*b,positive_max_list),"final")
    exit()
if not positive_max_list:
    print (negative_max_list[0]*negative_max_list[1]*max(arr),"final")
    exit()

pr1 = reduce(lambda a,b: a*b,[negative_max_list[0],negative_max_list[1],max(positive_max_list)])
pr2 = reduce(lambda a,b: a*b,positive_max_list)


print (pr1,pr2)
print (max(pr1,pr2))
