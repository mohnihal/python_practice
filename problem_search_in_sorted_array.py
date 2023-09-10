class Solution(object):
    def searchInRange(self,arr,low,high,val):
        if high==low:
            return low
        mid=(low+high)//2
        if arr[mid]==val:
            return mid
        
        if val > arr[mid]:
            return self.searchInRange(arr,mid+1,high,val)
        else:
            return self.searchInRange(arr,low,mid,val)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target>max(nums):
            return len(nums)
        elif target<min(nums):
            return 0
            
        return self.searchInRange(nums,0,len(nums)-1,target)


sol=Solution()
# print (sol.searchInsert([1,3,5,6,50],55))
print (sol.searchInsert([1],1))
        
