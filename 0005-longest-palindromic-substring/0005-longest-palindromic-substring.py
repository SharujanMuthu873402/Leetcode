class Solution:
    def longestPalindrome(self, s: str) -> str:
        def center(s, left, right):
            count = 1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    return right - left - 1
                left -= 1
                right += 1
            return right - left - 1
        
        maxLength = 1
        start = 0
        end = 0
        
        for i in range(len(s)):
            temp1 = center(s, i, i)
            temp2 = center(s, i, i+1)
            temp = max(temp1, temp2)
            if temp > maxLength:
                maxLength = temp
                start = i - (temp-1)//2
                end = i + temp//2
        
        return s[start:end+1]