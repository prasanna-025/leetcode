class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort()

        o=len(nums)-k

        return nums[o]

        
        

        
        