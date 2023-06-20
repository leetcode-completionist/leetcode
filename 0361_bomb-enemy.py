class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row_hits = [0] * m
        col_hits = [0] * n
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "E":
                    row_hits[i] += 1
                    col_hits[j] += 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    res = max(res, row_hits[i] + col_hits[j])
        return res
