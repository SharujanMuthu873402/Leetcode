class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter)-ord('a')] += 1
            if tuple(count) in anagram:
                anagram[tuple(count)].append(word)
            else:
                anagram[tuple(count)] = [word]
        
        return anagram.values()