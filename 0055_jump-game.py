class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None]*len(nums)
        
        # last index is always reachable from last element
        dp[-1] = True
        
        # starting at 2nd-to-last element
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                # if we encounter a zero, the end is
                # not reachable from here
                dp[i] = False
            else:
                # look ahead nums[i] of spaces to see
                # if the last index is reachable
                dp[i] = any(dp[i + 1 : i + 1 + nums[i]])
        
        # first element of DP will tell us if the last
        # index is reachable from the first index
        return dp[0]
