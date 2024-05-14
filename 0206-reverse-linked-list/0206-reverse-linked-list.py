# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        pointer = head.next
        temp = head

        while pointer:
            temp.next = pointer.next
            pointer.next = head
            head = pointer
            pointer = temp.next
        
        return head