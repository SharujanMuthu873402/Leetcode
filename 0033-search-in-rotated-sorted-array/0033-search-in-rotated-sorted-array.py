class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target <= nums[right] and nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            
        return -1