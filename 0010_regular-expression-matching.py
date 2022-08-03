class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # initialize dp
        dp = [[None] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[0][0] = True
        
        # initialize first row (i.e. match pattern against empty string)
        for i, c in enumerate(p, 1):
            if c == "*":
                dp[0][i] = dp[0][i - 2]
            else:
                dp[0][i] = False
                
        # initialize first column (i.e. always false)
        for i in range(1, len(s) + 1):
            dp[i][0] = False
                
        # for each cell in dp
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    # matching char, use top-left result
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # check two to the left
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    # check the top iff matching char
                    elif (s[i - 1] == p[j - 2] or p[j - 2] == ".") and dp[i - 1][j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                        
        # bottom-right cell contains the answer
        return dp[-1][-1]
