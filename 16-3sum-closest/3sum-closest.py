class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):

                l=i+1
                r=len(nums)-1
                while l<r:
                    current=nums[i]+nums[l]+nums[r]

                    if abs(current-target)<abs(closet-target):
                        closet=current
                    elif current<target:
                        l+=1
                    elif current>target:
                        r-=1
                    else:
                        return current
        return closet


        