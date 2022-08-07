class Solution:
    """
    If n = 1, then all possible strings are "a", "e", "i", "o", and "u"

    If n = 2, for each n = 1, find possible ways to extend the string.

    We can illustrate this with a 2d DP, for example:

        n = 1, dp = [[['a'], ['e'], ['i'], ['o'], ['u']]]

        n = 2, dp = [
                        [['a'], ['e'], ['i'], ['o'], ['u']],
                        [
                         ['ea', 'ia', 'ua']
                         ['ae', 'ie'],
                         ['ei', 'oi'],
                         ['io'],
                         ['iu', 'ou']
                        ]
                    ]

    The question only cares about the number of ways to build a valid string.
    So we can modify the DP table to contain ints instead.
    sum(dp[n-1]) will be the total number of strings at n.

                        0        1        2        3        4
                       'a',     'e',     'i',     'o',     'u'
    base case ->  1     1        1        1        1        1
                  2   1+1+1     1+1      1+1       1       1+1
                  3   2+2+2     3+2      2+2       2       2+1
                  ...
                  etc                      
    """

    VOWELS = ['a', 'e', 'i', 'o', 'u']
    
    VALID_PRECEDING_CHARS = [
        [1, 2, 4],  # "a" can follow "e", "i", or "u"
        [0, 2],     # "e" can follow "a" or "i"
        [1, 3],     # "i" can follow "e" or "o"
        [2],        # "o" can only follow "i"
        [2, 3]      # "u" can follow "i" or "o"
    ]
    
    def countVowelPermutation(self, n: int) -> int:
        num_of_vowels = 5
        
        dp = [[0] * num_of_vowels for _ in range(n)]
        
        for i in range(num_of_vowels):
            # base case of n = 1
            dp[0][i] = 1
            
        for i in range(1, n):
            for j in range(num_of_vowels):
                for preceding_char in Solution.VALID_PRECEDING_CHARS[j]:
                    dp[i][j] += dp[i-1][preceding_char]
                
        return sum(dp[-1]) % (10**9 + 7)
