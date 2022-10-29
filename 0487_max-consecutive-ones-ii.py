# https://leetcode.com/problems/max-consecutive-ones-ii/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = [0] * n
        right = [0] * n
        
        count = 0
        for i in range(n):
            left[i] = count
            if nums[i] == 1:
                count += 1
            else:
                count = 0
        
        count = 0
        for i in range(n - 1, -1, -1):
            right[i] = count
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            
        res = 0
        for i in range(n):
            res = max(res, left[i] + right[i] + 1)
        return res
