class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result =[]
        if  len(nums)<4:
            return []
        for i in range(len(nums)-3):
            if nums[i]==nums[i-1]  and i>0:
                continue
            for j in range(i+1,len(nums)-2):
                if nums[j]==nums[j-1] and j>i+1:
                    continue
                l=j+1
                r=len(nums)-1
                while l<r:
                    s=nums[i]+nums[j]+nums[l]+nums[r]
                    if s==target:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l=l+1
                        while l<r and nums[r]==nums[r+1]:
                            r=r-1
                    elif s<target:
                        l=l+1
                        while l<r and nums[l]==nums[l-1]:
                            l=l+1
                    elif s>target:
                        r=r-1
                        while l<r and nums[r]==nums[r+1]:
                            r=r-1
        return result