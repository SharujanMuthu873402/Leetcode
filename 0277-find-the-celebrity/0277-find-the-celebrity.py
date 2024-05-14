# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            count = 0
            for j in range(n):
                if knows(j, i) and (not knows(i, j) or i == j):
                    count += 1
                else:
                    break   
            if count == n:
                return i
        
        return -1