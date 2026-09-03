class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        ans=set()

        for i in arr:
            freq[i]=freq.get(i,0)+1

        for i in freq:
            ans.add(freq[i])
        if len(ans)==len(freq):
            return True
        else:
            return False
                