class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        maxe=0
        k=s.split()
        for i in range(len(k)):
            u=len(k[-1])
        return u