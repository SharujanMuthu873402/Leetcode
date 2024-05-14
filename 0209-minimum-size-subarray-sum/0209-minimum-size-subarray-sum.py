class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = nums[right]
        minCount = len(nums) + 1
        
        while right < len(nums):
            if total >= target:
                minCount = min(right-left+1, minCount)
                total -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    total += nums[right]
            if left > right:
                right = left
                total = 0
        
        if minCount > len(nums):
            return 0
        return minCount