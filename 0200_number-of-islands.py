class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # new island
                    res += 1
                    dfs(i, j)
        
        return res
