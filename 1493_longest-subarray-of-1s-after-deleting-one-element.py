class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        
        res = 0
        
        prev = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
            elif num == 0:
                res = max(prev + cur, res)
                prev = cur
                cur = 0
        
        res = max(prev + cur, res)
        
        return res
