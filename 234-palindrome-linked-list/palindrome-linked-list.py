
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        
        values = []
       
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        
        if values == values[::-1]:
            return True
        else:
            return False