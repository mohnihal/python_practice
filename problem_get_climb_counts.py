'''Get all combinations of climbs'''

class Solution:
    def __init__(self):
        pass

    def computeCombinations(self,arr,m,n):
        if n<0:
            return -1
        if m<1 and n>0:
            return 0
        
        if n==0:
            return 1
        
        return self.computeCombinations(arr,m-1,n)+self.computeCombinations(arr,m,n-arr[m-1])
        pass

    def getAllClimbs(self,climbTypes,steps):
        return self.computeCombinations(climbTypes,len(climbTypes),steps)



sol=Solution()
print (sol.getAllClimbs([1,2],5))