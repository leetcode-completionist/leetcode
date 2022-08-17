# https://leetcode.com/problems/two-sum-less-than-k/
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l, r = 0, len(nums) - 1
        
        res = -1
        
        while l < r:
            i = nums[r] + nums[l]
            if i >= k:
                r -= 1
            else:
                res = max(res, i)
                l += 1
                
        return res
