# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        
        res = -1
        for num in nums:
            if num <= 0:
                continue
            if (-1 * num) in nums:
                res = max(res, num)
        return res
