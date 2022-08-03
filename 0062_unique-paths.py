class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize 2d array to keep track of # of ways
        # we can arrive at any given i,j
        dp = [[0] * n for i in range(m)]
        
        # fill out first row
        for i in range(n):
          # there is only one way to go through top row
          dp[0][i] = 1
          
        # fill out first col
        for i in range(m):
          # there is only one way to go through left col
          dp[i][0] = 1
        
        for i in range(1, m):
          for j in range(1, n):
            # we can enter this cell from the top
            # and from the left
            #
            # so we will add up the possible number of ways
            # for both top and left cell
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # bottom-right cell is "finish" and will contain
        # total number of ways to arrive at "finish"
        return dp[m - 1][n - 1]
