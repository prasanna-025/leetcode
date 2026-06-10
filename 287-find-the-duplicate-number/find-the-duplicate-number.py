class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k={}

        for i in nums:
            if i not in k:
                k[i]=1
            else:
                k[i]+=1
            if k[i]>=2:
                return i