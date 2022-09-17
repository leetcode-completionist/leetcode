# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            return (1 +
                    dfs(i + 1, j) +
                    dfs(i - 1, j) +
                    dfs(i, j + 1) +
                    dfs(i, j - 1))
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
                    
        return res
