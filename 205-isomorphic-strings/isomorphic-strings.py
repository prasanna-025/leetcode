class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        freq={}
        freq1={}

 
        for i  in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=t[i]
            else:
                if freq[s[i]]!=t[i]:
                    return False
            
            if t[i] not in freq1:
                freq1[t[i]]=s[i]
            else:
                if freq1[t[i]]!=s[i]:
                    return False
        return True
  





        