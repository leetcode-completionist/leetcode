class Solution:
    
    MOD = 10 ** 9 + 7
    
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        
        def dfs(i: int, j: int, prev: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            if grid[i][j] <= prev:
                return 0
            
            if dp[i][j]:
                return dp[i][j]
            
            dp[i][j] = sum([
                1,                          # path of 1 (itself)
                dfs(i + 1, j, grid[i][j]),  # go down
                dfs(i - 1, j, grid[i][j]),  # go up
                dfs(i, j + 1, grid[i][j]),  # go right
                dfs(i, j - 1, grid[i][j]),  # go left
            ]) % Solution.MOD
            
            return dp[i][j]
            
        res = 0
        
        for i in range(m):
            for j in range(n):
                res += dfs(i, j, 0) % Solution.MOD
                
        return res % Solution.MOD
