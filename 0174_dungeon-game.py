class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # 2D dp table
        dp = [[0] * n for _ in range(m)]
        
        # initialize the last cell with the min health needed
        # for the knight to walk into the cell.
        #
        # if cell has a value of -5, then knight will need HP of 6
        #
        # if cell has a value of 5, then knight will need a min HP of 1
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        
        # initialize bottom row from right to left
        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = max(1, dp[m - 1][i + 1] - dungeon[m - 1][i])
            
        # initialize right most column from bottom to top
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])
        
        # fill out the rest of the dp table
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(
                    max(1, dp[i + 1][j] - dungeon[i][j]),
                    max(1, dp[i][j + 1] - dungeon[i][j]))

        # first cell (i.e. knight's starting position)
        # will have the minimum health needed to get to the
        # bottom-right cell.
        return dp[0][0]
