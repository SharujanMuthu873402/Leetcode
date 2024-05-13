class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        values = {"2":"abc", "3":"def",  "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [letter for letter in values[digits]]
        if len(digits) == 2:
            return [letter1 + letter2 for letter1 in values[digits[0]] for letter2 in values[digits[1]]]
        if len(digits) == 3:
            return [letter1 + letter2 + letter3 for letter1 in values[digits[0]] for letter2 in values[digits[1]] for letter3 in values[digits[2]]]
        if len(digits) == 4:
            return [letter1 + letter2 + letter3 + letter4 for letter1 in values[digits[0]] for letter2 in values[digits[1]] for letter3 in values[digits[2]] for letter4 in values[digits[3]]]