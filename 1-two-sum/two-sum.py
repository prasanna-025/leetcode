class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:


        freq={}

        for i in range(len(nums)):
            val=target -nums[i]

            if val in freq:
                return [freq[val],i]
            freq[nums[i]]=i



