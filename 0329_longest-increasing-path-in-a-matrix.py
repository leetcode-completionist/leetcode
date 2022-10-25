# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[None] * n for _ in range(m)]
        
        def dfs(i: int, j: int, prev: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                # out of bounds
                return 0
            
            cur = matrix[i][j]
            
            if cur <= prev:
                # not an increasing path
                return 0
            
            if dp[i][j]:
                # previously calculated
                return dp[i][j]
            
            dp[i][j] = 1 + max(
                dfs(i + 1, j, cur),
                dfs(i - 1, j, cur),
                dfs(i, j + 1, cur),
                dfs(i, j - 1, cur),
            )
            
            return dp[i][j]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, -1))
        return res
