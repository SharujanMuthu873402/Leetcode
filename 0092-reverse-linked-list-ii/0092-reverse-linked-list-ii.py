# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pointer = head.next
        temp = head
        prev = head

        for i in range(1, left):
            prev = temp
            pointer = pointer.next
            temp = temp.next
        p2 = temp
        
        for i in range(left, right):
            p2.next = pointer.next
            pointer.next = temp
            temp = pointer
            pointer = p2.next
            if left != 1:
                prev.next = temp
        if left == 1:
            return temp
        return head