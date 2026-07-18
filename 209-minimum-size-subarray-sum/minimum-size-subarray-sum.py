class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        window=0
        minimum=float('inf')

        for i in range(len(nums)):
            window =window+nums[i]

         
            while window>=target:
                minimum=min(minimum,i-l+1)

                window=window-nums[l]

                l+=1
        if minimum==float('inf'):
            return 0

        return minimum
        


        