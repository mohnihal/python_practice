'''Problem StockMarket Maximum Profit'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r=0,1
        maxP=0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(profit,maxP)
            else:
                l=r
            r+=1
        return maxP

sol=Solution()
print (sol.maxProfit([2,7,1,5,3,4]))
                
        
            
        