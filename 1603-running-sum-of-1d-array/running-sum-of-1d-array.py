class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=0
        for i in range(len(nums)):
            nums[i]=sums+nums[i]
            sums=nums[i]
        return nums
            



