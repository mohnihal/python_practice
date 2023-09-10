'''find if all intervals are mutually exclusive'''

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals):
        # Write your code here
        intervals = sorted(intervals,key=lambda x: x[1])
        prev=(0,0)
        for each in intervals:
            if each[0] <= prev[1]:
                return False
            prev = each
        return True
        pass


sol = Solution()
l = [(0,30),(5,10),(15,20)]
l = [(5,8),(9,15)]
print (sol.can_attend_meetings(l))
