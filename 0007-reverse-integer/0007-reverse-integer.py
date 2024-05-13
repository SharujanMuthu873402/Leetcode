class Solution:
    def reverse(self, x: int) -> int:
        number = 0
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        x= str(x)
        
        for i in range(len(x) - 1, -1, -1):
            number += int(x[i]) * 10 ** i
        
        x = number
        
        if x < -2 ** 31 - 1 or x > 2 ** 31 - 1:
            return 0
        
        if negative:
            x *= -1
        return x