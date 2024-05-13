class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while(left < right):
            if (right - left) * min(height[left], height[right]) > max_area:
                max_area = (right - left) * min(height[left], height[right])
            
            if height[right] > height[left]:
                left +=1
            else:
                right -= 1
        
        return max_area