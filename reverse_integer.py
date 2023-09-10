class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            signed=1
        else:
            signed=-1
        reversed_number = 0
        x = abs(x)
        while(x!=0):
            print (x)
            last_digit = x%10
            print ("last_digit",last_digit)
            last_digit_flipped = last_digit*(10**(len(str(x))-1))
            reversed_number+=signed*last_digit_flipped
            print ("reversed_number",reversed_number)
            print (signed*reversed_number)
            if (reversed_number >= (-2**31)) and (reversed_number <= ((2**31)-1)):
                x = x//10
            else:
                print (0)
                return 0
        
        print (reversed_number)


sol = Solution()
sol.reverse(-2147483312)