class Solution:
    def canJump(self, nums):
        pos=0
        last=len(nums)-1
        if last==0:
            return True
        while pos<=last:
            print (pos)
            if pos==last:
                return True
            elif nums[pos]==0:
                break
            else:
                pos+=nums[pos]
        return False

sol=Solution()
print (sol.canJump([3,2,1,0,4]))
