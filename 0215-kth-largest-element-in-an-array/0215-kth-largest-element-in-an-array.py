class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in range(len(nums)):
            heap.append(nums[i] * -1)
        
        
        heapq.heapify(heap)
        
        temp = 0
        for i in range(k):
            temp = heapq.heappop(heap)
        
        return temp * -1