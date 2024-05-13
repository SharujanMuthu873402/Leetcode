# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_list = []
        
        for arr in lists:
            current = arr
            while current:
                new_list.append(current.val)
                current = current.next
                
        heapq.heapify(new_list)
        
        new_linked = ListNode(None)
        current = new_linked
        
        for i in range(len(new_list)-1):
            current.val = heapq.heappop(new_list)
            current.next = ListNode(None)
            current = current.next
        if len(new_list) == 0:
            return new_linked.next
        else:
            current.val = heapq.heappop(new_list)
        
        
        return new_linked