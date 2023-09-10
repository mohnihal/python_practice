'''binary search rotated sorted list'''
class Solution(object):
    def binarySearch(self,arr,low,high,target):
        print (arr,low,high,target)
        if low>=high and target!= arr[low]:
            return -1
        mid = (high+low)//2
        if target==arr[mid]:
            return mid
        if target < arr[mid]:
            if arr[low] > arr[mid] or target >= arr[low]:
                return self.binarySearch(arr,low,mid-1,target)
            else:
                return self.binarySearch(arr,mid+1,high,target)
                
        else:
            if arr[mid]>arr[high] or target <= arr[high]:
                return self.binarySearch(arr,mid+1,high,target)
            else:
                return self.binarySearch(arr,low,mid-1,target)
                
                
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print self.binarySearch(nums,0,len(nums)-1,target)

sol = Solution()
sol.search([4,5,6,7,0,1,2],0)