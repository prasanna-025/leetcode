class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0

        while l<r:
            d=r-l
            m=min(height[l],height[r])
            f=d*m
            res=max(f,res)
            # if f>res:
            #     res=f
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res












        

            