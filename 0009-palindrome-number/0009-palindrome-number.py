class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or not x%10 and x!= 0:
            return False


        num = 0

        while x > num:
            num = num * 10 + x % 10
            x = x//10

        return x == num or x == num // 10 