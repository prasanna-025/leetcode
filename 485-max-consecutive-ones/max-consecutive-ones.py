class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current=0

        maxe=0

        for i in nums:
            if i==1:
                current+=1
            else:
                current=0
            maxe=max(current,maxe)
                
        return  maxe

       