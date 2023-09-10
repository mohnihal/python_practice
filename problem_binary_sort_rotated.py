class Solution:
    def binarySearch(self,start,end,arr,val):
        print (start,end,arr,val)
        if start==end:
            if arr[start]==val:
                return start
            return -1
        mid = (start+end)//2
        if mid==start:
            if val==arr[end]:
                return end
            else:
                if val !=arr[mid]:
                    return -1
        if val == arr[mid]:
            return mid
        if arr[mid] < arr[start]:
            if val > arr[start] or val < arr[mid]:
                return self.binarySearch(start,mid-1,arr,val)
            else:
                return self.binarySearch(mid+1,end,arr,val)
        else:
            if val > arr[mid] or val < arr[start]:
                return self.binarySearch(mid+1,end,arr,val)
            else:
                return self.binarySearch(start,mid-1,arr,val)
                
                
    def search(self, nums, target):
        return self.binarySearch(0,len(nums)-1,nums,target)
        pass

sol = Solution()
print (sol.search([4,5,6,7,0,1,2],3))
