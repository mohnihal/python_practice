'''Happy number problem'''
class Solution(object):
    def __init__(self):
        self.occured_dict = set()
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n in self.occured_dict or n <4:
            return False
        
        self.occured_dict.add(n)
            
        return self.isHappy(reduce(lambda a,b:a+b,map(lambda x : pow(x,2),[int(i) for i in str(n)])))
        

sol = Solution()
print(sol.isHappy(7))