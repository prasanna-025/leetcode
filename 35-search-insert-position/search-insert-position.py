class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k=0
        for i in nums:
            if i<target:
                k+=1
            elif i>target:
                return k
        return k



        