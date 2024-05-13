class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        isOne = False
        
        for i in range(len(nums)):
            if nums[i] == 1:
                isOne = True
            elif nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        
        if not isOne:
            return 1
        
        for i in range(len(nums)):
            if abs(nums[i]) == len(nums):
                nums[0] = abs(nums[0]) * -1
            else:
                nums[abs(nums[i])] = abs(nums[abs(nums[i])]) * -1
        
        for i in range(1, len(nums)):
            if nums[i] > 0 and i != 1:
                return i
        
        if nums[0] > 0:
            return len(nums)
        
        return len(nums) + 1