class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        count=0
        sume=0


        for i in nums:
            sume+=i

            if sume-k in freq:
                count+=freq[sume-k]
            

            freq[sume]=freq.get(sume,0)+1
        return count

   