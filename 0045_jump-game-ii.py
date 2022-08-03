class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        dp = [0] * len(nums)        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                # the end is unreachable from here
                dp[i] = float('inf')
                continue

            min_jump = min(dp[i+1:i+1+nums[i]])
            
        
        return dp[0]
