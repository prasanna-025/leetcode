class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr=nums
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==target:
                    return [i,j]