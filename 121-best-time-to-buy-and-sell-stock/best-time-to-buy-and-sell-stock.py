class Solution(object):
    def maxProfit(self, prices):
        result=0
        minu=prices[0]

        for i in range(len(prices)):
            if minu>prices[i]:
                minu=prices[i]
            result=max(result,prices[i]-minu)
        return result




        