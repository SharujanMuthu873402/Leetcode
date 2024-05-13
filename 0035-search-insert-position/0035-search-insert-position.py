class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        first = 0
        last = len(nums) - 1
        pos = 0
        
        while first <= last:
            if (first + last) % 2 == 0:
                mid = (first + last)//2
            else:
                mid = (first + last)//2 + 1
                
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
                pos = mid + 1
            else:
                pos = mid
                last = mid - 1
        
        return pos