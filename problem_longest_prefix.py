class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
    
        min_length_string = min(strs,key=len)
        i=0
        common_prefix=""
        for ind,char in enumerate(min_length_string):
            if all([i[ind]==char for i in strs]):
                common_prefix+=char
            else:
                break
        return common_prefix

sol=Solution()
print (sol.longestCommonPrefix(["dog","racecar","car"]))