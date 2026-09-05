class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        result=[]

        freq={}


        for i in  nums:
            freq[i]=freq.get(i,0)+1

        
        for i in freq:
            heapq.heappush(heap,(freq[i],i))

            if len(heap)>k:
                heapq.heappop(heap)

        for x,i in heap:
            result.append(i)
        return result
        