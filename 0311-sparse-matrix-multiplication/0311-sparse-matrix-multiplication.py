class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        answer = []
        
        for i in range(len(mat1)):
            temp = []
            for j in range(len(mat2[0])):
                total = 0
                for x in range(len(mat2)):
                    total += mat1[i][x] * mat2[x][j]
                temp.append(total)
            answer.append(temp)
        
        return answer