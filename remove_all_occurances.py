class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)-1,-1,-1):
            print (i)
            if nums[i]==val:
                del nums[i]
            print (nums)

        print (nums)

    
sol=Solution()
sol.removeElement([0,1,2,2,3,0,4,2],2)