class Solution:
    def myAtoi(self, s: str) -> int:
        new_string = ""
        checked = False
        factor = 1
        
        for char in s:
            if char == " ":
                if checked:
                    break
                continue
            elif char == "+":
                if checked:
                    break
                checked = True
                continue
            elif char == "-":
                if checked:
                    break
                checked = True
                factor = -1
                continue
            elif not char.isdigit():
                break
            else:
                checked = True
                new_string += char
        
        if new_string == "":
            return 0
        num = int(new_string) * factor
        
        if num < -2 ** 31:
            return -2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 -1
        
        return num