class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        total = 0
        maxLeft = height[0]
        maxRight = height[-1]
        
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                total += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                total += maxRight - height[right]
        return total