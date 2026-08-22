class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sume=0
        for i in range(len(nums)):
            sume=sume+nums[i]
            nums[i]=sume
        return nums