class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        factor = []
        p = 1
        length = len(nums)
        for i in range(length):
            factor.append(p)
            p*= nums[i]
        p = 1
        for i in range(length - 1, -1, -1):
            new_factor = nums[i]
            nums[i] = factor[i] * p
            p *= new_factor
        return nums