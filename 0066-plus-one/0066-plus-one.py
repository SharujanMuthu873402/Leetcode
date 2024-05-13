class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            index = len(digits) - 1 - i
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                return digits

        return [1] + digits