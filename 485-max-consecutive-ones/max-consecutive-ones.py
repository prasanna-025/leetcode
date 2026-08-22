class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current=0
        maxe=0


        for i in range(len(nums)):
            if nums[i]==1:
                current+=1
                maxe=max(current,maxe)
            else:
                current=0
        return maxe



   


        

        