class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1], [1, 1]]

        for i in range(2, rowIndex+1):
            temp = rows[i-1]
            temp.append(1)
            for j in range(len(temp)-2, 0, -1):
                temp[j] += temp[j-1]
            rows.append(temp)
        
        return rows[rowIndex]