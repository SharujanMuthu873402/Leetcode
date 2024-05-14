class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def word_number(string):
            if len(string) == 1:
                return "a"
            new_string = ""
            for i in range(1, len(string)):
                temp = (ord(string[i]) - ord('a')) - (ord(string[i-1]) - ord('a'))
                if temp < 0:
                    temp = 26 + temp
                new_string += str(temp * 10 ** i)
            return new_string
        
        numbers = {}
        
        for i in range(len(strings)):
            string = word_number(strings[i])
            if string in numbers:
                numbers[string].append(strings[i])
            else:
                numbers[string] = [strings[i]]
        
        return numbers.values()