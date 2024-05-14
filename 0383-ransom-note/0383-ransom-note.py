class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        
        for letter in magazine:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        for letter in ransomNote:
            if letter not in letters or letters[letter] == 0:
                return False
            letters[letter] -= 1
        
        return True