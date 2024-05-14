class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        nums = [[1],[1,1]]
        
        if numRows == 2:
            return nums
        
        for i in range(2, numRows):
            newRow = [1]
            for j in range(i-1):
                newRow.append(nums[i-1][j] + nums[i-1][j + 1])
            newRow.append(1)
            nums.append(newRow)
        
        return nums
            