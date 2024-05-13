# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        answer = ListNode(None)
        answer.next = head
        prev = answer
        p1 = head
        p2 = head.next

        temp = False

        while p2:
            if p1.val == p2.val:
                temp = True
                p2 = p2.next
            
            elif temp:
                temp = False
                p1 = p2
                p2 = p2.next
            
            else:
                prev.next = p1
                prev = p1
                p1 = p1.next
                p2 = p1.next
        
        if not temp:
            prev.next = p1
        
        else:
            prev.next = None
        
        return answer.next