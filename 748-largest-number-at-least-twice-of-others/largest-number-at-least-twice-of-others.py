class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        k=max(nums)
    

        for i in range(len(nums)):
            if nums[i]!=k:
                if nums[i]*2>k:
                    return -1
            else:
                z=i
        return z



        