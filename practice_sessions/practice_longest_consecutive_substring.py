class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        abcabc
        """
        string_dict = {}
        max_len_sub_string = 0
        current_length = 0
        for char_index, char in enumerate(s):
            if char not in string_dict:
                current_length += 1
                string_dict[char] = char_index
            else:
                last_char_index = string_dict[char]
                current_length = char_index - string_dict[char]
                string_dict = {k:v for k, v in string_dict.items() if v > last_char_index}

            max_len_sub_string = max(max_len_sub_string, current_length)

        return max_len_sub_string

sol = Solution()
print(sol.lengthOfLongestSubstring("abcdefgbhijklmnoonpqrstuvwtabc"))