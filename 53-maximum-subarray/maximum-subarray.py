class Solution(object):
    def maxSubArray(self, nums):
        m=nums[0]
        c=0
        for i in nums:
            if c<0:
                c=0
            c=c+i
   
            if c>m:
               m=c
        return m