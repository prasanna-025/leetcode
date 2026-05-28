class Solution(object):
    def isAnagram(self, s, t):

        if len(s)!=len(t):
            return False

        freq={}

        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for i in t:
            if i not in freq:
                return False

            freq[i]-=1

            if freq[i]<0:
                return False

        return True

        
        