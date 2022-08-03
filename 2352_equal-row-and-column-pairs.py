from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(lambda: 0)
        for row in grid:
            rows[tuple(row)] += 1
        
        res = 0
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            res += rows[tuple(col)]
        return res
