# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Sort coins so we can binary search the coin values
        # to end our inner loop.
        coins.sort()
        
        # Initialize DP array with "-1"
        # Indices map to amounts: $0, $1, ..., $amount
        dp = [-1] * (amount + 1)
        
        # It requires ZERO coins for $0
        dp[0] = 0
        
        for i in range(1, amount + 1):
            candidates = []
            
            for j in range(bisect.bisect_right(coins, i)):
                # try all coins from smallest until largest
                # while being able to stay <= $amount
                coin = coins[j]

                if dp[i - coin] >= 0:
                    candidates.append(dp[i - coin])
                    
            if not candidates:
                # No valid candidates found,
                # leave DP cell as "-1"
                continue
            
            # take the minimum from all candidates
            # and add 1 (one-coin)
            dp[i] = min(candidates) + 1
        
        # last cell ($amount) has our answer
        return dp[-1]
