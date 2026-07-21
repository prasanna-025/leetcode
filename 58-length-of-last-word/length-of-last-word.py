class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        maxe=0
        k=s.split()
        u=len(k[-1])
        return u