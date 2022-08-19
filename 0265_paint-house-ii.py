# https://leetcode.com/problems/paint-house-ii/
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        
        # initialize dp with an extra bottom row
        dp = [[0] * n for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n):
                left = dp[i + 1][:j]
                right = dp[i + 1][j + 1:]
                
                dp[i][j] = (costs[i][j] +
                            min(left + right))
        
        return min(dp[0])
