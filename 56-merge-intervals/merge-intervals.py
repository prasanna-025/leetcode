class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        

        for start,end in intervals[1:]:
            prev=result[-1]
            if start<=prev[1]:
                result[-1][1]=max(end,prev[1])
            else:
                result.append([start,end])
            
        return result