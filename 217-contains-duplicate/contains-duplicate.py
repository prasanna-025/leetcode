class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        k={}

        for  i in range(len(nums)):
            if nums[i] in k:
                return  True
            k[nums[i]]=i
        return False
