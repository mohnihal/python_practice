class Solution(object):
    
    def binSearch(self,low,high,key):
        print (low,high,key)
        if high==low:
            return low
        elif high==1:
            return high
        mid = (high+low)//2
        if mid==low:
            return low
        sq = mid*mid
        if sq==key:
            return mid
        elif sq > key:
            return self.binSearch(low,mid,key)
        else:
            return self.binSearch(mid,high,key)
    
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.binSearch(0,x,x)

sol = Solution()
print (sol.mySqrt(799))