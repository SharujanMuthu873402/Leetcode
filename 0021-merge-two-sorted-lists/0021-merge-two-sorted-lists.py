# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        temp = list1
        prev = ListNode(None)
        prev.next = list1
        answer = prev

        if not p1:
            return p2
        
        if not p2:
            return p1

        while p1 and p2:
            if p1.val <= p2.val:
                prev = p1
                p1 = p1.next
            
            else:
                temp = p2.next
                p2.next = p1
                prev.next = p2
                p1 = p2
                p2 = temp
        if p2:
            prev.next = p2
        

        

        return answer.next
        