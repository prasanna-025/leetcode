class Solution(object):
    def missingNumber(self, nums):
        freq={}

        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for i in range(len(nums)+1):
            if i not in freq:
                return i