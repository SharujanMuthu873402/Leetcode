class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0

        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        count = 0
        answer = []

        while p1 >= 0 and p2 >= 0:
            add = ord(num1[p1]) + ord(num2[p2]) - 2 * ord('0') + carry
            answer.append(add % 10)
            carry = add//10
            count += 1
            p1 -= 1
            p2 -= 1
        
        while p1 >= 0:
            add = ord(num1[p1]) - ord('0') + carry
            answer.append(add % 10)
            carry = add//10
            count += 1
            p1 -= 1
        
        while p2 >= 0:
            add = ord(num2[p2]) - ord('0') + carry
            answer.append(add % 10)
            carry = add//10
            count += 1
            p2 -= 1
        
        if carry != 0:
            answer.append(carry)

        return ''.join(str(x) for x in answer[::-1])
        