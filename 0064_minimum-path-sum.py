class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # fill out path sum for bottom row
        for i in range(n - 2, -1, -1):
            grid[m - 1][i] += grid[m - 1][i + 1]
            
        # fill out path sum for right col
        for i in range(m - 2, -1, -1):
            grid[i][n - 1] += grid[i + 1][n - 1]
        
        # fill out rest of the path sums
        for i in range(m - 2, -1, -1):
          for j in range(n - 2, -1, -1):
            grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        
        # first cell contains the min path sum
        return grid[0][0]
