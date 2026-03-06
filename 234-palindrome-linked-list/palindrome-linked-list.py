# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        
        values = []
        
        # Step 1: Traverse linked list
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Step 2: Check palindrome
        if values == values[::-1]:
            return True
        else:
            return False