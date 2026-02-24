class Solution(object):
    def search(self, nums, target):
        nums.sort()
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return True
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return False
   