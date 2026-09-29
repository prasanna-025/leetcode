class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total=sum(nums)
        k=0

        for i in range(len(nums)):
            k=k+nums[i]
            
            if k==total:
                return i
            total=total-nums[i]
        return -1




        