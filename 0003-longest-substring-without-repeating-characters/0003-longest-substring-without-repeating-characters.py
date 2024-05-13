class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        count = 0
        maxCount = 0

        characters = {}

        left = 0
        right = 0

        while left < len(s) and right < len(s):
            if s[right] not in characters or characters[s[right]] == 0:
                count += 1
                characters[s[right]] = 1
                right += 1
            else:
                maxCount = max(maxCount, count)
                while True:
                    characters[s[left]] = 0
                    left += 1
                    count -= 1
                    if s[left - 1] == s[right]:
                        break
        
        maxCount = max(maxCount, count)

        return maxCount