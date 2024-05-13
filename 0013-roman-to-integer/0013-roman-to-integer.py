class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0
        i = 0

        while i < len(s):
            if s[i] == "I" and i < len(s) - 1:
                if s[i+1] == "V" or s[i+1] == "X":
                    num += values[s[i+1]] - values[s[i]]
                    i += 2
                    continue

            elif s[i] == "X" and i < len(s) - 1:
                if s[i+1] == "L" or s[i+1] == "C":
                    num += values[s[i+1]] - values[s[i]]
                    i += 2
                    continue
            
            elif s[i] == "C" and i < len(s) - 1:
                if s[i+1] == "D" or s[i+1] == "M":
                    num += values[s[i+1]] - values[s[i]]
                    i += 2
                    continue
            
            num += values[s[i]]
            i += 1
        

        return num