class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        abcabc
        """
        s_index = 0
        max_len = 0
        curr_len = 0
        result_list = []
        string_length = len(s)
        while((string_length>s_index) and (max_len<= curr_len+string_length-s_index)):
        # while((string_length>s_index) and (string_length-s_index+1>curr_len)):
            # if curr_len+string_length-s_index
            if curr_len > max_len:
                max_len = curr_len
            if not s[s_index] in result_list:
                result_list.append(s[s_index])
                curr_len+=1
            else:
                print (result_list,"**"*5)
                result_list = result_list[result_list.index(s[s_index])+1:]+[s[s_index]]
                curr_len=len(result_list)
            s_index+=1
            print (len(s),s_index,max_len,result_list,curr_len)
        
        print (max(max_len,curr_len))


sol = Solution()
sol.lengthOfLongestSubstring("abcdefgbhijklmnoonpqrstuvwtabc")