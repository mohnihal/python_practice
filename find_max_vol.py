class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        # height_tuple_list = [(i,j) for i,j in enumerate(height)]
        # if len(height) <= max(height): 
        #     height_tuple_list.sort(key=lambda x:x[1])
        # for _index,_val in height_tuple_list:
        #     vol = max(_vol)
        for _index in range(0,len(height)-1):
            for _index2 in range(_index,len(height)):
                print (_index,_index2)
                vol = min(height[_index2],height[_index])*(_index2-_index)
                # print (vol)
                if vol>max_vol:
                    max_vol=vol
        
        return (max_vol)

sol = Solution()
print (sol.maxArea([1,8,6,2,5,4,8,3,7]))