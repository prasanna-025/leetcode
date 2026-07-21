class Solution:
    def maxArea(self,height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxe=0
        while l<r:
            d=r-l
            f=min(height[l],height[r])
            k=d*f
            maxe=max(maxe,k)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return maxe










        

            