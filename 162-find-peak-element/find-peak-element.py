class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)<=1:
            return 0
        l= 0
        vana=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[m+1]:
                r=m

            else:
                l=m+1
        return l
       