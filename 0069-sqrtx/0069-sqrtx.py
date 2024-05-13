class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1
        if x < 9:
            return 2
        if x < 16:
            return 3
        for i in range(1, int(x/2)):
            if i * i > x:
                return i -1