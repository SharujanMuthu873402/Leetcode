class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        answer = [0] * length
        for update in updates:
            answer[update[0]] += update[2]
            
            if update[1] < length - 1:
                answer[update[1] + 1] -= update[2]
        
        for i in range(1, length):
            answer[i] += answer[i-1]
        
        return answer