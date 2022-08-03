class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # initialize 2d array to keep track of # of ways
        # we can arrive at any given i,j
        dp = [[0] * n for i in range(m)]
        
        # initialize first cell with whether or not it is reachable
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # fill out first row
        for i in range(1, n):
          if obstacleGrid[0][i] == 1:
            # no way of getting to other cells from obstacle
            dp[0][i] = 0
            continue
          dp[0][i] = dp[0][i - 1]
          
        # fill out first col
        for i in range(1, m):
          if obstacleGrid[i][0] == 1:
            # no way of getting to other cells from obstacle
            dp[i][0] = 0
            continue
          dp[i][0] = dp[i - 1][0]
        
        # fill out remaining cells
        for i in range(1, m):
          for j in range(1, n):
            if obstacleGrid[i][j] == 1:
              # no way of getting to other cells from obstacle
              dp[i][j] = 0
              continue
            
            # we can enter this cell from the top
            # and from the left
            #
            # so we will add up the possible number of ways
            # for both top and left cell
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # bottom-right cell is "finish" and will contain
        # total number of ways to arrive at "finish"
        return dp[m - 1][n - 1]
