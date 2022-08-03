class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        dp = [0] * n
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                # the end is unreachable from here
                dp[i] = float('inf')
                continue

            min_jumps = min(dp[i+1:i+1+nums[i]])
            dp[i] = 1 + min_jumps
        
        return dp[0]
