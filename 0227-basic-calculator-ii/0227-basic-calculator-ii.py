class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        currentNumber = ""
        sign = "+"
        count = 0
        s.strip()
        for term in s:
            if term == " " and not count == len(s)-1:
                count += 1
                continue
            if term.isdigit():
                currentNumber += term
            if not term.isdigit() or count == len(s)-1:
                if sign == "+":
                    stack.append(int(currentNumber))
                elif sign == "-":
                    stack.append(int(currentNumber) * -1)
                elif sign == "*":
                    stack.append(int(stack.pop()) * int(currentNumber))
                elif sign == "/":
                    num = stack.pop()
                    if num >= 0:
                        stack.append(num // int(currentNumber))
                    else:
                        stack.append((abs(num) // int(currentNumber)) * -1)
                currentNumber = ""
                sign = term
            count += 1
        
        total = 0
        
        for num in stack:
            total += num
        
        return total