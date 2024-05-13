class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxSum = nums[0]
        
        for i in range(len(nums)):
            total += nums[i]
            
            if nums[i] > total:
                total = nums[i]
            
            maxSum = max(total, maxSum)
            
        return maxSum