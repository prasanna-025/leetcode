class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        k=len(nums)//2

        return nums[k]