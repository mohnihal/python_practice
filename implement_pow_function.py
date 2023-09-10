from cgitb import reset
from unittest import result


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        _result = 1
        for i in range(abs(n)):
            _result*=x
    
        if n>=0:
            return (_result)
        else:
            return (1/_result)

sol = Solution()
print (sol.myPow(2.000,2147483647))

0.00001
2147483647