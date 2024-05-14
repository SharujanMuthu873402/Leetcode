class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        

        for i in range(len(t)):
            if s[pointer] == t[i]:
                pointer += 1
                if pointer >= len(s):
                    return True
        return False