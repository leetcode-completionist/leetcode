# https://leetcode.com/problems/paint-house/
class Solution:
    
    COLORS = 3
    
    def minCost(self, costs: List[List[int]]) -> int:
        m = len(costs)
        
        # initialize DP with an extra bottom row
        dp = [[0] * Solution.COLORS for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            # red
            dp[i][0] = costs[i][0] + min(dp[i + 1][1], dp[i + 1][2])
            
            # blue
            dp[i][1] = costs[i][1] + min(dp[i + 1][0], dp[i + 1][2])
        
            # green
            dp[i][2] = costs[i][2] + min(dp[i + 1][0], dp[i + 1][1])
            
        # minimum at the top row will be our answer
        return min(dp[0])
