class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}

        for i in range(len(nums)):
            values=nums[i]
            sums=target-values
            if sums  in d:
                return[d[sums],i]
            d[values]=i
                

