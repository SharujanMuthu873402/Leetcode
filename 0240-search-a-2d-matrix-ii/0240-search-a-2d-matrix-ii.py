class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] > target:
                return False
            for j in range(len(matrix)):
                if matrix[j][i] == target:
                    return True
                elif matrix[j][i] > target:
                    break
        
        return False