class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        
        largest = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
                
            max_product = max(max_product * nums[i], nums[i])
            min_product = min(min_product * nums[i], nums[i])
        
            largest = max(largest, max_product)
        
        return largest