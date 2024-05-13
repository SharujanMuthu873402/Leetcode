class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n
        grid = []
        
        for i in range(m):
            grid.append(row)
        
        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                    
        
        return grid[m-1][n-1]