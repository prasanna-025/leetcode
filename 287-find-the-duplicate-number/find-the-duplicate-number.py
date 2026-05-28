class Solution(object):
    def findDuplicate(self, nums):
        freq={}

        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

            if freq[i]>=2:
                return i        