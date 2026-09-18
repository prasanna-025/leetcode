class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        l=0
        r=0
        count=0

        while l<len(s)and r<len(t):
            if s[l]==t[r]:
                count+=1
                l+=1
            r+=1
        
        if len(s)==count:
            return True
        else:
            return False        