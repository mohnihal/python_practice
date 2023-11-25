class Solution:
    def convert(self,s,numRows):
        res=""
        for i in range(numRows):
            j=i
            t=0
            while j<len(s):
                res+=s[j]
                if numRows-1==0:
                    j+=1
                if (t%2==0 or i==0) and i+1!=numRows:
                    j=j+(numRows-1-i)*2
                else:
                    j=j+(i-0)*2
                t+=1
                if j==0:
                    j+=1
                print (j)
        return res


sol=Solution()
print (sol.convert("AB",1))