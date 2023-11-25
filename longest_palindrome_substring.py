class Solution(object):

    def find_max_length_of_palindrome(self,s,s_index,s_index2):
        # print (s_index,s_index2)
        if s_index-1<0 or s_index2+1>len(s)-1:
            # print (s_index,s_index2+1)
            return s[s_index:s_index2+1]
        elif s[s_index-1] == s[s_index2+1]:
            return self.find_max_length_of_palindrome(s,s_index-1,s_index2+1)
        else:
            # return s_index2-s_index+1,
            # print (s_index,s_index2+1)
            # print (s[s_index:s_index2+1])
            return s[s_index:s_index2+1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_index = 0
        str_length = len(s)
        max_length_of_palindrome = s[s_index]
        cur_length_of_palindrome = s[s_index]
        cur_length_of_palindrome2 = s[s_index]
        while (s_index < str_length):
            # print (s_index)
            if s_index+1<str_length and s[s_index] == s[s_index+1]:
                cur_length_of_palindrome = self.find_max_length_of_palindrome(s,s_index,s_index+1)
                # print (cur_length_of_palindrome,"*"*8)
            if s_index+2<str_length and s[s_index] == s[s_index+2]:
                cur_length_of_palindrome2 = self.find_max_length_of_palindrome(s,s_index,s_index+2)
                # print (cur_length_of_palindrome2,"#"*8)
            # if len(cur_length_of_palindrome) > len(max_length_of_palindrome):
            max_length_of_palindrome = max([max_length_of_palindrome,cur_length_of_palindrome,cur_length_of_palindrome2],key=len)
            s_index+=1

        print (max_length_of_palindrome)
        return (max_length_of_palindrome)

import timeit
sol = Solution()
# sol.longestPalindrome("palalalalalsasasasaabcdefgfedcba")
# sol.longestPalindrome("aaaa")
elapsed_time = timeit.timeit(lambda: sol.longestPalindrome("palalalalalsasasasaabcdefgfedcba"), number=1)

print(f"Elapsed time: {elapsed_time} seconds")