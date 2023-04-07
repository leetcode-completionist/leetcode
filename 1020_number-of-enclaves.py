class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        for j in range(n):
            if grid[0][j] == 1:
                # top row
                dfs(0, j)
                
            if grid[m - 1][j] == 1:
                # bottom row
                dfs(m - 1, j)
        
        for i in range(m):
            if grid[i][0] == 1:
                # left row
                dfs(i, 0)
                
            if grid[i][n - 1] == 1:
                # right row
                dfs(i, n - 1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
        return res
