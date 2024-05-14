class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        answer = 0
        
        for i in range(len(nums)-2):
            total = 0
            left = i+1
            right = len(nums)-1
            
            while left < right:
                if nums[left] + nums[right] + nums[i] < target:
                    total += right - left
                    left += 1
                else:
                    right -= 1
            answer += total
        
        return answer