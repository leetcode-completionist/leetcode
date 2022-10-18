# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Sort coins so we can short-circuit
        # our inner loop (below)
        coins.sort()
        
        # Initialize DP array with "-1"
        # Indices map to amounts: $0, $1, ..., $amount
        dp = [-1] * (amount + 1)
        
        # It requires "0" coins for $0
        dp[0] = 0
        
        for i in range(1, amount + 1):
            candidates = []
            
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    # short-circuit
                    break
                if dp[diff] == -1:
                    # invalid option
                    continue
                candidates.append(dp[diff])

            if not candidates:
                # No valid candidates found,
                # leave DP cell as "-1"
                continue
            
            # take the minimum from all candidates
            # and add 1 (one-coin)
            dp[i] = min(candidates) + 1
        
        # last cell ($amount) has our answer
        return dp[-1]
