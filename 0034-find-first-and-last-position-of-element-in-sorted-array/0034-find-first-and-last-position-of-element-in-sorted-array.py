class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        left = 0
        right = len(nums)
        answer = []
        
        while left <= right:
            mid = (left + (right-left)//2)
            
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                answer.append(mid)
                break
            elif nums[mid] < target:
                if mid == len(nums)-1:
                    return [-1,-1]
                left = mid + 1
            else:
                if mid == 0:
                    return [-1,-1]
                right = mid-1
        
        if len(answer) == 0:
            return [-1,-1]
        
        left = 0
        right = len(nums)
        
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                answer.append(mid)
                return answer
            elif nums[mid] > target:
                if mid == 0:
                    return [-1,-1]
                right = mid-1
            else:
                if mid == len(nums)-1:
                    return [-1,-1]
                left = mid + 1
        
        return [-1,-1]