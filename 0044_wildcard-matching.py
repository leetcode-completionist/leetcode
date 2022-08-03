class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        # initialize dp of size (p+1)(s+1)
        dp: List[List[bool]] = [[None] * (s_len + 1) for i in range(p_len + 1)]
            
        # base case of s: "", p: ""
        dp[0][0] = True
        
        # initialize remainder of first row
        # all False because first row is empty p
        for j in range(s_len):
            dp[0][j + 1] = False
            
        # initialize remainder of first column
        for i in range(p_len):
            if p[i] == "*":
                dp[i + 1][0] = dp[i][0]
            else:
                dp[i + 1][0] = False

        # for all unfilled cells in dp
        dp_rows = len(p) + 1
        dp_cols = len(s) + 1
        for i in range(1, dp_rows):
            for j in range(1, dp_cols):
                # we always look up char at index-1 because
                # we added the empty string base case
                if s[j - 1] == p[i - 1] or p[i - 1] == "?":
                    # char match, look at top left
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == "*":
                    # we can use all three preceding cells
                    # (i.e. left, top-left, top)
                    dp[i][j] = (dp[i - 1][j] or
                                dp[i - 1][j - 1] or
                                dp[i][j - 1])
                else:
                    # char mismatch
                    dp[i][j] = False

        # last cell contains our result
        return dp[p_len][s_len]
