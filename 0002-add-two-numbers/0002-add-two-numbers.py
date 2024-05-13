# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(num1, num2, remainder):
            num = num1 + num2 + remainder

            if num < 10:
                return [num, 0]
            
            return [num%10, num//10]
        
        rem = 0

        answer = ListNode()
        temp = answer

        while l1 or l2 or rem:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            Sum = add(val1, val2, rem)
            temp.next = ListNode(Sum[0])
            rem = Sum[1]
            temp = temp.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        

        return answer.next