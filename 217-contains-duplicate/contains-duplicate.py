class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        freq={}

        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for i in freq:
            if freq[i]>=2:
                return True
        return False





