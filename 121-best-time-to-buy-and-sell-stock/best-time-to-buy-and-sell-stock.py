class Solution(object):
    def maxProfit(self, prices):
        result=0
        minmum=prices[0]
        


        for i in range(1,len(prices)):
            if prices[i]<minmum:
                minmum=prices[i]


            profit=prices[i]-minmum
            result=max(result,profit)
        return result














            

       
        