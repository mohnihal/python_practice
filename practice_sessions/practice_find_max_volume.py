"""Program finds the maximum volume the can be calculated between 2 pillars from a list of pillars."""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_height_index = 0
        right_height_index = len(height)-1
        max_vol = 0
        while left_height_index < right_height_index:
            vol = min(height[left_height_index], height[right_height_index]) * (right_height_index - left_height_index)
            max_vol = max(max_vol, vol)
            if height[left_height_index] > height[right_height_index]:
                right_height_index-=1
            else:
                left_height_index+=1
        
        
        return max_vol
    
sol = Solution()
print (sol.maxArea([1,8,6,2,5,11,8,3,7,2,5,3,4,4,4]))