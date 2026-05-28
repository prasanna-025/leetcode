class Solution(object):
    def sortColors(self, nums):

        z=[]
        o=[]
        s=[]

        for i in nums:
            if i==0:
                z.append(i)
            elif i==1:
                o.append(i)
            else:
                s.append(i)
        result= z+o+s

        for i in range(len(nums)):
            nums[i]=result[i]
        return nums