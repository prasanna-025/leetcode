class Solution(object):
    def maxProfit(self, prices):
        result=0
        minum=prices[0]
        for i in range(len(prices)):
            if prices[i]<minum:
                minum=prices[i]
            profit=prices[i]-minum
            result=max(profit,result)
        return result
        