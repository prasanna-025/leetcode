class Solution:
    def trap(self, height: List[int]) -> int:

        l=0
        r=len(height)-1


        left=0
        right=0
        water=0

        while l<r:
            if height[l]<height[r]:

                if height[l]>=left:
                    left=height[l]
                else:
                    water+= left-height[l]
                l+=1
            else:

                if height[r]>=right:
                    right=height[r]
                else:
                    water+=right-height[r]
                r-=1
        return water                     

