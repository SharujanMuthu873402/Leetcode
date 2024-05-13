class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        length = len(needle)
        hay = len(haystack)
        for i in range(hay - length + 1):
            if haystack[i:i+length] == needle:
                return i