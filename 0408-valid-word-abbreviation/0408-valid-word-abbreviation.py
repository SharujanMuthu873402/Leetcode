class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0
        p2 = 0
        currentNumber = ""
        
        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2].isdigit():
                currentNumber += abbr[p2]
                if currentNumber[0] == "0":
                    return False
                if p2 == len(abbr)-1 or p2 < len(abbr)-1 and not abbr[p2+1].isdigit():
                    p1 += int(currentNumber)
                    currentNumber = ""
                p2 += 1
            else:
                if word[p1] != abbr[p2]:
                    return False
                p1 += 1
                p2 += 1
        
        
        return p1 == len(word) and p2 == len(abbr)