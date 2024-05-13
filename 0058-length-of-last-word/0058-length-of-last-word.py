class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        pointer = len(s) - 1

        while pointer >= 0 and s[pointer] == ' ':
            pointer -= 1

        for i in range(pointer, -1, -1):
            print(s[i])
            if s[i] != ' ':
                count += 1
            else:
                break
        
        return count