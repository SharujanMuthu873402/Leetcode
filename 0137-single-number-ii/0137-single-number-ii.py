class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            nums[i] -= 1
            if num not in nums:
                return num
            nums[i] += 1