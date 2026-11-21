class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        freq={}


        for i in nums:
            if i in freq:
                return True
            freq[i]=freq.get(i,0)+1
        return False