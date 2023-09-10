'''Get all subsets'''

class Solution:
    def __init__(self):
        self.subsetList = []

    def getSubsets(self,arr):
        if len(arr) < 2 or tuple(arr) in self.subsetList:
            return
        self.subsetList.append(arr)
        for i in arr:
            self.getSubsets([j for j in arr if j!=i])
        pass

    def subsets(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.subsetList.extend([[i] for i in nums])
        self.getSubsets(nums)
        self.subsetList.append([])
        # sorted()
        return sorted(self.subsetList)
        pass        

l = [1,2,3]
sol = Solution()
print (sol.subsets(l))
# print (len(sol.getAllSubsets(l)))
# print (pow(2,len(l)))