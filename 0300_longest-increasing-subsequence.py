class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            num = nums[i]
            longest = 0
            for j in range(0, i):
                if num > nums[j]:
                    longest = max(longest, dp[j])
            dp[i] = longest + 1
        
        return max(dp)
