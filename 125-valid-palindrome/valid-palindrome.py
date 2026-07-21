class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=""

        for i in s:
            if i.isalnum():
                k+=i.lower()

        left=0
        right=len(k)-1

        while left<right:
            if k[left]!=k[right]:
                return False
            left+=1
            right-=1
        return True