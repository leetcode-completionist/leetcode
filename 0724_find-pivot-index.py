# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        running_sum = 0
        for i in range(len(nums)):
            if total - running_sum - nums[i] == running_sum:
                return i
            running_sum += nums[i]
            
        return -1
