class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        
        seen = {}
        
        while True:
            if temp == 1:
                return True
            
            seen[temp] = 1
            
            number = str(temp)
            temp = 0
            
            for i in range(len(number)):
                temp += int(number[i]) ** 2
            
            if temp in seen:
                return False