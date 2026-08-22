class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        k=0
        count=0

        for i in range(len(nums)):
            k=len(str(nums[i]))
            if k%2==0:
                count+=1
        return count
        