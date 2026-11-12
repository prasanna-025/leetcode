class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        freq={}

        for i in range(0,len(nums)):
            if target-nums[i] in freq:
                return [freq[target-nums[i]],i]
            else:
                freq[nums[i]]=i

    
