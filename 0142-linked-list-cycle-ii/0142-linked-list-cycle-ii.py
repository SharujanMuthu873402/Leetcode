# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        met = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                met = True
                break
        
        if not met:
            return None

        fast = head
        count = 0

        while fast != slow:
            fast = fast.next 
            slow = slow.next
            count += 1
        
        return fast
