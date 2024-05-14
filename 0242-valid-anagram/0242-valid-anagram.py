class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        for letter in t:
            if letter not in letters:
                return False
            else:
                if letter in letters and letters[letter] != 0:
                    letters[letter] -= 1
                else:
                    return False
        
        return len(s) == len(t)