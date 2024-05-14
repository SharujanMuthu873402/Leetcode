class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(left, right, string):
            while left < right:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        left = 0
        for i in range(len(s)):
            if s[i] == " ":
                reverse(left, i-1, s)
                left = i+1
        reverse(left, len(s)-1, s)