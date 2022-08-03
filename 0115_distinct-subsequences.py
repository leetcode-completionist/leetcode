class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # add one extra to the length for empty string base case
        m, n = len(t) + 1, len(s) + 1
        
        # initialize 2D dp
        dp = [[0] * n for i in range(m)]
        
        # first row is "s" vs. empty string
        # which always gives us 1 valid subsequence
        for i in range(len(dp[0])):
            dp[0][i] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                # subtract one for zero-based indices
                if s[j - 1] == t[i - 1]:
                    # if chars match, we sum up number of ways
                    # between "deleting 1 letter from both words"
                    # and "deleting 1 letter from s"
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    # chars do not match, we can only get the number
                    # of ways to get to current cell by
                    # "deleting 1 letter from s"
                    dp[i][j] = dp[i][j-1]

        # last cell in DP contains our result
        return dp[m - 1][n - 1]
