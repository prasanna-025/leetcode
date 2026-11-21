class Solution(object):
    def maxProfit(self, prices):
        result=0
        first=prices[0]

        for i in range(1,len(prices)):
            if first>prices[i]:
                first=prices[i]
            
            result=max(result,prices[i]-first)
        return result
