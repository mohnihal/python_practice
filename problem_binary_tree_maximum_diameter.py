'''Calculate maximum diameter of a Binary Tree'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_path = 0
    def calculateDiameter(self,node):
        if node is None:
            return 0
        d_left=self.calculateDiameter(node.left)
        d_right=self.calculateDiameter(node.right)
        self.max_path = max(self.max_path,d_left+d_right)

        t = max(d_left,d_right)
        return t+1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.calculateDiameter(root)
        return self.max_path    

node0 = TreeNode()
node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)
node8 = TreeNode(11)
node9 = TreeNode(12)
node10 = TreeNode(13)
node11 = TreeNode(14)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7
node5.right = node8
node8.right = node9
node9.right = node10
node5.left=node11
sol = Solution()
print (sol.diameterOfBinaryTree(node1))