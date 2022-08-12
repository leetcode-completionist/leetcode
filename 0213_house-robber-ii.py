class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            # 3 houses or less result in only
            # one option (i.e. all houses are
            # next to each other)
            return max(nums)
        
        houses1 = nums[1:]
        houses2 = nums[:len(nums) - 1]
        
        return max(self.maxMoney(houses1), self.maxMoney(houses2))
        
        
    def maxMoney(self, houses: List[int]) -> int:
        dp = [0] * (len(houses) + 2)
        
        for i in range(len(houses) - 1, -1, -1):
            dp[i] = max(houses[i] + dp[i + 2], dp[i + 1])
        
        return dp[0]
