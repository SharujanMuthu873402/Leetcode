class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        values = {}
        
        for i in range(len(numbers)):
            if numbers[i] in values:
                return [values[numbers[i]] + 1, i + 1]
            
            else:
                values[target - numbers[i]] = i
        