class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        if n >= 0:
            divisor = 1
        else:
            divisor = -1
        
        
        while n != 1:
            if n%2 != 0:
                return False
            n /= 2
        
        return True