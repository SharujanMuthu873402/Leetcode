class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            if (num > 10 and num < 100) or (num > 999 and num < 10000) or num > 99999:
                count += 1
                
        return count