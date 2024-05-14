class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        occurences = {}
        
        for letter in s:
            if letter in occurences:
                occurences[letter] += 1
            else:
                occurences[letter] = 1
        
        if len(s) % 2 == 0:
            for num in occurences.values():
                if num % 2 != 0:
                    return False
            return True
        
        count = 0
        
        for num in occurences.values():
            if num % 2 != 0:
                count += 1
                if count > 1:
                    return False
        
        return True