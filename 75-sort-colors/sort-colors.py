class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low=0
        mid=0
        height=len(nums)-1


        while mid<=height:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1     

            else:
                nums[height],nums[mid]=nums[mid],nums[height]
                height-=1
        return nums   

        