class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # initialize dp table with an extra row and column
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        max_square = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    dp[i][j] = min(
                        dp[i + 1][j],
                        dp[i][j + 1],
                        dp[i + 1][j + 1]
                    ) + 1
                    
                    max_square = max(max_square, dp[i][j])
        
        # square our max count to get the total area
        return max_square ** 2
