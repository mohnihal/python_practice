import sys
class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mysum = 0
        mymax = None


        for indx , value in enumerate(nums):
            if mysum+value <value:
                mysum = value
            else :
                mysum +=value
            if mymax is None :
                mymax = mysum
            mymax = max(mysum,mymax)
        return mymax

        # max_so_far = -(sys.maxsize-1)
        # max_ending_here = 0
        
        # for i in range(0, len(nums)):
        #     max_ending_here = max_ending_here + nums[i]
        #     if (max_so_far < max_ending_here):
        #         max_so_far = max_ending_here
    
        #     if max_ending_here < 0:
        #         max_ending_here = 0  
        # return max_so_far


sol=Solution()
print (sol.maxSubArray([-3,-5,-4,-1,-2,-8]))