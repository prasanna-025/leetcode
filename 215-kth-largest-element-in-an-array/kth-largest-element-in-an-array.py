class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        z=[]


        for i in nums:
            heapq.heappush(z,i)

            if len(z)>k:
                heapq.heappop(z)

        return z[0]
