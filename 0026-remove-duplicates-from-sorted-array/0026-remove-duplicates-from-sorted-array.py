class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1
        current = 0
        
        for i in range(len(nums)):
            if nums[i] != nums[current]:
                nums[pos] = nums[i]
                current = i
                pos += 1
        
        return pos