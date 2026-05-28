class Solution(object):
    def missingNumber(self, nums):
        a=0
        while a in nums:
            a+=1
        return a
