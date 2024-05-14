class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(words) != len(pattern):
            return False
        
        pairs = {}
        seen = []
        
        for i in range(len(words)):
            if words[i] in pairs:
                words[i] = pairs[words[i]]
            else:
                if pattern[i] in seen:
                    return False
                pairs[words[i]] = pattern[i]
                words[i] = pattern[i]
                seen.append(pattern[i])
        
        return "".join(words) == pattern