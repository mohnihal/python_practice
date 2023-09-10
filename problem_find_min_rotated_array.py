class Solution:
    def __init__(self):
        self.min = 5001
    def binarySearch(self,start,end,arr):
        print (start,end,self.min,arr)
        if end<start:
            return self.min
        
        mid = (start+end)//2
        if mid>0 and arr[mid] < arr[mid-1]:
            return arr[mid]
        
        if arr[mid]<arr[start]:
            self.min = min(self.min,arr[mid])
            return self.binarySearch(start,mid-1,arr)
        else:
            self.min = min(self.min,arr[start])
            return self.binarySearch(mid+1,end,arr)
    
    def findMin(self, nums):
        return self.binarySearch(0,len(nums)-1,nums)
        pass


sol = Solution()
print (sol.findMin([3,4,5,1,2]))
        