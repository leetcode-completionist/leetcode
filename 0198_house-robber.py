class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        
        for i in range(n - 1, -1, -1):
            # rob either current house + 2 houses down
            #
            # OR
            #
            # rob the next house ONLY
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
            
        return dp[0]
