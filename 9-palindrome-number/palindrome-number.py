class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        rev=0
        orignal=x
        while x!=0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        return rev ==orignal
        
    

        