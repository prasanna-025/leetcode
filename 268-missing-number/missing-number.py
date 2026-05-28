class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        freq={}

        for  i in nums:
            freq[i]=1
        for i in range(n+1):
            if i not in freq:
                return i
        
