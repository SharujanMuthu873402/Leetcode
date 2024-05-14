class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        first = s[0]
        second = ""
        start = 0
        
        for i in range(len(s)):
            if s[i] != first:
                second = s[i]
                start = i
                break
        if second == "":
            return (len(s))
        
        longest = start + 1
        p1 = 0
        temp = start
        for i in range(start+1, len(s)):
            if s[i] == second:
                longest = max(longest, i - p1 + 1)
            elif s[i] == first:
                first, second = second, first
                temp = i
                longest = max(longest, i - p1 + 1)
            else:
                p1 = temp
                first, second = second, s[i]
                temp = i
        
        
        return max(longest, len(s)-1 - p1 + 1)