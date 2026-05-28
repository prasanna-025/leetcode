class Solution(object):
    def missingNumber(self, nums):
        k={}

        for i in nums:
            k[i]=1
       
        for i in range(len(nums)+1):
            if i not in k:
                return i
        
