class Solution:
    def intToRoman(self, num: int) -> str:
        RomanDigits = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5:"V", 6:"VI", 7: "VII", 8: "VIII", 9: "IX", 
                       10: "X", 20:"XX", 30: "XXX", 40:"XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 
                       90: "XC", 100: "C", 200:"CC", 300:"CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 
                       800: "DCCC", 900: "CM", 1000: "M", 2000: "MM", 3000: "MMM"}
        
        ConvertedNumber = ""
        if num < 0:
            ConvertedNumber += "-"
        count = len(str(num))
        for digit in str(num):
            if count == 4:
                ConvertedNumber += RomanDigits.get(int(digit) * 1000)
                count = 3
            elif count == 3:
                ConvertedNumber += RomanDigits.get(int(digit) * 100)
                count = 2
            elif count == 2:
                ConvertedNumber += RomanDigits.get(int(digit) * 10)
                count = 1
            elif count == 1:
                ConvertedNumber += RomanDigits.get(int(digit))
                count = 0
                
        return ConvertedNumber