# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p1 = head
        p2 = head.next

        p1.next = p2.next
        p2.next = p1
        head = p2
        prev = p1

        while p1 and p2:
            if p1.next and p1.next.next:
                prev = p1
                p1 = p1.next
                p2 = p2.next.next.next
            else:
                return head
            p1.next = p2.next
            p2.next = p1
            prev.next = p2 

        return head