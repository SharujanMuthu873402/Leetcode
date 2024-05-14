class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        
        for i in range(len(num)):
            while True:
                if not stack or k == 0:
                    break
                if num[i] < stack[-1]:
                    stack.pop()
                    k -= 1
                else:
                    break
            stack.append(num[i])
        
        while k > 0:
            stack.pop()
            k -= 1
        
        for i in range(len(stack)):
            if stack[i] != "0":
                break
        
        stack = stack[i:]
        
        return "".join(stack)