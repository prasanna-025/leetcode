class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:


        result=[]


        for i in nums:
            if result.count(i)<2:
                result.append(i)

        nums[:]=result
        return len(nums)








        