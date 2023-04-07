class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n:
                # out of bounds
                return
            
            if grid[i][j] == 1:
                # water
                return
            
            if grid[i][j] == -1:
                # already visited
                return
            
            # mark as visited
            grid[i][j] = -1
            
            # expand
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
            
        for i in range(m):
            if grid[i][0] == 0:
                # left col
                dfs(i, 0)
                
            if grid[i][n - 1] == 0:
                # right col
                dfs(i, n - 1)
                
        for j in range(n):
            if grid[0][j] == 0:
                # top row
                dfs(0, j)
                
            if grid[m - 1][j] == 0:
                # bottom row
                dfs(m - 1, j)
                
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # closed
                    res += 1
                    dfs(i, j)
        return res
