'''Invert Binary Tree'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    # def flipBT(self,node,node_flipped):
    #     if not node:
    #         return 
    #     print (node.val,node_flipped.val)
    #     node_flipped.right=node.left
    #     node_flipped.left=node.right
    #     print ("#"*15)
    #     print (node_flipped.left.val,node.left.val)
    #     print (node_flipped.right.val,node.right.val)
    #     print ("*"*15)
    #     self.flipBT(node.right,node_flipped.left)
    #     self.flipBT(node.left,node_flipped.right)
        
    #     return node_flipped
    def flipBT(self,node):
        if not node:
            return 

        if node.left and node.right:
            node.left.val,node.right.val=node.right.val,node.left.val

        self.flipBT(node.left)
        self.flipBT(node.right)
        
        return node
        
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.flipBT(root)



node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7


sol=Solution()
sol.invertTree(node1)
        
        