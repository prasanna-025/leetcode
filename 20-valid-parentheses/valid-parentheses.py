class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in s:
            if i not in brackets:
                stack.append(i)

            else:
                if not stack or stack.pop()!=brackets[i]:
                    return False
            
        return len(stack)==0