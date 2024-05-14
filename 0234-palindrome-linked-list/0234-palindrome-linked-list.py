# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head
        while first and first.next:
            first = first.next.next
            second = second.next
        prev = None
        #current = head
        while(second != None):
            next = second.next
            second.next = prev
            prev = second
            second = next
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True