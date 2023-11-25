'''find max sum of non adjacent nodes'''
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data


class BinaryTree:
    def __init__(self):
        pass

    def sumOfGrandChildren(self, root, mp):
        sum=0
        if root.left:
            sum+=(self.maxPathSumUtil(root.left.left,mp)+self.maxPathSumUtil(root.left.right,mp))
        if root.right:
            sum+=(self.maxPathSumUtil(root.right.left,mp)+self.maxPathSumUtil(root.right.right,mp))
        
        return sum

    def maxPathSumUtil(self,root,mp):
        if root is None:
            return 0
        
        if root in mp:
            return mp[root]

        incl = (root.data+self.sumOfGrandChildren(root,mp))
        excl = (self.maxPathSumUtil(root.left, mp)+self.maxPathSumUtil(root.right, mp))

        mp[root] = max(incl,excl)
        return mp[root]

    def maxPathSum(self, root):
        if root is None:
            return root

        mp = dict()

        return (self.maxPathSumUtil(root,mp))


if __name__=="__main__":
     
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.left.left = Node(1)
    BT = BinaryTree()
    print(BT.maxPathSum(root))