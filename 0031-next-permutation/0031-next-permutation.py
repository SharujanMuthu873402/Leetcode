class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        replace = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                replace = i-1
                break
        
        if replace == -1:
            nums.reverse()
        else:
            for i in range(len(nums)-1,replace, -1):
                if nums[i] > nums[replace]:
                    nums[i],nums[replace] = nums[replace], nums[i]
                    break
            left = replace+1
            right = len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1