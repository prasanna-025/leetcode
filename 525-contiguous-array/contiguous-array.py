class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sume=0
        maxe=0
        freq={0:-1}

        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1

        
        for i  in range(len(nums)):
            sume+=nums[i]

            if sume in freq:
                maxe=max(maxe,i-freq[sume])
            
            else:
                freq[sume]=i


        return maxe







        