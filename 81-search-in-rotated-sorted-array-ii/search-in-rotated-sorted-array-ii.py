class Solution(object):
    def search(self, nums, target):
        # if len(nums)<=1:
        #     if nums[0]==target:
        #         return True
        for i in range(len(nums)):
            if nums[i]==target:
                return True
        return False
   