class Solution:
    def countAndSay(self, n):
        s=""
        s2=""
        for each_loop in range(n):
            # print (s2,"s2=========")
            prev=None
            if not s:
                s="1"
                s2="1"
                continue
            s=s2
            s2=""
            for i in s:

                if not prev:
                    prev=i
                    counter=1
                else:
                    if i==prev:
                        counter+=1
                    else:
                        s2+=str(counter)+prev
                        counter=1
                prev=i
            s2+=str(counter)+prev

        return s2

sol = Solution()
print (sol.countAndSay(3))
