# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        count = 0
        p1 = head

        while p1:
            count += 1
            p1 = p1.next

        k = k % count

        if k == 0:
            return head

        p1 = head


        for i in range(count - k):
            prev = p1
            p1 = p1.next
        
        while p1.next:
            p1 = p1.next
        
        p1.next = head
        p1 = prev.next
        prev.next = None

        return p1