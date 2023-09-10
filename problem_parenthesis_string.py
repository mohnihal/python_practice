class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_mapping = {"[":"]","(":")","{":"}"}
        expected_bracket_list = []
        for i in s:
            if i in bracket_mapping:
                expected_bracket_list.append(bracket_mapping[i])

            elif expected_bracket_list:
                if i!=expected_bracket_list.pop():
                    return False
            else:
                return False
        
        if expected_bracket_list:
            return False
        return True

sol=Solution()
print (sol.isValid(")"))
