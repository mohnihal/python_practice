"""Program to find the length of the longest palindrome substring."""
import timeit
class Solution(object):
    
    def checkIfPalindrome(self, check_string, start, end):
        while start < end:
            if check_string[start] != check_string[end]:
                return False
            start+=1
            end-=1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left_index = 0
        right_index = len(s) - 1
        max_len_palindrome = 0
        sub_str = s
        max_len_substr = ''
        while len(sub_str) > max_len_palindrome and left_index < right_index:
            if self.checkIfPalindrome(sub_str, left_index, right_index):
                if right_index-left_index +1 > max_len_palindrome:
                    max_len_palindrome = right_index-left_index +1
                    max_len_substr = sub_str[left_index: right_index+1]
                max_len_palindrome = max(max_len_palindrome, right_index-left_index)
            left_index+=1
        
        print(max_len_substr)
        return max_len_palindrome

sol = Solution()
print(sol.longestPalindrome("palalalalalsasasasaabcdefgfedcba"))
# Time the function with parameters
# elapsed_time = timeit.timeit(lambda: sol.longestPalindrome("palalalalalsasasasaabcdefgfedcba"), number=1)

# print(f"Elapsed time: {elapsed_time} seconds")