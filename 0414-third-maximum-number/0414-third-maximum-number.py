class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        maximum = nums[0]
        second = None
        third = None
        
        for i in range(1, len(nums)):
            if nums[i] > maximum:
                temp = maximum
                temp2 = second
                maximum = nums[i]
                second = temp
                third = temp2
            
            elif (second is None or nums[i] > second) and nums[i] != maximum:
                temp = second
                second = nums[i]
                third = temp
            
            elif (third is None or nums[i] > third) and nums[i] != second and nums[i] != maximum:
                third = nums[i]

        if third is not None:
            return third
        
        return maximum