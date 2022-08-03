class Solution:
    """
    Example dp with values filled for "intention" and "execution"    
    
        j	0	1	2	3	4	5	6	7	8	9
    i		_	i	n	t	e	n	t	i	o	n
    0	_	0	1	2	3	4	5	6	7	8	9
    1	e	1	1	2	3	3	4	5	6	7	8
    2	x	2	2	2	3	4	4	5	6	7	8
    3	e	3	3	3	3	3	4	5	6	7	8
    4	c	4	4	4	4	4	4	5	6	7	8
    5	u	5	5	5	5	5	5	5	6	7	8
    6	t	6	6	6	5	6	6	5	6	7	8
    7	i	7	6	7	6	6	7	6	5	6	7
    8	o	8	7	7	7	7	7	7	6	5	6
    9	n	9	8	7	8	8	7	8	7	6	5
    
    The three operations can be converted to a dp lookup:
    
        word1: "ab"
        word2: "b"
    
    - insert: ("bab", "b") -> ("ab", "")
    
      This means we use one less character from word2.
      We can express this as dp[i-1][j].
      
    - delete: ("b", "b")
    
      This means we use one less character from word1.
      We can express this as dp[i][j-1].
      
    - replace: ("bb", "b") -> ("b", "")
    
      This means we use one less character from both word1 and word2.
      We can express this as dp[i-1][j-1].
    """
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2), len(word1)
        
        # empty word1 requires exactly len(word2) edits
        if not m or not n:
            return max(m, n)
        
        # initialize dp with first col and row filled out
        # these are the empty string base cases
        dp = [[None] * (n + 1) for i in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                replace_cost = 0 if word1[j - 1] == word2[i - 1] else 1
                dp[i][j] = min(
                    # delete always requires an edit
                    dp[i][j - 1] + 1,
                    # insert always requires an edit
                    dp[i - 1][j] + 1,
                    # replace requires an edit
                    # iff chars are not matching
                    dp[i - 1][j - 1] + replace_cost
                )
                
        return dp[m][n]
