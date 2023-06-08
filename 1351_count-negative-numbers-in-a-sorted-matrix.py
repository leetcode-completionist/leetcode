class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0

        n = len(grid[0])
        
        first_neg = n - 1
        
        for row in grid:
            while first_neg >= 0 and row[first_neg] < 0:
                first_neg -= 1
            res += n - (first_neg + 1)
            
        return res
