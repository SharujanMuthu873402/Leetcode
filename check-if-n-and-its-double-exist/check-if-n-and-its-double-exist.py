class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}
        
        for i in range(len(arr)):
            if arr[i] in seen:
                return True
            
            if arr[i] % 2 == 0:
                seen[arr[i]//2] = 1
            
            seen[arr[i] * 2] = 1
        
        return False