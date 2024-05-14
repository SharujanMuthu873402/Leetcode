class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split()
        
        for i in range(len(array)//2):
            array[i], array[len(array) - 1 - i] = array[len(array) - i - 1], array[i]
            
        return " ".join(array)