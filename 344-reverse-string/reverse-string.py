class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        result=[]
        for i in range(len(s)-1,-1,-1):
            result.append(s[i])

        for i in range(len(result)):
            s[i]=result[i]

        return s
        